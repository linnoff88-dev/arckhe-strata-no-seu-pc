"""Confere apenas arquivos e script orientativo local, sem executar Strata."""
from pathlib import Path
from bs4 import BeautifulSoup
import csv,json,os,re,subprocess
root=Path(__file__).resolve().parents[1]
os.chdir(root)
rows=list(csv.reader(open('ferramentas/faixas.tsv'),delimiter='\t'))
pt=json.loads(Path('producao/fragmentos-fase7.pt.json').read_text())
tr={'pt':pt,**json.loads(Path('producao/fragmentos-fase7.traducoes.json').read_text())}
report=['# Conferência da fase 7\n\nSomente arquivos, script orientativo e navegador local. Nenhum comando Strata foi executado. As saídas abaixo usam RAM/VRAM informadas, arquitetura x86_64 e disco fixado em 70 GB para reprodução.\n']
def run(r,v,lang='pt',u=0):
 return subprocess.check_output(['bash','ferramentas/qual_tamanho.sh'],env={**os.environ,'QT_FAKE_RAM_GB':str(r),'QT_FAKE_VRAM_GB':str(v),'QT_FAKE_DISCO_GB':'70','QT_FAKE_ARCH':'x86_64','QT_LANG':lang,'QT_UNIFICADA':str(u)},text=True)
def pair(n):
 n=n.split(' (')[0]
 return '--family '+('coder' if n=='Coder' else 'gyro' if n=='Gyro-S' else 'nvfp4' if n=='NVFP4' else 'unsloth' if n.startswith('UD-') else 'qwen')+' --model '+('IQ1_M' if n=='Coder' else n)
for r,v,lang in [(31.3,12,'pt'),(62.5,16,'pt'),(62.5,16,'en'),(94,16,'es')]:
 out=run(r,v,lang)
 if r==31.3:
  assert '31.3 - 23 - 10 = -1.7 GB' in out
  assert out.count(pt['negative'])==1 and 'cabe apertado' not in out
 if r==62.5:
  for n in ['Q2_0','IQ2_XS','IQ3_XXS','IQ3_S']: assert 'strata launch --plan '+pair(n) in out
  for value in ['18.5','17','9.5','2.5']: assert f'= {value} GB.' in out
 if r==94:
  assert 'strata launch --plan --family unsloth --model UD-IQ4_XS' in out
  assert 'strata launch --plan --family unsloth --model UD-Q4_K_XL' in out
  assert '= -4 GB.' in out
 if lang!='pt': assert not re.search(r'ção|não| você|Sem indicação',out)
 command=f'QT_FAKE_RAM_GB={r} QT_FAKE_VRAM_GB={v} QT_FAKE_DISCO_GB=70 QT_FAKE_ARCH=x86_64 QT_UNIFICADA=0 QT_LANG={lang} bash ferramentas/qual_tamanho.sh'
 report.append('## '+str((r,v,lang))+'\n\n```sh\n'+command+'\n```\n\n```text\n'+out+'```\n')
# Check boundaries, platform qualifiers, localization and family/model for every option.
for lang in tr:
 for u,platform in [(0,'separada'),(1,'unificada')]:
  for r in [0,29.999,30,45.999,46,61.999,62,93.999,94,125.999,126,160]:
   matches=[x for x in rows if x[0]==platform and r>=float(x[1]) and (float(x[2])==0 or r<float(x[2]))];assert len(matches)==1
   row=matches[0];out=run(r,16,lang,u)
   for opt in row[4].split('; '):
    if opt!=pt['no_option']:assert 'strata launch --plan '+pair(opt) in out
   if lang!='pt':assert not re.search(r'ção|não| você|Sem indicação',out)
for lang,d in tr.items():
 path=Path('guia/index.html' if lang=='pt' else f'guia/{lang}/index.html');raw=path.read_text();s=BeautifulSoup(raw,'html.parser')
 md=Path('TABELA.md' if lang=='pt' else f'TABELA.{lang}.md').read_text()
 trs=s.select('#cabe tbody tr');assert len(trs)==len(rows)
 for row,trr in zip(rows,trs):
  opts=row[4].split('; ');codes=[x.get_text() for x in trr.select('code')]
  assert codes==[pair(x) for x in opts if x!=pt['no_option']]
  for code in codes:assert '`'+code+'`' in md
  for key in ['no_option','mac_spark','spark_only']:
   if pt[key] in row[4]:assert d[key] in trr.get_text()
 assert d['compression'] in s.get_text() and d['headroom'] in s.get_text()
 steps=s.select('#guia .step');assert steps[0].select_one('a[href="#passo2"]') and steps[1].select_one('a[href="#cabe"]')
 assert '--plan' not in steps[1].get_text()
 for row in rows:
  for option in row[4].split('; '):
   if option!=pt['no_option']:assert 'strata launch --plan '+pair(option) in steps[2].get_text()
 for val in ['model_reasoning_summary="auto"','approval_policy="never"','sandbox_mode="workspace-write"','check_for_update_on_startup=false','model_providers.strata.stream_idle_timeout_ms=600000']:
  assert ('-c \''+val+'\'') in s.get_text()
  assert val in Path('CONECTAR.md' if lang=='pt' else f'CONECTAR.{lang}.md').read_text()
 for name in ['claude-code','codex']:assert 'strata connect '+name+' --show-key' in s.get_text()
 assert '4–6 tokens/s' in s.select_one('#numeros').get_text()
 assert '{{' not in raw
 if lang!='pt':
  assert 'QT_LANG='+lang+' bash ferramentas/qual_tamanho.sh' in s.get_text()
  assert not re.search(r'ção|não| você|Sem indicação|CHAVE_DO_STRATA|&lt;tamanho&gt;',raw)
report.append('## Conferências estáticas e de comportamento\n\n72 combinações de limites/idiomas/plataformas: uma faixa em cada caso e --plan de cada opção. Tabelas HTML/Markdown conferidas contra faixas.tsv. Aviso negativo exclusivo. Opções do Codex, revelação de chave, comandos por família, termos e links presentes nos três idiomas.\n')
Path('producao/CONFERENCIA-FASE7.md').write_text('\n'.join(report))
print('Quatro saídas integrais gravadas; 72 combinações e três idiomas conferidos.')
