# Antes de instalar

- [ ] Comprueba el sistema, la arquitectura y la tarjeta gráfica en la documentación de instalación. Tener memoria suficiente no garantiza que el hardware sea compatible.
- [ ] Suma RAM + VRAM; cuenta la memoria unificada una sola vez. Lee [TABELA.es.md](../TABELA.es.md).
- [ ] Comprueba la RAM por separado y deja espacio para el sistema, el contexto y las aplicaciones.
- [ ] Elige la carpeta del modelo en un SSD; comprueba el espacio libre en ese disco. Para DeepSeek, la documentación pide NVMe.
- [ ] Comprueba el tamaño de la descarga y los archivos auxiliares. No confundas el tamaño en memoria con el espacio en disco.
- [ ] Ten conexión a internet para descargar el programa, el motor y el modelo.
- [ ] Comprueba el controlador que requiere el paquete. CUDA 13 requiere NVIDIA 580 o posterior; Spark requiere 580.65 o posterior.
- [ ] Elige la aplicación para conversar o el terminal para configurar herramientas.
- [ ] Empieza con acceso local; comparte solo con una clave.

Opcional, en Bash si ya está disponible, desde la carpeta del kit: `bash ferramentas/qual_tamanho.sh`. Solo lee información e imprime sugerencias; no instala ni confirma la compatibilidad.

Fuentes: `docs-oficiais/INSTALL.md`, `MODELS.md`, `DGX_SPARK_LINUX.md`, `SAFETY.md` (todos en `docs-oficiais/`).
