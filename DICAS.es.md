# 20 consejos para usar Strata en tu PC

Documentación organizada; nosotros no instalamos ni ejecutamos Strata.

## Antes de instalar

### 1. Suma sin contar dos veces

Suma la RAM (memoria del ordenador) y la VRAM (memoria de la tarjeta gráfica). En Mac y otros sistemas con memoria unificada, cuéntala una sola vez. La suma solo sirve como primera orientación; reserva espacio para el sistema.

(Origen: `docs-oficiais/MODELS.md`).

### 2. Comprueba el espacio libre en disco

La descarga no es uso de RAM: los paquetes originales más pequeños descargan 66–76 GB, además de los archivos auxiliares. Elige una carpeta con espacio para la descarga y la preparación.

(Origen: `docs-oficiais/MODELS.md`, `docs-oficiais/INSTALL.md`).

### 3. Prefiere un SSD y comprueba si es NVMe

Un SSD es almacenamiento rápido; NVMe es una interfaz para SSD. Si faltan expertos en la RAM, buscarlos en el disco hace que la respuesta sea mucho más lenta; para DeepSeek, la documentación pide NVMe.

(Origen: `docs-oficiais/MODELS.md`).

## Elegir el tamaño

### 4. Elige el mayor que quepa con holgura

Usa TABELA.es.md y comprueba la RAM por separado de la VRAM. El contexto y las aplicaciones abiertas también ocupan memoria; el archivo más grande disponible puede ser una mala elección para tu PC.

(Origen: `docs-oficiais/MODELS.md`).

### 5. Coder es para programar

Coder IQ1_M requiere alrededor de 32 GB de RAM con una GPU adecuada. Es más débil fuera de la programación y en idiomas distintos de los destacados en la documentación; para uso general, prefiere todos los expertos cuando quepan.

(Origen: `docs-oficiais/MODELS.md`).

### 6. Con poca RAM, el trabajo pasa al SSD

Con 32 GB de RAM y una tarjeta de 24 GB, la documentación describe Q2_0, IQ2_XS y Coder en el modo de poca RAM. Con una tarjeta de 12–16 GB, describe Coder; strata launch no tiene la opción --low-ram.

(Origen: `docs-oficiais/MODELS.md`).

### 7. ISTA-DASLab primero; Unsloth después

La documentación recomienda empezar con un paquete ISTA-DASLab compatible que quepa. Unsloth conserva más bits y requiere más RAM: UD-IQ4_XS descarga 94 GB y necesita ~72 GB de RAM para todos los expertos.

(Origen: `docs-oficiais/MODELS.md`).

### 8. Trampa: «cualquier tarjeta de 8 GB puede ejecutar el de 94 GB»

La tarjeta por sí sola no lo determina. Los 94 GB corresponden a la descarga de UD-IQ4_XS; la documentación pide ~72 GB de RAM para mantener sus expertos, y menos RAM puede trasladar trabajo al SSD.

(Origen: `docs-oficiais/MODELS.md`).

### 9. Trampa: «más rápido = tarjeta más rápida»

La documentación dice que, con este método, más VRAM importa más que una GPU más rápida. La tarjeta almacena los expertos más usados; tener más de ellos allí reduce el trabajo del procesador.

(Origen: `docs-oficiais/HOW_IT_WORKS.md`).

## Instalar

### 10. Trampa: «es solo un script y listo»

Elige la aplicación o el terminal y, después, el modelo y el tamaño. El terminal usa install.sh o install.ps1 y strata launch; descargar el instalador no significa que el modelo esté listo.

(Origen: `docs-oficiais/INSTALL.md`).

### 11. Elige la ruta para tu sistema

Hay una aplicación para Windows, Linux x86-64 y Mac Apple Silicon. Mac requiere macOS 15 o posterior; Intel Arc usa la ruta del terminal en Linux, y el paquete para Mac no es compatible con Mac Intel.

(Origen: `docs-oficiais/INSTALL.md`).

### 12. DGX Spark usa el terminal

No hay aplicación para Linux ARM64. El proyecto documenta IQ3_S, NVFP4 y DeepSeek 2.00 bpw en Spark; Q2_0 y Gyro tienen kernels solo para x86 y no funcionan allí.

(Origen: `docs-oficiais/DGX_SPARK_LINUX.md`).

### 13. El motor no sustituye al controlador

Los paquetes CUDA 13 requieren el controlador NVIDIA 580 o posterior; en Spark, 580.65 o posterior. Las tarjetas NVIDIA antiguas usan la ruta CUDA 12; consulta la documentación antes de elegir el paquete.

(Origen: `docs-oficiais/INSTALL.md`, `docs-oficiais/OLDER_GPUS.md`, `docs-oficiais/DGX_SPARK_LINUX.md`).

## Conectar herramientas

### 14. Pide la configuración lista para usar

strata connect enumera Claude Code, Codex CLI, OpenCode y otros. La dirección local predeterminada es http://127.0.0.1:8080; usa la dirección que Strata muestre para tu servidor.

(Origen: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 15. Guarda con copia de seguridad y comprueba

strata connect opencode --write pregunta antes de escribir y guarda una copia de seguridad de lo que sustituye. strata connect opencode --check envía un prompt y una llamada a una herramienta; puedes ejecutar esta comprobación.

(Origen: `docs-oficiais/TERMINAL_LAUNCH.md`).

### 16. Conserva la clave al acceder desde fuera del ordenador

--access acepta local, lan, tailscale o cloudflare. Strata genera una clave para un acceso más amplio; Tailscale debe estar conectado y Cloudflare requiere cloudflared. No muestres la clave en capturas de pantalla.

(Origen: `docs-oficiais/TERMINAL_LAUNCH.md`, `docs-oficiais/SAFETY.md`).

## Privacidad

### 17. Sin telemetría no significa que no haya ninguna conexión

La documentación dice que no se envían datos de uso, analíticas ni informes de errores. Las instalaciones y actualizaciones acceden a la red; las búsquedas, páginas, túneles, servicios externos y servidores de herramientas también pueden acceder a ella.

(Origen: `docs-oficiais/SAFETY.md`).

### 18. Las herramientas tienen sus propias reglas

Las conversaciones locales permanecen en el PC, pero un modelo externo recibe la conversación cuando lo eliges. Claude Code y Codex son programas independientes: Strata no controla lo que envían.

(Origen: `docs-oficiais/SAFETY.md`).

## Cuando algo falla

### 19. Resuelve rutas, descargas y controladores

Comando no encontrado: abre una nueva ventana de PowerShell o usa la ruta del instalador en Linux/Mac. Descarga interrumpida: repite la acción y comprueba el espacio; se reutilizan los pasos completos. Controlador antiguo: actualízalo según el paquete y reinicia si hace falta.

(Origen: `docs-oficiais/TROUBLESHOOTING.md`).

### 20. Resuelve el inicio lento y el puerto ocupado

Primer inicio lento: consulta el registro, cierra programas y reduce el modelo/contexto si falta memoria. Puerto ocupado: comprueba strata launch --status; --restart interrumpe las respuestas actuales. No cierres un programa ajeno por estar usando el puerto.

(Origen: `docs-oficiais/TROUBLESHOOTING.md`).

Los consejos 19–20 reúnen cinco problemas frecuentes para consulta: comando ausente, descarga interrumpida, controlador antiguo, inicio lento y puerto ocupado. La documentación no publica una clasificación por frecuencia.
