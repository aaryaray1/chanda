#!/usr/bin/env python3
"""Physics knowledge-base toolkit: paper search/fetch, reference verification, tree index, constants, hooks."""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
LIBRARY = ROOT / "library"
PAPERS_DB = LIBRARY / "papers.jsonl"
INDEX_JSON = LIBRARY / "index.json"
VERIFY_CACHE = LIBRARY / "verify-cache.json"
VERIFY_REPORT = LIBRARY / "verification-report.md"
FETCH_LOG = LIBRARY / "fetch-log.json"
CODATA_JSON = LIBRARY / "codata.json"
FULLTEXT = LIBRARY / "fulltext"
TREE_MD = ROOT / "TREE.md"
SKIP_DIRS = {"_templates", "reviews", "notes", "assets"}
INHERITED = ("arxiv", "source", "agent", "openalex_filter")
DEFAULT_OPENALEX_FILTER = "primary_topic.field.id:31"

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
OPENSEARCH = "{http://a9.com/-/spec/opensearch/1.1/}"
USER_AGENT = "physics-kb/1.0 (research knowledge base; python-urllib)"
MIN_INTERVAL = {"export.arxiv.org": 3.1, "arxiv.org": 3.1, "inspirehep.net": 0.35, "api.semanticscholar.org": 1.1,
                "api.openalex.org": 0.12, "api.crossref.org": 0.1, "doi.org": 0.2, "physics.nist.gov": 0.5}
SHARED_THROTTLE_HOSTS = {"export.arxiv.org", "arxiv.org", "inspirehep.net", "api.semanticscholar.org"}
THROTTLE_DIR = Path(tempfile.gettempdir()) / "physlib-throttle"
_last_call: dict[str, float] = {}
_budget_exhausted: set[str] = set()


class BudgetExhausted(Exception):
    """Raised when an API reports its daily budget is used up (retrying would only waste time)."""

ARXIV_ID = r"(?:\d{4}\.\d{4,5}|[a-z][a-z\-]+(?:\.[A-Za-z]{2})?/\d{7})"
ARXIV_REF = re.compile(r"arXiv:(" + ARXIV_ID + r")(?:v\d+)?", re.I)
DOI_REF = re.compile(r"doi:(10\.\d{4,9}/(?:[^\s\[\]\"'`()]|\([^\s()]*\))+)", re.I)
QUOTED_TITLE = re.compile(r"[\"“]([^\"”]{6,})[\"”]")
YEAR_IN_PARENS = re.compile(r"\((1[6-9]\d\d|20\d\d)[a-z]?\)")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def out(text: str = "") -> None:
    sys.stdout.write(text + "\n")


def clean(text) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", "", str(text or "")))
    return " ".join(text.split())


def today() -> str:
    return dt.date.today().isoformat()


def shared_throttle(host: str, interval: float) -> None:
    """Space requests to a host across all physlib processes via a stamp file guarded by an exclusive lock file."""
    THROTTLE_DIR.mkdir(exist_ok=True)
    stamp, lock = THROTTLE_DIR / f"{host}.stamp", THROTTLE_DIR / f"{host}.lock"
    fd, deadline = None, time.time() + 60
    while fd is None and time.time() < deadline:
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > 30:
                    lock.unlink()
            except OSError:
                pass
            time.sleep(0.2)
    try:
        last = float(stamp.read_text() or 0) if stamp.exists() else 0.0
        wait = interval - (time.time() - last)
        if wait > 0:
            time.sleep(wait)
        stamp.write_text(str(time.time()))
    finally:
        if fd is not None:
            os.close(fd)
            lock.unlink(missing_ok=True)


def http_get(url: str, accept: str = "application/json", binary: bool = False, retries: int = 5,
             data: bytes | None = None, headers: dict | None = None):
    host = urllib.parse.urlparse(url).netloc
    headers = {"User-Agent": USER_AGENT, "Accept": accept, **(headers or {})}
    if data is not None:
        headers["Content-Type"] = "application/json"
    if host in _budget_exhausted:
        raise BudgetExhausted(f"{host}: daily budget exhausted earlier in this run")
    for attempt in range(retries):
        if host in SHARED_THROTTLE_HOSTS:
            shared_throttle(host, MIN_INTERVAL[host])
        else:
            wait = MIN_INTERVAL.get(host, 0.2) - (time.monotonic() - _last_call.get(host, 0.0))
            if wait > 0:
                time.sleep(wait)
        _last_call[host] = time.monotonic()
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
                return data if binary else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            if err.code == 429:
                body = err.read().decode("utf-8", "replace")
                if "budget" in body.lower():
                    _budget_exhausted.add(host)
                    raise BudgetExhausted(f"{host}: daily budget exhausted (resets midnight UTC). {body[:160]}") from err
            if err.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep((20 if err.code == 429 else 6) * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as err:
            if "CERTIFICATE_VERIFY_FAILED" in str(err):
                return curl_get(url, binary, headers, data)
            if attempt < retries - 1:
                time.sleep(6 * (attempt + 1))
                continue
            raise
    return None


def curl_get(url: str, binary: bool, headers: dict, data: bytes | None = None):
    """Fallback when Python's bundled OpenSSL rejects a valid chain; curl verifies with the OS trust store."""
    cmd = ["curl", "-sSfL", "--max-time", "60"] + [arg for k, v in headers.items() for arg in ("-H", f"{k}: {v}")]
    if data is not None:
        cmd += ["--data-binary", "@-"]
    result = subprocess.run(cmd + [url], input=data, capture_output=True, timeout=90)
    if result.returncode == 22 and b"404" in result.stderr:
        return None
    if result.returncode != 0:
        raise urllib.error.URLError(f"curl fallback failed for {url}: {result.stderr.decode('utf-8', 'replace').strip()}")
    return result.stdout if binary else result.stdout.decode("utf-8", "replace")


def get_json(url: str, headers: dict | None = None):
    text = http_get(url, headers=headers)
    return json.loads(text) if text else None


def openalex_url(params: dict) -> str:
    mailto = os.environ.get("PHYSLIB_MAILTO")
    if mailto:
        params = {**params, "mailto": mailto}
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        params = {**params, "api_key": api_key}
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def normalize_doi(doi) -> str | None:
    if not doi:
        return None
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", str(doi).strip(), flags=re.I)
    return doi.rstrip(".,;").lower() or None


def normalize_arxiv(aid) -> str | None:
    if not aid:
        return None
    aid = re.sub(r"^(arxiv:|https?://arxiv\.org/(abs|pdf)/)", "", str(aid).strip(), flags=re.I)
    return re.sub(r"v\d+$", "", aid.removesuffix(".pdf")) or None


def make_record(**kw) -> dict:
    rec = {k: kw.get(k) for k in ("title", "authors", "n_authors", "year", "date", "venue", "doi",
                                  "arxiv", "citations", "abstract", "source", "url", "oa_pdf")}
    rec["title"] = clean(rec["title"])
    rec["abstract"] = clean(rec["abstract"])
    rec["doi"] = normalize_doi(rec["doi"])
    rec["arxiv"] = normalize_arxiv(rec["arxiv"])
    rec["authors"] = [clean(a) for a in (rec["authors"] or []) if a][:8]
    if rec["arxiv"]:
        rec["key"] = f"arxiv:{rec['arxiv']}"
    elif rec["doi"]:
        rec["key"] = f"doi:{rec['doi']}"
    else:
        rec["key"] = f"title:{re.sub(r'[^a-z0-9]+', '-', rec['title'].lower()).strip('-')[:120]}:{rec['year'] or ''}"
    if rec["arxiv"]:
        rec["url"] = f"https://arxiv.org/abs/{rec['arxiv']}"
    elif rec["doi"]:
        rec["url"] = f"https://doi.org/{rec['doi']}"
    return rec


def split_phrases(query: str) -> list[str]:
    return [p.strip() for p in query.split(";") if p.strip()]


def arxiv_parse(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    records = []
    for entry in root.findall(ATOM + "entry"):
        match = re.search(r"abs/(.+?)(v\d+)?$", entry.findtext(ATOM + "id") or "")
        title = clean(entry.findtext(ATOM + "title"))
        if not match or title.lower() == "error":
            continue
        authors = [entry_author.findtext(ATOM + "name") for entry_author in entry.findall(ATOM + "author")]
        published = (entry.findtext(ATOM + "published") or "")[:10]
        primary = entry.find(ARXIV_NS + "primary_category")
        category = primary.get("term") if primary is not None else "arXiv"
        records.append(make_record(
            title=title, authors=authors, n_authors=len(authors), date=published,
            year=int(published[:4]) if published[:4].isdigit() else None,
            venue=clean(entry.findtext(ARXIV_NS + "journal_ref")) or f"arXiv preprint [{category}]",
            doi=entry.findtext(ARXIV_NS + "doi"), arxiv=match.group(1),
            abstract=entry.findtext(ATOM + "summary"), source="arxiv"))
    return records


def arxiv_search(query: str, cats: list[str] | None = None, n: int = 5, since_days: int | None = None,
                 sort: str = "relevance", raw: str | None = None) -> list[dict]:
    parts = []
    if cats:
        parts.append("(" + " OR ".join(f"cat:{c}" for c in cats) + ")")
    if raw:
        parts.append(f"({raw})")
    elif query:
        parts.append("(" + " OR ".join(f'ti:"{p}" OR abs:"{p}"' for p in split_phrases(query)) + ")")
    if since_days:
        start = (dt.date.today() - dt.timedelta(days=since_days)).strftime("%Y%m%d")
        parts.append(f"submittedDate:[{start}0000 TO {dt.date.today().strftime('%Y%m%d')}2359]")
    sort_by = {"relevance": "relevance", "recent": "submittedDate"}.get(sort, "relevance")
    params = {"search_query": " AND ".join(parts), "sortBy": sort_by, "sortOrder": "descending", "max_results": n}
    text = http_get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params), accept="application/atom+xml")
    return arxiv_parse(text) if text else []


def arxiv_lookup(ids: list[str]) -> dict[str, dict]:
    found = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        params = {"id_list": ",".join(chunk), "max_results": len(chunk)}
        text = http_get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params), accept="application/atom+xml")
        for rec in arxiv_parse(text) if text else []:
            found[rec["arxiv"].lower()] = rec
    return found


def openalex_abstract(inverted: dict | None) -> str:
    if not inverted:
        return ""
    positions = sorted((pos, word) for word, spots in inverted.items() for pos in spots)
    return " ".join(word for _, word in positions)


def openalex_record(work: dict) -> dict:
    location = work.get("primary_location") or {}
    source = location.get("source") or {}
    biblio = work.get("biblio") or {}
    venue = source.get("display_name") or ""
    if venue and biblio.get("volume"):
        venue += f" {biblio['volume']}"
        if biblio.get("first_page"):
            venue += f", {biblio['first_page']}"
    arxiv = (work.get("ids") or {}).get("arxiv")
    for loc in work.get("locations") or []:
        landing = (loc or {}).get("landing_page_url") or ""
        if not arxiv and "arxiv.org/abs/" in landing:
            arxiv = landing.split("arxiv.org/abs/")[1]
    oa = work.get("best_oa_location") or {}
    authors = [(a.get("author") or {}).get("display_name") for a in work.get("authorships") or []]
    return make_record(
        title=work.get("title") or work.get("display_name"), authors=authors, n_authors=len(authors),
        year=work.get("publication_year"), date=work.get("publication_date"), venue=venue,
        doi=work.get("doi"), arxiv=arxiv, citations=work.get("cited_by_count"),
        abstract=openalex_abstract(work.get("abstract_inverted_index")), source="openalex", url=work.get("id"),
        oa_pdf=oa.get("pdf_url"))


OPENALEX_SELECT = ("id,doi,title,display_name,publication_year,publication_date,cited_by_count,authorships,"
                   "primary_location,locations,ids,biblio,abstract_inverted_index,best_oa_location,type")


def openalex_search(query: str, n: int = 6, sort: str = "cited", since_year: int | None = None,
                    reviews: bool = False, extra_filter: str | None = DEFAULT_OPENALEX_FILTER,
                    scope: str = "title_and_abstract") -> list[dict]:
    phrases = " OR ".join(f'"{p}"' for p in split_phrases(query))
    filters = [f"{scope}.search:{phrases}"]
    if extra_filter:
        filters.append(extra_filter)
    if since_year:
        filters.append(f"publication_year:>{since_year - 1}")
    if reviews:
        filters.append("type:review")
    sort_key = {"cited": "cited_by_count:desc", "recent": "publication_date:desc", "relevance": "relevance_score:desc"}[sort]
    data = get_json(openalex_url({"filter": ",".join(filters), "sort": sort_key, "per_page": n, "select": OPENALEX_SELECT}))
    return [openalex_record(w) for w in (data or {}).get("results", []) if w.get("title")]


def openalex_by_doi(dois: list[str]) -> dict[str, dict]:
    found = {}
    for i in range(0, len(dois), 40):
        chunk = [d for d in dois[i:i + 40] if not re.search(r"[<>|,;]", d)]
        try:
            data = get_json(openalex_url({"filter": "doi:" + "|".join(chunk), "per_page": 50, "select": OPENALEX_SELECT})) if chunk else None
        except (urllib.error.HTTPError, BudgetExhausted):
            data = None
        for work in (data or {}).get("results", []):
            rec = openalex_record(work)
            if rec["doi"]:
                found[rec["doi"]] = rec
    return found


def crossref_by_doi(doi: str) -> dict | None:
    data = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    msg = (data or {}).get("message")
    if not msg:
        return None
    parts = (msg.get("issued") or {}).get("date-parts") or [[None]]
    authors = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in msg.get("author") or []]
    return make_record(title=(msg.get("title") or [""])[0], authors=authors, n_authors=len(authors),
                       year=parts[0][0], venue=(msg.get("container-title") or [""])[0], doi=doi, source="crossref")


def doi_resolves(doi: str) -> bool:
    data = get_json("https://doi.org/api/handles/" + urllib.parse.quote(doi))
    return bool(data and data.get("responseCode") == 1)


INSPIRE_FIELDS = "control_number,titles,authors.full_name,author_count,arxiv_eprints,dois,citation_count,publication_info,abstracts,preprint_date,collaborations"


def inspire_record(meta: dict) -> dict:
    pub = (meta.get("publication_info") or [{}])[0]
    venue = " ".join(str(x) for x in (pub.get("journal_title"), pub.get("journal_volume")) if x)
    if venue and (pub.get("artid") or pub.get("page_start")):
        venue += f", {pub.get('artid') or pub.get('page_start')}"
    collab = [c.get("value") for c in meta.get("collaborations") or [] if c.get("value")]
    authors = [a.get("full_name") for a in meta.get("authors") or []]
    if collab:
        authors = [f"{collab[0]} Collaboration"] + authors[:3]
    date = meta.get("preprint_date") or ""
    return make_record(
        title=(meta.get("titles") or [{}])[0].get("title"), authors=authors,
        n_authors=meta.get("author_count") or len(authors), year=pub.get("year") or (int(date[:4]) if date[:4].isdigit() else None),
        date=date, venue=venue.strip(", ") or None,
        doi=(meta.get("dois") or [{}])[0].get("value"), arxiv=(meta.get("arxiv_eprints") or [{}])[0].get("value"),
        citations=meta.get("citation_count"), abstract=(meta.get("abstracts") or [{}])[0].get("value"), source="inspire",
        url=f"https://inspirehep.net/literature/{meta['control_number']}" if meta.get("control_number") else None)


def inspire_search(query: str, n: int = 6, sort: str = "cited", since_year: int | None = None,
                   reviews: bool = False, raw: str | None = None) -> list[dict]:
    q = raw or " or ".join(f"t {p}" for p in split_phrases(query))
    if since_year:
        q = f"({q}) and date > {since_year - 1}"
    if reviews:
        q = f"({q}) and tc r"
    params = {"q": q, "sort": "mostcited" if sort == "cited" else "mostrecent", "size": n, "fields": INSPIRE_FIELDS}
    data = get_json("https://inspirehep.net/api/literature?" + urllib.parse.urlencode(params))
    return [inspire_record(h["metadata"]) for h in (data or {}).get("hits", {}).get("hits", [])]


S2_API = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,year,publicationDate,externalIds,citationCount,venue,journal,authors,abstract,openAccessPdf"
OPENALEX_FIELD_TO_S2 = {"31": "Physics", "25": "Materials Science", "16": "Chemistry", "17": "Computer Science",
                        "26": "Mathematics", "13": "Biology", "28": "Biology", "11": "Biology", "27": "Medicine",
                        "22": "Engineering", "21": "Engineering", "19": "Geology", "23": "Environmental Science",
                        "12": "History,Philosophy", "33": "Sociology,Economics"}


def s2_fields(openalex_filter: str | None) -> str | None:
    match = re.fullmatch(r"primary_topic\.field\.id:([\d|]+)", openalex_filter or "")
    if not match:
        return None
    names = [name for fid in match.group(1).split("|") for name in OPENALEX_FIELD_TO_S2.get(fid, "").split(",") if name]
    return ",".join(dict.fromkeys(names)) or None


def s2_record(paper: dict) -> dict:
    ids = paper.get("externalIds") or {}
    journal = paper.get("journal") or {}
    venue = journal.get("name") or paper.get("venue") or ""
    if venue and (journal.get("volume") or "").strip():
        venue += f" {journal['volume'].split()[0]}"
        if journal.get("pages"):
            venue += f", {journal['pages'].split('-')[0].strip()}"
    authors = [a.get("name") for a in paper.get("authors") or []]
    title = re.sub(r"(?<![.\s])\.$", "", (paper.get("title") or "").strip())
    return make_record(
        title=title, authors=authors, n_authors=len(authors), year=paper.get("year"),
        date=paper.get("publicationDate"), venue=venue, doi=ids.get("DOI"), arxiv=ids.get("ArXiv"),
        citations=paper.get("citationCount"), abstract=paper.get("abstract"), source="semanticscholar",
        url=f"https://www.semanticscholar.org/paper/{paper['paperId']}",
        oa_pdf=(paper.get("openAccessPdf") or {}).get("url") or None)


def phrase_tokens(text: str) -> list[str]:
    return [w[:-1] if len(w) > 3 and w.endswith("s") else w for w in re.findall(r"[a-z0-9]+", text.lower())]


def has_phrase(text: str, phrases: list[str]) -> bool:
    words = f" {' '.join(phrase_tokens(text))} "
    return any(f" {' '.join(phrase_tokens(p))} " in words for p in phrases)


def s2_search(query: str, n: int = 6, sort: str = "cited", since_year: int | None = None, reviews: bool = False,
              fields_of_study: str | None = "Physics", title_first: bool = False) -> list[dict]:
    key = os.environ.get("S2_API_KEY")
    headers = {"x-api-key": key} if key else None
    params = {"query": " | ".join(f'"{p}"' for p in split_phrases(query))}
    if since_year:
        params["year"] = f"{since_year}-"
    if reviews:
        params["publicationTypes"] = "Review"
    if fields_of_study:
        params["fieldsOfStudy"] = fields_of_study
    if sort == "relevance":
        params.update(query=" ".join(split_phrases(query)), fields=S2_FIELDS, limit=n)
        data = get_json(f"{S2_API}/paper/search?" + urllib.parse.urlencode(params), headers)
        return [s2_record(p) for p in (data or {}).get("data") or [] if p.get("title")]
    params.update(fields="title,citationCount", sort="citationCount:desc" if sort == "cited" else "publicationDate:desc")
    hits = (get_json(f"{S2_API}/paper/search/bulk?" + urllib.parse.urlencode(params), headers) or {}).get("data") or []
    if title_first:
        hits = sorted(hits, key=lambda h: not has_phrase(h.get("title") or "", split_phrases(query)))
    ids = [h["paperId"] for h in hits[:n]]
    if not ids:
        return []
    text = http_get(f"{S2_API}/paper/batch?fields={S2_FIELDS}", data=json.dumps({"ids": ids}).encode(), headers=headers)
    return [s2_record(p) for p in json.loads(text or "[]") if p and p.get("title")]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, text[end + 4:].lstrip("\n")


def as_list(value) -> list[str]:
    if not value:
        return []
    return value if isinstance(value, list) else str(value).split()


def discover_nodes() -> list[dict]:
    nodes = []

    def walk(directory: Path, depth: int, inherited: dict, parent: str | None):
        for child in sorted(p for p in directory.iterdir() if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")):
            readme = child / "README.md"
            meta = parse_frontmatter(readme.read_text(encoding="utf-8"))[0] if readme.exists() else {}
            merged = {**inherited, **{k: meta[k] for k in INHERITED if meta.get(k)}}
            rel = child.relative_to(KNOWLEDGE).as_posix()
            papers_meta = {}
            papers_file = child / "papers.md"
            if papers_file.exists():
                with papers_file.open(encoding="utf-8") as fh:
                    papers_meta = parse_frontmatter(fh.read(600) + "\n")[0]
            node = {"path": rel, "title": meta.get("title") or child.name.replace("-", " ").title(),
                    "summary": meta.get("summary", ""), "depth": depth, "parent": parent,
                    "query": meta.get("query", ""), "arxiv": as_list(merged.get("arxiv")),
                    "source": merged.get("source", "openalex"), "agent": merged.get("agent", ""),
                    "openalex_filter": merged.get("openalex_filter", DEFAULT_OPENALEX_FILTER),
                    "has_readme": readme.exists(), "papers": int(papers_meta.get("count", 0) or 0),
                    "papers_partial": papers_meta.get("partial") == "true",
                    "papers_updated": papers_meta.get("generated", ""), "children": []}
            nodes.append(node)
            before = len(nodes)
            walk(child, depth + 1, merged, rel)
            node["children"] = [n["path"] for n in nodes[before:] if n["parent"] == rel]

    walk(KNOWLEDGE, 1, {}, None)
    return nodes


def level_name(node: dict) -> str:
    if node["depth"] <= 2:
        return "field" if node["depth"] == 1 else "subfield"
    return "branch" if node["children"] else "topic"


def load_db() -> list[dict]:
    if not PAPERS_DB.exists():
        return []
    return [json.loads(line) for line in PAPERS_DB.read_text(encoding="utf-8").splitlines() if line.strip()]


def save_db(records: list[dict]) -> None:
    LIBRARY.mkdir(exist_ok=True)
    records.sort(key=lambda r: r["key"])
    PAPERS_DB.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")


def merge_into_db(db: list[dict], new: list[dict], node_path: str) -> None:
    by_arxiv = {r["arxiv"]: r for r in db if r.get("arxiv")}
    by_doi = {r["doi"]: r for r in db if r.get("doi")}
    by_key = {r["key"]: r for r in db}
    for rec in new:
        existing = by_arxiv.get(rec.get("arxiv")) if rec.get("arxiv") else None
        existing = existing or (by_doi.get(rec.get("doi")) if rec.get("doi") else None)
        existing = existing or by_key.get(rec["key"])
        if existing is None:
            rec = {**rec, "nodes": [node_path]}
            db.append(rec)
            by_key[rec["key"]] = rec
            if rec.get("arxiv"):
                by_arxiv[rec["arxiv"]] = rec
            if rec.get("doi"):
                by_doi[rec["doi"]] = rec
            continue
        for key, value in rec.items():
            if value and not existing.get(key):
                existing[key] = value
        existing["citations"] = max(existing.get("citations") or 0, rec.get("citations") or 0) or None
        existing["nodes"] = sorted(set(existing.get("nodes", [])) | {node_path})
        if existing.get("arxiv"):
            existing["key"] = f"arxiv:{existing['arxiv']}"


def dedupe(records: list[dict], seen: set[str]) -> list[dict]:
    kept = []
    for rec in records:
        ids = {i for i in (rec.get("arxiv"), rec.get("doi"), rec["title"].lower()) if i}
        if ids & seen or not rec["title"]:
            continue
        seen |= ids
        kept.append(rec)
    return kept


def author_line(rec: dict) -> str:
    authors = rec.get("authors") or []
    if not authors:
        return "Unknown authors"
    shown = ", ".join(authors[:3])
    total = rec.get("n_authors") or len(authors)
    return shown + (" et al." if total > 3 else "")


def link_line(rec: dict) -> str:
    links = []
    if rec.get("arxiv"):
        links.append(f"[arXiv:{rec['arxiv']}](https://arxiv.org/abs/{rec['arxiv']})")
    if rec.get("doi"):
        links.append(f"[doi:{rec['doi']}](https://doi.org/{rec['doi']})")
    if rec.get("oa_pdf") and not rec.get("arxiv"):
        links.append(f"[open-access PDF]({rec['oa_pdf']})")
    if not links and rec.get("url"):
        links.append(f"[source record]({rec['url']})")
    return " · ".join(links) or "_no DOI or arXiv id in the source record_"


def render_paper(i: int, rec: dict, abstract_chars: int = 1400) -> str:
    bits = [f"**Authors:** {author_line(rec)}", f"**Year:** {rec.get('year') or '?'}"]
    if rec.get("venue"):
        bits.append(f"**Venue:** {rec['venue']}")
    if rec.get("citations") is not None:
        bits.append(f"**Citations:** {rec['citations']:,}")
    text = [f"### {i}. {rec['title']}", "- " + " · ".join(bits), f"- **Links:** {link_line(rec)}"]
    abstract = rec.get("abstract") or ""
    if abstract:
        if len(abstract) > abstract_chars:
            abstract = abstract[:abstract_chars].rsplit(" ", 1)[0] + " …"
        text.append(f"\n> {abstract}")
    return "\n".join(text)


PENDING = None


def guarded(fn, any_error: bool = False):
    try:
        return fn()
    except BudgetExhausted:
        return PENDING
    except (urllib.error.URLError, TimeoutError, ConnectionError, ET.ParseError):
        if any_error:
            return PENDING
        raise


S2_FALLBACK_LABEL = "Semantic Scholar (fallback: OpenAlex budget exhausted)"


def with_s2_fallback(primary, fallback) -> tuple[list[dict] | None, str]:
    recs = guarded(primary)
    if recs is PENDING:
        return guarded(fallback, any_error=True), S2_FALLBACK_LABEL
    return recs, "openalex"


def fetch_node(node: dict, n_cited: int, n_rising: int, n_latest: int, n_reviews: int) -> tuple[list[tuple[str, str, list[dict] | None]], list[dict]]:
    query = node["query"] or node["title"]
    source = node["source"]
    level = level_name(node)
    flt, fos = node["openalex_filter"], s2_fields(node["openalex_filter"])
    sections = []
    rising_since = dt.date.today().year - 2
    if level == "topic":
        if source == "inspire":
            cited, cited_src = guarded(lambda: inspire_search(query, n=n_cited)), source
            rising, rising_src = guarded(lambda: inspire_search(query, n=n_rising + 3, since_year=rising_since)), source
        else:
            def openalex_rising():
                recs = openalex_search(query, n=n_rising + 3, since_year=rising_since, extra_filter=flt, scope="title")
                if len(recs) < n_rising + 3:
                    recs += openalex_search(query, n=n_rising + 3, since_year=rising_since, extra_filter=flt)
                return recs

            cited, cited_src = with_s2_fallback(lambda: openalex_search(query, n=n_cited, extra_filter=flt),
                                                lambda: s2_search(query, n=n_cited + 3, fields_of_study=fos))
            rising, rising_src = with_s2_fallback(openalex_rising,
                                                  lambda: s2_search(query, n=n_rising + 3, since_year=rising_since,
                                                                    fields_of_study=fos, title_first=True))
        latest = guarded(lambda: arxiv_search(query, cats=node["arxiv"], n=n_latest + 3, since_days=365), any_error=True)
        seen: set[str] = set()

        def keep(recs, n):
            return PENDING if recs is PENDING else dedupe(recs, seen)[:n]

        sections.append(("Foundational — most cited of all time", f"{cited_src}, sorted by citations", keep(cited, n_cited)))
        sections.append((f"Rising — most cited since {rising_since}", f"{rising_src}, published {rising_since}+, sorted by citations", keep(rising, n_rising)))
        sections.append(("Latest — arXiv, last 12 months", "arXiv API, submitted in the last 365 days, sorted by relevance", keep(latest, n_latest)))
    else:
        if source == "inspire":
            reviews, reviews_src = guarded(lambda: inspire_search(query, n=n_reviews, reviews=True)), source
        else:
            reviews, reviews_src = with_s2_fallback(lambda: openalex_search(query, n=n_reviews, reviews=True, extra_filter=flt),
                                                    lambda: s2_search(query, n=n_reviews, reviews=True, fields_of_study=fos))
        sections.append(("Key reviews — most cited review articles", f"{reviews_src}, review articles, sorted by citations",
                         PENDING if reviews is PENDING else dedupe(reviews, set())))
    papers = [rec for _, _, recs in sections for rec in recs or []]
    return sections, papers


def write_papers_md(node: dict, sections: list[tuple[str, str, list[dict] | None]]) -> tuple[int, bool]:
    count = sum(len(recs or []) for _, _, recs in sections)
    partial = any(recs is PENDING for _, _, recs in sections)
    lines = ["---", f"generated: {today()}", f"node: {node['path']}", f"query: {node['query'] or node['title']}",
             f"source: {node['source']}", f"count: {count}", f"partial: {str(partial).lower()}", "---",
             f"# Papers — {node['title']}", "",
             "> Auto-generated by `python -I scripts/physlib.py fetch`. Every entry came from a live API query "
             "(arXiv, OpenAlex, INSPIRE-HEP or Semantic Scholar), so it exists; relevance is algorithmic, so judge it. "
             "Regenerated on refresh — curate keepers into README.md instead of editing here.", ""]
    number = 1
    for heading, provenance, recs in sections:
        lines += [f"## {heading}", f"*Source: {provenance}.*", ""]
        if recs is PENDING:
            lines += [f"_Pending — this source was unavailable on {today()} (daily API budget exhausted or service outage). "
                      "Complete with `python -I scripts/physlib.py fetch --partial`; for OpenAlex, a free `OPENALEX_API_KEY` "
                      "gives a 10x budget (see docs/SOURCES.md)._", ""]
            continue
        if not recs:
            lines += ["_No results for this query — refine `query:` in README.md and re-fetch._", ""]
        for rec in recs:
            lines += [render_paper(number, rec), ""]
            number += 1
    (KNOWLEDGE / node["path"] / "papers.md").write_text("\n".join(lines), encoding="utf-8")
    return count, partial


def cmd_fetch(args) -> int:
    nodes = [n for n in discover_nodes() if n["has_readme"] and n["depth"] >= 2]
    if args.node:
        prefix = args.node.strip("/").removeprefix("knowledge/")
        nodes = [n for n in nodes if n["path"] == prefix or n["path"].startswith(prefix + "/")]
    if args.missing or args.partial:
        nodes = [n for n in nodes if (args.missing and not (KNOWLEDGE / n["path"] / "papers.md").exists())
                 or (args.partial and n["papers_partial"])]
    if args.level:
        nodes = [n for n in nodes if level_name(n) == args.level]
    if args.limit:
        nodes = nodes[:args.limit]
    out(f"Fetching papers for {len(nodes)} node(s)…")
    db = load_db()
    log = json.loads(FETCH_LOG.read_text(encoding="utf-8")) if FETCH_LOG.exists() else {}
    failures, partials = 0, 0
    for i, node in enumerate(nodes, 1):
        label = f"[{i}/{len(nodes)}] {node['path']} ({level_name(node)}, {node['source']})"
        if args.dry_run:
            out(f"{label} query={node['query'] or node['title']!r} arxiv={node['arxiv']}")
            continue
        try:
            sections, papers = fetch_node(node, args.n_cited, args.n_rising, args.n_latest, args.n_reviews)
            count, partial = write_papers_md(node, sections)
            merge_into_db(db, papers, node["path"])
            partials += partial
            log[node["path"]] = {"date": today(), "count": count, "partial": partial}
            fallback = any(prov.startswith(S2_FALLBACK_LABEL) for _, prov, _ in sections)
            out(f"{label} → {count} papers" + (" (partial: source unavailable)" if partial else "")
                + (" (Semantic Scholar fallback)" if fallback else ""))
        except Exception as err:
            failures += 1
            log[node["path"]] = {"date": today(), "error": str(err)[:300]}
            out(f"{label} → ERROR {err}")
        if i % 10 == 0 or i == len(nodes):
            save_db(db)
            FETCH_LOG.write_text(json.dumps(log, indent=1, sort_keys=True), encoding="utf-8")
    if not args.dry_run:
        save_db(db)
        FETCH_LOG.write_text(json.dumps(log, indent=1, sort_keys=True), encoding="utf-8")
        build_tree(quiet=True)
        out(f"Done. Library now holds {len(db)} unique papers; {failures} node(s) failed; {partials} partial "
            "(rerun `fetch --partial` after the API budget resets or with OPENALEX_API_KEY set).")
    return 1 if failures else 0


def print_results(records: list[dict], abstracts: bool) -> None:
    for i, rec in enumerate(records, 1):
        cites = f" · {rec['citations']:,} citations" if rec.get("citations") is not None else ""
        out(f"{i}. {rec['title']} — {author_line(rec)} ({rec.get('year') or '?'}){cites}")
        out(f"   {rec.get('venue') or ''} · {link_line(rec)}".rstrip(" ·"))
        if abstracts and rec.get("abstract"):
            out(f"   > {rec['abstract'][:900]}{'…' if len(rec['abstract']) > 900 else ''}")


def cmd_search(args) -> int:
    sources = ["arxiv", "openalex", "inspire"] if args.source == "all" else [args.source]
    since_year = args.since
    results, notes = [], []
    if args.raw and args.source == "all" and not args.query:
        sources = ["arxiv"]
        notes.append("--raw with --source all searched arXiv only (INSPIRE uses different syntax; pass --source inspire)")
    s2_fos = None if args.any_field else s2_fields(args.filter or DEFAULT_OPENALEX_FILTER)
    for source in sources:
        try:
            if source == "semanticscholar":
                if not args.query:
                    notes.append("semanticscholar skipped: --raw queries apply to arXiv/INSPIRE only")
                    continue
                recs = s2_search(args.query, n=args.n, sort=args.sort, since_year=since_year, reviews=args.reviews,
                                 fields_of_study=s2_fos)
            elif source == "arxiv":
                since_days = (dt.date.today() - dt.date(since_year, 1, 1)).days if since_year else args.days
                sort = "relevance" if args.sort in ("relevance", "cited") else "recent"
                recs = arxiv_search(args.query, cats=args.cat, n=args.n, since_days=since_days, sort=sort, raw=args.raw)
            elif source == "openalex":
                if not args.query:
                    notes.append("openalex skipped: --raw queries apply to arXiv/INSPIRE only")
                    continue
                sort = "relevance" if args.sort == "relevance" else args.sort
                recs = openalex_search(args.query, n=args.n, sort=sort, since_year=since_year, reviews=args.reviews,
                                       extra_filter=None if args.any_field else (args.filter or DEFAULT_OPENALEX_FILTER))
            else:
                recs = inspire_search(args.query, n=args.n, sort="recent" if args.sort == "recent" else "cited",
                                      since_year=since_year, reviews=args.reviews, raw=args.raw)
        except BudgetExhausted as err:
            notes.append(f"{source} skipped: {err}")
            if source == "openalex" and "semanticscholar" not in sources:
                notes.append("searched Semantic Scholar instead of OpenAlex")
                sources.append("semanticscholar")
            continue
        results.append((source, recs))
    if args.save:
        db = load_db()
        for _, recs in results:
            merge_into_db(db, recs, args.save.strip("/").removeprefix("knowledge/"))
        save_db(db)
    if args.json:
        out(json.dumps({"results": {s: r for s, r in results}, "notes": notes, "saved": bool(args.save)}, ensure_ascii=False, indent=1))
        return 0
    for source, recs in results:
        out(f"## {source} — {len(recs)} result(s) for {args.query or args.raw!r}")
        print_results(recs, args.abstracts)
        out()
    for note in notes:
        out(f"NOTE: {note}")
    if args.save:
        out(f"Saved to library under node {args.save}.")
    return 0


def lookup_one(identifier: str) -> dict | None:
    ident = identifier.strip()
    if re.fullmatch(ARXIV_ID + r"(v\d+)?", normalize_arxiv(ident) or "", re.I):
        aid = normalize_arxiv(ident)
        rec = arxiv_lookup([aid]).get(aid.lower())
        if rec and rec.get("doi"):
            enriched = openalex_by_doi([rec["doi"]]).get(rec["doi"])
            if enriched:
                rec["citations"] = enriched.get("citations")
        return rec
    doi = normalize_doi(ident)
    return openalex_by_doi([doi]).get(doi) or crossref_by_doi(doi)


def cmd_paper(args) -> int:
    ident = args.id.strip()
    rec = None
    for r in load_db():
        if normalize_arxiv(ident) == r.get("arxiv") or normalize_doi(ident) == r.get("doi"):
            rec = r
            break
    if rec is None or args.live:
        rec = lookup_one(ident) or rec
    if not rec:
        out(f"NOT FOUND: {ident} (checked local library, arXiv, OpenAlex, Crossref)")
        return 1
    out(render_paper(1, rec, abstract_chars=10_000))
    if rec.get("nodes"):
        out("\n- **Filed under:** " + ", ".join(rec["nodes"]))
    return 0


def cmd_fulltext(args) -> int:
    FULLTEXT.mkdir(parents=True, exist_ok=True)
    ident = args.id.strip()
    aid = normalize_arxiv(ident)
    if aid and re.fullmatch(ARXIV_ID, aid, re.I):
        url = f"https://arxiv.org/pdf/{aid}"
        name = aid.replace("/", "_")
    else:
        rec = lookup_one(ident)
        if rec and rec.get("arxiv"):
            url, name = f"https://arxiv.org/pdf/{rec['arxiv']}", rec["arxiv"].replace("/", "_")
        elif rec and rec.get("oa_pdf"):
            url, name = rec["oa_pdf"], re.sub(r"[^\w.-]", "_", rec["doi"])
        else:
            out(f"No open-access full text found for {ident}. Landing page: https://doi.org/{normalize_doi(ident)}")
            return 1
    target = FULLTEXT / f"{name}.pdf"
    if target.exists() and not args.force:
        out(str(target))
        return 0
    data = http_get(url, accept="application/pdf", binary=True)
    if not data or not data.startswith(b"%PDF"):
        out(f"Download did not return a PDF ({url}). Try reading {url.replace('/pdf/', '/abs/')} with WebFetch.")
        return 1
    target.write_bytes(data)
    out(str(target))
    return 0


TITLE_STOPWORDS = {"a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "by", "at", "from", "as", "its",
                   "der", "die", "das", "und", "zur", "von", "des", "im", "einen", "eine", "ueber"}


def title_similarity(cited: str, record: str) -> float:
    def norm(s: str) -> str:
        s = re.sub(r"\$[^$]*\$|\\[a-zA-Z]+", " ", s.lower())
        return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())
    na, nb = norm(cited), norm(record)
    if not na or not nb:
        return 0.0
    if na == nb or (len(na.split()) >= 4 and re.sub(r"^(?:[ivxlcdm]+|\d+) ", "", nb).startswith(na)):
        return 1.0
    ratio = difflib.SequenceMatcher(None, na, nb).ratio()
    cited_words = [w for w in na.split() if w not in TITLE_STOPWORDS]
    record_words = {w for w in nb.split() if w not in TITLE_STOPWORDS}
    if len(cited_words) < 3 or not record_words:
        return ratio
    cited_coverage = sum(w in record_words for w in cited_words) / len(cited_words)
    record_coverage = len(set(cited_words) & record_words) / len(record_words)
    return max(ratio, cited_coverage) if cited_coverage >= 0.85 and record_coverage >= 0.3 else ratio


def collect_refs(paths: list[Path]) -> list[dict]:
    refs = []
    for path in paths:
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            matches = [(m.start(), m.end(), "arxiv", normalize_arxiv(m.group(1))) for m in ARXIV_REF.finditer(line)]
            matches += [(m.start(), m.end(), "doi", normalize_doi(m.group(1))) for m in DOI_REF.finditer(line)]
            seg_start, title, year = 0, None, None
            for start, end, kind, ident in sorted(matches):
                segment = line[seg_start:start]
                titles, years = QUOTED_TITLE.findall(segment), YEAR_IN_PARENS.findall(segment)
                title = titles[-1] if titles else title
                year = int(years[-1]) if years else year
                seg_start = end
                refs.append({"file": display_path(path), "line": lineno, "kind": kind, "id": ident,
                             "title": title, "year": year})
    return refs


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def year_consistent(kind: str, cited: int, recorded: int) -> bool:
    if kind == "arxiv":
        return recorded - 1 <= cited <= recorded + 5
    return abs(cited - recorded) <= 1


def cache_key(kind: str, ident: str) -> str:
    return f"{kind}:{ident.lower()}"


def cmd_verify(args) -> int:
    if args.stdin:
        fd, scratch = tempfile.mkstemp(prefix="physlib-verify-", suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(sys.stdin.read())
        files = [Path(scratch)]
    elif args.paths:
        files = [Path(p).resolve() for p in args.paths]
        files = [f for p in files for f in (sorted(p.rglob("*.md")) if p.is_dir() else [p])]
    else:
        files = [p for p in sorted(ROOT.rglob("*.md")) if ".claude" not in p.parts or "skills" in p.parts or "agents" in p.parts]
        files = [p for p in files if not {"fulltext", "scratch"} & set(p.parts) and "-workspace" not in str(p)
                 and p.resolve().parent != LIBRARY.resolve() and not any(part.startswith(CODEX_PREFIX) for part in p.parts)
                 and p.resolve() != CONNECTIONS_MD.resolve()]
    if not args.all:
        files = [f for f in files if f.name != "papers.md"]
    refs = collect_refs(files)
    cache = json.loads(VERIFY_CACHE.read_text(encoding="utf-8")) if VERIFY_CACHE.exists() else {}
    unique = {(r["kind"], r["id"]) for r in refs}
    pending_arxiv = sorted(i for k, i in unique if k == "arxiv" and (args.recheck or not cache.get(cache_key(k, i), {}).get("ok")))
    pending_doi = sorted(i for k, i in unique if k == "doi" and (args.recheck or not cache.get(cache_key(k, i), {}).get("ok")))
    out(f"Verifying {len(refs)} reference(s) in {len(files)} file(s): {len(pending_arxiv)} arXiv + {len(pending_doi)} DOI lookups needed.")
    found_arxiv = arxiv_lookup(pending_arxiv)
    for aid in pending_arxiv:
        rec = found_arxiv.get(aid.lower())
        cache[cache_key("arxiv", aid)] = ({"ok": True, "title": rec["title"], "year": rec["year"], "checked": today()}
                                          if rec else {"ok": False, "checked": today()})
    found = openalex_by_doi(pending_doi)
    for doi in pending_doi:
        rec = found.get(doi) or crossref_by_doi(doi)
        if rec:
            cache[cache_key("doi", doi)] = {"ok": True, "title": rec["title"], "year": rec["year"], "checked": today()}
        elif doi_resolves(doi):
            cache[cache_key("doi", doi)] = {"ok": True, "title": None, "year": None, "checked": today(), "note": "resolves at doi.org; no metadata"}
        else:
            cache[cache_key("doi", doi)] = {"ok": False, "checked": today()}
    LIBRARY.mkdir(exist_ok=True)
    VERIFY_CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    problems, ok = [], 0
    for ref in refs:
        entry = cache.get(cache_key(ref["kind"], ref["id"]), {})
        status = "OK"
        detail = ""
        if not entry.get("ok"):
            status = "NOT_FOUND"
        elif ref["title"] and entry.get("title") and title_similarity(ref["title"], entry["title"]) < 0.6:
            status, detail = "TITLE_MISMATCH", f"cited “{ref['title']}” but {ref['kind']} is “{entry['title']}”"
        elif ref["year"] and entry.get("year") and not year_consistent(ref["kind"], ref["year"], int(entry["year"])):
            status, detail = "YEAR_MISMATCH", f"cited {ref['year']} but record says {entry['year']}"
        if status == "OK":
            ok += 1
        else:
            problems.append({**ref, "status": status, "detail": detail})
    lines = ["# Reference verification report", "", f"- Run: {today()}", f"- Files scanned: {len(files)}",
             f"- References checked: {len(refs)} ({len(unique)} unique)", f"- Passed: {ok}", f"- Problems: {len(problems)}", ""]
    if problems:
        lines += ["| Status | File:line | ID | Detail |", "|---|---|---|---|"]
        lines += [f"| {p['status']} | {p['file']}:{p['line']} | {p['kind']}:{p['id']} | {p['detail']} |" for p in problems]
    else:
        lines.append("All references resolve to real records, and every quoted title and year matches.")
    full_scan = not (args.paths or args.stdin)
    if full_scan:
        VERIFY_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for p in problems:
        out(f"{p['status']:15} {p['file']}:{p['line']}  {p['kind']}:{p['id']}  {p['detail']}")
    out(f"{ok}/{len(refs)} references passed." + (f" Report: {VERIFY_REPORT.relative_to(ROOT).as_posix()}" if full_scan else ""))
    return 1 if problems else 0


def check_links(path: Path) -> list[str]:
    broken = []
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", "", path.read_text(encoding="utf-8"), flags=re.S)
    for target in MD_LINK.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        resolved = (path.parent / urllib.parse.unquote(target.split("#")[0])).resolve()
        if not resolved.exists():
            broken.append(target)
    return broken


def tree_problems(nodes: list[dict]) -> list[str]:
    problems = []
    for node in nodes:
        base = KNOWLEDGE / node["path"]
        if not node["has_readme"]:
            problems.append(f"{node['path']}: missing README.md")
            continue
        meta = parse_frontmatter((base / "README.md").read_text(encoding="utf-8"))[0]
        for key in ("title", "summary"):
            if not meta.get(key):
                problems.append(f"{node['path']}: README.md frontmatter lacks `{key}`")
        if level_name(node) == "topic" and not meta.get("query"):
            problems.append(f"{node['path']}: topic lacks `query` (used to fetch papers)")
        for md in [base / "README.md", *sorted((base / "reviews").glob("*.md"))]:
            problems += [f"{md.relative_to(ROOT).as_posix()}: broken link → {t}" for t in check_links(md)]
    for md in sorted(CONNECTIONS_DIR.rglob("*.md")) if CONNECTIONS_DIR.exists() else []:
        problems += [f"{md.relative_to(ROOT).as_posix()}: broken link → {t}" for t in check_links(md)]
        if md.parent == THEMES_DIR:
            meta = parse_frontmatter(md.read_text(encoding="utf-8"))[0]
            problems += [f"{md.relative_to(ROOT).as_posix()}: theme frontmatter lacks `{k}`" for k in ("title", "summary", "fields") if not meta.get(k)]
    return problems


def build_tree(quiet: bool = False, strict: bool = False) -> int:
    nodes = discover_nodes()
    by_path = {n["path"]: n for n in nodes}
    fields = [n for n in nodes if n["depth"] == 1]
    subfields = [n for n in nodes if n["depth"] == 2]
    topics = [n for n in nodes if n["depth"] >= 3]
    total_papers = len(load_db())
    lines = ["# Knowledge tree", "",
             "> Auto-generated by `python -I scripts/physlib.py tree` (also refreshed by the optional PostToolUse hook whenever a knowledge note changes). "
             "Do not edit by hand.", "",
             f"**{len(fields)} fields · {len(subfields)} subfields · {len(topics)} topics · {total_papers:,} unique papers in the library**", "",
             "Each node is a folder with `README.md` (curated notes) and `papers.md` (live-fetched literature). "
             "Paper counts are shown in parentheses.", ""]

    def emit(node: dict, indent: int):
        count = f" ({node['papers']})" if node["papers"] else ""
        summary = f" — {node['summary']}" if node["summary"] else ""
        link = f"knowledge/{node['path']}/README.md"
        if indent == 0:
            agent = f" · specialist: `{node['agent']}`" if node["agent"] else ""
            lines.extend([f"## [{node['title']}]({link}){count}", f"{node['summary']}{agent}", ""])
        else:
            lines.append("  " * (indent - 1) + f"- [{node['title']}]({link}){count}{summary}")
        for child in node["children"]:
            emit(by_path[child], indent + 1)
        if indent == 0:
            lines.append("")

    for field in fields:
        emit(field, 0)
    TREE_MD.write_text("\n".join(lines), encoding="utf-8")
    index = [{k: n[k] for k in ("path", "title", "summary", "depth", "parent", "children", "query", "arxiv",
                                "source", "agent", "papers", "papers_partial", "papers_updated")} | {"level": level_name(n)} for n in nodes]
    LIBRARY.mkdir(exist_ok=True)
    INDEX_JSON.write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")
    codices = build_codices(nodes)
    links = build_connections(nodes)
    problems = tree_problems(nodes) if (strict or not quiet) else []
    if not quiet:
        out(f"TREE.md rebuilt: {len(fields)} fields, {len(subfields)} subfields, {len(topics)} topics, {total_papers} papers.")
        sizes = sorted(size for _, size in codices)
        out(f"{len(codices)} branch codices rebuilt in .claude/skills/{CODEX_PREFIX}*/ "
            f"({sizes[0] // 1000}–{sizes[-1] // 1000} kB each)." if codices else "No branch codices built.")
        out(f"CONNECTIONS.md + codex-atlas rebuilt ({links['atlas_size'] // 1000} kB): {len(links['edges'])} links, "
            f"{len(links['concepts'])} concepts, {len(links['latent_across'])} + {len(links['latent_within'])} latent candidates, "
            f"{len(links['themes'])} themes.")
        no_papers = [n["path"] for n in nodes if n["depth"] >= 2 and not n["papers"]]
        if no_papers:
            out(f"{len(no_papers)} node(s) have no papers yet (run `fetch --missing`).")
        for p in problems:
            out(f"PROBLEM  {p}")
        out(f"{len(problems)} structural problem(s).")
    return 1 if (strict and problems) else 0


def cmd_tree(args) -> int:
    return build_tree(quiet=False, strict=args.check)


CODEX_SKILLS = ROOT / ".claude" / "skills"
CODEX_PREFIX = "codex-"
CODEX_DROP_SECTIONS = {"Topics", "Branch map"}
MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]*\$)", re.S)
LINK_PARTS = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
PAPER_HEADING = re.compile(r"^### \d+\. (.+)$")
PAPER_ID = re.compile(r"\[((?:arXiv|doi):[^\]]+)\]")


def outside_math(text: str, fn) -> str:
    return "".join(part if i % 2 else fn(part) for i, part in enumerate(MATH.split(text)))


def link_target(source_dir: Path, target: str) -> Path | None:
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return None
    return (source_dir / urllib.parse.unquote(target.split("#")[0])).resolve()


def repo_relative_links(text: str, source_dir: Path) -> str:
    def fix(match):
        resolved = link_target(source_dir, match.group(2))
        if resolved is None or ROOT not in resolved.parents:
            return match.group(0)
        return f"[{match.group(1)}]({resolved.relative_to(ROOT).as_posix()})"
    return outside_math(text, lambda part: LINK_PARTS.sub(fix, part))


def node_edges(nodes: list[dict]) -> list[tuple[str, str]]:
    paths = {n["path"] for n in nodes}
    edges = set()
    for node in nodes:
        if not node["has_readme"]:
            continue
        readme = KNOWLEDGE / node["path"] / "README.md"
        src = node["path"]
        for target in MD_LINK.findall(MATH.sub("", readme.read_text(encoding="utf-8"))):
            resolved = link_target(readme.parent, target)
            if resolved is None or resolved.name != "README.md" or KNOWLEDGE not in resolved.parents:
                continue
            dst = resolved.parent.relative_to(KNOWLEDGE).as_posix()
            if dst in paths and dst != src and not dst.startswith(src + "/") and not src.startswith(dst + "/"):
                edges.add((src, dst))
    return sorted(edges)


def surname(name: str) -> str:
    name = name.strip()
    if "collaboration" in name.lower():
        return name
    return name.split(",")[0].strip() if "," in name else (name.split() or ["?"])[-1]


def short_authors(rec: dict | None) -> str:
    authors = (rec or {}).get("authors") or []
    if not authors:
        return "Unknown"
    total = rec.get("n_authors") or len(authors)
    if total == 1:
        return surname(authors[0])
    if total == 2 and len(authors) == 2:
        return f"{surname(authors[0])} & {surname(authors[1])}"
    return f"{surname(authors[0])} et al."


def papers_digest(node_dir: Path, by_key: dict) -> list[str]:
    papers_file = node_dir / "papers.md"
    if not papers_file.exists():
        return []
    sections: list[tuple[str, list[str]]] = []
    for block in re.split(r"\n(?=## |### )", parse_frontmatter(papers_file.read_text(encoding="utf-8"))[1]):
        head = block.splitlines()[0] if block else ""
        if head.startswith("## "):
            sections.append((head[3:].split(" — ")[0].strip(), []))
            continue
        match = PAPER_HEADING.match(head)
        if not match or not sections:
            continue
        ids = PAPER_ID.findall(block)
        rec = next((by_key[i.lower()] for i in ids if i.lower() in by_key), None)
        year = re.search(r"\*\*Year:\*\* (\S+)", block)
        cites = re.search(r"\*\*Citations:\*\* ([\d,]+)", block)
        title = match.group(1).strip()
        title = title if len(title) <= 110 else title[:107].rsplit(" ", 1)[0] + "…"
        sections[-1][1].append(f"{short_authors(rec)} ({year.group(1) if year else '?'}) \"{title}\" "
                               f"{ids[0] if ids else '(no id)'}" + (f" [{cites.group(1)}]" if cites else ""))
    return [f"- *{name}:* " + "; ".join(items) for name, items in sections if items]


def codex_section(node: dict, by_key: dict) -> list[str]:
    base = KNOWLEDGE / node["path"]
    kept, dropping, started = [], False, False
    for line in parse_frontmatter((base / "README.md").read_text(encoding="utf-8"))[1].splitlines():
        if line.startswith("# "):
            continue
        if not started and line.startswith(">") and ("papers.md" in line or "Part of" in line):
            continue
        started = started or bool(line.strip())
        if line.startswith("## "):
            dropping = line[3:].strip() in CODEX_DROP_SECTIONS
            line = "#### " + line[3:]
        if not dropping:
            kept.append(line)
    heading = "## Field overview" if node["depth"] == 1 else ("##" if node["depth"] == 2 else "###") + f" {node['title']}"
    lines = [f"{heading} · `knowledge/{node['path']}`", "", repo_relative_links("\n".join(kept).strip(), base), ""]
    literature = papers_digest(base, by_key)
    if literature:
        lines += ["**Literature index** (from papers.md; algorithmic relevance, cites in brackets):", *literature, ""]
    return lines


def build_codices(nodes: list[dict]) -> list[tuple[str, int]]:
    by_path = {n["path"]: n for n in nodes}
    by_key = {}
    for rec in load_db():
        if rec.get("arxiv"):
            by_key[f"arxiv:{rec['arxiv'].lower()}"] = rec
        if rec.get("doi"):
            by_key[f"doi:{rec['doi'].lower()}"] = rec
    edges = node_edges(nodes)
    registry = load_registry(by_path)
    built = []
    for field in (n for n in nodes if n["depth"] == 1 and n["has_readme"]):
        members = [n for n in nodes if n["has_readme"] and (n["path"] == field["path"] or n["path"].startswith(field["path"] + "/"))]
        n_sub = sum(1 for n in members if n["depth"] == 2)
        n_top = sum(1 for n in members if n["depth"] >= 3)
        n_papers = sum(n["papers"] for n in members)
        name = CODEX_PREFIX + field["path"]
        agent = field["agent"] or "the field specialist"
        description = f"Full curated knowledge of {field['title']} ({n_sub} subfields, {n_top} topics), preloaded into {agent}."
        lines = ["---", f"name: {name}", f"description: {json.dumps(description, ensure_ascii=False)}", "user-invocable: false", "---",
                 f"# Codex — {field['title']}", "",
                 f"> Generated by `python -I scripts/physlib.py tree` on {today()} from the curated notes under `knowledge/{field['path']}/` "
                 "and their `papers.md`. Do not edit: edit the notes and rebuild. Links are repo-relative paths; Read them for full "
                 "abstracts (`papers.md`) and literature reviews (`reviews/`).", "",
                 f"**Specialist:** `{agent}` · {n_sub} subfields · {n_top} topics · {n_papers} paper entries", "", "## Contents", ""]
        lines += ["  " * (n["depth"] - 2) + f"- {n['title']} — {n['summary']}" for n in members[1:]]
        lines.append("")
        for node in members:
            lines += codex_section(node, by_key)
        inside = {n["path"] for n in members}
        groups = (("Out to other branches", "→", [(s, d) for s, d in edges if s in inside and d not in inside]),
                  ("In from other branches", "←", [(d, s) for s, d in edges if d in inside and s not in inside]),
                  ("Between this branch's subfields", "→", [(s, d) for s, d in edges if s in inside and d in inside
                                                            and s.split("/")[:2] != d.split("/")[:2]]))
        lines += ["## Bridges", "",
                  "Cross-links in the curated notes, grouped by the node in this branch (`→` it links out, `←` it is linked from); "
                  "paths are under `knowledge/`. Report the bridges you use to the orchestrator.", ""]
        for label, arrow, pairs in groups:
            lines += [f"#### {label} ({len(pairs)})", ""]
            for own in sorted({a for a, _ in pairs}):
                others = ", ".join(f"{by_path[b]['title']} (`{b}`)" for a, b in pairs if a == own)
                lines.append(f"- **{by_path[own]['title']}** {arrow} {others}")
            lines.append("")
        classified = [r for r in registry if r["a"] in inside or r["b"] in inside]
        if classified:
            lines += [f"#### Classified connections ({len(classified)})", "",
                      "From `connections/registry.jsonl`, found by the connections analysts and checked by the specialists. "
                      "Format: name · kind · strength 1–3 · the other note (field code). "
                      "Details: `python -I scripts/physlib.py connections <note>`.", ""]
            for r in sorted(classified, key=lambda r: (-r.get("strength", 1), r["name"])):
                other = r["b"] if r["a"] in inside else r["a"]
                lines.append(f"- {r['name']} · {r['kind']} · {r.get('strength', 1)} · {by_path[other]['title']} ({other[:2]})")
            lines.append("")
        text = "\n".join(lines).rstrip() + "\n"
        target = CODEX_SKILLS / name / "SKILL.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            target.write_text(text, encoding="utf-8")
        built.append((name, len(text)))
    return built


CONNECTIONS_DIR = ROOT / "connections"
CONCEPTS_MD = CONNECTIONS_DIR / "concepts.md"
THEMES_DIR = CONNECTIONS_DIR / "themes"
CONNECTIONS_JSON = LIBRARY / "connections.json"
CONNECTIONS_MD = ROOT / "CONNECTIONS.md"
ATLAS_SKILL = CODEX_SKILLS / "codex-atlas" / "SKILL.md"
AGENTS_DIR = ROOT / ".claude" / "agents"
DASHES = str.maketrans({"–": "-", "—": "-", "‐": "-", "‑": "-"})
KEY_EQUATIONS = re.compile(r"Key equations\.?\**\s*\n*\s*\$\$(.+?)\$\$", re.S)


def load_concepts() -> list[dict]:
    if not CONCEPTS_MD.exists():
        return []
    concepts = []
    for line in CONCEPTS_MD.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or len(cells) != 3 or cells[0] in ("Concept", "") or set(cells[0]) <= set("-: "):
            continue
        terms = [t.strip().lower().translate(DASHES) for t in cells[1].split(";") if t.strip()]
        concepts.append({"name": cells[0], "idea": cells[2], "terms": terms,
                         "pattern": re.compile("|".join(r"(?<![a-z0-9])" + re.escape(t) for t in terms))})
    return concepts


def node_text(node: dict) -> str:
    meta, body = parse_frontmatter((KNOWLEDGE / node["path"] / "README.md").read_text(encoding="utf-8"))
    text = re.sub(r"\]\([^)]*\)", "]", MATH.sub(" ", f"{meta.get('title', '')}. {meta.get('summary', '')}. {body}"))
    return text.lower().translate(DASHES)


def related(a: str, b: str) -> bool:
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def load_themes() -> list[dict]:
    themes = []
    for path in sorted(THEMES_DIR.glob("*.md")) if THEMES_DIR.exists() else []:
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))[0]
        themes.append({"path": path.relative_to(ROOT).as_posix(), "title": meta.get("title", path.stem),
                       "summary": meta.get("summary", ""), "fields": as_list(meta.get("fields"))})
    return themes


def roster() -> list[tuple[str, str]]:
    rows = []
    for path in sorted(AGENTS_DIR.glob("*.md")) if AGENTS_DIR.exists() else []:
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))[0]
        if meta.get("name") and meta.get("description"):
            rows.append((meta["name"], meta["description"].split(". Use ")[0].rstrip(".")))
    return rows


def connection_data(nodes: list[dict]) -> dict:
    import math
    by_path = {n["path"]: n for n in nodes}
    indexed = [n for n in nodes if n["has_readme"] and n["depth"] >= 2]
    concepts = load_concepts()
    has = {n["path"]: set() for n in indexed}
    for node in indexed:
        text = node_text(node)
        has[node["path"]] = {c["name"] for c in concepts if c["pattern"].search(text)}
    df = {c["name"]: sum(1 for p in has if c["name"] in has[p]) for c in concepts}
    idf = {name: math.log(len(indexed) / count) for name, count in df.items() if count}
    weight = {p: sum(idf.get(c, 0) for c in cs) or 1.0 for p, cs in has.items()}
    edges = node_edges(nodes)
    registry = load_registry(by_path)
    linked = set()
    for s, d in edges + [(r["a"], r["b"]) for r in registry]:
        for a in (s, *[x for x in by_path if s.startswith(x + "/")]):
            for b in (d, *[x for x in by_path if d.startswith(x + "/")]):
                linked.add(frozenset((a, b)))
    across, within = [], []
    paths = sorted(has)
    for i, a in enumerate(paths):
        for b in paths[i + 1:]:
            shared = has[a] & has[b]
            if len(shared) < 3 or related(a, b) or frozenset((a, b)) in linked:
                continue
            same_field = a.split("/")[0] == b.split("/")[0]
            if same_field and a.split("/")[1] == b.split("/")[1]:
                continue
            score = sum(idf[c] for c in shared) / math.sqrt(weight[a] * weight[b])
            (within if same_field else across).append({"a": a, "b": b, "score": round(score, 3),
                                                        "shared": sorted(shared, key=lambda c: -idf[c])})
    across.sort(key=lambda c: -c["score"])
    within.sort(key=lambda c: -c["score"])
    shared_lit: dict[tuple[str, str], list[dict]] = {}
    for rec in load_db():
        rec_nodes = sorted(set(rec.get("nodes") or []))
        for i, a in enumerate(rec_nodes):
            for b in rec_nodes[i + 1:]:
                if a.split("/")[0] != b.split("/")[0] and a in by_path and b in by_path:
                    shared_lit.setdefault((a, b), []).append(rec)
    literature = sorted(({"a": a, "b": b, "papers": [{"title": r["title"], "year": r.get("year"), "citations": r.get("citations") or 0,
                                                       "id": f"arXiv:{r['arxiv']}" if r.get("arxiv") else f"doi:{r.get('doi')}"} for r in recs]}
                         for (a, b), recs in shared_lit.items()),
                        key=lambda x: (-len(x["papers"]), -max(p["citations"] for p in x["papers"])))
    fields = [n["path"] for n in nodes if n["depth"] == 1]
    pair_links = {frozenset(e) for e in edges if e[0].split("/")[0] != e[1].split("/")[0]}
    matrix = {f: {g: 0 for g in fields} for f in fields}
    for pair in pair_links:
        a, b = sorted(pair)
        fa, fb = a.split("/")[0], b.split("/")[0]
        matrix[fa][fb] += 1
        matrix[fb][fa] += 1
    concept_index = {c["name"]: {"idea": c["idea"], "terms": c["terms"], "nodes": sorted(p for p in has if c["name"] in has[p])}
                     for c in concepts}
    return {"generated": today(), "edges": edges, "matrix": matrix, "concepts": concept_index,
            "node_concepts": {p: sorted(cs) for p, cs in has.items()}, "latent_across": across, "latent_within": within, "registry": registry,
            "shared_literature": literature, "themes": load_themes()}


def atlas_sections(data: dict, by_path: dict) -> list[str]:
    fields = list(data["matrix"])
    code = lambda p: p.split("/")[0][:2]
    title = lambda p: by_path[p]["title"]
    lines = ["## Link matrix", "",
             "Distinct cross-links between notes of two fields, either direction (generated from the curated *Connections* and *See also* sections).", "",
             "| | " + " | ".join(code(f) for f in fields) + " |", "|---" * (len(fields) + 1) + "|"]
    for f in fields:
        lines.append(f"| **{code(f)}** | " + " | ".join("·" if f == g else str(data["matrix"][f][g] or "") for g in fields) + " |")
    lines += ["", "Field codes: " + " · ".join(f"{code(f)} {by_path[f]['title']}" for f in fields), ""]
    field_concepts = {}
    for name, entry in data["concepts"].items():
        for p in entry["nodes"]:
            field_concepts.setdefault(code(p), set()).add(name)
    weak = sorted(((data["matrix"][f][g], f, g) for i, f in enumerate(fields) for g in fields[i + 1:] if data["matrix"][f][g] <= 1),
                  key=lambda t: (t[0], -len(field_concepts.get(code(t[1]), set()) & field_concepts.get(code(t[2]), set()))))
    lines += ["## Structural gaps", "",
              "Field pairs with at most one written cross-link, ordered by how many curated concepts they nonetheless share. "
              "These are the first places to look for missing bridges.", ""]
    for count, f, g in weak:
        shared = field_concepts.get(code(f), set()) & field_concepts.get(code(g), set())
        best = next((r for r in data["latent_across"] if {code(r["a"]), code(r["b"])} == {code(f), code(g)}), None)
        lead = f"; top candidate {title(best['a'])} ↔ {title(best['b'])}" if best else ""
        lines.append(f"- **{code(f)} {by_path[f]['title']} ↔ {code(g)} {by_path[g]['title']}** — {count} link(s), {len(shared)} shared concepts{lead}")
    lines += ["", "## Concept index", "",
              "Each curated concept from `connections/concepts.md`, with the notes that mention it, grouped by field code. "
              "Concepts spanning many fields are the main highways between branches.", ""]
    ranked = sorted(data["concepts"].items(), key=lambda kv: (-len({code(p) for p in kv[1]["nodes"]}), -len(kv[1]["nodes"])))
    for name, entry in ranked:
        groups = {}
        for p in entry["nodes"]:
            groups.setdefault(code(p), []).append(title(p))
        spread = "; ".join(f"{fc}: " + ", ".join(ts[:5]) + (f" +{len(ts) - 5}" if len(ts) > 5 else "") for fc, ts in sorted(groups.items()))
        lines.append(f"- **{name}** — {entry['idea']} *({len(groups)} fields, {len(entry['nodes'])} notes)* {spread}")
    for key, label, limit in (("latent_across", "Latent bridges across branches", 60), ("latent_within", "Latent bridges within branches", 30)):
        rows = data[key][:limit]
        lines += ["", f"## {label}", "",
                  "Pairs of notes that share several rare concepts but have no cross-link between them, or between notes inside them. "
                  "These are candidates, not findings: test each one physically before proposing a cross-link.", ""]
        lines += [f"{i}. {title(r['a'])} (`{r['a']}`) ↔ {title(r['b'])} (`{r['b']}`) — {r['score']:.2f}; shares {', '.join(r['shared'][:6])}"
                  for i, r in enumerate(rows, 1)]
    lines += ["", "## Shared literature", "",
              "Note pairs from different fields whose fetched literature contains the same paper. Relevance in `papers.md` is algorithmic, "
              "so this is weak evidence that sometimes exposes a real bridge.", ""]
    for r in data["shared_literature"][:40]:
        top = max(r["papers"], key=lambda p: p["citations"])
        lines.append(f"- {title(r['a'])} ↔ {title(r['b'])} — {len(r['papers'])} shared, e.g. \"{top['title'][:90]}\" ({top['year']}) {top['id']}")
    registry = data.get("registry", [])
    if registry:
        kinds = {}
        for r in registry:
            kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
        across = sum(1 for r in registry if r["a"][:2] != r["b"][:2])
        lines += ["", "## Classified connections", "",
                  f"{len(registry)} connections in `connections/registry.jsonl` ({across} across branches, {len(registry) - across} within), "
                  "found by the connections analysts and checked by the branch specialists. By kind: "
                  + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items(), key=lambda kv: -kv[1])) + ". "
                  "All of them are drawn in [the interactive map](connections/map.html) ([static SVG](connections/map.svg)). "
                  "The deepest (strength 3) are listed below; query any note with `physlib.py connections`.", ""]
        for r in sorted((r for r in registry if r.get("strength") == 3), key=lambda r: (r["a"][:2], r["b"][:2], r["name"])):
            lines.append(f"- **{r['name']}** ({r['kind']}) — {title(r['a'])} ↔ {title(r['b'])}")
    lines += ["", "## Curated themes", ""]
    lines += [f"- [{t['title']}]({t['path']}) — {t['summary']} *(fields {', '.join(t['fields'])})*" for t in data["themes"]] or \
             ["_None yet. The connections analyst proposes them; write them as `connections/themes/<slug>.md`._"]
    return lines


def field_map(nodes: list[dict]) -> list[str]:
    lines = []
    for node in nodes:
        if not node["has_readme"]:
            continue
        if node["depth"] == 1:
            lines += ["", f"### {node['path'][:2]} {node['title']} · `{node['agent']}`", node["summary"], ""]
            continue
        body = parse_frontmatter((KNOWLEDGE / node["path"] / "README.md").read_text(encoding="utf-8"))[1]
        eq = KEY_EQUATIONS.search(body)
        eq_text = " ".join(eq.group(1).split()) if eq else ""
        eq_text = f" · ${eq_text[:180]}{'…' if len(eq_text) > 180 else ''}$" if eq_text and len(eq_text) <= 180 else ""
        rel = node["path"].split("/", 1)[1]
        lines.append("  " * (node["depth"] - 2) + f"- **{node['title']}** `{rel}` — {node['summary']}{eq_text}")
    return lines


def build_connections(nodes: list[dict]) -> dict:
    data = connection_data(nodes)
    by_path = {n["path"]: n for n in nodes}
    LIBRARY.mkdir(exist_ok=True)
    CONNECTIONS_JSON.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    sections = atlas_sections(data, by_path)
    n_cross = sum(sum(row.values()) for row in data["matrix"].values()) // 2
    stats = (f"**{n_cross} cross-branch links · {len(data['concepts'])} curated concepts · {len(data['latent_across'])} latent cross-branch "
             f"and {len(data['latent_within'])} within-branch candidates · {len(data['themes'])} curated themes**")
    CONNECTIONS_MD.write_text("\n".join(["# Connections atlas", "",
                                         "> Auto-generated by `python -I scripts/physlib.py tree` from the curated notes, `connections/concepts.md`, "
                                         "`connections/themes/` and `library/papers.jsonl`. Do not edit by hand. Query it with "
                                         "`python -I scripts/physlib.py connections <node|field> [other]`. Every connection is drawn in "
                                         "[connections/map.html](connections/map.html) (interactive) and [connections/map.svg](connections/map.svg).",
                                         "", stats, "", *sections]) + "\n", encoding="utf-8")
    description = "Cross-branch atlas of all 12 fields (roster, field map, links, concepts, latent bridges), preloaded into connections-analyst."
    team = [f"- `{name}` — {desc}" for name, desc in roster()]
    atlas = ["---", "name: codex-atlas", f"description: {json.dumps(description)}", "user-invocable: false", "---",
             "# Atlas — every branch at once", "",
             f"> Generated by `python -I scripts/physlib.py tree` on {today()}. Do not edit. It is the cross-branch digest: for one branch in full, "
             "load its codex with the Skill tool (`codex-<NN-field>`); for any node, Read `knowledge/<path>/README.md`; "
             "to query the graph, run `python -I scripts/physlib.py connections …`.", "", stats, "",
             "## Roster", "", "The agents that report to the orchestrator, with their scope.", "", *team, "",
             "## Field map", "", "Every subfield and topic: title, path under its field, summary, and its first key equation when short.",
             *field_map(nodes), "", *sections]
    ATLAS_SKILL.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(atlas) + "\n"
    if not ATLAS_SKILL.exists() or ATLAS_SKILL.read_text(encoding="utf-8") != text:
        ATLAS_SKILL.write_text(text, encoding="utf-8")
    data["atlas_size"] = len(text)
    build_map(nodes, data["edges"])
    return data


REGISTRY = CONNECTIONS_DIR / "registry.jsonl"
MAP_TEMPLATE = ROOT / "scripts" / "connections_map.html"
MAP_HTML = CONNECTIONS_DIR / "map.html"
MAP_SVG = CONNECTIONS_DIR / "map.svg"
KINDS = ("identity", "mechanism", "analogy", "duality", "method transfer", "shared object", "historical")
RING_R = 560.0
FIELD_SHORT = {"00": "Foundations", "01": "Classical mechanics", "02": "EM and optics", "03": "Thermo & stat mech", "04": "Quantum",
               "05": "Relativity & gravity", "06": "Particle", "07": "Nuclear", "08": "Condensed matter", "09": "Astro & cosmology",
               "10": "Plasma", "11": "Interdisciplinary"}
SCOPE_COLORS = {"light": {"across": "#2a78d6", "within": "#eb6834"}, "dark": {"across": "#3987e5", "within": "#d95926"}}


def load_registry(by_path: dict) -> list[dict]:
    if not REGISTRY.exists():
        return []
    records = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            if rec.get("a") in by_path and rec.get("b") in by_path and rec["a"] != rec["b"]:
                records.append(rec)
    return records


def merged_connections(by_path: dict, edges: list[tuple[str, str]], registry: list[dict]) -> list[dict]:
    covered = {frozenset((r["a"], r["b"])) for r in registry}
    merged = [dict(r, origin="registry") for r in registry]
    for a, b in sorted({tuple(sorted(e)) for e in edges}):
        if frozenset((a, b)) not in covered:
            merged.append({"a": a, "b": b, "name": f"{by_path[a]['title']} ↔ {by_path[b]['title']}", "kind": "unclassified",
                           "status": "written", "summary": "Cross-link written in the curated notes; not yet classified.",
                           "confidence": "", "strength": 1, "sources": [], "origin": "notes"})
    for rec in merged:
        rec["scope"] = "across" if rec["a"].split("/")[0] != rec["b"].split("/")[0] else "within"
    return merged


def radial_layout(nodes: list[dict]) -> tuple[dict, dict]:
    import math
    ring = [n for n in nodes if n["has_readme"]]
    slots, prev = [], None
    for n in ring:
        field, sub = n["path"].split("/")[0], "/".join(n["path"].split("/")[:2])
        if prev and prev[0] != field:
            slots += [None] * 4
        elif prev and prev[1] != sub:
            slots.append(None)
        slots.append(n["path"])
        prev = (field, sub)
    slots += [None] * 4
    step = 2 * math.pi / len(slots)
    angle = {p: (i + 0.5) * step for i, p in enumerate(slots) if p}
    radius = {1: 0.30 * RING_R, 2: 0.62 * RING_R, 3: 0.84 * RING_R, 4: 0.92 * RING_R}
    anchors = {}
    for n in nodes:
        members = [a for p, a in angle.items() if p == n["path"] or p.startswith(n["path"] + "/")]
        if members:
            mean = math.atan2(sum(math.sin(a) for a in members), sum(math.cos(a) for a in members))
            r = radius.get(n["depth"], 0.95 * RING_R)
            anchors[n["path"]] = (r * math.sin(mean), -r * math.cos(mean), mean % (2 * math.pi))
    ring_pos = {p: (RING_R * math.sin(a), -RING_R * math.cos(a), a) for p, a in angle.items()}
    return ring_pos, anchors


def bundle_path(a: str, b: str, ring_pos: dict, anchors: dict, by_path: dict, beta: float = 0.85) -> str:
    def chain(p: str) -> list[str]:
        node = by_path[p]
        out = [p] if node["children"] else []
        parent = node["parent"]
        while parent:
            out.append(parent)
            parent = by_path[parent]["parent"]
        return out + ["__root__"]
    ca, cb = chain(a), chain(b)
    common = next(x for x in ca if x in cb)
    up, down = ca[:ca.index(common) + 1], list(reversed(cb[:cb.index(common)]))
    point = lambda p: (0.0, 0.0) if p == "__root__" else anchors[p][:2]
    pts = [ring_pos[a][:2], *[point(p) for p in up], *[point(p) for p in down], ring_pos[b][:2]]
    n = len(pts) - 1
    x0, y0, dx, dy = pts[0][0], pts[0][1], pts[-1][0] - pts[0][0], pts[-1][1] - pts[0][1]
    pts = [(beta * x + (1 - beta) * (x0 + i / n * dx), beta * y + (1 - beta) * (y0 + i / n * dy)) for i, (x, y) in enumerate(pts)]
    f = lambda v: f"{v:.1f}"
    d = [f"M{f(pts[0][0])},{f(pts[0][1])}"]
    if len(pts) == 2:
        return d[0] + f"L{f(pts[1][0])},{f(pts[1][1])}"
    d.append(f"L{f((5 * pts[0][0] + pts[1][0]) / 6)},{f((5 * pts[0][1] + pts[1][1]) / 6)}")
    for i in range(2, len(pts) + 1):
        p0, p1 = pts[i - 2], pts[i - 1]
        p2 = pts[i] if i < len(pts) else pts[-1]
        d.append(f"C{f((2 * p0[0] + p1[0]) / 3)},{f((2 * p0[1] + p1[1]) / 3)} {f((p0[0] + 2 * p1[0]) / 3)},{f((p0[1] + 2 * p1[1]) / 3)} "
                 f"{f((p0[0] + 4 * p1[0] + p2[0]) / 6)},{f((p0[1] + 4 * p1[1] + p2[1]) / 6)}")
    d.append(f"L{f(pts[-1][0])},{f(pts[-1][1])}")
    return "".join(d)


def map_data(nodes: list[dict], edges: list[tuple[str, str]]) -> dict:
    import math
    by_path = {n["path"]: n for n in nodes}
    registry = load_registry(by_path)
    connections = merged_connections(by_path, edges, registry)
    ring_pos, anchors = radial_layout(nodes)
    index = {p: i for i, p in enumerate(ring_pos)}
    out_nodes = []
    for p, (x, y, a) in ring_pos.items():
        node = by_path[p]
        out_nodes.append({"path": p, "title": node["title"], "summary": node["summary"], "field": p[:2], "depth": node["depth"],
                          "sub": "/".join(p.split("/")[:2]), "x": round(x, 1), "y": round(y, 1), "deg": round(math.degrees(a), 2)})
    fields = []
    for f in (n for n in nodes if n["depth"] == 1):
        degs = [math.degrees(ring_pos[p][2]) for p in ring_pos if p == f["path"] or p.startswith(f["path"] + "/")]
        if degs:
            fields.append({"code": f["path"][:2], "path": f["path"], "title": f["title"],
                           "short": FIELD_SHORT.get(f["path"][:2], f["title"].split(" — ")[0]), "start": round(min(degs), 2),
                           "end": round(max(degs), 2), "mid": round(math.degrees(anchors[f["path"]][2]), 2), "agent": f["agent"]})
    out_edges = []
    for rec in connections:
        out_edges.append({"a": index[rec["a"]], "b": index[rec["b"]], "name": rec.get("name", ""), "kind": rec.get("kind", "unclassified"),
                          "status": rec.get("status", "new"), "scope": rec["scope"], "confidence": rec.get("confidence", ""),
                          "strength": rec.get("strength", 1), "summary": rec.get("summary", ""), "map": rec.get("map", ""),
                          "breaks": rec.get("breaks", ""), "sources": rec.get("sources", []), "review": rec.get("review", ""),
                          "origin": rec["origin"], "d": bundle_path(rec["a"], rec["b"], ring_pos, anchors, by_path)})
    return {"generated": today(), "ring": RING_R, "kinds": list(KINDS) + ["unclassified"], "fields": fields,
            "nodes": out_nodes, "edges": out_edges, "registry_size": len(registry)}


def map_svg(data: dict) -> str:
    import math
    colors = SCOPE_COLORS["light"]
    half, hx = RING_R + 235, RING_R + 345
    esc = html.escape
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-hx} {-half - 70} {2 * hx} {2 * half + 140}" '
             'font-family="system-ui, -apple-system, Segoe UI, sans-serif">',
             f'<rect x="{-hx}" y="{-half - 70}" width="{2 * hx}" height="{2 * half + 140}" fill="#fcfcfb"/>',
             f'<text x="{-hx + 24}" y="{-half - 34}" font-size="26" font-weight="600" fill="#0b0b0b">Connections across physics</text>',
             f'<text x="{-hx + 24}" y="{-half - 8}" font-size="15" fill="#52514e">{len(data["edges"])} connections among '
             f'{len(data["nodes"])} notes in {len(data["fields"])} branches · generated {data["generated"]}</text>']
    for scope in ("within", "across"):
        for e in sorted((e for e in data["edges"] if e["scope"] == scope), key=lambda e: e["strength"]):
            width = {1: 0.6, 2: 1.0, 3: 1.6}.get(e["strength"], 0.6)
            opacity = {1: 0.28, 2: 0.42, 3: 0.6}.get(e["strength"], 0.28)
            parts.append(f'<path d="{e["d"]}" fill="none" stroke="{colors[scope]}" stroke-width="{width}" stroke-opacity="{opacity}"/>')
    for n in data["nodes"]:
        a = math.radians(n["deg"])
        flip = n["deg"] > 180
        lx, ly = (RING_R + 8) * math.sin(a), -(RING_R + 8) * math.cos(a)
        rot = n["deg"] - 90 + (180 if flip else 0)
        label = n["title"] if len(n["title"]) <= 34 else n["title"][:32] + "…"
        weight = ' font-weight="600"' if n["depth"] <= 2 else ""
        parts.append(f'<circle cx="{n["x"]}" cy="{n["y"]}" r="{2.6 if n["depth"] <= 2 else 1.8}" fill="#52514e"/>')
        parts.append(f'<text transform="translate({lx:.1f},{ly:.1f}) rotate({rot:.1f})" font-size="7.5"{weight} fill="#52514e" '
                     f'text-anchor="{"end" if flip else "start"}" dominant-baseline="middle">{esc(label)}</text>')
    for f in data["fields"]:
        r = RING_R + 160
        a0, a1 = math.radians(f["start"] - 0.4), math.radians(f["end"] + 0.4)
        large = 1 if (f["end"] - f["start"]) > 180 else 0
        parts.append(f'<path d="M{r * math.sin(a0):.1f},{-r * math.cos(a0):.1f} A{r},{r} 0 {large} 1 {r * math.sin(a1):.1f},{-r * math.cos(a1):.1f}" '
                     'fill="none" stroke="#c3c2b7" stroke-width="2" stroke-linecap="round"/>')
        m = math.radians(f["mid"])
        tx, ty = (r + 22) * math.sin(m), -(r + 22) * math.cos(m)
        anchor = "start" if 10 < f["mid"] < 170 else ("end" if 190 < f["mid"] < 350 else "middle")
        parts.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="15" font-weight="600" fill="#0b0b0b" text-anchor="{anchor}" '
                     f'dominant-baseline="middle">{f["code"]} {esc(f["short"])}</text>')
    ly = half + 34
    for i, (scope, label) in enumerate((("across", "Across branches"), ("within", "Within a branch"))):
        x = -hx + 24 + i * 210
        count = sum(1 for e in data["edges"] if e["scope"] == scope)
        parts.append(f'<line x1="{x}" y1="{ly}" x2="{x + 26}" y2="{ly}" stroke="{colors[scope]}" stroke-width="2" stroke-linecap="round"/>')
        parts.append(f'<text x="{x + 34}" y="{ly}" font-size="14" fill="#52514e" dominant-baseline="middle">{label} ({count})</text>')
    parts.append(f'<text x="{hx - 24}" y="{ly}" font-size="12" fill="#898781" text-anchor="end" dominant-baseline="middle">'
                 'Line weight = strength · links are bundled through the branch → subfield hierarchy</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def build_map(nodes: list[dict], edges: list[tuple[str, str]]) -> dict:
    data = map_data(nodes, edges)
    if MAP_TEMPLATE.exists():
        page = MAP_TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
        MAP_HTML.write_text(page, encoding="utf-8")
    MAP_SVG.write_text(map_svg(data), encoding="utf-8")
    return data


def cmd_plot(args) -> int:
    nodes = discover_nodes()
    data = build_map(nodes, node_edges(nodes))
    across = sum(1 for e in data["edges"] if e["scope"] == "across")
    out(f"Map written: {MAP_HTML.relative_to(ROOT).as_posix()} (interactive) and {MAP_SVG.relative_to(ROOT).as_posix()} — "
        f"{len(data['edges'])} connections ({across} across, {len(data['edges']) - across} within; {data['registry_size']} from the registry) "
        f"among {len(data['nodes'])} notes.")
    return 0


def cmd_connections(args) -> int:
    nodes = discover_nodes()
    by_path = {n["path"]: n for n in nodes}
    data = json.loads(CONNECTIONS_JSON.read_text(encoding="utf-8")) if CONNECTIONS_JSON.exists() else build_connections(nodes)

    def resolve(term: str) -> list[str]:
        term = term.strip("/").removeprefix("knowledge/")
        if term in by_path:
            return [term]
        if re.fullmatch(r"\d\d", term):
            return [p for p in by_path if p.startswith(term)]
        hits = [p for p, n in by_path.items() if term.lower() in n["title"].lower() or term.lower() in p]
        return hits

    first = resolve(args.target)
    if not first:
        out(f"No node or field matches '{args.target}'.")
        return 1
    second = resolve(args.other) if args.other else None
    if args.other and not second:
        out(f"No node or field matches '{args.other}'.")
        return 1
    one, two = set(first), set(second or [])
    title = lambda p: f"{by_path[p]['title']} ({p})"
    inside = lambda p, group: p in group or any(p.startswith(g + "/") for g in group)
    out(f"# Connections: {args.target}" + (f" ↔ {args.other}" if args.other else "") + f"  [{len(one)} node(s)" +
        (f" vs {len(two)}]" if two else "]"))
    links = [(s, d) for s, d in data["edges"] if (inside(s, one) and (not two or inside(d, two))) or
             (inside(d, one) and (not two or inside(s, two)))]
    if not two:
        links = [(s, d) for s, d in links if not (inside(s, one) and inside(d, one))]
    out(f"\n## Explicit cross-links ({len(links)})")
    for s, d in links[: args.n * 3]:
        out(f"- {title(s)} → {title(d)}")
    concepts_one = {c for p in one for c in data["node_concepts"].get(p, [])}
    if two:
        concepts_two = {c for p in two for c in data["node_concepts"].get(p, [])}
        out(f"\n## Shared concepts ({len(concepts_one & concepts_two)})")
        for c in sorted(concepts_one & concepts_two):
            out(f"- {c} — {data['concepts'][c]['idea']}")
    else:
        out(f"\n## Concepts present ({len(concepts_one)})\n" + ", ".join(sorted(concepts_one)))
    latent = [r for key in ("latent_across", "latent_within") for r in data[key]
              if (inside(r["a"], one) and (not two or inside(r["b"], two))) or (inside(r["b"], one) and (not two or inside(r["a"], two)))]
    latent.sort(key=lambda r: -r["score"])
    out(f"\n## Latent bridge candidates ({len(latent)}; showing {min(len(latent), args.n)})")
    for r in latent[: args.n]:
        out(f"- {title(r['a'])} ↔ {title(r['b'])} — score {r['score']:.2f}; shares {', '.join(r['shared'][:6])}")
    reg = [r for r in data.get("registry", []) if (inside(r["a"], one) and (not two or inside(r["b"], two))) or
           (inside(r["b"], one) and (not two or inside(r["a"], two)))]
    reg.sort(key=lambda r: (-r.get("strength", 1), r["name"]))
    out(f"\n## Classified connections ({len(reg)}; showing {min(len(reg), args.n * 2)})")
    for r in reg[: args.n * 2]:
        out(f"- [{r['id']}] {r['name']} — {r['kind']}, strength {r.get('strength')}, {r.get('confidence')} — "
            f"{title(r['a'])} ↔ {title(r['b'])}\n    {r.get('summary', '')}" + (f"\n    breaks: {r['breaks']}" if r.get("breaks") else ""))
    lit = [r for r in data["shared_literature"] if (inside(r["a"], one) and (not two or inside(r["b"], two))) or
           (inside(r["b"], one) and (not two or inside(r["a"], two)))]
    out(f"\n## Shared literature ({len(lit)} note pairs; algorithmic, weak evidence)")
    for r in lit[: args.n]:
        top = max(r["papers"], key=lambda p: p["citations"])
        out(f"- {title(r['a'])} ↔ {title(r['b'])}: \"{top['title'][:90]}\" ({top['year']}) {top['id']}")
    codes = {p[:2] for p in one} | {p[:2] for p in two}
    themes = [t for t in data["themes"] if codes & set(t["fields"])]
    out(f"\n## Curated themes touching these fields ({len(themes)})")
    for t in themes:
        out(f"- {t['title']} ({t['path']}) — {t['summary']}")
    return 0


NODE_TEMPLATE = """---
title: {title}
summary: {summary}
query: {query}
{extra}---
# {title}
> {breadcrumb} · Literature: [papers.md](papers.md)

**Scope.** {summary}

**Core ideas.**
- _To be curated._

**Key equations.** _To be curated._

**Landmarks.** _Add verified references as_ `Author (Year). "Title". *Venue*. [doi:…](https://doi.org/…)` _then run_ `python -I scripts/physlib.py verify <this file>`.

**Open questions.** _To be curated._

**See also.** [{parent_title}]({parent_link})
"""


def cmd_new_node(args) -> int:
    rel = args.path.strip("/").removeprefix("knowledge/")
    target = KNOWLEDGE / rel
    if (target / "README.md").exists():
        out(f"Node already exists: knowledge/{rel}")
        return 1
    parent = target.parent
    if parent != KNOWLEDGE and not (parent / "README.md").exists():
        out(f"Parent node knowledge/{parent.relative_to(KNOWLEDGE).as_posix()} does not exist; create it first.")
        return 1
    ancestors, node_dir = [], parent
    while node_dir != KNOWLEDGE:
        ancestors.append(parse_frontmatter((node_dir / "README.md").read_text(encoding="utf-8"))[0].get("title", node_dir.name))
        node_dir = node_dir.parent
    ancestors.reverse()
    crumbs = [f"[{title}]({'../' * (len(ancestors) - i)}README.md)" for i, title in enumerate(ancestors)]
    breadcrumb = " › ".join(crumbs) or "[Knowledge tree](../../TREE.md)"
    parent_title = ancestors[-1] if ancestors else "Knowledge tree"
    parent_link = "../README.md" if ancestors else "../../TREE.md"
    extra = "".join(f"{k}: {v}\n" for k, v in (("arxiv", args.arxiv), ("source", args.source), ("agent", args.agent)) if v)
    target.mkdir(parents=True, exist_ok=True)
    (target / "README.md").write_text(NODE_TEMPLATE.format(title=args.title, summary=args.summary, query=args.query or args.title.lower(),
                                                           extra=extra, parent_title=parent_title, parent_link=parent_link,
                                                           breadcrumb=breadcrumb), encoding="utf-8")
    build_tree(quiet=True)
    out(f"Created knowledge/{rel}/README.md — curate it, then run: python -I scripts/physlib.py fetch --node {rel}")
    return 0


def parse_codata(text: str) -> tuple[str, list[dict]]:
    version = re.search(r"(\d{4}) CODATA", text)
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("-----"):
            started = True
            continue
        if not started or not line.strip():
            continue
        name, value, unc, unit = line[:60].strip(), line[60:85].strip(), line[85:110].strip(), line[110:].strip()
        try:
            numeric = float(value.replace(" ", "").replace("...", ""))
        except ValueError:
            numeric = None
        rows.append({"name": name, "value": value, "uncertainty": unc, "unit": unit, "exact": "exact" in unc, "numeric": numeric})
    return (version.group(1) if version else "unknown"), rows


def cmd_constants(args) -> int:
    if args.update or not CODATA_JSON.exists():
        text = http_get("https://physics.nist.gov/cuu/Constants/Table/allascii.txt", accept="text/plain")
        version, rows = parse_codata(text)
        LIBRARY.mkdir(exist_ok=True)
        CODATA_JSON.write_text(json.dumps({"version": f"CODATA {version}", "source": "https://physics.nist.gov/cuu/Constants/Table/allascii.txt",
                                           "retrieved": today(), "constants": rows}, indent=1), encoding="utf-8")
        md_dir = KNOWLEDGE / "00-foundations" / "units-and-constants"
        if md_dir.exists():
            md = ["---", f"generated: {today()}", f"count: 0", "---", f"# CODATA {version} recommended values (NIST)", "",
                  f"> Pulled from the NIST table on {today()} by `python -I scripts/physlib.py constants --update`. "
                  f"{len(rows)} constants. `(exact)` marks values fixed by the 2019 SI definition.", "",
                  "| Quantity | Value | Standard uncertainty | Unit |", "|---|---|---|---|"]
            md += [f"| {r['name']} | {r['value']} | {r['uncertainty']} | {r['unit']} |" for r in rows]
            (md_dir / f"codata-{version}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        out(f"Stored {len(rows)} CODATA {version} constants in {CODATA_JSON.relative_to(ROOT).as_posix()}.")
    data = json.loads(CODATA_JSON.read_text(encoding="utf-8"))
    if args.name:
        terms = args.name.lower().split()
        hits = [r for r in data["constants"] if all(t in r["name"].lower() for t in terms)]
        out(f"{data['version']} — {len(hits)} match(es) for {args.name!r}:")
        for r in hits[:args.n]:
            out(f"  {r['name']}: {r['value']} {r['unit']}  (u = {r['uncertainty']})")
    return 0


def cmd_status(args) -> int:
    if not INDEX_JSON.exists():
        out("Physics knowledge base: index not built yet — run `python -I scripts/physlib.py tree`.")
        return 0
    index = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    counts = {lvl: sum(1 for n in index if n["depth"] == d) for lvl, d in (("fields", 1), ("subfields", 2))}
    topics = sum(1 for n in index if n["depth"] >= 3)
    dates = sorted(n["papers_updated"] for n in index if n.get("papers_updated"))
    missing = sum(1 for n in index if n["depth"] >= 2 and not n["papers"])
    partial = sum(1 for n in index if n.get("papers_partial"))
    verify = "not run yet"
    if VERIFY_REPORT.exists():
        report = VERIFY_REPORT.read_text(encoding="utf-8")
        run = re.search(r"Run: (\S+)", report)
        probs = re.search(r"Problems: (\d+)", report)
        verify = f"{probs.group(1) if probs else '?'} problem(s) on {run.group(1) if run else '?'}"
    papers = sum(1 for _ in PAPERS_DB.open(encoding="utf-8")) if PAPERS_DB.exists() else 0
    out(f"Physics knowledge base loaded: {counts['fields']} fields, {counts['subfields']} subfields, {topics} topics, "
        f"{papers:,} papers (literature refreshed {dates[0] if dates else 'never'}…{dates[-1] if dates else ''}; "
        f"{missing} node(s) without papers, {partial} partial). Reference verification: {verify}. "
        "You are the orchestrator: route with TREE.md, dispatch per .claude/agents/physics-orchestrator.md "
        "(specialists → connections-analyst), run the `physics` skill pipeline.")
    return 0


def cmd_hook(args) -> int:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        file_path = (payload.get("tool_input") or {}).get("file_path") or ""
        if not file_path:
            return 0
        path = Path(file_path)
        path = (ROOT / path).resolve() if not path.is_absolute() else path.resolve()
        watched = (KNOWLEDGE.resolve(), CONNECTIONS_DIR.resolve())
        if not any(w in path.parents for w in watched) or path.suffix != ".md" or path.name == "papers.md":
            return 0
        notes = []
        if path.name == "README.md":
            meta = parse_frontmatter(path.read_text(encoding="utf-8"))[0]
            notes += [f"frontmatter lacks `{k}`" for k in ("title", "summary") if not meta.get(k)]
        notes += [f"broken relative link → {t}" for t in check_links(path)]
        cache = json.loads(VERIFY_CACHE.read_text(encoding="utf-8")) if VERIFY_CACHE.exists() else {}
        unverified = sorted({f"{r['kind']}:{r['id']}" for r in collect_refs([path]) if not cache.get(cache_key(r["kind"], r["id"]), {}).get("ok")})
        if unverified:
            notes.append(f"{len(unverified)} unverified citation(s) ({', '.join(unverified[:5])}) — run "
                         f"`python -I scripts/physlib.py verify {path.relative_to(ROOT).as_posix()}` before finishing")
        build_tree(quiet=True)
        if notes:
            msg = f"[physics-kb hook] {path.relative_to(ROOT).as_posix()}: " + "; ".join(notes) + ". TREE.md was rebuilt."
            out(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
    except Exception as err:
        sys.stderr.write(f"physlib hook skipped: {err}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(prog="physlib", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("search", help="search arXiv / OpenAlex / INSPIRE-HEP / Semantic Scholar live")
    p.add_argument("query", nargs="?", default="", help="phrase(s); separate alternatives with ';'")
    p.add_argument("--source", choices=["all", "arxiv", "openalex", "inspire", "semanticscholar"], default="all",
                   help="'all' = arXiv + OpenAlex + INSPIRE; Semantic Scholar stands in when OpenAlex is out of budget")
    p.add_argument("--sort", choices=["cited", "recent", "relevance"], default="cited")
    p.add_argument("-n", type=int, default=8)
    p.add_argument("--cat", nargs="*", help="arXiv categories, e.g. hep-ph quant-ph")
    p.add_argument("--since", type=int, help="only works from this year on")
    p.add_argument("--days", type=int, help="arXiv: only the last N days")
    p.add_argument("--reviews", action="store_true", help="review articles only (OpenAlex/INSPIRE/Semantic Scholar)")
    p.add_argument("--filter", help="raw OpenAlex filter replacing the physics-field default")
    p.add_argument("--any-field", action="store_true", help="OpenAlex: drop the physics-field filter")
    p.add_argument("--raw", help="raw arXiv search_query / INSPIRE q string")
    p.add_argument("--abstracts", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("--save", metavar="NODE", help="file the results into library/papers.jsonl under NODE")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("fetch", help="refresh papers.md for tree nodes")
    p.add_argument("--node", help="node path prefix, e.g. 06-particle-physics/neutrino-physics")
    p.add_argument("--missing", action="store_true", help="only nodes without papers.md")
    p.add_argument("--partial", action="store_true", help="only nodes whose papers.md is partial (API budget ran out)")
    p.add_argument("--level", choices=["subfield", "branch", "topic"], help="only nodes at this level")
    p.add_argument("--limit", type=int)
    p.add_argument("--n-cited", type=int, default=6)
    p.add_argument("--n-rising", type=int, default=4)
    p.add_argument("--n-latest", type=int, default=5)
    p.add_argument("--n-reviews", type=int, default=6)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("paper", help="show one paper (arXiv id or DOI) with abstract")
    p.add_argument("id")
    p.add_argument("--live", action="store_true", help="skip the local library")
    p.set_defaults(func=cmd_paper)

    p = sub.add_parser("fulltext", help="download an open-access PDF into library/fulltext/")
    p.add_argument("id")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_fulltext)

    p = sub.add_parser("verify", help="check every arXiv id / DOI in markdown against live records")
    p.add_argument("paths", nargs="*")
    p.add_argument("--all", action="store_true", help="include auto-generated papers.md files")
    p.add_argument("--recheck", action="store_true", help="ignore the cache")
    p.add_argument("--stdin", action="store_true", help="verify citation lines piped on stdin (no file needed)")
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("tree", help="rebuild TREE.md + library/index.json")
    p.add_argument("--check", action="store_true", help="exit 1 on structural problems")
    p.set_defaults(func=cmd_tree)

    p = sub.add_parser("new-node", help="scaffold a new branch/topic folder")
    p.add_argument("path")
    p.add_argument("--title", required=True)
    p.add_argument("--summary", required=True)
    p.add_argument("--query")
    p.add_argument("--arxiv")
    p.add_argument("--source", choices=["openalex", "inspire"])
    p.add_argument("--agent")
    p.set_defaults(func=cmd_new_node)

    p = sub.add_parser("constants", help="look up CODATA constants (NIST)")
    p.add_argument("name", nargs="?")
    p.add_argument("--update", action="store_true")
    p.add_argument("-n", type=int, default=15)
    p.set_defaults(func=cmd_constants)

    p = sub.add_parser("connections", help="query the cross-branch graph: links, shared concepts, latent bridges, shared papers")
    p.add_argument("target", help="node path, field code (e.g. 08) or title fragment")
    p.add_argument("other", nargs="?", help="second node/field: show only what connects the two")
    p.add_argument("-n", type=int, default=15, help="rows per section")
    p.set_defaults(func=cmd_connections)

    sub.add_parser("plot", help="draw every connection: connections/map.html (interactive) + map.svg").set_defaults(func=cmd_plot)

    sub.add_parser("status", help="one-line summary (SessionStart hook)").set_defaults(func=cmd_status)
    sub.add_parser("hook", help="PostToolUse hook handler (reads JSON on stdin)").set_defaults(func=cmd_hook)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
