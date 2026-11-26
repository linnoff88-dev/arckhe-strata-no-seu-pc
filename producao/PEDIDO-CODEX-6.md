# Pedido ao Codex — fase 6: quinta rodada do revisor (nota 7) — fechar as divergências de uma vez

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte: FATOS.md + docs-oficiais/. Nêo diga "testei". Nêo rode o Strata.
Cada mudança nos três HTML (PT, en/, es/) trecho a trecho, sem regenerar en/es.

**Princípio para acabar com a divergência tabela × script:** UMA tabela só, por **RAM lida** (a soma é só referência, diga isso no topo),
com faixas contíguas e sem buraco: <30 · 30–45,9 · 46–61,9 · 62–93,9 · 94–125,9 · ≥126 (e uma linha separada para memória unificada:
DGX Spark e Mac, com as mesmas faixas). O script imprime EXATAMENTE o nome da faixa e a mesma lista de opções da linha da tabela
(mesmo texto), e depois a sobra calculada de cada opçêo da lista, com "cabe apertado" quando < 3 GB. Gere a tabela HTML e a TABELA.md a partir
das mesmas faixas (pode ser uma lista em bash no script + tabela escrita igual). Rode o script em 29, 31.3, 44.5, 46, 62.5, 94, 126 GB (VRAM 12)
e confira linha a linha com a tabela; cole as saídas.

1. **--plan depois de instalar**: o `strata launch --plan --family qwen --model <tamanho>` vai para DEPOIS do passo de instalaçêo (precisa do Strata
   instalado). No passo 2 fica só o script/Gerenciador de Tarefas. Ajuste a introduçêo do bloco.
2. Script na faixa ≥ 62 GB: compare o disco livre com a faixa de download da doc (66–76 GB para os três menores, ou o número da doc) e avise.
3. **Molde do Claude Code sem --write**: diga "copie TODAS as variáveis que o `strata connect claude-code` imprimir" e mostre o molde completo do
   `claude_env` do harness.py.txt (ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_MODEL, ANTHROPIC_SMALL_FAST_MODEL, ANTHROPIC_DEFAULT_*_MODEL,
   CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC, DISABLE_AUTOUPDATER, DISABLE_TELEMETRY, CLAUDE_CODE_MAX_CONTEXT_TOKENS, CLAUDE_CODE_MAX_OUTPUT_TOKENS,
   CLAUDE_CODE_SIMPLE quando contexto ≤ 40K — confira os nomes exatos no arquivo). Avise que ele imprime JSON e como virar `export`.
   Codex: inclua `stream_idle_timeout_ms` como o gerador oficial grava; separe Bash/PowerShell.
4. Node.js: link https://nodejs.org e conferir com `node -v` / `npm -v`.
5. Termos no 1º uso: tokens/s, 32K/128K (mil tokens), porta.
6. Lead mais curto: dor → soluçêo → mínimo de hardware (≤ 50 palavras), sem repetir "assinatura".
7. README.en.md / README.es.md: links para DICAS/TABELA/CONECTAR/checklists traduzidos.

No fim: as 7 saídas do script, `grep -c "{{"` nos 3 HTML, scrollWidth em 390 px nos 3 idiomas.
