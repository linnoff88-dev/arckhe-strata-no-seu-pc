# Before installing

- [ ] Check the system, architecture, and graphics card in the installation docs. Sufficient memory does not guarantee compatible hardware.
- [ ] Add RAM + VRAM; count unified memory once. Read [TABELA.en.md](../TABELA.en.md).
- [ ] Check RAM separately and leave room for the system, context, and applications.
- [ ] Choose the model folder on an SSD; check free space on that disk. For DeepSeek, the docs require NVMe.
- [ ] Check the download size and auxiliary files. Do not confuse memory size with disk space.
- [ ] Have an internet connection to download the program, engine, and model.
- [ ] Check the driver required by the package. CUDA 13 requires NVIDIA 580 or newer; Spark requires 580.65 or newer.
- [ ] Choose the app for chatting or the terminal for configuring tools.
- [ ] Start with local access; only share with a key.

Optional, in Bash if already available, from the kit folder: `bash ferramentas/qual_tamanho.sh`. It only reads information and prints suggestions; it does not install or confirm compatibility.

Sources: `docs-oficiais/INSTALL.md`, `MODELS.md`, `DGX_SPARK_LINUX.md`, `SAFETY.md` (all in `docs-oficiais/`).
