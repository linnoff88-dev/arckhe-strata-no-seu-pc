# DGX Spark: terminal no Linux ARM64

## O que a doc confirma

- [ ] É um DGX Spark: os resultados vêm de uma unidade com Ubuntu 24.04, driver 580.173 e CUDA 13.0. Não estenda a confirmação a qualquer máquina ARM.
- [ ] Requisitos do pacote: glibc 2.39 ou mais nova (Ubuntu 24.04 / DGX OS 7), driver NVIDIA 580.65 ou mais novo.
- [ ] Conte os 128 GB unificados uma vez. `nvidia-smi` pode não informar memória da GB10.
- [ ] Reserve disco: IQ3_S baixa 84 GB; DeepSeek V4.1-Flash 2.00 bpw baixa 257 GB. Confira também preparação e auxiliares.

**Roda, segundo o projeto:** Qwen3.8-Flash-Next IQ3_S, NVFP4 GPTQ (contexto 64K), DeepSeek V4.1-Flash 2.00 bpw (conversa curta), terminal e pacotes assinados do motor.

**Não existe para ARM nesta doc:** app de desktop, motores HIP, SYCL e só CPU. Q2_0 e Gyro não rodam: seus kernels de CPU são só x86.
Leitura de imagens foi compilada, mas não conferida no Spark pelo projeto. Contextos acima de 128K, mais de oito conversas simultâneas e uso prolongado não foram verificados na página.

## Comandos oficiais

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] Use o terminal; não procure AppImage ARM.
- [ ] O instalador usa `~/.local/share/strata`, sem administrador, e verifica o feed assinado.
- [ ] O lançamento busca o pacote `linux-aarch64`, mostra as necessidades e baixa o modelo escolhido.
- [ ] Escolha IQ3_S, NVFP4 ou o DeepSeek documentado; confira a pasta de download.
- [ ] Use as configurações automáticas do Spark antes de alterar ajustes avançados.

O projeto mede cerca de 45–48 tokens/s no IQ3_S. Não é resultado nosso nem promessa para outro ARM.
Este kit documenta a rota por pacote pronto; não exige compilar nem copiar o código do Strata.

Fonte: `docs-oficiais/DGX_SPARK_LINUX.md`.
