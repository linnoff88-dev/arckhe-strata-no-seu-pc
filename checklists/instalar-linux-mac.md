# Instalar no Linux ou Mac

- [ ] [Antes, veja o tamanho na tabela (passo 2).](../TABELA.md)

- [ ] Linux: confira placa e pacote compatíveis; Intel Arc usa a rota de terminal e tem requisitos próprios de preparação.
- [ ] Mac: Apple Silicon, macOS 15 ou mais novo. O pacote Mac não suporta Mac Intel.
- [ ] Leia [antes de instalar](antes-de-instalar.md). No Mac, conte memória unificada uma vez.
- [ ] Para app, use a [release oficial](https://github.com/Niko1221/Strata/releases/latest). Linux x86-64: `Strata-0.2.13-linux-x86_64.AppImage`; Mac: `Strata-0.2.13-macos-arm64.dmg`.
- [ ] Linux: torne o AppImage executável; se não houver FUSE, a doc oferece `--appimage-extract-and-run`. Mac: arraste o app para Applications e abra.
- [ ] Se preferir terminal (janela para digitar comandos), use:

```sh
curl -fsSL --connect-timeout 15 --max-time 120 https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch
```

- [ ] Se `strata` não for encontrado, use o caminho impresso pelo instalador, normalmente `~/.local/bin/strata`, ou inclua a pasta no PATH.
- [ ] Escolha modelo, contexto, pasta e acesso local. Veja o progresso da primeira preparação.
- [ ] No Mac, se houver aviso, confira origem oficial, Apple Silicon e macOS antes de seguir a orientação de `TROUBLESHOOTING.md`. Não remova proteções de arquivo de origem desconhecida.
- [ ] Para compartilhar ou conectar ferramentas, leia [CONECTAR.md](../CONECTAR.md).

Para DGX Spark/Linux ARM64, siga [a checklist própria](dgx-spark.md). Nenhum destes comandos foi executado por nós.

Fontes: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md`, `DGX_SPARK_LINUX.md`.

Depois de instalar o Strata e abrir um novo terminal, confira o plano antes de baixar o modelo. Escolha somente o comando da opção compatível da tabela; --plan mostra o plano sem iniciar o modelo. Não troque só o tamanho mantendo a família qwen: Coder, Gyro, Unsloth e NVFP4 têm famílias próprias. Para IQ3_S em x86, confirme aqui o download da sua plataforma. [TABELA.md](../TABELA.md).
