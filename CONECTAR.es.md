# Conecta tus herramientas a Strata

Strata ofrece un servidor compatible con las API (interfaces de comunicación entre programas) de OpenAI y Anthropic.
La dirección predeterminada es `http://127.0.0.1:8080`. Usa la dirección que muestre efectivamente tu servidor.
Debes instalar tu herramienta por separado e iniciar un modelo en Strata antes de comprobar la conexión.

Instala Node.js con npm desde [Node.js](https://nodejs.org). Comprueba ambas versiones antes de instalar las CLIs:

```sh
node -v
npm -v
```

## Ver, guardar, comprobar

```sh
strata launch
```

El monitor es la pantalla de seguimiento que `strata launch` abre en el terminal. Pulsa `q`: te preguntará si quieres mantener el servidor en segundo plano o detenerlo. Elige mantenerlo para conectar tus herramientas.
Claude Code y Codex CLI son asistentes de programación en el terminal que se instalan por separado. Prompt es la solicitud en texto que se envía al modelo.

WSL es Linux dentro de Windows. Un shard es una parte del archivo del modelo. Un endpoint es una dirección del servidor que recibe un tipo de solicitud. Un alias es un nombre alternativo para el mismo comando. Una variable de entorno es un valor con nombre que el terminal pasa a los programas que se abren en él.

## Claude Code

strata connect claude-code y strata connect codex muestran la clave enmascarada de forma predeterminada. Antes de copiar ANTHROPIC_AUTH_TOKEN o STRATA_API_KEY, usa strata connect claude-code --show-key o strata connect codex --show-key, respectivamente; otra opción es strata launch --show-key. Copia la clave real, no la máscara.

Para quienes usan Claude Code con la suscripción: --write modifica el archivo global ~/.claude/settings.json; Claude Code pasa a usar Strata y deja de usar la suscripción en esas llamadas. Para conservar la configuración global, abre un terminal separado y ejecuta strata connect claude-code sin --write. Copia todas las variables que imprime (dirección, clave, modelos y límites) y expórtalas solo en ese terminal. Los ejemplos de abajo son plantillas: sustituye ... por los valores impresos. Después abre claude en ese mismo terminal. Para volver a la suscripción, cierra ese terminal.

Copia TODAS las variables que imprima strata connect claude-code. Imprime JSON, con las variables dentro de env; JSON no es un comando de terminal. Para cada par "NOMBRE": "valor", usa export NOMBRE="valor" en Bash o $env:NOMBRE="valor" en PowerShell. Sustituye ... por los valores reales, incluidos los modelos y los límites. Incluye CLAUDE_CODE_SIMPLE="1" solo si aparece en el JSON (contexto ≤ 40.960 tokens, 40K). Ejecuta claude en ese mismo terminal.

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
# Solo si aparece en el JSON (contexto ≤ 40.960 tokens):
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
# Solo si aparece en el JSON (contexto ≤ 40.960 tokens):
$env:CLAUDE_CODE_SIMPLE="1"
```

```sh
strata connect claude-code --show-key
strata connect claude-code --check
claude -p "tu tarea"
```

`claude` también es un alias de `claude-code` en el comando `strata connect`. Sin `--write`, muestra la configuración; con `--write`, guarda `~/.claude/settings.json` y crea una copia de seguridad del archivo existente. Después, usa `claude -p "tu tarea"` o `claude` para conversar.
El generador configura `ANTHROPIC_BASE_URL` (la dirección de Strata **sin /v1**, normalmente `http://127.0.0.1:8080`), `ANTHROPIC_AUTH_TOKEN` (la clave de tu Strata; no se usa ninguna cuenta de Anthropic), el modelo, `CLAUDE_CODE_MAX_CONTEXT_TOKENS` y `CLAUDE_CODE_MAX_OUTPUT_TOKENS`. Usa los límites de tu servidor que muestra el generador.
El aviso `[claude-code:unrecognized_model]` es inofensivo.

## Codex CLI

La misma precaución se aplica a Codex: --write modifica ~/.codex/config.toml global y cambia el proveedor a Strata. Sin modificar ese archivo, ejecuta strata connect codex sin --write; copia la configuración en opciones -c solo para esa ejecución y define STRATA_API_KEY en el terminal separado. La variable de la clave por sí sola no selecciona Strata. En la plantilla de abajo, sustituye ... por los valores generados; usa también los límites model_context_window y model_auto_compact_token_limit impresos por el generador. Al terminar esa ejecución y cerrar el terminal, la configuración global permanece como estaba.

Los ejemplos sin --write incluyen todas las opciones que codex_file escribe en harness.py.txt: model_reasoning_summary="auto", approval_policy="never", sandbox_mode="workspace-write" y check_for_update_on_startup=false, además del modelo, proveedor, límites y tiempo de espera. approval_policy="never" hace que Codex no pida aprobación. workspace-write permite escribir en el espacio de trabajo. Estas opciones -c solo valen para esta ejecución.

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

Sin `--write`, muestra la configuración; con `--write`, guarda `~/.codex/config.toml` y crea una copia de seguridad del archivo existente. Define `STRATA_API_KEY` en el terminal desde el que ejecutarás Codex, con la clave de tu Strata, según la salida del generador. No es una clave de OpenAI. La variable es obligatoria: si el servidor no exige una clave, el código oficial indica que sirve cualquier texto. No publiques tu clave.
El aviso `Model metadata ... not found` es inofensivo.

**Atención:** `--write` cambia la configuración global de la herramienta, que pasa a usar Strata. Para volver atrás, restaura la copia de seguridad creada (el comando indica la ruta); si no había un archivo anterior, elimina solo la configuración creada. Revierte también las variables de entorno que hayas definido.
`--check` comprueba la conexión enviando un prompt y una llamada a una herramienta al servidor elegido; estos comandos son instrucciones para el lector, no se ejecutaron aquí.
`strata connect` sin argumentos muestra las configuraciones disponibles; usa el identificador de la herramienta en el comando. OpenCode, por ejemplo, usa `strata connect opencode`.

## Quién puede acceder

Para empezar, déjalo en `local`.

| Opción de `--access` | Alcance | Precaución |
|---|---|---|
| `local` | Solo este PC, en `127.0.0.1` | Es la opción predeterminada. |
| `lan` | Otros dispositivos de tu red | Usa la dirección LAN que se muestra y la clave generada. |
| `tailscale` | Tu red Tailscale | Tailscale debe estar instalado y conectado. |
| `cloudflare` | Túnel por Internet | Necesita `cloudflared`; conserva la clave. |

Las opciones de acceso pertenecen a `strata launch`. La sintaxis documentada es `--access local|lan|cloudflare|tailscale`: elige un valor, no copies las barras como si fueran un comando.
Fuera del PC, Strata genera una clave. El terminal permite desactivarla, pero avisa que cualquier persona que pueda acceder a la dirección podrá usar el modelo y tus herramientas. **Conserva la clave.**
Para la conexión, la documentación ofrece `--url URL`, `--key KEY` o `--key-env NAME`; esos nombres en mayúsculas son marcadores para tus valores, no variables de entorno listas para usar.
Evita publicar la clave en registros, capturas de pantalla o repositorios. Comprueba el destino antes de enviar documentos.

## La privacidad tiene límites claros

El motor local no cobra por token; la energía y tu equipo siguen corriendo por tu cuenta. Esto no cambia las condiciones comerciales de cada herramienta conectada.
Strata no envía telemetría. Las descargas y actualizaciones usan la red; las búsquedas y páginas, los modelos externos, los túneles y los servidores de herramientas pueden enviar datos al exterior.
Los programas conectados tienen su propio comportamiento de red. No tomes “IA local” como garantía de que todo el conjunto funciona sin Internet.

Fuentes: [docs-oficiais/harness.py.txt](https://github.com/linnoff88-dev/strata-no-seu-pc/blob/main/docs-oficiais/harness.py.txt), [docs-oficiais/TERMINAL_LAUNCH.md](https://github.com/linnoff88-dev/strata-no-seu-pc/blob/main/docs-oficiais/TERMINAL_LAUNCH.md) (Connect your apps, Access), [docs-oficiais/INSTALL.md](https://github.com/linnoff88-dev/strata-no-seu-pc/blob/main/docs-oficiais/INSTALL.md), [docs-oficiais/SAFETY.md](https://github.com/linnoff88-dev/strata-no-seu-pc/blob/main/docs-oficiais/SAFETY.md), [FATOS.md](https://github.com/linnoff88-dev/strata-no-seu-pc/blob/main/FATOS.md).

Si ya usaste --write, cerrar el terminal no deshace el cambio global: restaura la copia de seguridad de ~/.claude/settings.json o ~/.codex/config.toml indicada por el comando; si no había un archivo anterior, elimina solo la configuración creada. Revierte también las variables de entorno. --check envía una solicitud y una llamada a herramienta al servidor elegido; no se ejecutó aquí.
