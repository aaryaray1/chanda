#!/usr/bin/env bash
# One-time (re-runnable) setup of chanda on a Linux Mint / Ubuntu server; see docs/SERVER.md.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CONF="$HOME/.config/chanda"
UNITS="$HOME/.config/systemd/user"
export PATH="$HOME/.local/bin:$HOME/.bun/bin:$PATH"
say() { printf '\n== %s\n' "$*"; }

say "packages"
need=()
command -v python3 >/dev/null || need+=(python3)
command -v python >/dev/null || need+=(python-is-python3)
for c in tmux curl unzip; do command -v "$c" >/dev/null || need+=("$c"); done
python3 -c 'import sympy, numpy' 2>/dev/null || need+=(python3-sympy python3-numpy)
if [ ${#need[@]} -gt 0 ]; then
  echo "installing: ${need[*]}"
  sudo apt-get update -qq && sudo apt-get install -y "${need[@]}"
fi
python3 -c 'import sys; assert sys.version_info >= (3, 9), "chanda needs Python 3.9+"'
echo "python $(python3 -V 2>&1 | cut -d' ' -f2), python -> $(command -v python)"

say "line endings and permissions"
find "$ROOT/scripts" -type f \( -name '*.sh' -o -name '*.py' -o -name '*.service' -o -name '*.timer' -o -name 'env.example' \) -exec sed -i 's/\r$//' {} +
chmod +x "$ROOT"/scripts/server/*.sh "$ROOT"/scripts/*.py

say "Claude Code and Bun"
if ! command -v claude >/dev/null; then
  echo "installing Claude Code (official installer)"
  curl -fsSL https://claude.ai/install.sh | bash
fi
claude --version
if ! command -v bun >/dev/null; then
  echo "installing Bun, which the Discord channel plugin needs (official installer)"
  curl -fsSL https://bun.sh/install | bash
fi
echo "bun $(bun --version)"

say "settings, secrets and memory"
mkdir -p "$CONF" && chmod 700 "$CONF"
[ -f "$CONF/env" ] || cp "$ROOT/scripts/server/env.example" "$CONF/env"
sed -i 's/\r$//' "$CONF/env" && chmod 600 "$CONF/env"
echo "secrets file: $CONF/env"
if [ -f "$ROOT/.claude/settings.json" ]; then
  echo "kept the existing .claude/settings.json (compare it with scripts/server/claude-settings.json)"
else
  cp "$ROOT/scripts/server/claude-settings.json" "$ROOT/.claude/settings.json"
  echo "installed .claude/settings.json (tool permissions for the unattended agent)"
fi
slug=$(printf '%s' "$ROOT" | sed 's/[^A-Za-z0-9]/-/g')
mem="$HOME/.claude/projects/$slug/memory"
if [ -d "$ROOT/.server-memory" ] && [ ! -e "$mem/MEMORY.md" ]; then
  mkdir -p "$mem" && cp "$ROOT"/.server-memory/*.md "$mem"/
  echo "copied Claude's project memory to $mem"
fi

say "systemd user units"
hours=$(python3 -I -c 'import json, sys; h = int(json.load(open(sys.argv[1])).get("interval_hours", 2)); print(h if 1 <= h <= 23 else 2)' \
  "$ROOT/connections/pipeline/config.json")
mkdir -p "$UNITS"
for f in chanda-pipeline.service chanda-pipeline.timer chanda-agent.service; do
  sed -e "s|__ROOT__|$ROOT|g" -e "s|__HOURS__|$hours|g" "$ROOT/scripts/server/$f" > "$UNITS/$f"
done
systemctl --user daemon-reload
systemctl --user enable --now chanda-pipeline.timer
echo "pipeline timer: every $hours h at :13 (the review gate in config.json decides when work starts)"
if [ "$(loginctl show-user "$USER" -p Linger --value 2>/dev/null)" != "yes" ]; then
  echo "enabling lingering so the timer and agent run without a login"
  sudo loginctl enable-linger "$USER"
fi

say "health check"
python3 -I "$ROOT/scripts/connections_runner.py" --health || true

say "next steps (docs/SERVER.md)"
cat <<EOF
1. Sign in for the pipeline: claude setup-token, then put CLAUDE_CODE_OAUTH_TOKEN=... in $CONF/env
2. Sign in for the Discord session: cd $ROOT && claude, then /login, and trust the folder
3. Connect the bot: in that session run /plugin install discord@claude-plugins-official, then /discord:configure <bot token>
4. Put the findings channel id in $CONF/env as CHANDA_DISCORD_CHANNEL=..., then check: python3 -I scripts/connections_runner.py --health --test-discord
5. Start the agent: systemctl --user enable --now chanda-agent.service, attach: tmux -L chanda attach (detach: Ctrl-b d), pair and allowlist there
EOF
