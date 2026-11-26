from pathlib import Path
from bs4 import BeautifulSoup
import csv,os,subprocess,json,re
root=Path(__file__).resolve().parents[1]
os.chdir(root)
rows=list(csv.reader(open('ferramentas/faixas.tsv'),delimiter='\t'))
expected=[('<30 GB','Sem indicaçêo automática segura'),('30–45,9 GB','Gyro-S; Coder'),('30–45,9 GB','Gyro-S; Coder'),('46–61,9 GB','Q2_0; IQ2_XS'),('62–93,9 GB','IQ3_XXS; IQ3_S'),('94–125,9 GB','Q2_0; IQ2_XS; IQ3_XXS; IQ3_S; UD-IQ4_XS; UD-Q4_K_XL'),('≥126 GB','Q2_0; IQ2_XS; IQ3_XXS; IQ3_S; UD-IQ4_XS; UD-Q4_K_XL; UD-Q5_K_XL; UD-Q6_K_XL')]
report=['# Conferência da fase 6\n\nSomente o script de orientaçêo e os arquivos locais foram executados/verificados. Nenhum comando Strata foi executado. RAM/VRAM/disco/arquitetura substituídos para resultados reproduzíveis: VRAM 12 GB, disco livre 70 GB, x86_64.\n']
def run(r,u=0):
 return subprocess.check_output(['bash','ferramentas/qual_tamanho.sh'],env={**os.environ,'QT_FAKE_RAM_GB':str(r),'QT_FAKE_VRAM_GB':'12','QT_FAKE_DISCO_GB':'70','QT_FAKE_ARCH':'x86_64','QT_UNIFICADA':str(u)},text=True)
for r,(label,options) in zip([29,31.3,44.5,46,62.5,94,126],expected):
 out=run(r)
 assert 'Faixa: '+label+'\nOpções: '+options+'\n' in out
 row=next(x for x in rows if x[0]=='separada' and x[3]==label)
 assert row[4]==options
 if r==46:assert '46 - 34 - 10 = 2 GB' in out and '46 - 35.5 - 10 = 0.5 GB' in out and out.count('cabe apertado')==2
 if r==62.5:assert '62.5 - 43 - 10 = 9.5 GB' in out and '62.5 - 50 - 10 = 2.5 GB' in out and '66–76 GB' in out and 'AVISO: disco abaixo' in out
 report.append(f'## RAM {r} GB / VRAM 12 GB\n\nFaixa e lista: correspondência literal com TABELA.md.\n\n```text\n{out}```\n')
# Every bound and just below it, shared/unified; verify single matching row.
for u,platform in [(0,'separada'),(1,'unificada')]:
 for r in [0,29.999,30,45.9,45.999,46,61.999,62,93.999,94,125,125.999,126,160]:
  matching=[x for x in rows if x[0]==platform and r>=float(x[1]) and (float(x[2])==0 or r<float(x[2]))];assert len(matching)==1
  row=matching[0];assert 'Faixa: '+row[3]+'\nOpções: '+row[4]+'\n' in run(r,u)
for lang in ['pt','en','es']:
 path=Path('guia/index.html' if lang=='pt' else f'guia/{lang}/index.html');s=BeautifulSoup(path.read_text(),'html.parser')
 assert len(s.select_one('.lead').get_text().split())<=50
 table=s.select('#cabe table');assert len(table)==1
 for tr,row in zip(table[0].select('tbody tr'),rows):
  td=tr.select('td');assert td[1].get_text()==row[3] and td[2].get_text()==row[4]
 md=Path('TABELA.md' if lang=='pt' else f'TABELA.{lang}.md').read_text()
 for row in rows:assert '| '+row[3]+' | '+row[4]+' |' in md
 steps=s.select('#guia .step');assert '--plan' not in steps[1].get_text()
 codes=[x.get_text() for x in steps[2].select('pre')]
 assert next(i for i,x in enumerate(codes) if 'install.ps1' in x)<next(i for i,x in enumerate(codes) if '--plan' in x)<codes.index('strata launch')
 assert s.select_one('a[href="https://nodejs.org"]')
 assert 'node -v\nnpm -v' in s.get_text()
 assert 'model_providers.strata.stream_idle_timeout_ms=600000' in s.get_text()
 for name in re.findall(r'"([A-Z_]+)"',Path('docs-oficiais/harness.py.txt').read_text().split('def claude_env')[1].split('def claude_file')[0]):
  if name=='1':continue
  assert f'export {name}=' in s.get_text() and f'$env:{name}=' in s.get_text(),name
 assert '{{' not in path.read_text()
report.append('## Verificações adicionais\n\n28 combinações de limites e memória unificada: uma única faixa e lista literal em cada caso. Três tabelas HTML e três Markdown correspondem à fonte TSV. Leads ≤50 palavras; --plan depois do instalador; variáveis do harness presentes em Bash e PowerShell.\n')
Path('producao/CONFERENCIA-FASE6.md').write_text('\n'.join(report))
print('7 saídas integrais gravadas; 28 limites e 3 idiomas conferidos.')
