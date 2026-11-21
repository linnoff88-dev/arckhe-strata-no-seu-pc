# Antes de instalar

- [ ] Confira sistema, arquitetura e placa na doc de instalação. Memória suficiente não garante hardware compatível.
- [ ] Some RAM + VRAM; conte memória unificada uma vez. Leia [TABELA.md](../TABELA.md).
- [ ] Confira a RAM separadamente e deixe espaço para sistema, contexto e aplicativos.
- [ ] Escolha a pasta do modelo num SSD; veja o espaço livre nesse disco. Para DeepSeek, a doc pede NVMe.
- [ ] Confira download e arquivos auxiliares. Não confunda tamanho em memória com espaço em disco.
- [ ] Tenha internet para baixar o programa, o motor e o modelo.
- [ ] Confira o driver exigido pelo pacote. CUDA 13 pede NVIDIA 580 ou mais novo; Spark pede 580.65 ou mais novo.
- [ ] Escolha app para conversar ou terminal para configurar ferramentas.
- [ ] Comece com acesso local; só compartilhe com chave.

Opcional, em Bash já disponível, na pasta do kit: `bash ferramentas/qual_tamanho.sh`. Ele só lê informações e imprime sugestões; não instala nem confirma compatibilidade.

Fontes: `docs-oficiais/INSTALL.md`, `MODELS.md`, `DGX_SPARK_LINUX.md`, `SAFETY.md` (todos em `docs-oficiais/`).
