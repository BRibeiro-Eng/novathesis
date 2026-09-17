#!/bin/sh
# Diagnostico: reproduz o que a extensao LaTeX Workshop corre no VS Code.
cd "$HOME/Desktop/Tese/novathesis" || exit 1
export PATH=/Library/TeX/texbin:$PATH
echo "== processos de sincronizacao a correr:"
ps -Aco command | sort -u | grep -Ei 'bird|icloud|onedrive|dropbox|googledrive|nextcloud|megasync|pcloud|sync' || echo "  (nenhum obvio)"
echo
echo "== atributos da pasta (iCloud/Desktop&Documents):"
ls -l@ template.tex | head -5
echo
echo "== latexmk (receita por omissao da extensao):"
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error template.tex > /tmp/lmk.log 2>&1
echo "rc=$?"
