# Instalar en Linux o Mac

- [ ] [Antes, mira el tamaño en la tabla (paso 2).](../TABELA.es.md)

- [ ] Linux: comprueba que la tarjeta y el paquete sean compatibles; Intel Arc usa la ruta del terminal y tiene requisitos de preparación propios.
- [ ] Mac: Apple Silicon, macOS 15 o posterior. El paquete para Mac no es compatible con Mac Intel.
- [ ] Lee [antes de instalar](antes-de-instalar.es.md). En Mac, cuenta la memoria unificada una sola vez.
- [ ] Para la aplicación, usa la [versión oficial](https://github.com/Niko1221/Strata/releases/latest). Linux x86-64: `Strata-0.2.13-linux-x86_64.AppImage`; Mac: `Strata-0.2.13-macos-arm64.dmg`.
- [ ] Linux: haz ejecutable el AppImage; si no hay FUSE, la documentación ofrece `--appimage-extract-and-run`. Mac: arrastra la aplicación a Applications y ábrela.
- [ ] Si prefieres el terminal (ventana para escribir comandos), usa:

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] Si no se encuentra `strata`, usa la ruta que muestra el instalador, normalmente `~/.local/bin/strata`, o añade la carpeta a PATH.
- [ ] Elige modelo, contexto, carpeta y acceso local. Observa el progreso de la primera preparación.
- [ ] En Mac, si aparece una advertencia, comprueba el origen oficial, Apple Silicon y macOS antes de seguir las indicaciones de `TROUBLESHOOTING.md`. No elimines las protecciones de archivos de origen desconocido.
- [ ] Para compartir o conectar herramientas, lee [CONECTAR.es.md](../CONECTAR.es.md).

Para DGX Spark/Linux ARM64, sigue [su propia lista de verificación](dgx-spark.es.md). Nosotros no ejecutamos ninguno de estos comandos.

Fuentes: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md`, `DGX_SPARK_LINUX.md`.

Después de instalar Strata y abrir una terminal nueva, comprueba el plan antes de descargar el modelo. Elige solamente el comando de la opción compatible de la tabla; --plan muestra el plan sin iniciar el modelo. No cambies solo el tamaño y mantengas la familia qwen: Coder, Gyro, Unsloth y NVFP4 tienen familias propias. Para IQ3_S en x86, confirma aquí la descarga para tu plataforma. [TABELA.es.md](../TABELA.es.md).
