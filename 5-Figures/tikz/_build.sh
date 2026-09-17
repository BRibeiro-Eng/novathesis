#!/bin/sh
# Compila as figuras TikZ isoladas para inspecao rapida (2026-09-17).
set -e
D=/tmp/tkt
rm -rf $D; mkdir -p $D
cd "$(dirname "$0")"
cp *.tex $D/
cd $D
/usr/bin/python3 - <<'PY'
figs=["f01-duas-camadas","f03-cdu","f04-prisma","f06-arquitetura-dados",
      "f07-linha-temporal","f17-referencia-estado-monitor","f21-ficha-estados"]
s=open("_teste.tex").read()
s=s.replace("\\FIGS","\n".join("\\input{%s}\n\\clearpage"%f for f in figs))
open("t.tex","w").write(s)
PY
/Library/TeX/texbin/pdflatex -interaction=nonstopmode t.tex > /dev/null 2>&1 || true
echo "== erros:"; grep -n '^!' t.log | head -20 || true
echo "== overfull:"; grep -n 'Overfull .hbox' t.log | head -20 || true
/usr/local/bin/python3 - <<'PY'
import fitz
d=fitz.open("/tmp/tkt/t.pdf")
print("== paginas:", d.page_count)
for i in range(d.page_count):
    d[i].get_pixmap(dpi=125).save("/tmp/tkt/p%d.png"%i)
PY
for i in 0 1 2 3 4 5 6; do cp /tmp/tkt/p$i.png ~/Desktop/Tese/novathesis/.rev-p$i.png 2>/dev/null || true; done
echo "== feito"
