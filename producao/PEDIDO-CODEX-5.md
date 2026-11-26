# Pedido ao Codex — fase 5: quarta rodada do revisor (nota 7)

Pasta `/home/nmaldaner/projetos/strata-no-seu-pc/`. Fonte: FATOS.md + docs-oficiais/. Nêo diga "testei". Nêo rode o Strata.
Cada mudança nos três HTML (PT, en/, es/) trecho a trecho, sem regenerar en/es.

1. **Rolagem horizontal em 390 px**: o `div.glow` da hero passa da tela (scrollWidth 398). Corrija só o necessário (ex.: `overflow:hidden` no
   container da hero ou `overflow-x:clip` no body) sem mexer no resto do CSS. Confira com Chromium headless em 390 px que
   `document.documentElement.scrollWidth <= 390` nos 3 idiomas e cole o número.
2. **Script × tabela em 48 e 64 GB**: o script mostra sempre as DUAS opções da faixa (Q2_0/IQ2_XS; IQ3_XXS/IQ3_S), calcula a sobra
   (RAM lida − especialistas − 10 GB) e avisa quando a sobra for < 3 GB ("cabe apertado: prefira o menor, ou feche programas"); na faixa de 64 GB
   repita a ressalva da doc "IQ3_S com pouca coisa aberta". Tabela da página com a mesma regra/texto.
3. **Rótulo**: "40 GB lidos ≈ PC de 32 GB" confunde — use "40 GB lidos (fica na faixa de 32 GB da tabela)". A linha "PC gamer…placa de 12 GB" só
   quando a VRAM for 12–16; com outra VRAM descreva a placa do leitor.
4. **Conferir antes de baixar, oficial**: no passo 2 inclua `strata launch --plan --family qwen --model <tamanho>` (MODELS.md: mostra o plano sem baixar).
   Download do IQ3_S/IQ3_XXS em PC x86: se a doc nêo der o número, troque por "o --plan mostra o tamanho do download".
5. **Quem usa Claude Code pela assinatura**: o `--write` troca o `~/.claude/settings.json` global e o Claude Code passa a usar o Strata (deixa de usar a
   assinatura). Mostre a alternativa sem mexer no global: rodar `strata connect claude-code` (sem `--write`), copiar as variáveis que ele imprime e
   exportar só num terminal separado (`export ANTHROPIC_BASE_URL=...` etc. / `$env:...` no PowerShell); para voltar, fechar esse terminal. Se usou
   `--write`, restaurar o backup. Mesma lógica para o Codex (`~/.codex/config.toml`). Atualize CONECTAR (PT/EN/ES).
6. **Hero**: acrescente à dor "gasta o limite da assinatura" junto de "paga assinatura" (sem alongar demais o h1; pode ir no lead).
7. **Termos**: explique ou troque MemTotal ("a memória que o sistema enxerga, um pouco menor que a instalada"), shard ("parte do arquivo do modelo"),
   WSL ("Linux dentro do Windows"), endpoint, alias, variável de ambiente; tire "harness.py oficial" do texto do leitor (diga "o código oficial do strata connect").
8. **ES meta description**: tire "en portugués" (o kit tem ES). Confira a meta EN igual.
9. Em "O que o projeto mede", destaque a linha RTX 5070 12 GB + 64 GB (IQ3_S ~53, IQ3_XXS ~62 tokens/s — confira no MODELS.md) como o caso mais
   parecido com 64 GB de RAM + placa de 12–16 GB.

No fim: os scrollWidth nos 3 idiomas, saídas do script para (46,16), (62.5,16), (40,16), (31.3,12), `grep -c "{{"` nos 3 HTML.
