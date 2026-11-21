# 20 dicas para usar o Strata no seu PC

Documentação organizada; nenhuma instalação ou execução do Strata foi feita por nós.

## Antes de instalar

### 1. Some sem duplicar

Some RAM (memória do computador) e VRAM (memória da placa). No Mac e em outros sistemas com memória unificada, conte uma vez. A soma é só a primeira triagem; reserve espaço para o sistema.

(Origem: `docs-oficiais/MODELS.md`).

### 2. Confira o disco livre

Download não é uso de RAM: os menores pacotes originais baixam 66–76 GB, além dos auxiliares. Escolha a pasta com espaço para download e preparação.

(Origem: `docs-oficiais/MODELS.md`, `docs-oficiais/INSTALL.md`).

### 3. Prefira SSD e observe o NVMe

SSD é armazenamento rápido; NVMe é uma interface de SSD. Se faltarem especialistas na RAM, buscá-los no disco deixa a resposta muito mais lenta; no DeepSeek, a doc pede NVMe.

(Origem: `docs-oficiais/MODELS.md`).

## Escolher o tamanho

### 4. Escolha o maior que cabe com folga

Use TABELA.md e confira a RAM separada da VRAM. Contexto e aplicativos abertos também ocupam memória; o maior arquivo disponível pode ser uma escolha ruim para seu PC.

(Origem: `docs-oficiais/MODELS.md`).

### 5. Coder é para programar

O Coder IQ1_M pede por volta de 32 GB de RAM com GPU adequada. Ele é mais fraco fora de código e em idiomas fora dos destacados na doc; para uso geral, prefira todos os especialistas quando couber.

(Origem: `docs-oficiais/MODELS.md`).

### 6. Pouca RAM leva trabalho ao SSD

Com 32 GB de RAM e placa de 24 GB, a doc descreve Q2_0, IQ2_XS e Coder no modo pouca RAM. Com placa de 12–16 GB, descreve Coder; strata launch não tem flag --low-ram.

(Origem: `docs-oficiais/MODELS.md`).

### 7. ISTA-DASLab primeiro; Unsloth depois

A doc recomenda começar pelo pacote compatível ISTA-DASLab que caiba. Unsloth guarda mais bits e pede mais RAM: UD-IQ4_XS baixa 94 GB e pede ~72 GB de RAM para todos os especialistas.

(Origem: `docs-oficiais/MODELS.md`).

### 8. Pegadinha: “qualquer placa de 8 GB roda o de 94 GB”

A placa sozinha não decide. Os 94 GB são o download do UD-IQ4_XS; a doc pede ~72 GB de RAM para manter seus especialistas, e menos RAM pode empurrar trabalho ao SSD.

(Origem: `docs-oficiais/MODELS.md`).

### 9. Pegadinha: “mais rápido = placa mais rápida”

A doc diz que mais VRAM importa mais que uma GPU mais rápida neste método. A placa guarda os especialistas mais usados; ter mais deles ali reduz o trabalho do processador.

(Origem: `docs-oficiais/HOW_IT_WORKS.md`).

## Instalar

### 10. Pegadinha: “é só um script e pronto”

Você escolhe app ou terminal, depois modelo e tamanho. O terminal usa install.sh ou install.ps1 e strata launch; baixar o instalador não significa ter o modelo pronto.

(Origem: `docs-oficiais/INSTALL.md`).

### 11. Escolha o caminho do seu sistema

Há app para Windows, Linux x86-64 e Mac Apple Silicon. Mac pede macOS 15 ou mais novo; Intel Arc usa terminal no Linux, e o pacote Mac não atende Mac Intel.

(Origem: `docs-oficiais/INSTALL.md`).

### 12. DGX Spark usa terminal

No Linux ARM64 não há app. O projeto documenta IQ3_S, NVFP4 e DeepSeek 2.00 bpw no Spark; Q2_0 e Gyro têm kernels só x86 e não rodam ali.

(Origem: `docs-oficiais/DGX_SPARK_LINUX.md`).

### 13. Driver não vem substituído pelo motor

Os pacotes CUDA 13 pedem driver NVIDIA 580 ou mais novo; no Spark, 580.65 ou mais novo. Placas NVIDIA antigas usam a rota CUDA 12; confira a documentação antes de escolher o pacote.

(Origem: `docs-oficiais/INSTALL.md`, `docs-oficiais/OLDER_GPUS.md`, `docs-oficiais/DGX_SPARK_LINUX.md`).

## Ligar nas ferramentas

### 14. Peça a configuração pronta

strata connect lista Claude Code, Codex CLI, OpenCode e outros. O endereço local padrão é http://127.0.0.1:8080; use o endereço que o Strata mostrar para o seu servidor.

(Origem: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 15. Grave com backup e confira

strata connect opencode --write pergunta antes de gravar e guarda backup do que substituir. strata connect opencode --check envia um prompt e uma chamada de ferramenta; isso é uma verificação que você poderá executar.

(Origem: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 16. Fora do computador, mantenha a chave

--access aceita local, lan, tailscale ou cloudflare. O Strata gera uma chave para acesso mais amplo; Tailscale precisa estar conectado e Cloudflare precisa de cloudflared. Não exponha a chave em prints.

(Origem: `docs-oficiais/TERMINAL_LAUNCH.md`, `docs-oficiais/SAFETY.md`).

## Privacidade

### 17. Sem telemetria não é sem nenhuma conexão

A doc diz que não há envio de uso, analytics ou relatórios de erro. Instalações e atualizações acessam a rede; buscas, páginas, túneis, serviços externos e servidores de ferramentas também podem acessá-la.

(Origem: `docs-oficiais/SAFETY.md`).

### 18. As ferramentas têm suas próprias regras

Conversas locais ficam no PC, mas um modelo externo recebe a conversa quando você o escolhe. Claude Code e Codex são programas separados: o Strata não controla o que eles enviam.

(Origem: `docs-oficiais/SAFETY.md`).

## Quando dá erro

### 19. Resolva caminho, download e driver

Comando não encontrado: abra novo PowerShell ou use o caminho do instalador no Linux/Mac. Download parou: repita a ação e confira espaço; as etapas completas são reaproveitadas. Driver antigo: atualize conforme o pacote e reinicie se necessário.

(Origem: `docs-oficiais/TROUBLESHOOTING.md`).

### 20. Resolva lentidão e porta ocupada

Primeira partida lenta: acompanhe o log, feche programas e reduza modelo/contexto se faltar memória. Porta ocupada: confira strata launch --status; --restart interrompe respostas atuais. Não encerre um programa alheio por ocupar a porta.

(Origem: `docs-oficiais/TROUBLESHOOTING.md`).

As dicas 19–20 reúnem cinco problemas frequentes para consulta: comando ausente, download interrompido, driver antigo, partida lenta e porta ocupada. A doc não publica um ranking de frequência.
