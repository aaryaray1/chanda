#!/usr/bin/env bash
# Always-on chanda session wired to Discord through the official channel plugin; starts fresh every day at 05:00.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT" || exit 1
if [ -f "$HOME/.config/chanda/env" ]; then
  while IFS='=' read -r key value; do
    case "$key" in ''|\#*) continue ;; esac
    value="${value%$'\r'}"; value="${value%\"}"; value="${value#\"}"
    export "$key=$value"
  done < "$HOME/.config/chanda/env"
fi
unset ANTHROPIC_API_KEY
[ "${CHANDA_AGENT_USE_TOKEN:-0}" = "1" ] || unset CLAUDE_CODE_OAUTH_TOKEN
export PATH="$HOME/.local/bin:$HOME/.bun/bin:$PATH"
while true; do
  now=$(date +%s)
  until=$(date -d 'today 05:00' +%s)
  [ "$until" -gt "$now" ] || until=$(date -d 'tomorrow 05:00' +%s)
  echo "$(date '+%F %T') starting chanda on Discord (fresh context until $(date -d "@$until" '+%a %H:%M'))"
  # shellcheck disable=SC2086
  timeout --foreground "$((until - now))" claude --channels plugin:discord@claude-plugins-official ${CHANDA_AGENT_ARGS:-}
  echo "$(date '+%F %T') claude exited ($?); restarting in 15 s"
  sleep 15
done
