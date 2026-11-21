#!/usr/bin/env python3
"""Parse the ATNF pulsar catalogue glitch table (glitchTbl.html) into {PSRJ: [(epoch_mjd, dnu_over_nu_1e-9 or None)]}."""
from __future__ import annotations

import html
import re
from pathlib import Path

SNAPSHOT = Path(__file__).resolve().parent.parent / "data" / "g4" / "atnf-glitchTbl-2026-11-21.html"
NUM = re.compile(r"^\s*([-+]?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?)")


def num(cell: str) -> float | None:
    m = NUM.match(cell)
    return float(m.group(1)) if m else None


def parse_atnf(text: str, merge_days: float = 0.0) -> dict:
    cat: dict = {}
    for row in re.findall(r"<tr>(.*?)</tr>", text, re.S):
        cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td>(.*?)</td>", row, re.S)]
        if len(cells) < 4 or not re.match(r"^J\d{4}[+-]\d{2,4}", cells[1]):
            continue
        t = num(cells[2])
        if t is None:
            continue
        s = num(cells[3])
        cat.setdefault(cells[1], []).append((t, s))
    out = {}
    for p, g in cat.items():
        g = sorted(g)
        merged = [g[0]]
        for t, s in g[1:]:
            if t - merged[-1][0] <= merge_days:
                continue  # the same glitch listed twice (two references)
            merged.append((t, s))
        out[p] = merged
    return out


if __name__ == "__main__":
    cat = parse_atnf(SNAPSHOT.read_text(encoding="utf-8", errors="replace"), merge_days=1.0)
    raw = parse_atnf(SNAPSHOT.read_text(encoding="utf-8", errors="replace"))
    print("pulsars", len(cat), "glitches", sum(map(len, cat.values())), "| before merging same-day duplicates:", sum(map(len, raw.values())))
    print("non-positive sizes", sum(1 for g in cat.values() for t, s in g if s is not None and s <= 0), "missing sizes", sum(1 for g in cat.values() for t, s in g if s is None))
    for k in (5, 8):
        print(f">= {k} sized glitches:", sum(1 for g in cat.values() if sum(1 for t, s in g if s and s > 0) >= k), "pulsars")
