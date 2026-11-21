# Pedido ao Codex — fase 7: sexta rodada do revisor (últimos defeitos concretos)

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte: FATOS.md + docs-oficiais/. Não diga "testei". Não rode o Strata.
Cada mudança nos três HTML (PT, en/, es/) e nos .md correspondentes; sem regenerar en/es do zero.

1. **--plan por família** (MODELS.md: `--family qwen|coder|gyro|unsloth|swift|deepseek41`): no passo 3 mostre o comando certo para cada opção da
   tabela — qwen (Q2_0/IQ2_XS/IQ3_XXS/IQ3_S), `--family coder --model IQ1_M`, Gyro (confira o nome exato do model na doc, ex. Gyro-S), Unsloth
   (`--family unsloth --model UD-IQ4_XS`…). Na tabela, ao lado de cada opção, o par `--family/--model`. O script também imprime o comando --plan
   de cada opção da faixa.
2. **Chave mascarada**: `strata connect claude-code` mostra a chave mascarada; diga para usar `strata connect claude-code --show-key` (ou pegar a
   chave em `strata launch --show-key`) antes de copiar ANTHROPIC_AUTH_TOKEN / STRATA_API_KEY. Idem Codex.
3. **Faixa 62–93,9 GB**: a doc diz "With 64 GB of RAM every size fits (IQ3_S with little else open)": liste os quatro (Q2_0, IQ2_XS, IQ3_XXS, IQ3_S)
   com a sobra de cada; Q2_0 o mais rápido. Tabela e script iguais (mesma fonte de faixas).
4. Sobra negativa no script: só a mensagem "não cabe no modo normal; só modo pouca RAM" (sem "cabe apertado" junto).
5. **EN/ES**: traduza as células da tabela (e da TABELA.en/.es.md) e os marcadores `<tamanho>`/`CHAVE_DO_STRATA` (→ `<size>`/`STRATA_KEY`,
   `<tamaño>`/`CLAVE_DE_STRATA`). O script: acrescente `QT_LANG=en|es` com as mensagens da saída traduzidas (as linhas principais: faixa, opções,
   sobra, avisos), padrão pt; as páginas EN/ES mandam usar `QT_LANG=en` / `QT_LANG=es`. ES padronizado em "tú".
6. **Termos**: uma frase antes da tabela: "Q2_0, IQ2_XS, IQ3_S, UD-Q4_K_XL, NVFP4 são níveis de compressão do mesmo modelo: menos bits = menos
   memória e um pouco menos de qualidade"; ISTA-DASLab e Unsloth = grupos que preparam esses pacotes; bpw (bits por peso), mmap, WSL, CLI, JSON, endpoint.
7. Codex sem --write: inclua as linhas que o gerador oficial grava (approval_policy, sandbox_mode, etc. — copie do harness.py.txt) e avise que
   `approval_policy="never"` faz o Codex não pedir aprovação.
8. Passo 1 (app): "antes, veja o tamanho na tabela (passo 2)" com link. Números: inclua DeepSeek na RTX 5070 + 64 GB (4–6 tokens/s, README).

No fim: saídas do script para (31.3,12), (62.5,16), (62.5,16,QT_LANG=en), (94,16,QT_LANG=es); `grep -c "{{"` nos 3 HTML; scrollWidth 390 nos 3;
`grep -cE "ção|não| você|Sem indicação" guia/en/index.html guia/es/index.html`.
