# Ligue suas ferramentas ao Strata

O Strata oferece um servidor compatível com API (interface de comunicação entre programas) OpenAI e Anthropic.
O endereço padrão é `http://127.0.0.1:8080`. Use o endereço efetivamente mostrado pelo seu servidor.
Você precisa instalar sua ferramenta separadamente e iniciar um modelo no Strata antes de conferir a conexão.

Instale Node.js com npm em [Node.js](https://nodejs.org). Confira as duas versões antes de instalar as CLIs:

```sh
node -v
npm -v
```

## Veja, grave, confira

```sh
strata launch
```

O monitor é a tela de acompanhamento que `strata launch` abre no terminal. Pressione `q`: ele pergunta se deve manter o servidor em segundo plano ou parar. Escolha manter para conectar suas ferramentas.
Claude Code e Codex CLI são assistentes de programação no terminal, instalados separadamente. Prompt é o pedido em texto enviado ao modelo.

WSL é Linux dentro do Windows. Shard é uma parte do arquivo do modelo. Endpoint é um endereço do servidor que recebe um tipo de pedido. Alias é um nome alternativo para o mesmo comando. Variável de ambiente é um valor com nome que o terminal passa aos programas abertos nele.

## Claude Code

strata connect claude-code e strata connect codex mostram a chave mascarada por padrão. Antes de copiar ANTHROPIC_AUTH_TOKEN ou STRATA_API_KEY, use strata connect claude-code --show-key ou strata connect codex --show-key, respectivamente; outra opção é strata launch --show-key. Copie a chave real, não a máscara.

Quem usa Claude Code pela assinatura: --write altera o arquivo global ~/.claude/settings.json; o Claude Code passa a usar o Strata e deixa de usar a assinatura nessas chamadas. Para preservar o global, abra um terminal separado e rode strata connect claude-code sem --write. Copie todas as variáveis que ele imprime (endereço, chave, modelos e limites) e exporte só nesse terminal. Os exemplos abaixo são moldes: substitua ... pelos valores impressos. Depois abra claude nesse mesmo terminal. Para voltar à assinatura, feche esse terminal.

Copie TODAS as variáveis que o strata connect claude-code imprimir. Ele imprime JSON, com as variáveis dentro de env; JSON não é um comando de terminal. Para cada par "NOME": "valor", use export NOME="valor" no Bash ou $env:NOME="valor" no PowerShell. Substitua ... pelos valores reais, inclusive modelos e limites. Inclua CLAUDE_CODE_SIMPLE="1" somente se aparecer no JSON (contexto ≤ 40.960 tokens, 40K). Execute claude nesse mesmo terminal.

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
# Somente se estiver no JSON (contexto ≤ 40.960 tokens):
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
# Somente se estiver no JSON (contexto ≤ 40.960 tokens):
$env:CLAUDE_CODE_SIMPLE="1"
```

```sh
strata connect claude-code --show-key
strata connect claude-code --check
claude -p "sua tarefa"
```

`claude` também é alias de `claude-code` no comando `strata connect`. Sem `--write`, mostra a configuração; com `--write`, grava `~/.claude/settings.json` com backup do arquivo existente. Depois use `claude -p "sua tarefa"` ou `claude` para conversar.
O gerador configura `ANTHROPIC_BASE_URL` (endereço do Strata **sem /v1**, normalmente `http://127.0.0.1:8080`), `ANTHROPIC_AUTH_TOKEN` (a chave do seu Strata; nenhuma conta da Anthropic é usada), modelo, `CLAUDE_CODE_MAX_CONTEXT_TOKENS` e `CLAUDE_CODE_MAX_OUTPUT_TOKENS`. Use os limites do seu servidor mostrados pelo gerador.
O aviso `[claude-code:unrecognized_model]` é inofensivo.

## Codex CLI

A mesma cautela vale para o Codex: --write altera ~/.codex/config.toml global e troca o provedor para Strata. Sem alterar esse arquivo, rode strata connect codex sem --write; copie a configuração para opções -c apenas nessa execução, além de definir STRATA_API_KEY no terminal separado. Só a variável da chave não seleciona o Strata. No molde abaixo, substitua ... pelos valores gerados; use também os limites model_context_window e model_auto_compact_token_limit impressos pelo gerador. Ao terminar essa execução e fechar o terminal, a configuração global continua sendo a anterior.

Os exemplos sem --write incluem todas as opções que codex_file grava em harness.py.txt: model_reasoning_summary="auto", approval_policy="never", sandbox_mode="workspace-write" e check_for_update_on_startup=false, além de modelo, provedor, limites e timeout. approval_policy="never" faz o Codex não pedir aprovação. workspace-write permite escrita no espaço de trabalho. Essas opções -c valem apenas para esta execução.

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

Sem `--write`, mostra a configuração; com `--write`, grava `~/.codex/config.toml` com backup do arquivo existente. Defina `STRATA_API_KEY` no terminal em que executará o Codex, com a chave do seu Strata, conforme a saída do gerador. Não é uma chave da OpenAI. A variável é obrigatória: se o servidor não exige chave, o código oficial informa que qualquer texto funciona. Não publique sua chave.
O aviso `Model metadata ... not found` é inofensivo.

**Atenção:** `--write` muda a configuração global da ferramenta, que passa a usar o Strata. Para voltar, restaure o backup criado (o comando informa o caminho); se não havia arquivo anterior, remova somente a configuração criada. Reverta também as variáveis de ambiente que definiu.
`--check` verifica a conexão enviando um prompt e uma chamada de ferramenta ao servidor escolhido; esses comandos são instruções para o leitor, não foram executados aqui.
`strata connect` sem argumentos lista as configurações disponíveis; use o identificador da ferramenta no comando. OpenCode, por exemplo, usa `strata connect opencode`.

## Quem pode acessar

Para começar, deixe em `local`.

| Opção de `--access` | Alcance | Cuidado |
|---|---|---|
| `local` | Só este PC, em `127.0.0.1` | É o padrão. |
| `lan` | Outros dispositivos da sua rede | Use o endereço LAN mostrado e a chave gerada. |
| `tailscale` | Sua rede Tailscale | Tailscale precisa estar instalado e conectado. |
| `cloudflare` | Túnel pela internet | Precisa de `cloudflared`; mantenha a chave. |

As opções de acesso pertencem a `strata launch`. A sintaxe documentada é `--access local|lan|cloudflare|tailscale`: escolha um valor, não copie as barras como comando.
Fora do PC, Strata gera uma chave. O terminal permite desativá-la, mas avisa que qualquer pessoa que alcance o endereço pode usar o modelo e suas ferramentas. **Mantenha a chave.**
Para a conexão, a doc oferece `--url URL`, `--key KEY` ou `--key-env NAME`; esses nomes em maiúsculas são lugares para seus valores, não variáveis de ambiente prontas.
Evite publicar a chave em logs, capturas ou repositórios. Confira o destino antes de enviar documentos.

## Privacidade tem limites claros

O motor local não cobra por token; a energia e seu equipamento continuam por sua conta. Isso não muda as regras comerciais de cada ferramenta conectada.
O Strata não envia telemetria. Downloads e atualizações usam a rede; buscas e páginas, modelos externos, túneis e servidores de ferramentas podem enviar dados para fora.
Os programas conectados têm comportamento de rede próprio. Não trate “IA local” como garantia de que todo o conjunto trabalha sem internet.

Fontes: [docs-oficiais/harness.py.txt](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/harness.py.txt), [docs-oficiais/TERMINAL_LAUNCH.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/TERMINAL_LAUNCH.md) (Connect your apps, Access), [docs-oficiais/INSTALL.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/INSTALL.md), [docs-oficiais/SAFETY.md](https://github.com/inematds/strata-no-seu-pc/blob/main/docs-oficiais/SAFETY.md), [FATOS.md](https://github.com/inematds/strata-no-seu-pc/blob/main/FATOS.md).

Se já usou --write, fechar o terminal não desfaz a mudança global: restaure o backup de ~/.claude/settings.json ou ~/.codex/config.toml indicado pelo comando; se não havia arquivo anterior, remova somente a configuração criada. Reverta também as variáveis de ambiente. --check envia um pedido e uma chamada de ferramenta ao servidor escolhido; não foi executado aqui.
