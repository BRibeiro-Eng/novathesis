#!/bin/sh
cd "$HOME/Desktop/Tese/novathesis" || exit 1
export PATH=/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:$PATH
rm -f /tmp/estado.txt
latexmk -f -e '$max_repeat=10;' -synctex=1 -interaction=nonstopmode -file-line-error -pdf template > /tmp/build_final3.log 2>&1
{
  echo "rc=$?"
  echo "undefined=$(grep -c undefined template.log)"
  echo "erros=$(grep -a -c '^!' template.log)"
  pdfinfo template.pdf | grep Pages
  echo FIM
} > /tmp/estado.txt
