import pymupdf, re
d = pymupdf.open('template.pdf')
print('paginas', d.page_count)
for i in range(64, 72):
    p = d[i]; itens = []
    for b in p.get_text('dict')['blocks']:
        if b['type'] != 0: continue
        for l in b['lines']:
            t = ''.join(s['text'] for s in l['spans']).strip()
            m = re.match(r'^(3\.3\.\d)', t); m2 = re.match(r'^Figura (3\.\d+):', t)
            if m: itens.append((l['bbox'][1], 'SUBSEC ' + m.group(1)))
            if m2: itens.append((l['bbox'][1], 'Fig ' + m2.group(1)))
    itens.sort()
    ys = [l['bbox'][3] for b in p.get_text('dict')['blocks'] if b['type'] == 0
          for l in b['lines'] if l['bbox'][3] < 785]
    print('impressa %2d  fundo %6.1f  %s' % (i - 26, max(ys) if ys else 0,
          ' -> '.join(x[1] for x in itens)))
