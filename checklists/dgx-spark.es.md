# DGX Spark: terminal en Linux ARM64

## Lo que confirma la documentación

- [ ] Es un DGX Spark: los resultados proceden de una unidad con Ubuntu 24.04, controlador 580.173 y CUDA 13.0. No extiendas esta confirmación a cualquier máquina ARM.
- [ ] Requisitos del paquete: glibc 2.39 o posterior (Ubuntu 24.04 / DGX OS 7), controlador NVIDIA 580.65 o posterior.
- [ ] Cuenta los 128 GB de memoria unificada una sola vez. Es posible que `nvidia-smi` no informe de la memoria de GB10.
- [ ] Reserva espacio en disco: IQ3_S descarga 84 GB; DeepSeek V4.1-Flash 2.00 bpw descarga 257 GB. Ten en cuenta también la preparación y los archivos auxiliares.

**Funciona, según el proyecto:** Qwen3.8-Flash-Next IQ3_S, NVFP4 GPTQ (contexto de 64K), DeepSeek V4.1-Flash 2.00 bpw (conversaciones breves), terminal y paquetes firmados del motor.

**No está disponible para ARM en esta documentación:** aplicación de escritorio, motores HIP y SYCL, y solo CPU. Q2_0 y Gyro no funcionan: sus kernels de CPU son solo para x86.
La lectura de imágenes se compiló, pero el proyecto no la comprobó en Spark. La página no verificó contextos superiores a 128K, más de ocho conversaciones simultáneas ni el uso prolongado.

## Comandos oficiales

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] Usa el terminal; no busques un AppImage para ARM.
- [ ] El instalador usa `~/.local/share/strata`, sin privilegios de administrador, y verifica el feed firmado.
- [ ] El lanzamiento descarga el paquete `linux-aarch64`, muestra los requisitos y descarga el modelo elegido.
- [ ] Elige IQ3_S, NVFP4 o el DeepSeek documentado; comprueba la carpeta de descarga.
- [ ] Usa los ajustes automáticos de Spark antes de cambiar las opciones avanzadas.

El proyecto mide alrededor de 45–48 tokens/s con IQ3_S. No es un resultado nuestro ni una promesa para otra máquina ARM.
Este kit documenta la ruta con paquetes listos para usar; no exige compilar ni copiar el código de Strata.

Fuente: `docs-oficiais/DGX_SPARK_LINUX.md`.
