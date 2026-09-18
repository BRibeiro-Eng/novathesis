#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara o manual do dashboard para entrar no Apêndice D.

    python3 _gerador/manual_apendice.py

1. Converte ../manual-dashboard/Manual_Dashboard_Energia_apendice.docx (versão
   corpo, sem anexos — gerada com VERSAO=tese node build.js) em PDF, com o
   LibreOffice, para 5-Figures/apendice-D/manual-corpo.pdf.
2. Lê os marcadores do PDF e escreve 3-BackMatter/gerado/appendix-D-includepdf.tex
   com o \\includepdf e as entradas de índice (só o nível 1: capítulos e partes
   do manual), para que o índice da dissertação as liste com a página certa.

O LibreOffice é usado de propósito: é determinístico e está disponível nas duas
máquinas. Reconverter com o Word muda a paginação e invalida as entradas de
índice — se isso acontecer, correr este script outra vez.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOCX = REPO.parent / "manual-dashboard" / "Manual_Dashboard_Energia_apendice.docx"
DESTDIR = REPO / "5-Figures" / "apendice-D"
PDF = DESTDIR / "manual-corpo.pdf"
TEX = REPO / "3-BackMatter" / "gerado" / "appendix-D-includepdf.tex"

ESCAPES = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}
# Os titulos entram em \addcontentsline e nos marcadores do PDF, e o \bookmark do
# pdfpages nao aceita comando nenhum: \emph rebenta e \texorpdfstring tambem
# (testado a 2026-09-18, "Use of \bookmark doesn't match its definition", seguido
# de estouro da pilha de parametros). Por isso "dashboard" fica sem italico no
# indice. Travessoes em "--", que o TeX compoe, e nunca um em-dash cru.


def escape(txt):
    return "".join(ESCAPES.get(c, c) for c in txt)


def normaliza(titulo):
    """Titulo do manual -> entrada de indice da dissertacao.

    Tira o numero do capitulo do manual, porque a dissertacao ja numera a
    entrada (D.1, D.2, ...) e "D.1 1. Inicio" le-se mal; passa as partes de
    caixa alta para caixa normal.
    """
    if titulo.isupper() or titulo.startswith("PARTE "):
        cabeca, _, cauda = titulo.partition(" — ")
        if cauda:
            cabeca = cabeca.capitalize().replace("Parte a", "Parte A").replace("Parte b", "Parte B")
            return "%s -- %s" % (cabeca, cauda.capitalize())
    return re.sub(r"^\d+\.\s*", "", titulo)



def main():
    if not DOCX.exists():
        sys.exit("falta %s — correr 'VERSAO=tese node build.js' em manual-dashboard/_gerador" % DOCX)
    DESTDIR.mkdir(parents=True, exist_ok=True)
    TEX.parent.mkdir(parents=True, exist_ok=True)

    tmp = DESTDIR / "_tmp"
    tmp.mkdir(exist_ok=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(DOCX)],
                   check=True, capture_output=True, timeout=600)
    gerado = tmp / (DOCX.stem + ".pdf")
    shutil.move(str(gerado), str(PDF))
    shutil.rmtree(tmp, ignore_errors=True)

    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    doc = pymupdf.open(PDF)
    npag = len(doc)
    entradas = []
    for nivel, titulo, pagina in doc.get_toc():
        if nivel != 1:
            continue
        rotulo = "man:%s" % re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")[:28]
        entradas.append((pagina, escape(normaliza(titulo)).replace("\u2014", "--"), rotulo))
    doc.close()

    linhas = [
        "%% GERADO por _gerador/manual_apendice.py — não editar à mão.",
        "%% Fonte: ../manual-dashboard/Manual_Dashboard_Energia_apendice.docx",
        "%% %d páginas; %d entradas de índice." % (npag, len(entradas)),
        "\\includepdf[pages=-,scale=0.82,frame,pagecommand={\\thispagestyle{plain}},",
        "  addtotoc={",
    ]
    for i, (pag, titulo, rotulo) in enumerate(entradas):
        virgula = "," if i < len(entradas) - 1 else ""
        linhas.append("    %d,section,1,{%s},%s%s" % (pag, titulo, rotulo, virgula))
    linhas += ["  }]{5-Figures/apendice-D/manual-corpo.pdf}", ""]
    TEX.write_text("\n".join(linhas), encoding="utf-8")
    print("%s: %d páginas" % (PDF.relative_to(REPO), npag))
    print("%s: %d entradas" % (TEX.relative_to(REPO), len(entradas)))
    for pag, titulo, _ in entradas:
        print("   p.%-3d %s" % (pag, titulo))


if __name__ == "__main__":
    main()
