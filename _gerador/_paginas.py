#!/usr/bin/env python3
"""Exporta para PNG as paginas do PDF que contem certas frases (inspeccao)."""
import sys, fitz
d = fitz.open("/tmp/tese-build/template.pdf")
alvos = sys.argv[1:]
pags = set()
for a in alvos:
    ps = [i + 1 for i in range(d.page_count) if a in " ".join(d[i].get_text().split())]
    print(a[:34], "->", ps)
    pags.update(ps)
import os
for p in sorted(pags):
    d[p - 1].get_pixmap(dpi=105).save(os.path.expanduser("~/Desktop/Tese/novathesis/.rev-n%d.png" % p))
