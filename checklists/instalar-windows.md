# Instalar no Windows

- [ ] [Antes, veja o tamanho na tabela (passo 2).](../TABELA.md)

- [ ] Confira Windows 10/11 x86-64 e GPU compatível. Windows ARM nêo é uma rota suportada nesta doc.
- [ ] Leia [antes de instalar](antes-de-instalar.md) e escolha um tamanho.
- [ ] Para conversar, abra a [release oficial](https://github.com/Niko1221/Strata/releases/latest) e baixe `Strata-0.2.13-windows-x64-setup.exe`, conforme a cópia da doc. Nêo escolha um arquivo `strata-engine-…` como instalador.
- [ ] O app instala para seu usuário, sem administrador. Na primeira abertura, baixe o motor indicado; depois escolha modelo e pasta.
- [ ] Se preferir terminal, abra PowerShell (a janela em que você digita comandos) e use o comando oficial abaixo.

```powershell
irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

- [ ] Abra um **novo** PowerShell e inicie:

```powershell
strata launch
```

- [ ] Escolha modelo, contexto, pasta e acesso. Acompanhe a preparaçêo; nêo há tempo universal para a primeira partida.
- [ ] Para ferramentas de programaçêo, siga [CONECTAR.md](../CONECTAR.md).
- [ ] Se `strata` nêo aparecer, confira a nova janela e `strata --version`. Se o driver for antigo, siga o pacote indicado na doc.

O script de tamanho é Bash. Nêo cole o comando `bash` no PowerShell supondo que Bash já exista; se nêo houver Bash disponível, use a ficha do computador para identificar RAM e memória da placa; confira o espaço livre no disco de destino e compare com a tabela. Sem esses dados, adie o download do modelo.
Nenhum destes comandos foi executado por nós.

Fontes: `docs-oficiais/INSTALL.md`, `TROUBLESHOOTING.md` e `SAFETY.md`.

Depois de instalar o Strata e abrir um novo terminal, confira o plano antes de baixar o modelo. Escolha somente o comando da opçêo compatível da tabela; --plan mostra o plano sem iniciar o modelo. Nêo troque só o tamanho mantendo a família qwen: Coder, Gyro, Unsloth e NVFP4 têm famílias próprias. Para IQ3_S em x86, confirme aqui o download da sua plataforma. [TABELA.md](../TABELA.md).
