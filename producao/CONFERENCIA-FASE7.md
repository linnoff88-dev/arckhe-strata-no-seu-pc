# Conferência da fase 7

Somente arquivos, script orientativo e navegador local. Nenhum comando Strata foi executado. As saídas abaixo usam RAM/VRAM informadas, arquitetura x86_64 e disco fixado em 70 GB para reprodução.

## (31.3, 12, 'pt')

```sh
QT_FAKE_RAM_GB=31.3 QT_FAKE_VRAM_GB=12 QT_FAKE_DISCO_GB=70 QT_FAKE_ARCH=x86_64 QT_UNIFICADA=0 QT_LANG=pt bash ferramentas/qual_tamanho.sh
```

```text
Sistema: Linux | Arquitetura: x86_64
RAM: 31.3 GB | VRAM detectada: 12 GB
VRAM informada por QT_FAKE_VRAM_GB
Soma apenas como referência: 43.3 GB | Disco livre na pasta atual: 70 GB
Leituras em base binária, exibidas como GB para comparação aproximada com a doc.
VRAM AMD/Intel não é detectada. Em outra memória compartilhada, não some duas vezes.
Faixa: 30–45,9 GB
Opções: Gyro-S; Coder
strata launch --plan --family gyro --model Gyro-S
Gyro-S: sobra conjunta de referência = 31.3 + 12 - 27.6 - 10 = 5.7 GB (não confirma a divisão RAM/VRAM).
Download — Gyro-S: 58.5 GB; fora auxiliares e preparação.
Disco acima da referência; ainda precisa de espaço extra.
strata launch --plan --family coder --model IQ1_M
Coder: sobra = 31.3 - 23 - 10 = -1.7 GB.
não cabe no modo normal; só modo pouca RAM
Download — Coder: 58.6 GB; fora auxiliares e preparação.
Disco acima da referência; ainda precisa de espaço extra.
Coder: estimativa do kit (29,6 + ~29 GB).
Condição: GPU compatível de pelo menos 12 GB; Coder usa pouca RAM. A soma não escolhe a faixa.
Estimativas com reserva de 10 GB; contexto e buffers podem exigir mais. Não é memória livre medida nem garantia de que cabe.
Somente leitura local. Consulte TABELA.md; nenhum comando Strata foi executado.
```

## (62.5, 16, 'pt')

```sh
QT_FAKE_RAM_GB=62.5 QT_FAKE_VRAM_GB=16 QT_FAKE_DISCO_GB=70 QT_FAKE_ARCH=x86_64 QT_UNIFICADA=0 QT_LANG=pt bash ferramentas/qual_tamanho.sh
```

```text
Sistema: Linux | Arquitetura: x86_64
RAM: 62.5 GB | VRAM detectada: 16 GB
VRAM informada por QT_FAKE_VRAM_GB
Soma apenas como referência: 78.5 GB | Disco livre na pasta atual: 70 GB
Leituras em base binária, exibidas como GB para comparação aproximada com a doc.
VRAM AMD/Intel não é detectada. Em outra memória compartilhada, não some duas vezes.
Faixa: 62–93,9 GB
Opções: Q2_0; IQ2_XS; IQ3_XXS; IQ3_S
strata launch --plan --family qwen --model Q2_0
Q2_0: sobra = 62.5 - 34 - 10 = 18.5 GB.
Download — Q2_0: 66–76 GB; fora auxiliares e preparação.
AVISO: disco abaixo da referência superior; pode faltar espaço.
strata launch --plan --family qwen --model IQ2_XS
IQ2_XS: sobra = 62.5 - 35.5 - 10 = 17 GB.
Download — IQ2_XS: 66–76 GB; fora auxiliares e preparação.
AVISO: disco abaixo da referência superior; pode faltar espaço.
strata launch --plan --family qwen --model IQ3_XXS
IQ3_XXS: sobra = 62.5 - 43 - 10 = 9.5 GB.
Download — IQ3_XXS: 66–76 GB; fora auxiliares e preparação.
AVISO: disco abaixo da referência superior; pode faltar espaço.
strata launch --plan --family qwen --model IQ3_S
IQ3_S: sobra = 62.5 - 50 - 10 = 2.5 GB.
cabe apertado: prefira o menor, ou feche programas
Download — IQ3_S: 84 GB; fora auxiliares e preparação.
AVISO: disco abaixo da referência superior; pode faltar espaço.
84 GB: referência do DGX Spark; confirme o download do pacote da sua plataforma com --plan após instalar.
Estimativas com reserva de 10 GB; contexto e buffers podem exigir mais. Não é memória livre medida nem garantia de que cabe.
Somente leitura local. Consulte TABELA.md; nenhum comando Strata foi executado.
```

## (62.5, 16, 'en')

```sh
QT_FAKE_RAM_GB=62.5 QT_FAKE_VRAM_GB=16 QT_FAKE_DISCO_GB=70 QT_FAKE_ARCH=x86_64 QT_UNIFICADA=0 QT_LANG=en bash ferramentas/qual_tamanho.sh
```

```text
System: Linux | Architecture: x86_64
RAM: 62.5 GB | Detected VRAM: 16 GB
VRAM provided by QT_FAKE_VRAM_GB
Sum for reference only: 78.5 GB | Free disk space in the current folder: 70 GB
Readings use a binary base, displayed as GB for approximate comparison with the docs.
AMD/Intel VRAM is not detected. With other shared memory, do not add it twice.
Range: 62–93.9 GB
Options: Q2_0; IQ2_XS; IQ3_XXS; IQ3_S
strata launch --plan --family qwen --model Q2_0
Q2_0: remaining memory = 62.5 - 34 - 10 = 18.5 GB.
Download — Q2_0: 66–76 GB; excludes auxiliary files and preparation.
WARNING: disk space is below the upper reference; there may not be enough space.
strata launch --plan --family qwen --model IQ2_XS
IQ2_XS: remaining memory = 62.5 - 35.5 - 10 = 17 GB.
Download — IQ2_XS: 66–76 GB; excludes auxiliary files and preparation.
WARNING: disk space is below the upper reference; there may not be enough space.
strata launch --plan --family qwen --model IQ3_XXS
IQ3_XXS: remaining memory = 62.5 - 43 - 10 = 9.5 GB.
Download — IQ3_XXS: 66–76 GB; excludes auxiliary files and preparation.
WARNING: disk space is below the upper reference; there may not be enough space.
strata launch --plan --family qwen --model IQ3_S
IQ3_S: remaining memory = 62.5 - 50 - 10 = 2.5 GB.
fits tightly: prefer the smaller one, or close programs
Download — IQ3_S: 84 GB; excludes auxiliary files and preparation.
WARNING: disk space is below the upper reference; there may not be enough space.
84 GB: DGX Spark reference; confirm the download for your platform's package with --plan after installing.
Estimates reserve 10 GB; context and buffers may require more. This is not measured free memory or a guarantee that it fits.
Local read only. See TABELA.en.md; no Strata command was run.
```

## (94, 16, 'es')

```sh
QT_FAKE_RAM_GB=94 QT_FAKE_VRAM_GB=16 QT_FAKE_DISCO_GB=70 QT_FAKE_ARCH=x86_64 QT_UNIFICADA=0 QT_LANG=es bash ferramentas/qual_tamanho.sh
```

```text
Sistema: Linux | Arquitectura: x86_64
RAM: 94 GB | VRAM detectada: 16 GB
VRAM indicada por QT_FAKE_VRAM_GB
Suma solo como referencia: 110.0 GB | Espacio libre en disco en la carpeta actual: 70 GB
Lecturas en base binaria, mostradas como GB para compararlas de forma aproximada con la documentación.
No se detecta la VRAM de AMD/Intel. Si tienes otra memoria compartida, no la sumes dos veces.
Rango: 94–125,9 GB
Opciones: Q2_0; IQ2_XS; IQ3_XXS; IQ3_S; UD-IQ4_XS; UD-Q4_K_XL
strata launch --plan --family qwen --model Q2_0
Q2_0: memoria restante = 94 - 34 - 10 = 50 GB.
Descarga — Q2_0: 66–76 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
strata launch --plan --family qwen --model IQ2_XS
IQ2_XS: memoria restante = 94 - 35.5 - 10 = 48.5 GB.
Descarga — IQ2_XS: 66–76 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
strata launch --plan --family qwen --model IQ3_XXS
IQ3_XXS: memoria restante = 94 - 43 - 10 = 41 GB.
Descarga — IQ3_XXS: 66–76 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
strata launch --plan --family qwen --model IQ3_S
IQ3_S: memoria restante = 94 - 50 - 10 = 34 GB.
Descarga — IQ3_S: 84 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
84 GB: referencia del DGX Spark; después de instalar, confirma la descarga del paquete de tu plataforma con --plan.
strata launch --plan --family unsloth --model UD-IQ4_XS
UD-IQ4_XS: memoria restante = 94 - 72 - 10 = 12 GB.
Descarga — UD-IQ4_XS: 94 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
strata launch --plan --family unsloth --model UD-Q4_K_XL
UD-Q4_K_XL: memoria restante = 94 - 88 - 10 = -4 GB.
no cabe en el modo normal; solo en modo de poca RAM
Descarga — UD-Q4_K_XL: 111 GB; no incluye archivos auxiliares ni preparación.
AVISO: el espacio en disco está por debajo de la referencia superior; puede que falte espacio.
Las estimaciones reservan 10 GB; el contexto y los búferes pueden necesitar más. No es una medición de memoria libre ni una garantía de que quepa.
Solo lectura local. Consulta TABELA.es.md; no se ejecutó ningún comando de Strata.
```

## Conferências estáticas e de comportamento

72 combinações de limites/idiomas/plataformas: uma faixa em cada caso e --plan de cada opção. Tabelas HTML/Markdown conferidas contra faixas.tsv. Aviso negativo exclusivo. Opções do Codex, revelação de chave, comandos por família, termos e links presentes nos três idiomas.

## HTML a 390 px

Navegador Chromium local, fontes externas bloqueadas para manter a conferência sem rede.

```json
[
  {
    "lang": "PT",
    "innerWidth": 390,
    "scrollWidth": 390,
    "bodyScrollWidth": 390
  },
  {
    "lang": "en/",
    "innerWidth": 390,
    "scrollWidth": 390,
    "bodyScrollWidth": 390
  },
  {
    "lang": "es/",
    "innerWidth": 390,
    "scrollWidth": 390,
    "bodyScrollWidth": 390
  }
]
```

## Contagens solicitadas

```text
guia/index.html:0
guia/en/index.html:0
guia/es/index.html:0
```

```text
guia/en/index.html:0
guia/es/index.html:0
```

`grep` retornou 1 porque não houve ocorrências. `bash -n ferramentas/qual_tamanho.sh` e `git diff --check` retornaram 0, sem saída. EN/ES do script exigem Python 3, agora informado nas páginas e READMEs.
