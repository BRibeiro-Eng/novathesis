#!/bin/sh
# Build da tese (2026-09-17). Os ficheiros intermedios vao para /tmp/tese-build:
# a pasta da tese esta no Desktop, que e sincronizado, e a sincronizacao apagava
# ou trancava .bcf/.bbl/.pdf a meio das passagens. So o PDF final volta ca.
cd "$HOME/Desktop/Tese/novathesis" || exit 1
export PATH=/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:$PATH
OUT=/tmp/tese-build
mkdir -p "$OUT"
rm -f /tmp/estado.txt
P="pdflatex -interaction=nonstopmode -file-line-error -synctex=1 -output-directory=$OUT"
$P template > /tmp/b1.log 2>&1
biber --input-directory "$OUT" --output-directory "$OUT" template > /tmp/b_biber.log 2>&1
MI="makeindex -s $OUT/template.ist"
$MI -t "$OUT/template.glg" -o "$OUT/template.gls" "$OUT/template.glo" > /dev/null 2>&1
$MI -t "$OUT/template.alg" -o "$OUT/template.acr" "$OUT/template.acn" > /dev/null 2>&1
$MI -t "$OUT/template.slg" -o "$OUT/template.sls" "$OUT/template.slo" > /dev/null 2>&1
$P template > /tmp/b2.log 2>&1
$MI -t "$OUT/template.glg" -o "$OUT/template.gls" "$OUT/template.glo" > /dev/null 2>&1
$MI -t "$OUT/template.alg" -o "$OUT/template.acr" "$OUT/template.acn" > /dev/null 2>&1
$MI -t "$OUT/template.slg" -o "$OUT/template.sls" "$OUT/template.slo" > /dev/null 2>&1
$P template > /tmp/b3.log 2>&1
$P template > /tmp/b4.log 2>&1
cp "$OUT/template.pdf" template.pdf 2>/dev/null
{
  echo "undefined=$(grep -c undefined $OUT/template.log)"
  echo "erros=$(grep -a -c '^\!' $OUT/template.log)"
  echo "paginas=$(pdfinfo $OUT/template.pdf | awk '/Pages/{print $2}')"
  echo "bbl=$(wc -c < $OUT/template.bbl)"
  echo FIM
} > /tmp/estado.txt
