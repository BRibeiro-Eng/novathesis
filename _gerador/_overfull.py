#!/usr/bin/env python3
"""Lista os Overfull hbox do build com o ficheiro correto (pilha de parenteses)."""
import re, sys
texto = open("/tmp/tese-build/template.log", errors="ignore").read()
pilha, saida, i = [], [], 0
tok = re.compile(r"\(([^()\s]*\.tex)|(\()|(\))|(Overfull \\hbox \([0-9.]+pt too wide\)[^\n]*)")
for m in tok.finditer(texto):
    if m.group(1):   pilha.append(m.group(1))
    elif m.group(2): pilha.append(None)
    elif m.group(3):
        if pilha: pilha.pop()
    else:
        atual = next((x for x in reversed(pilha) if x), "?")
        saida.append((atual, m.group(4)))
from collections import Counter
c = Counter(a for a, _ in saida)
for f, n in c.most_common():
    print(f"{n:4d}  {f}")
print("-" * 40)
for a, l in saida:
    if "tikz" in a or "gerado" in a:
        print(a, "|", l[:80])
