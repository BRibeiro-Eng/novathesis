"""Extrai G e a bibliografia, reconstruindo as ligações para as páginas extraídas."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import Fit, NullObject
import json, re
import pypdfium2 as pdfium
root=Path(__file__).resolve().parent
source=root/'projeto-compilacao/template.pdf'
r=PdfReader(source)
def walk(items):
    for x in items:
        if isinstance(x,list): yield from walk(x)
        else: yield x
outline=list(walk(r.outline))
o={x.title:r.get_destination_page_number(x) for x in outline}
g=next(v for k,v in o.items() if k.startswith('G Fundamentos'))
h=next(v for k,v in o.items() if k.startswith('H Notas'))
bib=o['Bibliografia']; a=next(v for k,v in o.items() if k.startswith('A '))
selected=list(range(g,h))+list(range(bib,a)); mapping={p:i for i,p in enumerate(selected)}
w=PdfWriter()
for page_index in selected:
    w.add_page(r.pages[page_index],excluded_keys=['/Annots'])
links={'internal':0,'external':0,'omitted':[]}
def number(v): return None if v is None or isinstance(v,NullObject) else float(v)
for old,new in mapping.items():
    for ar in r.pages[old].get('/Annots',[]):
        ann=ar.get_object()
        if ann.get('/Subtype')!='/Link':continue
        action=ann.get('/A',{}); dest=action.get('/D',ann.get('/Dest'))
        rect=tuple(float(x) for x in ann['/Rect'])
        if action.get('/S')=='/URI':
            link=Link(rect=rect,url=str(action['/URI']));links['external']+=1
        elif isinstance(dest,str) and dest in r.named_destinations:
            d=r.named_destinations[dest]; target=r.get_destination_page_number(d)
            if target not in mapping:
                links['omitted'].append({'page':old,'destination':dest});continue
            fit=Fit.xyz(left=number(d.get('/Left')),top=number(d.get('/Top')),zoom=number(d.get('/Zoom')))
            link=Link(rect=rect,target_page_index=mapping[target],fit=fit);links['internal']+=1
        else:
            links['omitted'].append({'page':old,'destination':str(dest)});continue
        w.add_annotation(new,link)
parent=w.add_outline_item('Apêndice G — Rascunho',0);secparent=parent
for x in outline:
    if re.match(r'G\.\d+ ',x.title):secparent=w.add_outline_item(x.title,r.get_destination_page_number(x)-g,parent=parent)
    elif re.match(r'G\.\d+\.\d+ ',x.title):w.add_outline_item(x.title,r.get_destination_page_number(x)-g,parent=secparent)
w.add_outline_item('Bibliografia da tese — consulta',h-g)
w.add_metadata({'/Title':'Fundamentos e formulações matemáticas da dissertação — Rascunho','/Author':'Bernardo Ribeiro','/Subject':'Apêndice G em revisão, com bibliografia da tese para consulta'})
output=root/'anexo-G-rascunho.pdf'
with output.open('wb') as f:w.write(f)
rr=PdfReader(output);texts=[p.extract_text() for p in rr.pages]
samples={'abertura':0,'notacao':1,'auditoria':next(i for i,t in enumerate(texts[:h-g]) if 'Clopper' in t and 'Beta' in t),'pares':next(i for i,t in enumerate(texts[:h-g]) if 'Esquema dos cinco pares' in t),'canais':next(i for i,t in enumerate(texts[:h-g]) if 'Decomposição conceptual dos canais' in t),'simulacao':next(i for i,t in enumerate(texts[:h-g]) if 'Separação entre calibração' in t),'fecho':h-g-1}
(root/'anexo-G-texto-extraido.txt').write_text('\n\n'.join(f'=== PÁGINA PDF {i+1} ===\n{t}' for i,t in enumerate(texts)))
render=root/'verificacao-visual';render.mkdir(exist_ok=True)
pdf=pdfium.PdfDocument(str(output))
for name,index in samples.items():pdf[index].render(scale=1.6).to_pil().save(render/f'{name}.png')
report={'appendix_pages':h-g,'bibliography_pages':a-bib,'total_pages':len(rr.pages),'links':links,'samples':samples,'original_pdf_pages':len(r.pages),'output_size_bytes':output.stat().st_size}
(root/'extracao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({**report,'links':{k:(len(v) if isinstance(v,list) else v) for k,v in links.items()}},ensure_ascii=False))
