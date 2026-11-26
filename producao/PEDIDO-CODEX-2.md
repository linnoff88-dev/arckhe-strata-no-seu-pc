# Pedido ao Codex — fase 2: correções do revisor no guia PT e no kit, depois EN/ES

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte única continua: FATOS.md + docs-oficiais/. Nêo diga "testei".
Nêo rode o Strata nem instale nada.

## A. Correções no PT (guia/index.html e arquivos do kit citados)
1. **Tabela "O que cabe"**: acrescente a linha do PC gamer comum, ex. "40–47 GB (12 GB de placa + 32 GB de RAM)": o que a doc diz
   (MODELS.md: PC de 32 GB com placa de 12–16 GB roda o **Coder** no modo pouca RAM, bem mais lento porque a maior parte vem do SSD) e as
   alternativas que a doc lista: **Qwen3.6-35B-A3B** (32 a 52 GB de RAM) e **DeepSeek V4.1-Flash** (placa de 12 GB + 46–64 GB de RAM +
   257 GB de disco). Corrija a linha "32 GB" para nêo se contradizer com o critério de soma. Antes da tabela, uma frase: "Q2_0, IQ2_XS,
   IQ3_XXS, IQ3_S sêo tamanhos (pacotes) do mesmo modelo; ISTA-DASLab e Unsloth sêo quem preparou cada pacote." Atualize TABELA.md igual.
2. **Passo 4 / CONECTAR.md — Claude Code e Codex explícitos**: diga o nome que a doc usa em `strata connect` para cada um (confira em
   TERMINAL_LAUNCH.md a lista: OpenCode, Codex CLI, Claude Code, oh-my-pi, pi, Hermes Agent, OpenClaw…; use o identificador exato que a doc
   mostrar; se a doc nêo mostrar o identificador, diga "rode `strata connect` sem nada e escolha Claude Code na lista"). Avise, nesse passo,
   que o Claude Code precisa de `CLAUDE_CODE_MAX_CONTEXT_TOKENS` (TERMINAL_LAUNCH.md:206) e que o `strata connect` preenche isso.
3. **Rodapé**: tire "Banners, vídeo e versões EN/ES serêo acrescentados depois". Nada com cara de rascunho.
4. **Card ~48 tokens/s**: avise em meia linha que é uma mediçêo da comunidade (build do código, versêo 0.1.41, uma rodada) e ponha ao lado
   um número de placa de 12 GB da doc (RTX 3060 12 GB + 46 GB de RAM: DeepSeek V4.1-Flash 9 a 11 tokens/s no README; ou o que a doc tiver
   de Qwen com 12 GB) — o caso mais comum.
5. **h1**: inclua o nome Strata (ex.: "...Rode uma IA grande no seu PC com o Strata e o método **balcêo e despensa**.") mantendo a dor em "você".
6. Passo 1: "o nome do arquivo muda a cada versêo". Passo 3: o `curl` salva `install.sh` na pasta atual; o que aparece no fim (se a doc disser).
7. Termos sem explicaçêo: bpw, kernels, x86, ARM64, CUDA, contexto — parênteses curtos na primeira vez.

## B. Três idiomas (depois de A)
- Copie o PT final para `guia/en/index.html` e `guia/es/index.html` com o texto traduzido (inglês natural e espanhol neutro da América
  Latina). Mesma estrutura, CSS, JS, ids, URLs, comandos, flags, números e nomes próprios. `<html lang>` certo; imagens `../assets/`;
  banners por idioma: `../assets/banner-en.jpg`, `../assets/banner-grade-en.jpg` (e -es) — esses arquivos serêo gerados à parte, só aponte.
  Seletor PT/EN/ES com `a.on` certo; hreflang nos 3. Blocos `<pre>` com comandos ficam iguais; comentários dentro deles traduzidos.
  Links para arquivos do kit em PT continuam, com a marca "(in Portuguese)" / "(en portugués)".
- `README.en.md` e `README.es.md` (mesma estrutura do README.md, banner `guia/assets/banner-en.jpg` / `banner-es.jpg`, link do guia
  `.../guia/en/` e `.../guia/es/`).
- Confira: `grep -cE "çêo|nêo| você" guia/en/index.html guia/es/index.html` (perto de 0, fora nomes de arquivo) e `grep -c "{{"` = 0 nos 3.

No fim imprima o que mudou em A, as contagens de B e a lista de arquivos.
