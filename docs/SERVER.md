# Running chanda on the Linux server

The server laptop (Linux Mint) runs two things. Both work from the same `~/chanda` folder.

| What | How it runs | What it does |
|---|---|---|
| **Pipeline** (specialist review) | systemd user timer `chanda-pipeline.timer`, every 2 h at :13, which runs `scripts/connections_runner.py` | Works through the review packets, then finalizes the registry. After each run it posts its findings to Discord. |
| **Discord agent** | `chanda-agent.service`: a Claude Code session in tmux with the official Discord channel plugin | Answers your questions in your Discord server. Starts with a fresh context every day at 05:00. |

Review is held until **Monday 2026-11-09 00:00** and runs only on Linux. Both rules come from `stage_gate` in `connections/pipeline/config.json`. To change the start, edit `not_before`; to start now, delete it. The Windows laptop already handed off: its scheduled task removed itself on 2026-11-05.

## 1. Pack on Windows
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\pack_for_server.ps1
```
This writes `Downloads\chanda-<date>.tar.gz`, about 15 MB. The archive includes Claude's memory for this project. The script prints the exact `scp` and unpack commands, with a checksum. A USB stick works too.

## 2. Unpack and set up on the server
```bash
tar -xzf ~/chanda-*.tar.gz -C ~
bash ~/chanda/scripts/server/setup.sh
```
`setup.sh` is safe to run again. It does the following:
- installs the missing packages (`python-is-python3`, `tmux`, `curl`, `unzip`, `python3-sympy`, `python3-numpy`);
- installs Claude Code and Bun with their official installers;
- creates `~/.config/chanda/env` (mode 600) from `scripts/server/env.example`;
- installs `.claude/settings.json`, the tool permissions for the unattended agent;
- copies Claude's project memory;
- installs and starts the pipeline timer;
- enables lingering, so services run without a login;
- prints a health check.

## 3. Sign in
- **Pipeline:** run `claude setup-token` and put `CLAUDE_CODE_OAUTH_TOKEN=...` in `~/.config/chanda/env`. The token lasts about a year.
- **Discord agent:** run `cd ~/chanda && claude`, then `/login`, and trust the folder. Channels need claude.ai sign-in. It isn't documented whether the setup token counts. To test it, set `CHANDA_AGENT_USE_TOKEN=1` in the env file. If the session then starts with the channel active, keep it, because the token doesn't expire like `/login`. Otherwise set it back to `0`.
- `ANTHROPIC_API_KEY` must not be set: it outranks the subscription. The pipeline service and `agent.sh` unset it.

## 4. Create the Discord bot
1. In the [Discord Developer Portal](https://discord.com/developers/applications), click **New Application**, open **Bot**, then **Reset Token**, and copy the token.
2. On the same page, under **Privileged Gateway Intents**, turn on **Message Content Intent**.
3. Open **OAuth2 → URL Generator**:
   - scope `bot`;
   - permissions: View Channels, Send Messages, Send Messages in Threads, Read Message History, Attach Files, Add Reactions.
4. Open the generated URL and add the bot to your server.
5. Make a private channel for it, for example `#chanda`.
6. In Discord, turn on **Settings → Advanced → Developer Mode**, then right-click the channel and choose **Copy Channel ID**.

## 5. Connect the bot to chanda
In a `claude` session in `~/chanda`, install the plugin and give it the token:
```
/plugin install discord@claude-plugins-official      (choose user scope; run /reload-plugins if asked)
/discord:configure <bot token>                        (stored in ~/.claude/channels/discord/.env)
```
Leave that session, then start the agent and attach to it:
```bash
systemctl --user enable --now chanda-agent.service
tmux -L chanda attach                                 (detach again with Ctrl-b d)
```
In the attached session:
1. DM the bot. It replies with a pairing code.
2. Run:
   ```
   /discord:access pair <code>
   /discord:access policy allowlist
   /discord:access group add <channel-id>             (add --no-mention to answer every message, not only @mentions)
   ```
3. Send a test question in the channel. If the terminal asks to allow the plugin's `reply` tool, choose "don't ask again".

## 6. Findings channel
Put `CHANDA_DISCORD_CHANNEL=<channel-id>` in `~/.config/chanda/env`. The pipeline then posts as the same bot. Check it:
```bash
python3 -I scripts/connections_runner.py --health --test-discord
```

## Day to day
- **Ask** in the channel. Long answers arrive as several messages, or as an attached `.md` file.
- **Pipeline posts:**
  - after each run, one message: the packets reviewed, with counts of confirmed, revised, rejected and new connections, plus a few of the new ones and the rejections;
  - alerts, once per problem per day: usage limit, expired sign-in, blocked units, runner failures.
- **Health:** `python3 -I scripts/connections_runner.py --health` checks the timer, sign-in, executables, lingering, the agent, Discord and the lock, then runs `doctor`.
- **Logs:**
  - pipeline: `connections/pipeline/runs.log` and `journalctl --user -u chanda-pipeline`;
  - agent: `tmux -L chanda attach`.
- **One run now:** `systemctl --user start chanda-pipeline.service`. Without systemd: `python3 -I scripts/connections_runner.py [--units N] [--dry-run]`.
- **Stop:** `python -I scripts/connections_pipeline.py pause [--hours N]` / `resume` for the pipeline; `systemctl --user stop chanda-agent` for the agent.

## Security
- Through permission relay, anyone who can post in an allowed channel can approve the agent's tool use. Allowlist only yourself and keep the channel private.
- Secrets are kept in two files, both mode 600:
  - `~/.config/chanda/env`;
  - `~/.claude/channels/discord/.env`.

  `.claude/settings.json` stops the agent from reading them, and the pipeline's unit sessions never see the bot token.
- The agent can do these without asking: read and search the project, search and fetch the web, and run `physlib.py` and the pipeline's `status`/`doctor`. Anything else, such as other shell commands or edits, asks you in Discord first.

## Quota
The pipeline and the agent share your subscription.
- **Review:** a packet costs about $0.5–0.9 at API prices on Opus. 47 packets are left, capped at 4 per run and 30 per day.
- **Questions:** a question costs what it needs. Each specialist it consults preloads a 30–50k-token codex.

If the two compete, lower `max_units_per_day` in `config.json`.

## Check on first start
These aren't documented, so confirm them on the server:
- whether channels accept the setup token (step 3);
- that the Claude Code version is at least 2.1.234, which permission relay needs (Windows runs 2.1.318);
- that the Bun version works with the plugin.
