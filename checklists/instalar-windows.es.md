# Instalar en Windows

- [ ] [Antes, mira el tamaño en la tabla (paso 2).](../TABELA.es.md)

- [ ] Comprueba que tienes Windows 10/11 x86-64 y una GPU compatible. Windows ARM no es una ruta compatible según esta documentación.
- [ ] Lee [antes de instalar](antes-de-instalar.es.md) y elige un tamaño.
- [ ] Para conversar, abre la [versión oficial](https://github.com/Niko1221/Strata/releases/latest) y descarga `Strata-0.2.13-windows-x64-setup.exe`, según la copia de la documentación. No elijas un archivo `strata-engine-…` como instalador.
- [ ] La aplicación se instala para tu usuario, sin privilegios de administrador. En el primer inicio, descarga el motor indicado; después elige un modelo y una carpeta.
- [ ] Si prefieres el terminal, abre PowerShell (la ventana donde escribes comandos) y usa el comando oficial de abajo.

```powershell
irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

- [ ] Abre una ventana **nueva** de PowerShell e inicia:

```powershell
strata launch
```

- [ ] Elige modelo, contexto, carpeta y acceso. Sigue la preparación; no hay un tiempo universal para el primer inicio.
- [ ] Para herramientas de programación, sigue [CONECTAR.es.md](../CONECTAR.es.md).
- [ ] Si no aparece `strata`, comprueba la nueva ventana y `strata --version`. Si el controlador es antiguo, sigue el paquete indicado en la documentación.

El script de tamaño es Bash. No pegues el comando `bash` en PowerShell suponiendo que Bash ya está disponible; si no tienes Bash, usa las especificaciones del ordenador para identificar la RAM y la memoria de la tarjeta gráfica; comprueba el espacio libre en el disco de destino y compáralo con la tabla. Sin esos datos, aplaza la descarga del modelo.
Nosotros no ejecutamos ninguno de estos comandos.

Fuentes: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md` y `SAFETY.md`.

Después de instalar Strata y abrir una terminal nueva, comprueba el plan antes de descargar el modelo. Elige solamente el comando de la opción compatible de la tabla; --plan muestra el plan sin iniciar el modelo. No cambies solo el tamaño y mantengas la familia qwen: Coder, Gyro, Unsloth y NVFP4 tienen familias propias. Para IQ3_S en x86, confirma aquí la descarga para tu plataforma. [TABELA.es.md](../TABELA.es.md).
