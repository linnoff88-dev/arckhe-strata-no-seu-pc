# Falhas corrigidas

| data | o que quebrou | menor correção | prompt ou infra |
|---|---|---|---|
| 2026-11-15 | Guia omitia Gyro-S, confundia soma com RAM e desconhecia identificadores do connect; script não comparava disco | alinhar trechos e limiares com MODELS.md e harness.py, acrescentar comparação do download | prompt |
| 2026-11-15 | Tradução interpretou “abaixo” como qualidade inferior e deixou ambígua a linha de 32 GB | explicitar referência à tabela e “nenhum pacote por inteiro”, retraduzindo só os trechos pelo tradutor central | prompt |
| 2026-11-15 | Guia omitia o PC gamer de 12 GB, condições do benchmark e requisito de contexto do Claude Code | incluir caso de 44 GB totais, fontes e condições das medições, seleção por lista e variável gerada pelo connect | prompt |
| 2026-11-15 | Guia não identificava instaladores nem a saída do monitor para conectar | indicar nomes da release, abrir .dmg e usar q para manter servidor em segundo plano | prompt |
| 2026-11-15 | Guia podia levar iniciante ao download antes da escolha do tamanho e não explicitava a primeira conversa | acrescentar pré-checagem antes dos passos e fechamento do chat no caminho do app | prompt |
