#!/usr/bin/env python3
"""Localizaçêo estática da saída de leitura; nêo chama tradutor nem rede."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
pt=json.loads((root/'producao/fragmentos-fase7.pt.json').read_text())
lang=sys.argv[1]
d=json.loads((root/'producao/fragmentos-fase7.traducoes.json').read_text())[lang]
replacements={v:d['output'][k] for k,v in pt['output'].items()}
replacements.update({pt[k]:d[k] for k in ['no_option','mac_spark','spark_only']})
replacements['TABELA.md']=f'TABELA.{lang}.md'
pattern=re.compile('|'.join(re.escape(k) for k in sorted(replacements,key=len,reverse=True)))
for line in sys.stdin:
    line=pattern.sub(lambda m:replacements[m.group()],line)
    line=line.replace('TABELA.md',f'TABELA.{lang}.md')
    if lang=='en': line=re.sub(r'(\d),(\d)',r'\1.\2',line)
    print(line,end='')
