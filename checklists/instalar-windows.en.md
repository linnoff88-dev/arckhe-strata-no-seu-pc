# Install on Windows

- [ ] [First, check the size in the table (step 2).](../TABELA.en.md)

- [ ] Check for Windows 10/11 x86-64 and a compatible GPU. Windows ARM is not a supported path in these docs.
- [ ] Read [before installing](antes-de-instalar.en.md) and choose a size.
- [ ] To chat, open the [official release](https://github.com/Niko1221/Strata/releases/latest) and download `Strata-0.2.13-windows-x64-setup.exe`, according to the copy of the docs. Do not choose a `strata-engine-…` file as the installer.
- [ ] The app installs for your user, without administrator privileges. On first launch, download the indicated engine; then choose a model and folder.
- [ ] If you prefer the terminal, open PowerShell (the window where you type commands) and use the official command below.

```powershell
irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

- [ ] Open a **new** PowerShell window and start:

```powershell
strata launch
```

- [ ] Choose a model, context, folder, and access setting. Follow the preparation; there is no universal first-start time.
- [ ] For programming tools, follow [CONECTAR.en.md](../CONECTAR.en.md).
- [ ] If `strata` does not appear, check the new window and `strata --version`. If the driver is old, follow the package indicated in the docs.

The size script is Bash. Do not paste the `bash` command into PowerShell assuming Bash is already available; if Bash is unavailable, use the computer’s specifications to identify RAM and graphics memory; check free space on the destination disk and compare it with the table. Without this information, postpone downloading the model.
None of these commands was run by us.

Sources: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md`, and `SAFETY.md`.

After installing Strata and opening a new terminal, check the plan before downloading the model. Choose only the command for the compatible option in the table; --plan shows the plan without starting the model. Do not change only the size while keeping the qwen family: Coder, Gyro, Unsloth, and NVFP4 have their own families. For IQ3_S on x86, confirm the download for your platform here. [TABELA.en.md](../TABELA.en.md).
