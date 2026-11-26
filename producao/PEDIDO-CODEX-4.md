# Pedido ao Codex — fase 4: terceira rodada do revisor

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte: FATOS.md + docs-oficiais/ (inclui harness.py.txt). Nêo diga "testei". Nêo rode o Strata.
Aplique cada mudança nos três HTML (PT, en/, es/) trecho a trecho (sem regenerar en/es do zero). Rode o NOSSO script com QT_FAKE_* para conferir.

1. `ferramentas/qual_tamanho.sh`: margem nos limiares (MemTotal fica abaixo do pente instalado): r≥30 conta como "32 GB", r≥46 como 48, r≥62 como 64,
   r≥94 como 96, r≥126 como 128; diga "X GB lidos ≈ PC de Y GB". Tire a frase fixa "32 GB totais nêo comportam..." do ramo final (só quando for o caso).
   Na faixa 96 GB, só os pacotes Unsloth que cabem. Rode e cole as saídas: (31.3 RAM, 12 VRAM), (40, 8), (46.9, 16), (62.5, 16), (125, 0 aarch64), (15.5, 8).
   A saída do script e a tabela da página têm de dar a mesma resposta em cada caso. Com < 30 GB de RAM: diga claramente que fica abaixo do mínimo da doc.
2. Passo 4: pré-requisitos — Claude Code e Codex CLI precisam estar instalados (`npm i -g @anthropic-ai/claude-code`, `npm i -g @openai/codex`,
   do harness.py oficial; precisam do Node.js). Chave: de onde vem (`strata launch --show-key` ou a tela Connect do launch, `k` mostra — confira em
   TERMINAL_LAUNCH.md) e como definir `STRATA_API_KEY` no Linux/Mac (`export STRATA_API_KEY=...`) e no PowerShell (`$env:STRATA_API_KEY="..."`).
3. Passo 3: como conferir que funcionou — o que TROUBLESHOOTING.md / AI_SETUP.md mandam (`strata launch --status`, `curl -fsS http://127.0.0.1:8080/health`;
   confira os comandos exatos na doc).
4. Tabela linha 96 GB: use a tabela de velocidade dos Unsloth do MODELS.md (R9700, com o IQ3_S ao lado) em vez de "sem velocidade comparável".
   Em "O que o projeto mede", inclua a tabela oficial do MODELS.md da RTX 5070 12 GB + 64 GB (Q2_0 ~94, IQ3_S ~53 tokens/s — confira os números) como o caso
   mais próximo do PC comum; avise que README e MODELS.md dêo números diferentes para a RTX 3060 no DeepSeek (9–11 × 6–9) e cite os dois.
5. Hero/lead: diga já no lead o mínimo prático segundo a doc ("a partir de 32 GB de RAM com placa de 12 GB, mais lento; 48–64 GB de RAM para o modelo
   principal"). Troque "confortável" pela frase literal da doc. Passo 1 Linux: `chmod +x` no AppImage (INSTALL.md). Rotule "~58,6 GB do Coder" como
   estimativa do kit também na página.
6. EN/ES: traduza DICAS.md e as 4 checklists (`DICAS.en.md`, `DICAS.es.md`, `checklists/*.en.md`, `*.es.md`, pelo `ARCKHÉ-traduz`), aponte os links das
   páginas EN/ES para eles e corrija "TABELA.md (in Portuguese)" → TABELA.en.md (e o ES). A saída do script continua em PT: diga isso numa linha nas páginas EN/ES.

No fim: as 6 saídas do script, `grep -c "{{"` nos 3 HTML, `grep -cE "çêo|nêo| você"` em en/es.
