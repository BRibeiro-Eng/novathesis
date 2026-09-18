#!/usr/bin/env python3
"""Extrai todas as caixas \revisaotese ainda abertas, em JSON."""
import re, json, os, glob
RAIZ = os.path.expanduser("~/Desktop/Tese/novathesis")
if not os.path.isdir(RAIZ): RAIZ = os.path.expanduser("~/mnt/novathesis")
pat = re.compile(r"\\revisaotese\{([^}]*)\}\{(P\d)\}\{([^}]*)\}\s*\n?\s*\{(.*?)\}\s*\n?\s*\{", re.S)
out = []
for sub in ("1-FrontMatter", "2-MainMatter", "3-BackMatter"):
    for f in sorted(glob.glob(os.path.join(RAIZ, sub, "*.tex"))):
        rel = os.path.relpath(f, RAIZ)
        if "proposta-estilo" in rel:      # ficheiro alternativo, nao incluido
            continue
        s = open(f, encoding="utf-8").read()
        for m in pat.finditer(s):
            out.append({"id": m.group(1), "prio": m.group(2), "cat": m.group(3),
                        "titulo": " ".join(m.group(4).split()), "ficheiro": rel})
print(json.dumps(out, ensure_ascii=False, indent=1))
