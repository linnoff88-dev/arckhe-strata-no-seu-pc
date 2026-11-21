# Install on Linux or Mac

- [ ] [First, check the size in the table (step 2).](../TABELA.en.md)

- [ ] Linux: check for a compatible card and package; Intel Arc uses the terminal route and has its own preparation requirements.
- [ ] Mac: Apple Silicon, macOS 15 or newer. The Mac package does not support Intel Macs.
- [ ] Read [before installing](antes-de-instalar.en.md). On Mac, count unified memory once.
- [ ] For the app, use the [official release](https://github.com/Niko1221/Strata/releases/latest). Linux x86-64: `Strata-0.2.13-linux-x86_64.AppImage`; Mac: `Strata-0.2.13-macos-arm64.dmg`.
- [ ] Linux: make the AppImage executable; if FUSE is unavailable, the docs offer `--appimage-extract-and-run`. Mac: drag the app to Applications and open it.
- [ ] If you prefer the terminal (a window for typing commands), use:

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] If `strata` is not found, use the path printed by the installer, usually `~/.local/bin/strata`, or add the folder to PATH.
- [ ] Choose a model, context, folder, and local access. Watch the first preparation progress.
- [ ] On Mac, if a warning appears, check the official source, Apple Silicon, and macOS before following the guidance in `TROUBLESHOOTING.md`. Do not remove protections from files of unknown origin.
- [ ] To share or connect tools, read [CONECTAR.en.md](../CONECTAR.en.md).

For DGX Spark/Linux ARM64, follow [its own checklist](dgx-spark.en.md). None of these commands was run by us.

Sources: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md`, `DGX_SPARK_LINUX.md`.

After installing Strata and opening a new terminal, check the plan before downloading the model. Choose only the command for the compatible option in the table; --plan shows the plan without starting the model. Do not change only the size while keeping the qwen family: Coder, Gyro, Unsloth, and NVFP4 have their own families. For IQ3_S on x86, confirm the download for your platform here. [TABELA.en.md](../TABELA.en.md).
