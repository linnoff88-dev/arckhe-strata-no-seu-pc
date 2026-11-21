# Qué tamaño cabe en mi PC

Elige según la RAM detectada. La suma de RAM + VRAM es solo una referencia; la memoria unificada se cuenta una sola vez. Los rangos son contiguos: 30–45,9 significa 30 ≤ RAM < 46, e incluye lecturas como 45,99. Son agrupaciones conservadoras del kit, no nuevos requisitos oficiales.

Q2_0, IQ2_XS, IQ3_S, UD-Q4_K_XL, NVFP4 son niveles de compresión del mismo modelo: menos bits = menos memoria y un poco menos de calidad. ISTA-DASLab y Unsloth son grupos que preparan estos paquetes.

bpw significa bits por peso (cuántos bits guardan cada parámetro del modelo). mmap asigna un archivo a la memoria y te permite leer partes según lo necesites. WSL es Linux dentro de Windows. CLI es la interfaz de línea de comandos, que se usa en la terminal. JSON es un formato de datos con nombres y valores. Endpoint es una dirección del servidor que recibe un tipo de solicitud.

| Memoria | RAM detectada | Opciones y par --family / --model |
|---|---|---|
| RAM + tarjeta gráfica dedicada | <30 GB | Sin recomendación automática segura |
| RAM + tarjeta gráfica dedicada | 30–45,9 GB | Gyro-S (`--family gyro --model Gyro-S`); Coder (`--family coder --model IQ1_M`) |
| RAM + tarjeta gráfica dedicada | 46–61,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`) |
| RAM + tarjeta gráfica dedicada | 62–93,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`) |
| RAM + tarjeta gráfica dedicada | 94–125,9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`) |
| RAM + tarjeta gráfica dedicada | ≥126 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`); UD-Q5_K_XL (`--family unsloth --model UD-Q5_K_XL`); UD-Q6_K_XL (`--family unsloth --model UD-Q6_K_XL`) |
| Unificada: Mac / DGX Spark | <30 GB | Sin recomendación automática segura |
| Unificada: Mac / DGX Spark | 30–45,9 GB | Sin recomendación automática segura |
| Unificada: Mac / DGX Spark | 46–61,9 GB | IQ2_XS (Mac) (`--family qwen --model IQ2_XS`) |
| Unificada: Mac / DGX Spark | 62–93,9 GB | IQ3_XXS (Mac) (`--family qwen --model IQ3_XXS`); IQ3_S (Mac) (`--family qwen --model IQ3_S`) |
| Unificada: Mac / DGX Spark | 94–125,9 GB | IQ3_S (Mac o DGX Spark de 128 GB) (`--family qwen --model IQ3_S`); NVFP4 (solo DGX Spark de 128 GB) (`--family nvfp4 --model NVFP4`) |
| Unificada: Mac / DGX Spark | ≥126 GB | IQ3_S (Mac o DGX Spark de 128 GB) (`--family qwen --model IQ3_S`); NVFP4 (solo DGX Spark de 128 GB) (`--family nvfp4 --model NVFP4`) |

En el rango de 62–93,9 GB de RAM con una tarjeta gráfica separada, los cuatro paquetes son opciones: Q2_0 es el más rápido. Con 62,5 GB leídos, quedan Q2_0: 18,5 GB; IQ2_XS: 17 GB; IQ3_XXS: 9,5 GB; IQ3_S: 2,5 GB. El cálculo reserva 10 GB para el sistema. La documentación dice que con 64 GB de RAM caben todos, IQ3_S con muy pocas cosas abiertas.

Memoria restante estimada: RAM leída − expertos − 10 GB. Expertos: Q2_0 34; IQ2_XS 35,5; IQ3_XXS 43; IQ3_S 50; Coder 23; Unsloth UD-IQ4_XS 72, UD-Q4_K_XL 88, UD-Q5_K_XL 108 y UD-Q6_K_XL 118 GB. Memoria restante de 0 a menos de 3 GB: “cabe justo”; negativa: “no cabe en el modo normal; solo en modo de poca RAM”. En el rango de 30–45,9, necesitas una GPU compatible de al menos 12 GB; Coder usa poca RAM y el SSD, con pérdida de velocidad. Para Gyro-S, la documentación solo indica la memoria conjunta: memoria restante de referencia = RAM + VRAM − 27,6 − 10 GB; esto no confirma cómo se divide entre las dos memorias.

Memoria unificada: los mismos rangos, sin sumar VRAM. Mac requiere Apple Silicon y macOS 15+; comprueba el paquete en el plan. Las opciones Spark solo se aplican al DGX Spark documentado de 128 GB nominales, aunque el sistema lea 125 GB. No se ha confirmado para otros sistemas ARM. En Spark, NVFP4 usa un archivo de expertos de 68 GB con mmap: RAM − 68 − 10 es solo una referencia, porque el contexto, la caché y la tabla también compiten por la memoria. Q2_0 y Gyro no funcionan en Spark.

Disco: Q2_0, IQ2_XS e IQ3_XXS tienen un rango de descarga conjunto de 66–76 GB; el script compara con 76 GB. IQ3_S: 84 GB es una referencia para DGX Spark, no una cifra universal para x86; confirma con --plan después de instalar. Gyro-S: 58,5 GB. Coder: ~58,6 GB, estimación del kit (29,6 + ~29). Unsloth: 94/111/158/169 GB en el orden de la lista; NVFP4: 128 GB. Reserva espacio adicional para archivos auxiliares y preparación. IQ3_S requiere tener pocas cosas abiertas; Q8_0 no está en la lista automática: ~136 GB solo para expertos.

Después de instalar Strata y abrir una terminal nueva, comprueba el plan antes de descargar el modelo. Elige solamente el comando de la opción compatible de la tabla; --plan muestra el plan sin iniciar el modelo. No cambies solo el tamaño y mantengas la familia qwen: Coder, Gyro, Unsloth y NVFP4 tienen familias propias. Para IQ3_S en x86, confirma aquí la descarga para tu plataforma.

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
