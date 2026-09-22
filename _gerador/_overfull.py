#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atribui cada Overfull do log ao ficheiro .tex em que ocorre.

O log do TeX da o numero de linha do ficheiro aberto nesse momento, nao o
nome; sem seguir a pilha de ficheiros, um overfull do Apendice C parece ser
do Apendice A. Uso: python3 _gerador/_overfull.py [limiar_pt]
"""
import re, sys
LIM = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
log = open('/tmp/tese-build/template.log', encoding='utf-8', errors='replace').read()
tok = re.compile(r'\((\.?[-\w./]*\.tex)|(\))|Overfull \\hbox \(([0-9.]+)pt too wide\) in (alignment|paragraph) at lines (\d+)--(\d+)')
pilha, achados = [], []
for m in tok.finditer(log):
    if m.group(1):
        pilha.append(m.group(1))
    elif m.group(2):
        if pilha: pilha.pop()
    else:
        achados.append((float(m.group(3)), m.group(4),
                        pilha[-1] if pilha else '?', m.group(5)))
vistos, ded = set(), []
for a in achados:
    k = (a[0], a[2], a[3])
    if k in vistos: continue
    vistos.add(k); ded.append(a)
for tipo, rot in (('alignment', 'TABELAS'), ('paragraph', 'PARAGRAFOS')):
    sub = sorted([a for a in ded if a[1] == tipo and a[0] >= LIM], key=lambda x: -x[0])
    print(f'OVERFULL EM {rot} (>= {LIM:g}pt): {len(sub)}')
    for pt, _, f, ln in sub[:25]:
        print('  %8.2fpt  %-44s l.%s' % (pt, f, ln))
    print()
