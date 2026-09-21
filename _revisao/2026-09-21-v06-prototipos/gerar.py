#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prototipos para substituir a Figura 3.7 (familias de modelos).

A figura actual e um ranking de dez categorias cujo ranking ja esta escrito
por extenso na primeira frase da subseccao, e nao mostra a distincao que a
subseccao argumenta (racio vs modelo ajustado). Estes tres prototipos atacam
isso de maneiras diferentes. Numeros calculados do analysis_dataset.csv.
"""
import os, ast, sys, collections, itertools
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

CM = 1 / 2.54
TINTA, CINZA, CINZA_C = "#1A1A1A", "#6E6E6E", "#CFCFCF"
P3 = ["#278CB1", "#65B9E7", "#6FAC74", "#AF6F43"]
CORPO, CORPO_C = "#456B80", "#CFDCE4"   # corpo: um so azul, dois passos
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix", "font.size": 8, "axes.titlesize": 8.5,
    "axes.edgecolor": "#B0B0B0", "axes.linewidth": .6,
    "xtick.color": CINZA, "ytick.color": CINZA, "text.color": TINTA,
    "axes.labelcolor": TINTA, "savefig.bbox": "tight", "savefig.pad_inches": .02,
    "pdf.fonttype": 42})

BASE = os.path.expanduser(
    "~/Desktop/Tese/novathesis") if os.path.isdir(os.path.expanduser("~/Desktop/Tese/novathesis")) else None
CAND = ["~/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado",
        "~/mnt/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado"]
BIB = next(p for p in map(os.path.expanduser, CAND) if os.path.isdir(p))
OUT = os.path.dirname(os.path.abspath(__file__))

def pt(x):
    return f"{x:,.0f}".replace(",", " ")

def lst(v):
    if v is None or (isinstance(v, float) and np.isnan(v)): return []
    t = str(v).strip()
    if t == "" or t.lower() == "nan": return []
    try:
        x = ast.literal_eval(t); return x if isinstance(x, list) else [x]
    except Exception:
        return [t]

def dados():
    p = pd.read_csv(os.path.join(BIB, "tables", "analysis_dataset.csv"), encoding="utf-8-sig")
    p["fam"] = [lst(v) for v in p["enpi_enb_model_types"]]
    p["prot"] = [lst(v) for v in p["mv_protocol"]]
    p["norm"] = [lst(v) for v in p["ems_standard"]]
    p["ms"] = [lst(v) for v in p["multi_site"]]
    return p

RACIO = {"simple intensity ratio", "SEC mean"}
AJUST = {"linear regression", "multiple regression"}
ROT = {"simple intensity ratio": "Rácio de intensidade", "linear regression": "Regressão linear",
       "multiple regression": "Regressão múltipla", "physical model": "Modelo físico",
       "change-point or SPC": "Ponto de mudança ou CEP", "ML": "Aprendizagem automática",
       "SEC mean": "Média do consumo específico", "other": "Outra",
       "composite index": "Índice composto", "process integration": "Integração de processo"}
ORDEM = ["simple intensity ratio", "linear regression", "multiple regression", "physical model",
         "change-point or SPC", "ML", "SEC mean", "other"]

def tabela(p):
    cls = p[p.fam.map(len) > 0]
    fora = len(p) - len(cls)
    quad = collections.Counter()
    for f in cls.fam:
        quad[(bool(set(f) & RACIO), bool(set(f) & AJUST))] += 1
    so_racio = sum(1 for f in cls.fam if set(f) <= RACIO)
    linhas = []
    for f in ORDEM:
        sub = cls[cls.fam.map(lambda x: f in x)]
        prot = int(sub.prot.map(lambda r: any(x != "none" for x in r)).sum())
        iso6 = int(sub.norm.map(lambda r: "ISO 50006" in r).sum())
        msit = int(sub.ms.map(lambda r: True in r).sum())
        linhas.append((f, len(sub), prot, iso6, msit))
    return cls, fora, quad, so_racio, linhas

def grava(fig, nome):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, nome + "." + ext), dpi=200)
    plt.close(fig); print(nome, "ok")

def guarda(ax):
    ax.grid(True, axis="x", color="#E9E9E9", lw=.4, zorder=0); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)

# ------------------------------------------------------------- faixa comum --
def faixa(fig, rect, quad, fora, so_racio, n=331):
    """Faixa do denominador: as 331 numa so barra, particionada.

    A primeira versao punha as 169 por resolver no mesmo eixo de contagem das
    barras das familias, e o resultado era que as quatro barras reais ocupavam
    um quarto do eixo. A faixa mostra a ausencia a escala -- a convencao do
    capitulo -- sem custar escala ao resto da figura. A particao e um 2x2
    exclusivo: tem racio ou media? tem modelo ajustado?
    """
    ax = fig.add_axes(rect)
    segs = [(u"R\u00e1cio ou m\u00e9dia, sem\nmodelo ajustado", quad[(True, False)],  P3[3]),
            (u"R\u00e1cio ou m\u00e9dia e\nmodelo ajustado",    quad[(True, True)],   P3[2]),
            (u"Modelo ajustado,\nsem r\u00e1cio", quad[(False, True)],  P3[0]),
            (u"Nem r\u00e1cio nem\nmodelo ajustado",        quad[(False, False)], P3[1]),
            (u"Campo por resolver\nou sem extra\u00e7\u00e3o",   fora,                CINZA_C)]
    x = 0
    for rot, v, cor in segs:
        ax.add_patch(Rectangle((x, 0), v, 1, facecolor=cor, edgecolor="white", lw=.9))
        ax.text(x + v / 2., .5, pt(v), ha="center", va="center", fontsize=7.6,
                color="white" if cor != CINZA_C else TINTA)
        ax.annotate(rot, (x + v / 2., -.42), ha="center", va="top", fontsize=6.0,
                    color=TINTA if cor != CINZA_C else CINZA, linespacing=1.3,
                    annotation_clip=False)
        x += v
    assert x == n, x
    ax.set_xlim(0, n); ax.set_ylim(0, 1); ax.axis("off")
    ax.annotate(u"As 331 publica\u00e7\u00f5es do Corpus A, pelo modelo que declaram",
                (0, 1.55), fontsize=8.2, color=TINTA, va="bottom", annotation_clip=False)
    ax.annotate(u"%s destas n\u00e3o declaram mais nenhuma fam\u00edlia"
                % pt(so_racio), (quad[(True, False)] / 2., -1.78), ha="center",
                va="top", fontsize=6.0, color=CINZA, annotation_clip=False)
    return ax

def linhas_familia(ax, linhas, protocolo=True):
    linhas = sorted(linhas, key=lambda r: r[1])
    y = np.arange(len(linhas))
    if protocolo:
        ax.barh(y, [r[1] for r in linhas], color=CORPO_C, height=.66, zorder=3)
        ax.barh(y, [r[2] for r in linhas], color=CORPO, height=.66, zorder=4)
        for i, r in enumerate(linhas):
            ax.annotate(u"%d   %d com protocolo" % (r[1], r[2]), (r[1] + 1.6, i),
                        va="center", fontsize=6.9, color=TINTA)
    else:
        ax.barh(y, [r[1] for r in linhas], color=CORPO, height=.66, zorder=3)
        for i, r in enumerate(linhas):
            ax.annotate(pt(r[1]), (r[1] + 1.6, i), va="center", fontsize=7, color=TINTA)
    ax.set_yticks(y); ax.set_yticklabels([ROT[r[0]] for r in linhas], fontsize=7.3)
    ax.set_xlim(0, 96); ax.set_ylim(-.65, len(linhas) - .35)
    guarda(ax)
    return linhas

# ---------------------------------------------------------------- PROT. A --
def proto_a(p):
    """Faixa da particao + familias com o segmento do protocolo de M&V."""
    cls, fora, quad, so_racio, linhas = tabela(p)
    fig = plt.figure(figsize=(15.5 * CM, 7.6 * CM))
    faixa(fig, (.055, .855, .93, .050), quad, fora, so_racio)
    ax = fig.add_axes((.215, .105, .655, .560))
    linhas_familia(ax, linhas, protocolo=True)
    ax.set_xlabel(u"publica\u00e7\u00f5es que declaram a fam\u00edlia (as categorias n\u00e3o s\u00e3o exclusivas)",
                  fontsize=7.3)
    ax.annotate(u"Fam\u00edlias declaradas pelas 162 classificadas; a parte escura \u00e9 a que invoca um protocolo de M&V",
                (0, 1.035), xycoords="axes fraction", fontsize=8.0, color=TINTA, va="bottom")
    grava(fig, "proto-A-faixa-protocolo")

# ---------------------------------------------------------------- PROT. B --
def proto_b(p):
    """Conservador: faixa da particao + o ranking actual, sem mais nada."""
    cls, fora, quad, so_racio, linhas = tabela(p)
    fig = plt.figure(figsize=(15.5 * CM, 7.2 * CM))
    faixa(fig, (.055, .855, .93, .050), quad, fora, so_racio)
    ax = fig.add_axes((.215, .11, .655, .585))
    linhas_familia(ax, linhas, protocolo=False)
    ax.set_xlabel(u"publica\u00e7\u00f5es que declaram a fam\u00edlia (as categorias n\u00e3o s\u00e3o exclusivas)",
                  fontsize=7.3)
    ax.annotate(u"Fam\u00edlias declaradas pelas 162 classificadas",
                (0, 1.035), xycoords="axes fraction", fontsize=8.0, color=TINTA, va="bottom")
    grava(fig, "proto-B-faixa-ranking")

# ---------------------------------------------------------------- PROT. C --
def proto_c(p):
    """Denso: faixa + familias + tres colunas de contexto, em comprimento.

    Circulos proporcionais a area foram tentados e rejeitados: para contagens
    de 0 a 13 a area discrimina pior do que o comprimento e os dois valores
    baixos ficavam indistinguiveis do zero.
    """
    cls, fora, quad, so_racio, linhas = tabela(p)
    fig = plt.figure(figsize=(15.5 * CM, 8.0 * CM))
    faixa(fig, (.055, .860, .93, .048), quad, fora, so_racio)
    ax = fig.add_axes((.185, .145, .385, .545))
    linhas = linhas_familia(ax, linhas, protocolo=False)
    ax.set_xlabel(u"publica\u00e7\u00f5es", fontsize=7.3)
    ax.annotate(u"Fam\u00edlias declaradas", (0, 1.035), xycoords="axes fraction",
                fontsize=8.0, color=TINTA, va="bottom")
    cols = [(u"Protocolo\nde M&V", 2, CORPO), (u"ISO\n50006", 3, CORPO),
            (u"Multi-\ninstala\u00e7\u00e3o", 4, CORPO)]
    L, W, GAP = .625, .108, .015
    y = np.arange(len(linhas))
    for j, (tit, k, cor) in enumerate(cols):
        a = fig.add_axes((L + j * (W + GAP), .145, W, .545))
        a.barh(y, [r[k] for r in linhas], color=cor, height=.66, zorder=3)
        for i, r in enumerate(linhas):
            a.annotate(str(r[k]), (r[k] + .45, i), va="center", fontsize=6.6, color=TINTA)
        a.set_xlim(0, 16); a.set_ylim(-.65, len(linhas) - .35)
        a.set_yticks([]); a.set_xticks([0, 5, 10])
        a.tick_params(labelsize=6.2, length=0)
        a.grid(True, axis="x", color="#E9E9E9", lw=.4, zorder=0); a.set_axisbelow(True)
        for s in ("top", "right", "left"): a.spines[s].set_visible(False)
        a.annotate(tit, (0, 1.045), xycoords="axes fraction", fontsize=7.2,
                   color=TINTA, va="bottom", linespacing=1.25)
    fig.text(.625, .022, u"contagens sobre o total de cada fam\u00edlia,\n"
             u"\u00e0 esquerda; n\u00fameros pequenos e descritivos",
             fontsize=6.2, color=CINZA, linespacing=1.3)
    grava(fig, "proto-C-faixa-contexto")

if __name__ == "__main__":
    p = dados()
    cls, fora, quad, so_racio, linhas = tabela(p)
    print("classificadas", len(cls), "| por resolver", fora, "| so racio/media", so_racio)
    print("quadrantes", dict(quad))
    for r in linhas: print("   ", r)
    alvo = sys.argv[1:] or ["a", "b", "c"]
    if "a" in alvo: proto_a(p)
    if "b" in alvo: proto_b(p)
    if "c" in alvo: proto_c(p)
