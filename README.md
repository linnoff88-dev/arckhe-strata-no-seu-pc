# ðŸ§  strata-no-seu-pc

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![strata-no-seu-pc](guia/assets/banner.jpg)](https://inematds.github.io/strata-no-seu-pc/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

VocÃª quer usar IA sem pagar por cada pergunta e manter seus arquivos no seu computador. O Strata Ã© um motor grÃ¡tis e aberto que divide uma IA grande entre a placa de vÃ­deo, a memÃ³ria e o armazenamento. Este kit ajuda vocÃª a escolher um tamanho e conectar suas ferramentas, com base na documentaÃ§Ã£o oficial. VocÃª precisa de hardware compatÃ­vel, memÃ³ria e espaÃ§o para o modelo; quem tem Windows ou Mac e sÃ³ quer conversar pode usar o aplicativo e pular a parte tÃ©cnica.

## ðŸ“– Guia de uso

https://inematds.github.io/strata-no-seu-pc/guia/

Kit pÃºblico e gratuito do INEMA.CLUB. MÃ©todo: **balcÃ£o e despensa**.
**Nada aqui foi rodado por nÃ³s: Ã© a documentaÃ§Ã£o oficial organizada.** Os nÃºmeros sÃ£o do projeto ou da comunidade dele.
[Strata oficial](https://github.com/Niko1221/Strata) â€” motor de cÃ³digo aberto, licenÃ§a MIT; os modelos tÃªm licenÃ§as prÃ³prias.

## Os arquivos

- [DICAS.md](DICAS.md): dicas, pegadinhas e problemas frequentes.
- [TABELA.md](TABELA.md): memÃ³ria, tamanhos e limites.
- [CONECTAR.md](CONECTAR.md): Claude Code, Codex CLI, OpenCode e acesso com chave.
- [Checklists](checklists/): [antes de instalar](checklists/antes-de-instalar.md), [Windows](checklists/instalar-windows.md), [Linux/Mac](checklists/instalar-linux-mac.md), [DGX Spark](checklists/dgx-spark.md).
- [qual_tamanho.sh](ferramentas/qual_tamanho.sh): leitura de hardware, sem instalaÃ§Ã£o.
- [FATOS.md](FATOS.md) e [docs-oficiais/](docs-oficiais/): fontes locais.

## O processo, do inÃ­cio ao fim

1. ðŸ§  VocÃª entende a cozinha: placa no balcÃ£o, RAM na despensa, SSD no porÃ£o.
2. âš™ï¸ Script: se vocÃª o executar em Bash, lÃª RAM, VRAM NVIDIA, arquitetura e disco; sugere candidatos sem instalar nada.
3. ðŸ§  VocÃª confere a tabela, o hardware compatÃ­vel e o espaÃ§o; escolhe um tamanho com folga.
4. ðŸ§  VocÃª baixa o app ou executa o instalador oficial e escolhe o modelo. O Strata faz o download e prepara os arquivos.
5. ðŸ§  VocÃª usa `strata connect`, revisa a configuraÃ§Ã£o, autoriza a gravaÃ§Ã£o com backup e confere a conexÃ£o.
6. ðŸ¤– IA: o modelo local responde no seu computador. VocÃª revisa as respostas e controla o acesso e as ferramentas.

Segundo o README oficial, DeepSeek V4.1-Flash 2.00 bpw na RTX 5070 12 GB + 64 GB de RAM produz 4â€“6 tokens/s. Ã‰ uma mediÃ§Ã£o do projeto, nÃ£o deste kit. ([README](docs-oficiais/strata-README.md)).

O script usa Bash; a saÃ­da traduzida com QT_LANG=en ou QT_LANG=es tambÃ©m exige Python 3 instalado. Sem QT_LANG, o padrÃ£o Ã© portuguÃªs.

```sh
bash ferramentas/qual_tamanho.sh
```

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>