#!/usr/bin/env python3
"""Post text to chanda's Discord channel as the bot (DISCORD_BOT_TOKEN + CHANDA_DISCORD_CHANNEL) or via DISCORD_WEBHOOK_URL; exit 2 if unconfigured."""
from __future__ import annotations

import argparse
import contextlib
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API, LIMIT = "https://discord.com/api/v10", 1900
UA = "DiscordBot (https://discord.com/developers/docs, 1.0) chanda"
ENV_FILES = (Path.home() / ".config" / "chanda" / "env", Path.home() / ".claude" / "channels" / "discord" / ".env")
WHY = {401: "the bot token is wrong or was reset", 403: "the bot can't post in that channel (invite it, check its permissions)",
       404: "unknown channel id or webhook"}


def load_env() -> None:
    for path in ENV_FILES:
        with contextlib.suppress(OSError):
            for line in path.read_text(encoding="utf-8").splitlines():
                key, sep, value = line.strip().partition("=")
                if sep and key and not key.startswith("#") and value.strip():
                    os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def target() -> tuple[str, dict, str] | None:
    hook, token, channel = (os.environ.get(k, "").strip() for k in ("DISCORD_WEBHOOK_URL", "DISCORD_BOT_TOKEN", "CHANDA_DISCORD_CHANNEL"))
    if hook:
        return hook + ("&" if "?" in hook else "?") + "wait=true", {}, "webhook"
    if token and channel.isdigit():
        return f"{API}/channels/{channel}/messages", {"Authorization": f"Bot {token}"}, f"bot -> channel {channel}"
    return None


def chunks(text: str, limit: int = LIMIT) -> list[str]:
    lines = [part for line in text.splitlines() for part in ([line[i:i + limit - 20] for i in range(0, len(line), limit - 20)] or [""])]
    out, cur, size, fence = [], [], 0, ""
    for line in lines:
        if cur and size + len(line) + 1 > limit - 4:
            out.append("\n".join(cur) + ("\n```" if fence else ""))
            cur, size = ([fence] if fence else []), len(fence)
        cur.append(line)
        size += len(line) + 1
        if line.lstrip().startswith("```"):
            fence = "" if fence else line.strip()
    out.append("\n".join(cur))
    return [c for c in out if c.strip()]


def send(url: str, headers: dict, content: str) -> None:
    body = json.dumps({"content": content, "allowed_mentions": {"parse": []}}).encode("utf-8")
    for attempt in range(5):
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Content-Type": "application/json", "User-Agent": UA, **headers})
        try:
            with urllib.request.urlopen(req, timeout=30):
                return
        except urllib.error.HTTPError as exc:
            raw = exc.read() or b"{}"
            if exc.code == 429:
                try:
                    wait = float(json.loads(raw).get("retry_after", 2))
                except (ValueError, AttributeError):
                    wait = 2.0
            elif exc.code >= 500:
                wait = 3 * (attempt + 1)
            else:
                raise RuntimeError(f"Discord refused the message ({exc.code}): {WHY.get(exc.code, raw[:200].decode('utf-8', 'replace'))}")
        except (urllib.error.URLError, socket.timeout, ConnectionError) as exc:
            wait = 5 * (attempt + 1)
            if attempt == 4:
                raise RuntimeError(f"Discord is unreachable: {exc}")
        time.sleep(min(wait, 30))
    raise RuntimeError("Discord did not accept the message after 5 tries")


def main() -> int:
    with contextlib.suppress(AttributeError):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="discord_post", description=__doc__)
    ap.add_argument("text", nargs="*")
    ap.add_argument("--stdin", action="store_true", help="read the message from stdin")
    ap.add_argument("--check", action="store_true", help="only report whether posting is configured")
    ap.add_argument("--test", action="store_true", help="post a test message")
    args = ap.parse_args()
    load_env()
    where = target()
    if not where:
        print("Discord posting is not configured: set CHANDA_DISCORD_CHANNEL in ~/.config/chanda/env "
              "(the bot token comes from /discord:configure), or DISCORD_WEBHOOK_URL")
        return 2
    url, headers, label = where
    if args.check:
        print(f"Discord posting is configured ({label})")
        return 0
    text = f"chanda test message from {socket.gethostname()}" if args.test else \
        (sys.stdin.read() if args.stdin else " ".join(args.text))
    try:
        for part in chunks(text.strip()):
            send(url, headers, part)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"posted to Discord ({label})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
