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

# ---------------------------------------------------------------- PROT. A --
def proto_a(p):
    """Particao 2x2 (tem racio? tem modelo ajustado?) + protocolo por familia."""
    cls, fora, quad, so_racio, linhas = tabela(p)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(15.5 * CM, 6.4 * CM),
                                 gridspec_kw={"width_ratios": [1, 1.12]})
    # --- esquerda: particao exclusiva
    part = [("Rácio ou média,\nsem modelo ajustado", quad[(True, False)], P3[3]),
            ("Modelo ajustado,\nsem rácio nem média", quad[(False, True)], P3[0]),
            ("Rácio ou média\ne modelo ajustado", quad[(True, True)], P3[2]),
            ("Nem uma coisa\nnem outra", quad[(False, False)], P3[1])]
    part.sort(key=lambda r: r[1])
    y = np.arange(len(part))
    a1.barh(y, [r[1] for r in part], color=[r[2] for r in part], height=.62,
            edgecolor="white", lw=.6, zorder=3)
    a1.barh([len(part) + .4], [fora], color=CINZA_C, height=.34, zorder=3)
    for i, r in enumerate(part):
        a1.annotate(pt(r[1]), (r[1] + 1.5, i), va="center", fontsize=7.5, color=TINTA)
    a1.annotate(pt(fora), (fora + 1.5, len(part) + .4), va="center", fontsize=7.5, color=CINZA)
    a1.set_yticks(list(y) + [len(part) + .4])
    a1.set_yticklabels([r[0] for r in part] + ["Campo por resolver\nou sem extração"], fontsize=7.2)
    a1.get_yticklabels()[-1].set_color(CINZA)
    a1.set_xlim(0, 200); a1.set_ylim(-.6, len(part) + 1.0)
    a1.set_xlabel("publicações", fontsize=7.5)
    a1.set_title("As 162 classificadas, em grupos exclusivos", loc="left", fontsize=8.5, pad=6)
    guarda(a1)
    a1.annotate("%s destas não declaram\nmais nenhuma família" % pt(so_racio),
                xy=(quad[(True, False)] * .5, [r[1] for r in part].index(quad[(True, False)])),
                xytext=(92, .35), fontsize=6.6, color=CINZA, ha="left", va="center")
    # --- direita: protocolo de M&V por familia
    y2 = np.arange(len(linhas))[::-1]
    a2.barh(y2, [r[1] for r in linhas], color="#E4EEF4", height=.62, zorder=3)
    a2.barh(y2, [r[2] for r in linhas], color=P3[0], height=.62, zorder=4)
    for yy, r in zip(y2, linhas):
        a2.annotate("%d de %d" % (r[2], r[1]), (r[1] + 1.5, yy), va="center",
                    fontsize=7, color=TINTA)
    a2.set_yticks(y2); a2.set_yticklabels([ROT[r[0]] for r in linhas], fontsize=7.2)
    a2.set_xlim(0, 92); a2.set_ylim(-.7, len(linhas) - .3)
    a2.set_xlabel("publicações que usam a família", fontsize=7.5)
    a2.set_title("Destas, quantas invocam um protocolo de M&V", loc="left", fontsize=8.5, pad=6)
    guarda(a2)
    fig.tight_layout(w_pad=1.6)
    grava(fig, "proto-A-particao-protocolo")

# ---------------------------------------------------------------- PROT. B --
def proto_b(p):
    """Mantem o ranking das familias; o segmento escuro e o que tem protocolo."""
    cls, fora, quad, so_racio, linhas = tabela(p)
    linhas = sorted(linhas, key=lambda r: r[1])
    fig, ax = plt.subplots(figsize=(13.4 * CM, 6.4 * CM))
    y = np.arange(len(linhas))
    ax.barh(y, [r[1] for r in linhas], color="#E4EEF4", height=.66,
            edgecolor="white", lw=.6, zorder=3)
    ax.barh(y, [r[2] for r in linhas], color=P3[0], height=.66, zorder=4)
    ax.barh([len(linhas) + .5], [fora], color=CINZA_C, height=.34, zorder=3)
    for i, r in enumerate(linhas):
        ax.annotate("%d  (%d com protocolo)" % (r[1], r[2]), (r[1] + 2, i),
                    va="center", fontsize=7, color=TINTA)
    ax.annotate(pt(fora), (fora + 2, len(linhas) + .5), va="center", fontsize=7, color=CINZA)
    ax.set_yticks(list(y) + [len(linhas) + .5])
    ax.set_yticklabels([ROT[r[0]] for r in linhas] + ["Campo por resolver ou sem extração"], fontsize=7.4)
    ax.get_yticklabels()[-1].set_color(CINZA)
    ax.set_xlim(0, 205); ax.set_ylim(-.7, len(linhas) + 1.1)
    ax.set_xlabel("publicações (de 331; uma publicação pode declarar mais de uma família)", fontsize=7.5)
    guarda(ax)
    fig.tight_layout()
    grava(fig, "proto-B-ranking-protocolo")

# ---------------------------------------------------------------- PROT. C --
def proto_c(p):
    """Tabela grafica: a familia e a barra; o contexto sao tres colunas."""
    cls, fora, quad, so_racio, linhas = tabela(p)
    linhas = sorted(linhas, key=lambda r: -r[1])
    fig = plt.figure(figsize=(15.5 * CM, 5.8 * CM))
    ax = fig.add_axes((.20, .17, .40, .70))
    axd = fig.add_axes((.635, .17, .345, .70))
    y = np.arange(len(linhas))[::-1]
    ax.barh(y, [r[1] for r in linhas], color=P3[0], height=.58, zorder=3)
    for yy, r in zip(y, linhas):
        ax.annotate(pt(r[1]), (r[1] + 1.6, yy), va="center", fontsize=7, color=TINTA)
    ax.set_yticks(y); ax.set_yticklabels([ROT[r[0]] for r in linhas], fontsize=7.2)
    ax.set_xlim(0, 92); ax.set_ylim(-.8, len(linhas) - .2)
    ax.set_xlabel("publicações", fontsize=7.4)
    ax.set_title("Famílias declaradas (162 classificadas; 169 por resolver)",
                 loc="left", fontsize=8.5, pad=6)
    guarda(ax)
    cols = [("Protocolo\nde M&V", 2, P3[0]), ("ISO 50006", 3, P3[2]), ("Multi-\ninstalação", 4, P3[3])]
    RMAX = .34
    for j, (tit, k, cor) in enumerate(cols):
        for yy, r in zip(y, linhas):
            frac = r[k] / float(r[1])
            axd.add_patch(plt.Circle((j, yy), RMAX * np.sqrt(max(frac, 0.0)),
                                     facecolor=cor, edgecolor="white", lw=.5, zorder=3))
            axd.annotate(str(r[k]), (j + .30, yy), va="center", ha="left",
                         fontsize=6.6, color=CINZA)
    axd.set_xlim(-.55, len(cols) - .25); axd.set_ylim(-.8, len(linhas) - .2)
    axd.set_xticks(range(len(cols))); axd.set_xticklabels([c[0] for c in cols], fontsize=7.0)
    axd.xaxis.set_ticks_position("top"); axd.xaxis.set_label_position("top")
    axd.set_yticks([]); axd.tick_params(length=0)
    for s in ("top", "right", "left", "bottom"): axd.spines[s].set_visible(False)
    axd.set_aspect("equal", adjustable="datalim")
    axd.annotate("área do círculo proporcional à fração da família;\no número é a contagem absoluta",
                 (-.5, -.72), fontsize=6.3, color=CINZA, va="center")
    grava(fig, "proto-C-tabela-grafica")

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
