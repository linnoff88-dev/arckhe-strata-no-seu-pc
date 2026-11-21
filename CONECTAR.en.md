# Connect your tools to Strata

Strata provides an API-compatible server for OpenAI and Anthropic (an interface for communication between programs).
The default address is `http://127.0.0.1:8080`. Use the address actually shown by your server.
You need to install your tool separately and start a model in Strata before checking the connection.

Install Node.js with npm from [Node.js](https://nodejs.org). Check both versions before installing the CLIs:

```sh
node -v
npm -v
```

## View, write, check

```sh
strata launch
```

The monitor is the tracking screen that `strata launch` opens in the terminal. Press `q`: it asks whether to keep the server running in the background or stop it. Choose to keep it running to connect your tools.
Claude Code and Codex CLI are terminal coding assistants, installed separately. A prompt is the text request sent to the model.

WSL is Linux inside Windows. A shard is one part of a model file. An endpoint is a server address that receives a type of request. An alias is an alternative name for the same command. An environment variable is a named value that the terminal passes to programs opened in it.

## Claude Code

strata connect claude-code and strata connect codex show the masked key by default. Before copying ANTHROPIC_AUTH_TOKEN or STRATA_API_KEY, use strata connect claude-code --show-key or strata connect codex --show-key, respectively; another option is strata launch --show-key. Copy the real key, not the mask.

For users of Claude Code through the subscription: --write changes the global file ~/.claude/settings.json; Claude Code then uses Strata and stops using the subscription for those calls. To preserve the global configuration, open a separate terminal and run strata connect claude-code without --write. Copy all the variables it prints (address, key, models and limits) and export them only in that terminal. The examples below are templates: replace ... with the printed values. Then open claude in that same terminal. To return to the subscription, close that terminal.

Copy ALL the variables printed by strata connect claude-code. It prints JSON, with the variables inside env; JSON is not a terminal command. For each "NAME": "value" pair, use export NAME="value" in Bash or $env:NAME="value" in PowerShell. Replace ... with the actual values, including models and limits. Include CLAUDE_CODE_SIMPLE="1" only if it appears in the JSON (context ≤ 40.960 tokens, 40K). Run claude in that same terminal.

Bash:
```sh
strata connect claude-code --show-key

export ANTHROPIC_BASE_URL="..."
export ANTHROPIC_AUTH_TOKEN="..."
export ANTHROPIC_MODEL="..."
export ANTHROPIC_SMALL_FAST_MODEL="..."
export ANTHROPIC_DEFAULT_SONNET_MODEL="..."
export ANTHROPIC_DEFAULT_OPUS_MODEL="..."
export ANTHROPIC_DEFAULT_HAIKU_MODEL="..."
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"
export DISABLE_AUTOUPDATER="1"
export DISABLE_TELEMETRY="1"
export CLAUDE_CODE_MAX_CONTEXT_TOKENS="..."
export CLAUDE_CODE_MAX_OUTPUT_TOKENS="..."
# Only if it appears in the JSON (context ≤ 40.960 tokens):
export CLAUDE_CODE_SIMPLE="1"
```

PowerShell:
```powershell
strata connect claude-code --show-key

$env:ANTHROPIC_BASE_URL="..."
$env:ANTHROPIC_AUTH_TOKEN="..."
$env:ANTHROPIC_MODEL="..."
$env:ANTHROPIC_SMALL_FAST_MODEL="..."
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="..."
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="..."
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="..."
$env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"
$env:DISABLE_AUTOUPDATER="1"
$env:DISABLE_TELEMETRY="1"
$env:CLAUDE_CODE_MAX_CONTEXT_TOKENS="..."
$env:CLAUDE_CODE_MAX_OUTPUT_TOKENS="..."
# Only if it appears in the JSON (context ≤ 40.960 tokens):
$env:CLAUDE_CODE_SIMPLE="1"
```

```sh
strata connect claude-code --show-key
strata connect claude-code --check
claude -p "your task"
```

`claude` is also an alias for `claude-code` in the `strata connect` command. Without `--write`, it shows the configuration; with `--write`, it writes to `~/.claude/settings.json` and backs up the existing file. Then use `claude -p "your task"` or `claude` to chat.
The generator configures `ANTHROPIC_BASE_URL` (the Strata address **without /v1**, usually `http://127.0.0.1:8080`), `ANTHROPIC_AUTH_TOKEN` (your Strata key; no Anthropic account is used), the model, `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, and `CLAUDE_CODE_MAX_OUTPUT_TOKENS`. Use the limits for your server shown by the generator.
The `[claude-code:unrecognized_model]` warning is harmless.

## Codex CLI

The same caution applies to Codex: --write changes the global ~/.codex/config.toml and switches the provider to Strata. Without changing that file, run strata connect codex without --write; copy the configuration into -c options for that run only, and set STRATA_API_KEY in the separate terminal. The key variable alone does not select Strata. In the template below, replace ... with the generated values; also use the model_context_window and model_auto_compact_token_limit limits printed by the generator. When that run ends and you close the terminal, the global configuration remains as it was.

The examples without --write include all the options codex_file writes to harness.py.txt: model_reasoning_summary="auto", approval_policy="never", sandbox_mode="workspace-write" and check_for_update_on_startup=false, as well as the model, provider, limits, and timeout. approval_policy="never" means Codex will not ask for approval. workspace-write allows writing to the workspace. These -c options apply only to this run.

Bash:
```sh
strata connect codex --show-key
export STRATA_API_KEY="..."
codex -c 'model="..."' -c 'model_provider="strata"' -c 'model_providers.strata.name="Strata (local)"' -c 'model_providers.strata.base_url="..."' -c 'model_providers.strata.wire_api="responses"' -c 'model_providers.strata.env_key="STRATA_API_KEY"' -c 'model_providers.strata.stream_idle_timeout_ms=600000' -c 'model_context_window=...' -c 'model_auto_compact_token_limit=...' -c 'model_reasoning_summary="auto"' -c 'approval_policy="never"' -c 'sandbox_mode="workspace-write"' -c 'check_for_update_on_startup=false'
```

PowerShell:
```powershell
strata connect codex --show-key
$env:STRATA_API_KEY="..."
codex -c 'model="..."' -c 'model_provider="strata"' -c 'model_providers.strata.name="Strata (local)"' -c 'model_providers.strata.base_url="..."' -c 'model_providers.strata.wire_api="responses"' -c 'model_providers.strata.env_key="STRATA_API_KEY"' -c 'model_providers.strata.stream_idle_timeout_ms=600000' -c 'model_context_window=...' -c 'model_auto_compact_token_limit=...' -c 'model_reasoning_summary="auto"' -c 'approval_policy="never"' -c 'sandbox_mode="workspace-write"' -c 'check_for_update_on_startup=false'
```

```sh
strata connect codex --show-key
strata connect codex --check
```

Without `--write`, it shows the configuration; with `--write`, it writes to `~/.codex/config.toml` and backs up the existing file. Set `STRATA_API_KEY` in the terminal where you will run Codex, using your Strata key as shown in the generator output. It is not an OpenAI key. The variable is required: if the server does not require a key, the official code says any text will work. Do not publish your key.
The `Model metadata ... not found` warning is harmless.

**Attention:** `--write` changes the tool’s global configuration, so it will start using Strata. To revert, restore the backup created (the command shows its path); if there was no previous file, remove only the configuration that was created. Also revert any environment variables you set.
`--check` verifies the connection by sending a prompt and a tool call to the selected server; these commands are instructions for the reader and were not run here.
Running `strata connect` without arguments lists the available configurations; use the tool identifier in the command. For example, OpenCode uses `strata connect opencode`.

## Who can access it

To get started, leave it set to `local`.

| `--access` option | Scope | Caution |
|---|---|---|
| `local` | This PC only, at `127.0.0.1` | This is the default. |
| `lan` | Other devices on your network | Use the LAN address shown and the generated key. |
| `tailscale` | Your Tailscale network | Tailscale must be installed and connected. |
| `cloudflare` | Internet tunnel | Requires `cloudflared`; keep the key. |

The access options belong to `strata launch`. The documented syntax is `--access local|lan|cloudflare|tailscale`: choose one value; do not copy the bars as a command.
For access beyond your PC, Strata generates a key. The terminal lets you disable it, but warns that anyone who can reach the address can use the model and its tools. **Keep the key.**
For the connection, the docs provide `--url URL`, `--key KEY`, or `--key-env NAME`; these uppercase names are placeholders for your values, not ready-to-use environment variables.
Avoid publishing the key in logs, screenshots, or repositories. Check the destination before sending documents.

## Privacy has clear limits

The local engine does not charge per token; electricity and your equipment are still your responsibility. This does not change the commercial terms of each connected tool.
Strata does not send telemetry. Downloads and updates use the network; searches and pages, external models, tunnels, and tool servers may send data outside your machine.
Connected programs have their own network behavior. Do not treat “local AI” as a guarantee that the entire setup works without internet.

Sources: [docs-oficiais/harness.py.txt](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/harness.py.txt), [docs-oficiais/TERMINAL_LAUNCH.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/TERMINAL_LAUNCH.md) (Connect your apps, Access), [docs-oficiais/INSTALL.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/INSTALL.md), [docs-oficiais/SAFETY.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/SAFETY.md), [FATOS.md](https://github.com/inematds/strata-no-seu-pc/blob/main/FATOS.md).

If you already used --write, closing the terminal does not undo the global change: restore the backup of ~/.claude/settings.json or ~/.codex/config.toml indicated by the command; if there was no previous file, remove only the configuration that was created. Also revert the environment variables. --check sends a request and a tool call to the selected server; it was not run here.
