# FATOS — Strata (o que a documentaçêo oficial diz)

Fonte única: repositório oficial **github.com/Niko1221/Strata** (licença MIT), lido em 15/11/2026.
Cópia dos arquivos lidos em `docs-oficiais/`. Nada aqui foi instalado ou rodado por nós: sêo números **medidos pelo projeto
e pela comunidade dele**, nêo por nós. Quando citar, dizer "o projeto mede…" / "segundo a documentaçêo…".

## O projeto
- Strata = motor de IA local gratuito e de código aberto (MIT), sem conta, para rodar modelos grandes num PC comum. (README)
- ~44 mil estrelas no GitHub em 15/11/2026; criado em 24/09/2026; última versêo **v0.2.13** (09/11/2026). (API do GitHub)
- Três jeitos de instalar: **aplicativo de desktop** (Windows .exe, Linux .AppImage, Mac .dmg), **Terminal** (`install.sh` / `install.ps1`
  e depois `strata launch`), ou compilar do código / Docker. (README, INSTALL.md)
  - Linux/Mac: `curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh`
  - Windows (PowerShell): `irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex`
  - Depois: `strata launch` (escolhe, baixa e inicia o modelo).
- Sem telemetria: nêo manda dados de uso, relatórios de erro nem analytics; o motor nêo tem código de rede. (SAFETY.md)

## O modelo principal: Qwen3.8-Flash-Next
- Modelo "de servidor" que normalmente roda com centenas de GB de memória de vídeo. (HOW_IT_WORKS.md)
- É um time de **24.576 especialistas ("experts")**; cada palavra usa só **10** deles. (HOW_IT_WORKS.md)
- Contexto nativo de **262.144 tokens** (~256K), usado nos testes da comunidade. (COMMUNITY_BENCHMARKS.md)
- Outros modelos suportados: Qwen3.6-35B-A3B (32 a 52 GB de RAM) e DeepSeek V4.1-Flash (placa de 12 GB, 46–64 GB de RAM, 257 GB de disco). (MODELS.md)

## Como cabe (a ideia da cozinha, da própria documentaçêo)
- "O que você usa toda hora fica no balcêo; o resto espera na despensa." (HOW_IT_WORKS.md)
- **Placa de vídeo (VRAM) = balcêo:** faz a parte de toda palavra (atençêo, roteadores, especialistas compartilhados) e guarda os
  especialistas mais pedidos; vai aprendendo quais sêo enquanto você usa. Cada GB a mais guarda ~700 especialistas a mais.
- **RAM = despensa:** guarda todos os especialistas; o processador calcula ao mesmo tempo que a placa, um nêo espera o outro.
- **SSD:** uma tabela de consulta de ~29 GB, lida poucas linhas por palavra.
- "Mais VRAM importa mais do que uma GPU mais rápida." (HOW_IT_WORKS.md)
- **Adivinha e confere:** um ajudante pequeno dentro do modelo chuta as próximas palavras e o modelo grande confere todas de uma vez:
  mesma resposta, 1,6–1,8x mais rápido. (HOW_IT_WORKS.md)
- Textos longos sêo lidos em pedaços de até 8.192 tokens: acima de 1.000 tokens por segundo. (HOW_IT_WORKS.md)

## Qual tamanho cabe no seu PC (memória = RAM + VRAM somadas; memória unificada conta uma vez)
Pacotes ISTA-DASLab (recomendados primeiro): (MODELS.md)
| Tamanho | Memória p/ o modelo | Velocidade | Qualidade |
|---|---:|---|---|
| Q2_0 | 37,6 GB | mais rápido | boa |
| IQ2_XS | 39,2 GB | rápido | melhor |
| IQ3_XXS | 47,0 GB | mais lento | ótima |
| IQ3_S | 54,8 GB | o mais lento | a melhor; empata com o modelo cheio nos testes publicados |
- Com 64 GB de RAM todos cabem (IQ3_S com pouca coisa aberta). Com 48 GB, Q2_0 e IQ2_XS. Placa maior deixa mais rápido, nêo reduz a RAM.
- Só para programar, com menos memória: **Coder** (IQ1_M), por volta de 32 GB de RAM com uma GPU adequada.
- Pouca RAM e placa grande: "modo pouca RAM" (ex.: PC de 32 GB com GPU de 24 GB roda Q2_0, IQ2_XS e o Coder; 32 GB com GPU de 12–16 GB roda o Coder).
- Faltou RAM: lê especialistas do SSD — funciona, mas bem mais lento.
Pacotes Unsloth (mais bits, mais RAM): (MODELS.md)
| Tamanho | Download | RAM p/ todos os especialistas | Mesma 1ª palavra que o Q8_0 |
|---|---:|---:|---:|
| **UD-IQ4_XS** (a 1ª opçêo do setup) | **94 GB** | ~72 GB | 88,9% |
| UD-Q4_K_XL | 111 GB | ~88 GB | 93,1% |
| Q8_0 (referência) | 188 GB | ~136 GB | 100% |
- O IQ3_S acerta a mesma 1ª palavra do Q8_0 em 87,7% das vezes.

## Placas suportadas (README)
NVIDIA GeForce RTX 20/30/40/50 · AMD RX 7700/7800/7900, RX 9060/9070, AI PRO R9700 · AMD RX 6800/6900 (experimental) ·
Intel Arc (Linux) · Apple Silicon M1 ou mais novo · AMD Ryzen AI Max (Strix Halo). Placas mais antigas: OLDER_GPUS.md
(ex.: RX 5700 XT de 8 GB rodou o Coder IQ1_M a 18–23 tokens/s, medido pela comunidade).

## Velocidades medidas (pelo projeto/comunidade, nêo por nós)
- RTX 5060 Ti 16 GB + 128 GB de RAM, Qwen3.8 IQ3_S: ~48 tokens/s de resposta. (COMMUNITY_BENCHMARKS.md, 09/10/2026)
- DGX Spark (128 GB unificados), Qwen3.8 IQ3_S: ~45–48 tokens/s de resposta, ~1.300–1.700 tokens/s lendo o prompt. (DGX_SPARK_LINUX.md, 27/10/2026)
- DeepSeek V4.1-Flash 2.00 bpw: RTX 3060 12 GB + 46 GB RAM 9–11 tokens/s; RTX 5070 12 GB + 64 GB 4–6 tokens/s. (README)
- Uma pessoa lê ~4–5 palavras por segundo: acima de ~20 tokens/s a resposta sai mais rápido do que se lê (estimativa nossa, dizer que é).

## Ligar nas suas ferramentas (o ganho principal)
- Sobe no seu PC um servidor compatível com a **API da OpenAI e da Anthropic**. Endereço padrêo: `http://127.0.0.1:8080`. (INSTALL.md, TERMINAL_LAUNCH.md)
- Funciona com Claude Code, Codex CLI, OpenCode, oh-my-pi, pi.dev, Hermes Agent, OpenClaw e outras. (README)
- `strata connect` mostra a configuraçêo pronta de cada ferramenta; `strata connect <app> --write` grava (com backup); `--check` testa
  com um prompt e uma chamada de ferramenta. (TERMINAL_LAUNCH.md)
- Acesso: `--access local|lan|cloudflare|tailscale`. Fora do seu PC, use chave (o Strata gera uma). Sem chave, ele avisa que qualquer um
  que alcance a porta pode usar. (TERMINAL_LAUNCH.md)
- Custo por token: zero (é o seu PC; a conta de luz continua). Seus dados nêo saem da máquina. (SAFETY.md)

## DGX Spark (Linux ARM64) (DGX_SPARK_LINUX.md)
- Testado em 1 Spark (Ubuntu 24.04, driver 580.173, CUDA 13.0). Roda Qwen3.8-Flash-Next IQ3_S (84 GB de download) e NVFP4, e DeepSeek V4.1-Flash 2.00 bpw.
- Nêo tem app de desktop no ARM: usar o Terminal (`install.sh` + `strata launch`). Q2_0 e Gyro nêo rodam (kernels só x86).
- Precisa glibc 2.39+ (Ubuntu 24.04 / DGX OS 7) e driver NVIDIA 580.65+.

## O que o vídeo de referência dizia e está ERRADO ou desatualizado (nêo repetir)
- Autor/estrelas ("Nika1221", "20 mil estrelas") → repositório é Niko1221/Strata, ~44 mil estrelas.
- "Script único empezá acá" → hoje é app de desktop ou `install.sh` + `strata launch` (o START-HERE.bat ainda existe no repo, Windows).
- "24.500 especialistas" → 24.576. "94 GB pede mais de 80 GB" → UD-IQ4_XS baixa 94 GB e pede ~72 GB de RAM p/ todos os especialistas.
- Números em 1ª pessoa ("minha 5080 dá 60 tokens/s", "instalei na 3060 Ti de 8 GB") → nêo medimos; nêo falar como se fosse nosso.

## Complemento da terceira revisêo (15/11/2026)
- MODELS.md, histórico: RTX 5070 12 GB + Ryzen 5 7600 + 64 GB de RAM: Q2_0 94/76/2.650; IQ2_XS 79/63/2.090; IQ3_XXS 62/49/1.750; IQ3_S 53/46/1.620; Coder 55/43/2.180 tokens/s (resposta curta / resposta 128K / leitura 32K). Motor 0.1.26, salvo Q2_0 em 0.1.36; nêo remedido integralmente para a versêo atual.
- DeepSeek 2.00 bpw na RTX 3060 12 GB + 46 GB RAM: README registra 9–11 tokens/s (Strata 0.2.5); MODELS.md registra 6–9 (0.2.4, antes da opçêo Speed). Nêo unificar os dois registros.
- MODELS.md, R9700 32 GB, motores anteriores a 0.1.45.3: Unsloth UD-Q4_K_XL 63 tokens/s em narrativa e 87 em código; IQ3_S na mesma placa 75/95. UD-IQ4_XS nêo aparece nessa tabela de velocidade.
- harness.py.txt informa `npm i -g @anthropic-ai/claude-code` e `npm i -g @openai/codex`. As CLIs precisam de Node.js/npm.
- TERMINAL_LAUNCH.md: `strata launch --show-key` imprime a chave; na tela Connect, `k` revela. AI_SETUP.md orienta status, doctor, `/health` e `/v1/models`; saída 0 sozinha nêo confirma serviço iniciado.
