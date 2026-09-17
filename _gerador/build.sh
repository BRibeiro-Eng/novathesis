#!/bin/sh
# Build deterministico da tese (2026-09-17): pdflatex -> biber -> pdflatex x3.
# O latexmk entra em ciclo com o automake dos glossarios; este script evita-o.
cd "$HOME/Desktop/Tese/novathesis" || exit 1
export PATH=/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:$PATH
rm -f /tmp/estado.txt
pdflatex -interaction=nonstopmode -file-line-error -synctex=1 template > /tmp/b1.log 2>&1
biber template > /tmp/b_biber.log 2>&1
for i in 2 3 4; do pdflatex -interaction=nonstopmode -file-line-error -synctex=1 template > /tmp/b$i.log 2>&1; done
{
  echo "rc=$?"
  echo "undefined=$(grep -c undefined template.log)"
  echo "erros=$(grep -a -c '^\!' template.log)"
  echo "paginas=$(pdfinfo template.pdf | awk '/Pages/{print $2}')"
  echo FIM
} > /tmp/estado.txt
