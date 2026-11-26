# Falhas corrigidas

| data | o que quebrou | menor correçêo | prompt \| infra |
|---|---|---|---|
| 2026-11-15 | Planos usavam qwen para outras famílias; chave mascarada copiável, faixa 64 GB incompleta, aviso negativo contraditório e textos EN/ES em PT | Explicitar família/modelo, --show-key e opções do harness; completar TSV, tornar avisos exclusivos e localizar fragmentos | prompt |
| 2026-11-15 | Faixas da tabela divergiam do script; --plan precedia instalaçêo e moldes de conexêo omitiam variáveis | Fonte única TSV para faixas, geraçêo das tabelas e comparaçêo das saídas; mover --plan e completar moldes pelo harness oficial | prompt |
| 2026-11-15 | Novas variáveis longas estouravam o corpo para 518 px, ocultadas por overflow-x:clip | Permitir quebra em parágrafos e largura mínima zero nos itens de grade; corpo e documento medidos em 390 px | prompt |
| 2026-11-15 | Página carregada extrapolava 390 px para 398 px nos três idiomas | Acrescentar apenas overflow-x:clip a html e body e medir após carregamento e fontes | prompt |
| 2026-11-15 | Script ocultava a segunda opçêo de RAM, atribuía 12 GB a outras placas e generalizava download do Spark; guia omitia alternativa à configuraçêo global | Mostrar pares e sobra, descrever VRAM lida, consultar --plan e documentar sessêo isolada nos três idiomas | prompt |
| 2026-11-15 | Tradutor retornou JSON com chaves extras e quebras escapadas | Corrigir só o invólucro JSON e normalizar quebras antes de validar e aplicar | prompt |
| 2026-11-15 | Limiares literais de RAM descartavam PCs de 32/64 GB e Spark com memória reservada; guia omitia pré-requisitos, verificações e traduções de apoio | Aplicar margem nominal, manter orçamento real por pacote, incluir comandos documentados e traduzir só trechos/documentos faltantes | prompt |
