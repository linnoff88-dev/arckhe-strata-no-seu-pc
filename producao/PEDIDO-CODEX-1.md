# Pedido ao Codex — kit "strata-no-seu-pc" (kit + guia PT)

Você está em `/home/nmaldaner/projetos/strata-no-seu-pc/` (projeto novo do INEMA, público, grátis em inema.club).
Assunto: o **Strata** (github.com/Niko1221/Strata, MIT), motor gratuito e aberto que roda IA grande (Qwen3.8-Flash-Next e
outros) num PC comum, dividindo o modelo entre placa de vídeo, RAM e SSD. Método do kit: **"balcêo e despensa"** — o que a IA usa
toda hora fica no balcêo (placa de vídeo); o resto espera na despensa (RAM); o porêo é o SSD (a própria doc usa a cozinha).

Escreva em **português do Brasil**, frases curtas, falando com "você". Termos técnicos em inglês quando forem nomes de comando,
flag ou arquivo (strata launch, strata connect, install.sh, VRAM, SSD, API).

## Regras duras
- **Fonte única = `FATOS.md` (já escrito, NêO mude o sentido; pode acrescentar linhas com fonte) e a doc oficial copiada em
  `docs-oficiais/`** (README.pt-BR, MODELS, HOW_IT_WORKS, TERMINAL_LAUNCH, INSTALL, DGX_SPARK_LINUX, SAFETY, TROUBLESHOOTING,
  OLDER_GPUS, COMMUNITY_BENCHMARKS, SETTINGS, AI_SETUP, AGENTS). Todo número/comando/flag escrito no kit tem de estar lá.
  Nêo invente flag, porta, tamanho nem velocidade. Se nêo achar, nêo escreva.
- **Nêo dizer "testei", "instalei", "rodei", "medimos".** Nada foi rodado (ordem do Nei: "nêo precisa simular ou testar, só documentar").
  Números sêo "medidos pelo projeto / pela comunidade do projeto".
- Nêo citar canais do YouTube nem youtubers. Link oficial permitido: https://github.com/Niko1221/Strata (e páginas dele).
- Nêo rode o Strata, nêo instale nada, nêo baixe modelo, nêo chame API. Nêo copie código do Strata para cá.

## O que entregar
1. `DICAS.md` — **20 dicas** numeradas em blocos: Antes de instalar (some RAM + VRAM; disco livre; NVMe) · Escolher o tamanho
   (tabela; "o maior que cabe com folga"; Coder para programar; quando o SSD entra e fica lento; Unsloth × ISTA-DAS) · Instalar
   (app × terminal; Windows/Linux/Mac; DGX Spark/ARM só terminal; drivers) · Ligar nas ferramentas (strata connect, --write com
   backup, --check; endereço padrêo; chave fora de casa; --access) · Privacidade (sem telemetria, o que sai da máquina segundo
   SAFETY.md) · Quando dá erro (TROUBLESHOOTING.md: 5 problemas mais comuns e o que a doc manda fazer). Cada dica: título + 2–3
   linhas + (arquivo de origem). Inclua 3 **pegadinhas** (o que se fala por aí × o que a doc diz): "qualquer placa de 8 GB roda o
   de 94 GB" × a tabela de memória; "é só um script e pronto" × app/install.sh + escolher tamanho; "mais rápido = placa mais rápida"
   × "mais VRAM importa mais".
2. `TABELA.md` — "Qual tamanho cabe no meu PC": tabela por memória total (32 / 48 / 64 / 96 / 128+ GB) → o que a doc indica,
   com a velocidade relativa e a nota de qualidade da doc; uma linha para DGX Spark e Mac; os pacotes Unsloth; o modo pouca RAM.
3. `CONECTAR.md` — ligar Claude Code, Codex CLI, OpenCode e outros: o fluxo `strata connect` / `--write` / `--check` como a doc
   descreve, o endereço padrêo `http://127.0.0.1:8080`, acesso local × lan × tailscale × cloudflare, chave, e um aviso de segurança.
   Nêo invente variável de ambiente que a doc nêo mostre; se a doc mostrar o arquivo/variáveis de alguma ferramenta, copie igual.
4. `checklists/antes-de-instalar.md`, `checklists/instalar-windows.md`, `checklists/instalar-linux-mac.md`,
   `checklists/dgx-spark.md` (do DGX_SPARK_LINUX.md: o que roda, o que nêo roda, requisitos, comandos).
5. `ferramentas/qual_tamanho.sh` — script **só leitura** (bash, sem sudo, sem instalar nada) que lê RAM total (`/proc/meminfo` ou
   `sysctl` no Mac), VRAM (`nvidia-smi --query-gpu=memory.total` se existir; senêo "nêo achei placa NVIDIA"), arquitetura e disco
   livre, soma RAM+VRAM (memória unificada conta uma vez: se arquitetura aarch64 e nvidia-smi sem memória, use só a RAM) e imprime
   qual tamanho da TABELA.md cabe, o comando de instalaçêo do sistema dele e "veja TABELA.md". Variáveis `QT_FAKE_RAM_GB`,
   `QT_FAKE_VRAM_GB`, `QT_FAKE_ARCH`, `QT_FAKE_DISCO_GB` para simular. Nêo precisa de teste rodando (o Nei pediu só documentar),
   mas o script tem de passar `bash -n`.
6. `README.md` curto (PT): o que é, para quem, os arquivos, link do guia `https://inematds.github.io/strata-no-seu-pc/guia/`,
   link oficial do Strata, aviso "nada aqui foi rodado por nós: é a documentaçêo oficial organizada", e a seçêo
   **"O processo, do início ao fim"** (passos numerados com quem faz: 🧠 você · ⚙️ script · 🤖 IA).

## Guia PT: `guia/index.html`
Base obrigatória: copie `/home/nmaldaner/.claude/skills/projetos-landing-guia/assets/template.html` e **nêo reescreva o CSS**
(edite só conteúdo e placeholders; nenhum `{{...}}` pode sobrar). Leia antes `/home/nmaldaner/.claude/skills/projetos-landing-guia/SKILL.md`
(seções "Chamada da hero", "Texto breve", "Entendimento em cima, parte técnica embaixo", "Invariantes de design", "Estrutura")
e `~/projetos/inema-design/regras/chamada.md`. Molde de um guia aprovado ontem: `/home/nmaldaner/projetos/nod-n8n/guia/index.html`.
- Nome/emoji: `🧠 strata-no-seu-pc`. Repo: https://github.com/inematds/strata-no-seu-pc.
- **h1 pela dor/desejo, em "você", com o método**: "Você paga assinatura de IA e manda seus arquivos para fora. Rode uma IA grande
  no seu PC com **balcêo e despensa**." (`.amb` em "balcêo e despensa"). **lead** (1 parágrafo, branco): o Strata é um motor grátis
  e aberto que roda o Qwen3.8-Flash-Next (modelo de servidor) numa placa de vídeo comum, dividindo o trabalho entre placa, memória
  e SSD; liga no Claude Code e no Codex trocando só um endereço; sem conta, sem telemetria. Sem contagem de peças no h1/lead.
- CTA principal → `#metodo` ("Entender o método"); segundo → GitHub do kit.
- `<figure>` da hero: `assets/banner.jpg` (vai ser gerado depois; deixe o caminho).
- `#resumo` (Em resumo): 3–5 frases simples + "quem tem Windows ou Mac e só quer conversar pode usar o aplicativo e pular a parte
  técnica". Logo abaixo `<figure>` com `assets/banner-grade.jpg`.
- `#video` logo depois do resumo, **oculto** (`hidden`), com a marca exata `<!-- VIDEO: entra o explicavideo do projeto quando publicado -->`.
- Entendimento (antes do divisor técnico):
  1. `#metodo` "Balcêo e despensa" — a cozinha (placa = balcêo, RAM = despensa, SSD = porêo), 24.576 especialistas / 10 por palavra,
     "mais VRAM vale mais que placa mais rápida", "adivinha e confere". Cards, sem código.
  2. `#cabe` "O que cabe no seu PC" — a tabela (responsiva: wrapper `overflow-x:auto`, sem estourar 360 px).
  3. `#numeros` "O que o projeto mede" — cards grandes: ~48 tokens/s (placa de 16 GB + 128 GB RAM), ~46 tokens/s (DGX Spark),
     >1.000 tokens/s lendo texto longo, 262.144 tokens de contexto; frase "medido pelo projeto e pela comunidade dele, nêo por nós".
  4. `#ganho` "O melhor uso: suas ferramentas de graça" — servidor compatível com API OpenAI/Anthropic, Claude Code/Codex/OpenCode,
     custo zero por pergunta (a luz continua), dados em casa, cuidado com a chave.
  5. `#pegadinhas` tabela de 2 colunas.
  6. `#limites` "Onde ele ainda nêo resolve" (pouca RAM → SSD lento; ARM sem app; Q2_0/Gyro só x86; baixar 37–188 GB; é projeto novo).
  Termos explicados na primeira vez, em parênteses curtos: VRAM, RAM, SSD/NVMe, token, quantizaçêo/bits, API, MoE/especialistas.
- Divisor `#tecnico` (techhead) "O kit: para quem vai instalar hoje" + "Você nêo precisa desta parte para entender o que está acima".
  Zona técnica: `#kit` (cards para DICAS.md, TABELA.md, CONECTAR.md, checklists/, ferramentas/qual_tamanho.sh no GitHub);
  `#guia` passos `.step` com comandos REAIS: (1) "Vai usar só para conversar no Windows/Mac? Baixe o app" (link da release oficial);
  (2) descobrir o tamanho: baixar o kit (ZIP `https://github.com/inematds/strata-no-seu-pc/archive/refs/heads/main.zip` ou `git clone`)
  e `bash ferramentas/qual_tamanho.sh`; (3) instalar pelo terminal (os comandos oficiais Linux/Mac e PowerShell, iguais ao FATOS.md)
  e `strata launch`; (4) `strata connect` (e `--write`, `--check`); (5) DGX Spark. Explique em meia linha o que é terminal.
  `#dicas` as 20 dicas (acordeêo `<details>` por bloco).
- Nav: só as seções de entendimento + "Kit (técnico)" → `#tecnico`; INEMA.CLUB e PRO obrigatórios; botêo GitHub.
- Footer: pills (Strata, IA local, Qwen3.8, MIT) + link do repo + INEMA.CLUB.
- `<title>` e meta description em PT; 3 `<link rel="alternate" hreflang>` para `/guia/`, `/guia/en/`, `/guia/es/` de
  https://inematds.github.io/strata-no-seu-pc/.
- Nada de rolagem horizontal em 360 px. Nêo crie en/ nem es/ ainda.
- README.md: logo abaixo do `# título`, `[![strata-no-seu-pc](guia/assets/banner.jpg)](https://inematds.github.io/strata-no-seu-pc/guia/)`,
  depois `**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**`, `## O que é` (mesmo parágrafo
  do #resumo), `## 📖 Guia de uso` com a URL, e "O processo, do início ao fim".

No fim imprima: lista de arquivos criados, `bash -n ferramentas/qual_tamanho.sh && echo SINTAXE_OK`, `grep -c "{{" guia/index.html` (tem de ser 0)
e o número de seções do guia.
