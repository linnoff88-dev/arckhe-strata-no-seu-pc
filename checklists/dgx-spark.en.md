# DGX Spark: terminal on Linux ARM64

## What the docs confirm

- [ ] This is a DGX Spark: the results are from a unit with Ubuntu 24.04, driver 580.173, and CUDA 13.0. Do not extend this confirmation to every ARM machine.
- [ ] Package requirements: glibc 2.39 or newer (Ubuntu 24.04 / DGX OS 7), NVIDIA driver 580.65 or newer.
- [ ] Count the 128 GB of unified memory once. `nvidia-smi` may not report GB10 memory.
- [ ] Reserve disk space: IQ3_S downloads 84 GB; DeepSeek V4.1-Flash 2.00 bpw downloads 257 GB. Also account for preparation and auxiliary files.

**Runs, according to the project:** Qwen3.8-Flash-Next IQ3_S, NVFP4 GPTQ (64K context), DeepSeek V4.1-Flash 2.00 bpw (short conversations), terminal, and signed engine packages.

**Not available for ARM in these docs:** desktop app, HIP and SYCL engines, and CPU-only mode. Q2_0 and Gyro do not run: their CPU kernels are x86-only.
Image reading was compiled, but the project did not verify it on Spark. Contexts above 128K, more than eight simultaneous conversations, and prolonged use were not verified on the page.

## Official commands

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] Use the terminal; do not look for an ARM AppImage.
- [ ] The installer uses `~/.local/share/strata`, without administrator privileges, and verifies the signed feed.
- [ ] Launch fetches the `linux-aarch64` package, shows the requirements, and downloads the selected model.
- [ ] Choose IQ3_S, NVFP4, or the documented DeepSeek; check the download folder.
- [ ] Use the Spark automatic settings before changing advanced options.

The project measures about 45–48 tokens/s on IQ3_S. This is not our result or a promise for another ARM machine.
This kit documents the ready-made package route; it does not require compiling or copying Strata’s code.

Source: `docs-oficiais/DGX_SPARK_LINUX.md`.
