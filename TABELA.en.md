# What size fits on my PC

Choose based on the detected RAM. The sum of RAM + VRAM is only a reference; unified memory is counted once. The ranges are contiguous: 30–45.9 means 30 ≤ RAM < 46, including readings such as 45.99. These are conservative kit groupings, not new official requirements.

Q2_0, IQ2_XS, IQ3_S, UD-Q4_K_XL, NVFP4 are compression levels of the same model: fewer bits = less memory and slightly lower quality. ISTA-DASLab and Unsloth are groups that prepare these packages.

bpw means bits per weight (how many bits store each model parameter). mmap maps a file into memory and lets you read parts of it as needed. WSL is Linux inside Windows. CLI is the command-line interface, used by the terminal. JSON is a data format with names and values. Endpoint is a server address that receives a type of request.

| Memory | Detected RAM | Options and --family / --model pair |
|---|---|---|
| RAM + discrete graphics card | <30 GB | No safe automatic recommendation |
| RAM + discrete graphics card | 30–45.9 GB | Gyro-S (`--family gyro --model Gyro-S`); Coder (`--family coder --model IQ1_M`) |
| RAM + discrete graphics card | 46–61.9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`) |
| RAM + discrete graphics card | 62–93.9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`) |
| RAM + discrete graphics card | 94–125.9 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`) |
| RAM + discrete graphics card | ≥126 GB | Q2_0 (`--family qwen --model Q2_0`); IQ2_XS (`--family qwen --model IQ2_XS`); IQ3_XXS (`--family qwen --model IQ3_XXS`); IQ3_S (`--family qwen --model IQ3_S`); UD-IQ4_XS (`--family unsloth --model UD-IQ4_XS`); UD-Q4_K_XL (`--family unsloth --model UD-Q4_K_XL`); UD-Q5_K_XL (`--family unsloth --model UD-Q5_K_XL`); UD-Q6_K_XL (`--family unsloth --model UD-Q6_K_XL`) |
| Unified: Mac / DGX Spark | <30 GB | No safe automatic recommendation |
| Unified: Mac / DGX Spark | 30–45.9 GB | No safe automatic recommendation |
| Unified: Mac / DGX Spark | 46–61.9 GB | IQ2_XS (Mac) (`--family qwen --model IQ2_XS`) |
| Unified: Mac / DGX Spark | 62–93.9 GB | IQ3_XXS (Mac) (`--family qwen --model IQ3_XXS`); IQ3_S (Mac) (`--family qwen --model IQ3_S`) |
| Unified: Mac / DGX Spark | 94–125.9 GB | IQ3_S (Mac or 128 GB DGX Spark) (`--family qwen --model IQ3_S`); NVFP4 (128 GB DGX Spark only) (`--family nvfp4 --model NVFP4`) |
| Unified: Mac / DGX Spark | ≥126 GB | IQ3_S (Mac or 128 GB DGX Spark) (`--family qwen --model IQ3_S`); NVFP4 (128 GB DGX Spark only) (`--family nvfp4 --model NVFP4`) |

In the range of 62–93.9 GB of RAM with a separate GPU, all four packages are options: Q2_0 is the fastest. With 62.5 GB read, the remaining amounts are Q2_0: 18.5 GB; IQ2_XS: 17 GB; IQ3_XXS: 9.5 GB; IQ3_S: 2.5 GB. The calculation reserves 10 GB for the system. The docs say that with 64 GB of RAM they all fit, IQ3_S with very few things open.

Estimated remaining memory: read RAM − experts − 10 GB. Experts: Q2_0 34; IQ2_XS 35.5; IQ3_XXS 43; IQ3_S 50; Coder 23; Unsloth UD-IQ4_XS 72, UD-Q4_K_XL 88, UD-Q5_K_XL 108 and UD-Q6_K_XL 118 GB. Remaining memory from 0 to less than 3 GB: “fits tightly”; negative: “does not fit in normal mode; low-memory mode only”. In the 30–45.9 range, a compatible GPU with at least 12 GB is required; Coder uses little RAM and the SSD, with a speed penalty. For Gyro-S, the docs give only combined memory: reference remaining memory = RAM + VRAM − 27.6 − 10 GB; this does not confirm how memory is divided between the two.

Unified memory: the same ranges, without adding VRAM. Mac requires Apple Silicon and macOS 15+; check the package in the plan. Spark options apply only to the documented DGX Spark with 128 GB nominal memory, even if the system reads 125 GB. Other ARM systems are unconfirmed. On Spark, NVFP4 uses a 68 GB expert file with mmap: RAM − 68 − 10 is only a reference, because context, cache and table also compete for memory. Q2_0 and Gyro do not run on Spark.

Disk: Q2_0, IQ2_XS and IQ3_XXS have a combined download range of 66–76 GB; the script compares against 76 GB. IQ3_S: 84 GB is a DGX Spark reference, not a universal figure for x86; confirm with --plan after installing. Gyro-S: 58,5 GB. Coder: ~58,6 GB, kit estimate (29,6 + ~29). Unsloth: 94/111/158/169 GB in the order listed; NVFP4: 128 GB. Reserve extra space for auxiliary files and preparation. IQ3_S requires few things to be open; Q8_0 is not included in the automatic list: ~136 GB for experts alone.

After installing Strata and opening a new terminal, check the plan before downloading the model. Choose only the command for the compatible option in the table; --plan shows the plan without starting the model. Do not change only the size while keeping the qwen family: Coder, Gyro, Unsloth, and NVFP4 have their own families. For IQ3_S on x86, confirm the download for your platform here.

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
