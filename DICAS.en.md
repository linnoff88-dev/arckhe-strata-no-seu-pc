# 20 tips for using Strata on your PC

Organized documentation; we did not install or run Strata.

## Before installing

### 1. Add them without double-counting

Add RAM (the computer’s memory) and VRAM (the graphics card’s memory). On a Mac and other systems with unified memory, count it once. The sum is only an initial screening; leave room for the system.

(Source: `docs-oficiais/MODELS.md`).

### 2. Check free disk space

A download is not RAM usage: the smallest original packages download 66–76 GB, plus auxiliary files. Choose a folder with enough space for the download and preparation.

(Source: `docs-oficiais/MODELS.md`, `docs-oficiais/INSTALL.md`).

### 3. Prefer an SSD and check whether it is NVMe

An SSD is fast storage; NVMe is an SSD interface. If some experts do not fit in RAM, retrieving them from disk makes responses much slower; for DeepSeek, the docs require NVMe.

(Source: `docs-oficiais/MODELS.md`).

## Choosing a size

### 4. Choose the largest one that fits comfortably

Use TABELA.en.md and check RAM separately from VRAM. Context and open applications also use memory; the largest available file may be a poor choice for your PC.

(Source: `docs-oficiais/MODELS.md`).

### 5. Coder is for programming

Coder IQ1_M requires around 32 GB of RAM with a suitable GPU. It is weaker outside of code and in languages other than those highlighted in the docs; for general use, prefer all experts when they fit.

(Source: `docs-oficiais/MODELS.md`).

### 6. Low RAM shifts work to the SSD

With 32 GB of RAM and a 24 GB card, the docs describe Q2_0, IQ2_XS, and Coder in low-RAM mode. With a 12–16 GB card, they describe Coder; strata launch has no --low-ram flag.

(Source: `docs-oficiais/MODELS.md`).

### 7. ISTA-DASLab first; Unsloth afterward

The docs recommend starting with a compatible ISTA-DASLab package that fits. Unsloth stores more bits and requires more RAM: UD-IQ4_XS downloads 94 GB and needs ~72 GB of RAM for all experts.

(Source: `docs-oficiais/MODELS.md`).

### 8. Pitfall: “any 8 GB card can run the 94 GB one”

The card alone does not decide. 94 GB is the UD-IQ4_XS download size; the docs require ~72 GB of RAM to keep its experts, and less RAM may shift work to the SSD.

(Source: `docs-oficiais/MODELS.md`).

### 9. Pitfall: “faster means a faster card”

The docs say that more VRAM matters more than a faster GPU in this method. The card stores the most frequently used experts; keeping more of them there reduces the processor’s workload.

(Source: `docs-oficiais/HOW_IT_WORKS.md`).

## Installing

### 10. Pitfall: “it’s just one script and you’re done”

You choose the app or terminal, then the model and size. The terminal uses install.sh or install.ps1 and strata launch; downloading the installer does not mean the model is ready.

(Source: `docs-oficiais/INSTALL.md`).

### 11. Choose the path for your system

There is an app for Windows, Linux x86-64, and Mac Apple Silicon. Mac requires macOS 15 or newer; Intel Arc uses the terminal on Linux, and the Mac package does not support Intel Macs.

(Source: `docs-oficiais/INSTALL.md`).

### 12. DGX Spark uses the terminal

There is no app for Linux ARM64. The project documents IQ3_S, NVFP4, and DeepSeek 2.00 bpw on Spark; Q2_0 and Gyro have x86-only kernels and do not run there.

(Source: `docs-oficiais/DGX_SPARK_LINUX.md`).

### 13. The engine does not replace the driver

CUDA 13 packages require NVIDIA driver 580 or newer; on Spark, 580.65 or newer. Older NVIDIA cards use the CUDA 12 route; check the documentation before choosing the package.

(Source: `docs-oficiais/INSTALL.md`, `docs-oficiais/OLDER_GPUS.md`, `docs-oficiais/DGX_SPARK_LINUX.md`).

## Connecting tools

### 14. Ask for the ready-made configuration

strata connect lists Claude Code, Codex CLI, OpenCode, and others. The default local address is http://127.0.0.1:8080; use the address Strata shows for your server.

(Source: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 15. Write with a backup and check

strata connect opencode --write asks before writing and keeps a backup of what it replaces. strata connect opencode --check sends a prompt and a tool call; this is a check you can run.

(Source: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 16. Keep the key when accessing from outside the computer

--access accepts local, lan, tailscale, or cloudflare. Strata generates a key for broader access; Tailscale must be connected and Cloudflare requires cloudflared. Do not expose the key in screenshots.

(Source: `docs-oficiais/TERMINAL_LAUNCH.md`, `docs-oficiais/SAFETY.md`).

## Privacy

### 17. No telemetry does not mean no connections at all

The docs say there is no transmission of usage data, analytics, or error reports. Installations and updates access the network; searches, pages, tunnels, external services, and tool servers may also access it.

(Source: `docs-oficiais/SAFETY.md`).

### 18. Tools have their own rules

Local conversations stay on the PC, but an external model receives the conversation when you choose it. Claude Code and Codex are separate programs: Strata does not control what they send.

(Source: `docs-oficiais/SAFETY.md`).

## When something goes wrong

### 19. Fix paths, downloads, and drivers

Command not found: open a new PowerShell window or use the installer path on Linux/Mac. Download stopped: repeat the action and check the available space; completed steps are reused. Old driver: update according to the package and restart if needed.

(Source: `docs-oficiais/TROUBLESHOOTING.md`).

### 20. Fix slow startup and a busy port

Slow first startup: check the log, close programs, and reduce the model/context if memory is low. Busy port: check strata launch --status; --restart interrupts current responses. Do not stop another program just because it is using the port.

(Source: `docs-oficiais/TROUBLESHOOTING.md`).

Tips 19–20 bring together five common issues for reference: missing command, interrupted download, old driver, slow startup, and busy port. The docs do not publish a frequency ranking.
