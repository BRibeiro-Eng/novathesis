#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventario das tabelas da tese e do seu idioma tipografico.

Uma coluna por convencao do padrao da Tabela 3.2, para se ver de relance
qual e a tabela que destoa. Uso: python3 _gerador/_tabelas.py
"""
import io, re, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUX = '/tmp/tese-build/template.aux'
num = {}
if os.path.exists(AUX):
    for m in re.finditer(r'newlabel\{(tab:[^}]*)\}\{\{([0-9A-Z.]+)\}\{(\d+)\}',
                         io.open(AUX, encoding='utf-8', errors='replace').read()):
        num[m.group(1)] = m.group(2)
linhas = []
for p in sorted(glob.glob("2-MainMatter/*.tex")) + sorted(glob.glob("3-BackMatter/*.tex")):
    s = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r'\\begin\{(xltabular|tabularx|tabular)\}', s):
        ini = m.start()
        fim = s.index("\\end{" + m.group(1) + "}", ini)
        ctx = s[max(0, ini - 1400):fim]
        seg = s[ini:fim]
        lab = re.search(r'\\label\{(tab:[^}]*)\}', s[max(0, ini - 1400):ini + 1600])
        L = lab.group(1) if lab else "?"
        tam = re.search(r'\\(footnotesize|small|scriptsize|tiny)\b', ctx)
        cab = seg[seg.index("\\toprule"):seg.index("\\midrule")] \
              if "\\toprule" in seg and "\\midrule" in seg else ""
        linhas.append(dict(
            n=num.get(L, "?"), lab=L, amb=m.group(1),
            larg="textwidth" if "{\\textwidth}" in s[ini:ini+80]
                 else ("linewidth" if "{\\linewidth}" in s[ini:ini+80] else "--"),
            tam=(tam.group(1) if tam else "NORMAL"),
            zeb="s" if "\\ntzebra" in ctx else "-",
            hide="s" if "\\hiderowcolors" in seg else "-",
            show="s" if "\\showrowcolors" in seg else "-",
            cont="s" if "continua na p" in seg else "-",
            elf="s" if "\\endlastfoot" in seg else "-",
            neg="s" if "\\textbf" in cab else "-"))
linhas.sort(key=lambda d: (0, [int(x) for x in d["n"].split(".")])
            if d["n"][:1].isdigit() else (1, d["n"]))
print(f"{'Tab':6s} {'ambiente':10s} {'largura':10s} {'tamanho':12s} zeb hide show cont elf neg  label")
for d in linhas:
    print(f"{d['n']:6s} {d['amb']:10s} {d['larg']:10s} {d['tam']:12s}  {d['zeb']}   {d['hide']}    "
          f"{d['show']}    {d['cont']}    {d['elf']}   {d['neg']}   {d['lab']}")
