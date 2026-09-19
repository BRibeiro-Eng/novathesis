#!/bin/sh
# Compilacao incremental para o VS Code (2026-09-18).
#
# Porque existe este wrapper em vez de se chamar o latexmk directamente na
# receita do LaTeX Workshop: a receita nua nao garante duas coisas.
#
#  1. PATH. Uma aplicacao aberta pelo Dock ou pelo Finder herda o PATH do
#     launchd -- /usr/bin:/bin:/usr/sbin:/sbin -- que NAO inclui
#     /Library/TeX/texbin. Para essa instancia do VS Code o latexmk nao
#     existe e a compilacao falha antes de comecar. Aberto por "code" a
#     partir do terminal, o mesmo VS Code ja o encontra: e por isso que o
#     problema aparece e desaparece sem nada mudar no documento.
#
#  2. A pasta de auxiliares. O macOS limpa /tmp no arranque, e a receita nua
#     nao a recria.
#
# O build.sh ja fazia as duas coisas; era so por isso que funcionava sempre.
cd "$HOME/Desktop/Tese/novathesis" || exit 1
export PATH=/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:$PATH
#  3. Pasta de saida PROPRIA (2026-09-19). O build.sh usa /tmp/tese-build.
#     Enquanto os dois partilharam a mesma pasta, uma compilacao no VS Code
#     ao mesmo tempo que uma compilacao pelo build.sh punha dois pdflatex a
#     escrever o mesmo template.aux: o resultado era centenas de referencias
#     por resolver e um PDF com menos paginas, sem um unico erro no log.
#     Pastas separadas tornam isso impossivel.

OUT=/tmp/tese-build-code
mkdir -p "$OUT"
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -outdir="$OUT" template.tex
STATUS=$?
# copia atomica: os dois compiladores escrevem o mesmo template.pdf na raiz
cp "$OUT/template.pdf" template.pdf.tmp 2>/dev/null && mv -f template.pdf.tmp template.pdf
exit $STATUS
