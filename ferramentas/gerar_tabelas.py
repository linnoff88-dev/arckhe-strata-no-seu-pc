#!/usr/bin/env python3
"""Atualiza só faixas/planos: fonte TSV comum ao script; preserva o resto do HTML."""
from pathlib import Path
import csv,html,json,re
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.reader((ROOT/'ferramentas/faixas.tsv').open(),delimiter='\t'))
def load(name): return json.loads((ROOT/'producao'/name).read_text())
old={'pt':load('fragmentos-fase6.pt.json'),**load('fragmentos-fase6.traducoes.json')}
new={'pt':load('fragmentos-fase7.pt.json'),**load('fragmentos-fase7.traducoes.json')}
def pair(option):
    n=option.split(' (')[0]
    family='coder' if n=='Coder' else 'gyro' if n=='Gyro-S' else 'nvfp4' if n=='NVFP4' else 'unsloth' if n.startswith('UD-') else 'qwen'
    return f'--family {family} --model '+('IQ1_M' if n=='Coder' else n)
options=list(dict.fromkeys(x for row in rows for x in row[4].split('; ') if x!=new['pt']['no_option']))
plans=list(dict.fromkeys('strata launch --plan '+pair(x) for x in options))
for lang,base in old.items():
    d={**base,**new[lang]}
    def local(s):
        for key in ['no_option','mac_spark','spark_only']: s=s.replace(new['pt'][key],d[key])
        return re.sub(r'(\d),(\d)',r'\1.\2',s) if lang=='en' else s
    path=ROOT/('guia/index.html' if lang=='pt' else f'guia/{lang}/index.html')
    s=path.read_text()
    section=re.search(r'<section id="cabe">.*?</section>',s,re.S).group()
    title=re.search(r'<h2>.*?</h2>',section,re.S).group()
    cells=[]
    for row in rows:
        opts=row[4].split('; ')
        rendered=[local(x)+(f' (`{pair(x)}`)' if x!=new['pt']['no_option'] else '') for x in opts]
        cells.append([d['platforms'][0 if row[0]=='separada' else 1],local(row[3]),'; '.join(rendered)])
    headers=[*d['headers'][:2],d['options_header']]
    def markup(t):return re.sub(r'`([^`]+)`',r'<code>\1</code>',html.escape(t))
    table='<div style="overflow-x:auto"><table><thead><tr>'+''.join('<th scope="col">'+html.escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>'
    table+=''.join('<tr>'+''.join('<td>'+markup(x)+'</td>' for x in row)+'</tr>' for row in cells)+'</tbody></table></div>'
    paras=lambda keys: ''.join('<p>'+html.escape(d[k])+'</p>' for k in keys)
    replacement='<section id="cabe"><div class="wrap">'+title+paras(['intro','compression','glossary'])+table+paras(['headroom','notes','unified','disk'])+'<p>MODELS.md · DGX_SPARK_LINUX.md · FATOS.md</p></div></section>'
    path.write_text(s.replace(section,replacement,1))
    md=ROOT/('TABELA.md' if lang=='pt' else f'TABELA.{lang}.md')
    heading=md.read_text().splitlines()[0]
    text=heading+'\n\n'+'\n\n'.join(d[k] for k in ['intro','compression','glossary'])+'\n\n| '+' | '.join(headers)+' |\n|---|---|---|\n'
    text+=''.join('| '+' | '.join(c)+' |\n' for c in cells)
    text+='\n'+'\n\n'.join(d[k] for k in ['headroom','notes','unified','disk','plan'])+'\n\n```sh\n'+'\n'.join(plans)+'\n```\n\n'
    text+='Fontes / Sources / Fuentes: [MODELS.md](docs-oficiais/MODELS.md), [DGX_SPARK_LINUX.md](docs-oficiais/DGX_SPARK_LINUX.md), [FATOS.md](FATOS.md).\n'
    md.write_text(text)
