# Pedido ao Codex — fase 3: segunda rodada do revisor (PT primeiro, depois espelhar em EN/ES à mêo)

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte: FATOS.md + docs-oficiais/ (inclui agora `docs-oficiais/harness.py.txt`, o código
oficial do `strata connect`). Nêo diga "testei". Nêo rode o Strata. **Nêo use o tradutor para regenerar en/es do zero**: aplique as mesmas
mudanças nos três HTML (PT, en/, es/) trecho a trecho, traduzindo só os trechos novos.

1. **PC gamer comum (12–16 GB de placa + 32 GB de RAM), uso geral**: a doc (MODELS.md, "Less memory, general use: compare Unsloth, then Gyro")
   indica o **Gyro-S** (27,6 GB somando RAM e placa, o menor, qualidade menor, mais lento; confira a tabela Gyro em MODELS.md ~linha 215) e o
   Coder para código. Ponha isso na linha "40–47 GB" da tabela, no TABELA.md, numa dica e no passo 2. Explique Gyro e NVFP4 em parênteses curtos
   (ex.: "Gyro: um jeito de compactar que usa menos memória e é mais lento"; "NVFP4: formato de 4 bits da NVIDIA para placas novas").
2. **RAM × soma**: deixe a regra da doc explícita (MODELS.md ~linha 121: o modelo cabe quando a **RAM** tem os especialistas + ~10 GB para o
   sistema; a placa maior deixa mais rápido, nêo reduz a RAM, fora do modo pouca RAM). Ponha a tabela "especialistas na RAM" da doc
   (Q2_0 34 / IQ2_XS 35,5 / IQ3_XXS 43 / IQ3_S 50 / Coder 23 GB — confira os números exatos no MODELS.md) e corrija as linhas 48/64 GB para falar
   de RAM. O h1 continua; logo abaixo da tabela, uma frase: "para uso geral confortável a doc aponta 48–64 GB de RAM; com menos, Gyro ou Coder, mais lentos".
3. **Script × tabela**: `ferramentas/qual_tamanho.sh` tem de usar as MESMAS faixas e a mesma regra da tabela nova (RAM para os especialistas;
   soma só como referência; memória unificada conta uma vez) e comparar o disco livre com o download do tamanho sugerido (avisar se nêo cabe).
   Exemplos que têm de bater com a tabela: 12 GB placa + 32 GB RAM → Gyro-S (uso geral) ou Coder (código), mais lentos; 16 + 64 → IQ3_S;
   aarch64 128 GB unificado → IQ3_S ou NVFP4 (DGX Spark). Rode `bash -n` e rode o script com as variáveis QT_FAKE_* nesses 3 casos
   (é só o nosso script de leitura, nêo o Strata) e cole as saídas no fim.
4. **Windows sem bash**: no passo 2, para Windows: onde ver RAM, memória da placa e disco livre (Gerenciador de Tarefas > Desempenho:
   Memória, GPU "Memória dedicada", Disco; ou "Configurações > Sistema > Sobre") e comparar com a tabela. O script fica para Linux/Mac/WSL.
5. **Passo 4, ligar no Claude Code e no Codex** — do `harness.py.txt` oficial:
   - Claude Code: `strata connect claude-code` (alias `claude`) mostra o que entra em `~/.claude/settings.json`; `strata connect claude-code --write`
     grava com backup; `strata connect claude-code --check` testa. Ele configura `ANTHROPIC_BASE_URL` (o endereço **sem** /v1),
     `ANTHROPIC_AUTH_TOKEN` (a chave do seu Strata, nenhuma conta da Anthropic é usada), `CLAUDE_CODE_MAX_CONTEXT_TOKENS` e
     `CLAUDE_CODE_MAX_OUTPUT_TOKENS`. Depois: `claude -p "sua tarefa"` ou `claude`. Aviso "[claude-code:unrecognized_model]" é inofensivo.
   - Codex CLI: `strata connect codex` / `--write` grava `~/.codex/config.toml` e usa a variável `STRATA_API_KEY`; depois
     `codex exec --skip-git-repo-check "sua tarefa"`. Aviso "Model metadata ... not found" é inofensivo.
   - Atençêo: o `--write` muda a config global da ferramenta (ela passa a usar o Strata); para voltar, o backup que ele cria.
   Uma linha dizendo o que sêo Claude Code e Codex ("assistentes de programaçêo no terminal"). Tire "escolha na lista".
   Explique "monitor" = a tela de acompanhamento que o `strata launch` abre no terminal (e o `q` sai dela deixando o servidor rodando, se a doc diz isso).
   Atualize CONECTAR.md igual.
6. Passo 1: inclua Linux (AppImage) no título ou explique. Dica de acesso: "para começar, deixe em local" + 1 linha por opçêo (local, lan, tailscale,
   cloudflare). Termos: PowerShell (como abrir), release, prompt, DGX Spark (computador compacto da NVIDIA com 128 GB de memória unificada).
7. Rodapés de fonte: link para FATOS.md e docs-oficiais/ no GitHub (https://github.com/inematds/strata-no-seu-pc/blob/main/...).
8. Repo: mova `PEDIDO-CODEX-*.md` e `FALHAS.md` para uma pasta `producao/` (fica como registro, fora da raiz). Nêo apague.
9. Traduza TABELA.md e CONECTAR.md para `TABELA.en.md`, `TABELA.es.md`, `CONECTAR.en.md`, `CONECTAR.es.md` (pelo tradutor central
   `inema-traduz` se preferir) e aponte os links das páginas EN/ES para eles.

No fim: diff resumido por item, `grep -c "{{"` nos 3 HTML (0), `grep -cE "çêo|nêo| você"` em en/es (0), e as 3 saídas do script.
