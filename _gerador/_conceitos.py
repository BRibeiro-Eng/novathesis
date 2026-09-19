#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventario de conceitos para reeditar o Apendice E.

    python3 _gerador/_conceitos.py            # resumo
    python3 _gerador/_conceitos.py --detalhe  # com as ocorrencias

CORRER DEPOIS DA REVISAO INTEGRAL, nao antes: a lista e uma fotografia do que
o corpo usa, e muda com qualquer corte no texto.

Cruza tres coisas:
  1. simbolos matematicos que o corpo usa (modo matematico inline e destacado);
  2. o que o Apendice E define hoje (seccoes, rotulos, simbolos);
  3. onde o corpo remete para o apendice, e com que promessa.

Devolve, para decidir entrada a entrada:
  USADO E NAO DEFINIDO  -> o corpo usa e o apendice nao explica: candidato a entrar
  DEFINIDO E NAO USADO  -> o apendice explica e o corpo nunca usa: candidato a sair
"""
import argparse, collections, glob, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
CORPO = sorted(glob.glob(os.path.join(REPO, "2-MainMatter", "chapter-[1-8]-*.tex")))
APENDICE = os.path.join(REPO, "3-BackMatter", "appendix-E-matematica.tex")

# tokens sem conteudo proprio: aparecem em qualquer formula e nao sao conceitos
RUIDO = {"", "i", "j", "k", "n", "t", "y", "x", "e", "a", "b", "c", "d", "p", "q", "s",
         "0", "1", "2", "3", "5", "7", "10", "30", "95", "100", "\\pm", "\\times",
         "\\le", "\\ge", "\\to", "\\%", "\\,", "\\;", "\\"}


def limpa(s):
    """Tira comentarios e as caixas de revisao, que nao sao texto da tese."""
    s = re.sub(r"%+ \[REV-[0-9-]+\]\[[^\]]+\].*?%+ \[/REV-[0-9-]+\]\n", "", s, flags=re.S)
    return re.sub(r"(?<!\\)%.*", "", s)


def simbolos(texto):
    """Simbolos e comandos matematicos, por ocorrencia."""
    formulas = re.findall(r"(?<!\\)\$([^$]+)\$", texto)
    formulas += re.findall(r"\\\[(.+?)\\\]", texto, flags=re.S)
    formulas += re.findall(r"\\begin\{(?:equation|align|gather)\*?\}(.+?)\\end\{(?:equation|align|gather)\*?\}",
                           texto, flags=re.S)
    out = collections.Counter()
    for f in formulas:
        for tok in re.findall(r"\\[A-Za-z]+|[A-Za-z]+_\{?[A-Za-z0-9]+\}?|\\?[A-Za-z]", f):
            tok = tok.strip()
            if tok.lower() in RUIDO or len(tok) < 2:
                continue
            out[tok] += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detalhe", action="store_true")
    a = ap.parse_args()
    if not os.path.exists(APENDICE):
        sys.exit("apendice E nao encontrado: %s" % APENDICE)

    corpo_txt = {}
    for f in CORPO:
        corpo_txt[os.path.basename(f)] = limpa(open(f, encoding="utf-8").read())
    ap_txt = limpa(open(APENDICE, encoding="utf-8").read())

    # --- 1. onde o corpo remete para o apendice, e o que promete ---
    print("== REMISSOES DO CORPO PARA O APENDICE ==")
    for nome, t in corpo_txt.items():
        for m in re.finditer(r"[^.]*\\ref\{app:matematica\}[^.]*\.", t):
            frase = " ".join(m.group(0).split())
            print("  %-28s %s" % (nome.replace("chapter-", "").replace(".tex", ""), frase[:150]))

    # --- 2. o que o apendice tem hoje ---
    seccoes = re.findall(r"\\(?:sub)?section\{([^}]*)\}", ap_txt)
    rotulos = re.findall(r"\\label\{([^}]*)\}", ap_txt)
    citados = set()
    for t in corpo_txt.values():
        citados |= set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", t))
    orfaos = [r for r in rotulos if r not in citados]
    print("\n== APENDICE E, HOJE ==")
    print("  %d seccoes, %d rotulos, %d linhas" % (len(seccoes), len(rotulos), ap_txt.count("\n")))
    print("  rotulos que o corpo nunca cita: %d de %d" % (len(orfaos), len(rotulos)))

    # --- 3. simbolos: usados no corpo vs definidos no apendice ---
    no_corpo = collections.Counter()
    onde = collections.defaultdict(set)
    for nome, t in corpo_txt.items():
        c = simbolos(t)
        no_corpo.update(c)
        for s in c:
            onde[s].add(nome.replace("chapter-", "").split("-")[0])
    no_ap = simbolos(ap_txt)

    usados_nao_definidos = [(s, n) for s, n in no_corpo.most_common() if s not in no_ap]
    definidos_nao_usados = [(s, n) for s, n in no_ap.most_common() if s not in no_corpo]

    print("\n== USADO NO CORPO E AUSENTE DO APENDICE (candidatos a entrar) ==")
    print("  %d simbolos distintos" % len(usados_nao_definidos))
    for s, n in usados_nao_definidos[:40 if not a.detalhe else 10**6]:
        print("  %-26s %3d ocorrencias   caps. %s" % (s, n, ",".join(sorted(onde[s]))))

    print("\n== DEFINIDO NO APENDICE E AUSENTE DO CORPO (candidatos a sair) ==")
    print("  %d simbolos distintos" % len(definidos_nao_usados))
    for s, n in definidos_nao_usados[:40 if not a.detalhe else 10**6]:
        print("  %-26s %3d ocorrencias no apendice" % (s, n))

    if a.detalhe and orfaos:
        print("\n== ROTULOS DO APENDICE QUE O CORPO NUNCA CITA ==")
        for r in orfaos:
            print("  %s" % r)


if __name__ == "__main__":
    main()
