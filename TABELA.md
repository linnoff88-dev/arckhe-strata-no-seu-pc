# Qual tamanho cabe no meu PC

Escolha pela RAM lida. A soma RAM + VRAM é apenas referência; memória unificada conta uma vez. As faixas são contíguas: 30–45,9 significa 30 ≤ RAM < 46, inclusive leituras como 45,99. São grupos conservadores do kit, não novos requisitos oficiais.

Q2_0, IQ2_XS, IQ3_S, UD-Q4_K_XL, NVFP4 são níveis de compressão do mesmo modelo: menos bits = menos memória e um pouco menos de qualidade. ISTA-DASLab e Unsloth são grupos que preparam esses pacotes.

bpw significa bits por peso (quantos bits guardam cada parâmetro do modelo). mmap mapeia um arquivo em memória e permite ler partes dele conforme necessário. WSL é Linux dentro do Windows. CLI é a interface de linha de comando, usada pelo terminal. JSON é um formato de dados com nomes e valores. Endpoint é um endereço do servidor que recebe um tipo de pedido.

| Memória | RAM lida | Opções e par --family / --model |
|---|---|---|
| RAM + placa separada | <30 GB | Sem indicação automática segura |
| RAM + placa separada | 30–45,9 GB | Gyro-S (`--family gyro --model Gyro-S`); Coder (`--family coder --model IQ1_M`) |
| RAM + placa separada | 46–61,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`) |
| RAM + placa separada | 62–93,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`) |
| RAM + placa separada | 94–125,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`) |
| RAM + placa separada | ≥126 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`); UD-Q5_K_XL (`--family unsloth --model UD-Q5_K_XL`); UD-Q6_K_XL (`--family unsloth --model UD-Q6_K_XL`) |
| Unificada: Mac / DGX Spark | <30 GB | Sem indicação automática segura |
| Unificada: Mac / DGX Spark | 30–45,9 GB | Sem indicação automática segura |
| Unificada: Mac / DGX Spark | 46–61,9 GB | IQ2_XS (Mac) (`--family qwen --model IQ2_XS`) |
| Unificada: Mac / DGX Spark | 62–93,9 GB | IQ3_XXS (Mac) (`--family qwen --model IQ3_XXS`); IQ3_S (Mac) (`--family qwen --model IQ3_S`) |
| Unificada: Mac / DGX Spark | 94–125,9 GB | IQ3_S (Mac ou DGX Spark de 128 GB) (`--family qwen --model IQ3_S`); NVFP4 (somente DGX Spark de 128 GB) (`--family nvfp4 --model NVFP4`) |
| Unificada: Mac / DGX Spark | ≥126 GB | IQ3_S (Mac ou DGX Spark de 128 GB) (`--family qwen --model IQ3_S`); NVFP4 (somente DGX Spark de 128 GB) (`--family nvfp4 --model NVFP4`) |

Na faixa 62–93,9 GB de RAM com placa separada, os quatro pacotes são opções: Q2_0 é o mais rápido. Com leitura de 62,5 GB, sobram Q2_0: 18,5 GB; IQ2_XS: 17 GB; IQ3_XXS: 9,5 GB; IQ3_S: 2,5 GB. A conta reserva 10 GB para o sistema. A doc diz que com 64 GB de RAM todos cabem, IQ3_S com pouca coisa aberta.

Sobra estimada: RAM lida − especialistas − 10 GB. Especialistas: Q2_0 34; IQ2_XS 35,5; IQ3_XXS 43; IQ3_S 50; Coder 23; Unsloth UD-IQ4_XS 72, UD-Q4_K_XL 88, UD-Q5_K_XL 108 e UD-Q6_K_XL 118 GB. Sobra de 0 a menos de 3 GB: “cabe apertado”; negativa: “não cabe no modo normal; só modo pouca RAM”. Na faixa 30–45,9, é preciso GPU compatível de pelo menos 12 GB; Coder usa pouca RAM e SSD, com perda de velocidade. Para Gyro-S, a doc só dá memória conjunta: sobra de referência = RAM + VRAM − 27,6 − 10 GB; isso não confirma a divisão entre as duas memórias.

Memória unificada: as mesmas faixas, sem somar VRAM. Mac exige Apple Silicon e macOS 15+; confira o pacote no plano. As opções Spark só valem para o DGX Spark documentado de 128 GB nominais, mesmo se o sistema ler 125 GB. Outro ARM não está confirmado. No Spark, NVFP4 usa arquivo de especialistas de 68 GB com mmap: RAM − 68 − 10 é só referência, pois contexto, cache e tabela também disputam memória. Q2_0 e Gyro não rodam no Spark.

Disco: Q2_0, IQ2_XS e IQ3_XXS têm faixa conjunta de download de 66–76 GB; o script compara com 76 GB. IQ3_S: 84 GB é referência do DGX Spark, não número universal para x86; confirme com --plan após instalar. Gyro-S: 58,5 GB. Coder: ~58,6 GB, estimativa do kit (29,6 + ~29). Unsloth: 94/111/158/169 GB na ordem da lista; NVFP4: 128 GB. Reserve espaço extra para auxiliares e preparação. IQ3_S pede pouca coisa aberta; Q8_0 não entra na lista automática: ~136 GB só de especialistas.

Depois de instalar o Strata e abrir um novo terminal, confira o plano antes de baixar o modelo. Escolha somente o comando da opção compatível da tabela; --plan mostra o plano sem iniciar o modelo. Não troque só o tamanho mantendo a família qwen: Coder, Gyro, Unsloth e NVFP4 têm famílias próprias. Para IQ3_S em x86, confirme aqui o download da sua plataforma.

```sh
strata launch --plan --family gyro --model Gyro-S
strata launch --plan --family coder --model IQ1_M
strata launch --plan --family qwen --model Q2_0
strata launch --plan --family qwen --model IQ2_XS
strata launch --plan --family qwen --model IQ3_XXS
strata launch --plan --family qwen --model IQ3_S
strata launch --plan --family unsloth --model UD-IQ4_XS
strata launch --plan --family unsloth --model UD-Q4_K_XL
strata launch --plan --family unsloth --model UD-Q5_K_XL
strata launch --plan --family unsloth --model UD-Q6_K_XL
strata launch --plan --family nvfp4 --model NVFP4
```

Fontes / Sources / Fuentes: [MODELS.md](docs-oficiais/MODELS.md), [DGX_SPARK_LINUX.md](docs-oficiais/DGX_SPARK_LINUX.md), [FATOS.md](FATOS.md).
