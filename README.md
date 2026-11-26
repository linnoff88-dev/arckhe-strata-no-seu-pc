ï»¿# ê°Å¸Â§Â  strata-no-seu-pc

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![strata-no-seu-pc](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/arckhe-/guia/)

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

VocêÂª quer usar IA sem pagar por cada pergunta e manter seus arquivos no seu computador. O Strata êÂ© um motor grêÂ¡tis e aberto que divide uma IA grande entre a placa de vêÂ­deo, a memêÂ³ria e o armazenamento. Este kit ajuda vocêÂª a escolher um tamanho e conectar suas ferramentas, com base na documentaêÂ§êÂ£o oficial. VocêÂª precisa de hardware compatêÂ­vel, memêÂ³ria e espaêÂ§o para o modelo; quem tem Windows ou Mac e sêÂ³ quer conversar pode usar o aplicativo e pular a parte têÂ©cnica.

## ê°Å¸ââ Guia de uso

https://linnoff88-dev.github.io/arckhe-/guia/

Kit pêÂºblico e gratuito do ARCKHÉ AI. MêÂ©todo: **balcêÂ£o e despensa**.
**Nada aqui foi rodado por nêÂ³s: êÂ© a documentaêÂ§êÂ£o oficial organizada.** Os nêÂºmeros sêÂ£o do projeto ou da comunidade dele.
[Strata oficial](https://github.com/Niko1221/Strata) ê¢â¬â motor de cêÂ³digo aberto, licenêÂ§a MIT; os modelos têÂªm licenêÂ§as prêÂ³prias.

## Os arquivos

- [DICAS.md](DICAS.md): dicas, pegadinhas e problemas frequentes.
- [TABELA.md](TABELA.md): memêÂ³ria, tamanhos e limites.
- [CONECTAR.md](CONECTAR.md): Claude Code, Codex CLI, OpenCode e acesso com chave.
- [Checklists](checklists/): [antes de instalar](checklists/antes-de-instalar.md), [Windows](checklists/instalar-windows.md), [Linux/Mac](checklists/instalar-linux-mac.md), [DGX Spark](checklists/dgx-spark.md).
- [qual_tamanho.sh](ferramentas/qual_tamanho.sh): leitura de hardware, sem instalaêÂ§êÂ£o.
- [FATOS.md](FATOS.md) e [docs-oficiais/](docs-oficiais/): fontes locais.

## O processo, do inêÂ­cio ao fim

1. ê°Å¸Â§Â  VocêÂª entende a cozinha: placa no balcêÂ£o, RAM na despensa, SSD no porêÂ£o.
2. ê¢Å¡â¢ê¯Â¸Â Script: se vocêÂª o executar em Bash, lêÂª RAM, VRAM NVIDIA, arquitetura e disco; sugere candidatos sem instalar nada.
3. ê°Å¸Â§Â  VocêÂª confere a tabela, o hardware compatêÂ­vel e o espaêÂ§o; escolhe um tamanho com folga.
4. ê°Å¸Â§Â  VocêÂª baixa o app ou executa o instalador oficial e escolhe o modelo. O Strata faz o download e prepara os arquivos.
5. ê°Å¸Â§Â  VocêÂª usa `strata connect`, revisa a configuraêÂ§êÂ£o, autoriza a gravaêÂ§êÂ£o com backup e confere a conexêÂ£o.
6. ê°Å¸Â¤â IA: o modelo local responde no seu computador. VocêÂª revisa as respostas e controla o acesso e as ferramentas.

Segundo o README oficial, DeepSeek V4.1-Flash 2.00 bpw na RTX 5070 12 GB + 64 GB de RAM produz 4ê¢â¬â6 tokens/s. êâ° uma mediêÂ§êÂ£o do projeto, nêÂ£o deste kit. ([README](docs-oficiais/strata-README.md)).

O script usa Bash; a saêÂ­da traduzida com QT_LANG=en ou QT_LANG=es tambêÂ©m exige Python 3 instalado. Sem QT_LANG, o padrêÂ£o êÂ© portuguêÂªs.

```sh
bash ferramentas/qual_tamanho.sh
```

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>