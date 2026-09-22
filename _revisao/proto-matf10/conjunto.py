#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAT-F10 (prototipo, metade de apendice) -- contagens separadas contra
sucesso conjunto na regra de quatro pares em cinco.

Exemplo construido e enumeracao exacta; nenhum valor da refinaria entra
nesta figura. A metade empirica desta caixa ja existe no corpo
(cap7-matriz-decisao).
"""
import os, sys
from itertools import product
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def _first(paths):
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.isdir(p): return p
    raise SystemExit("caminho nao encontrado: " + str(paths))
TESE = _first(["~/Desktop/Tese/novathesis", "~/mnt/novathesis"])

COR = {"fuel_gas": "#0072B2", "vapor_24bar": "#B37700",
       "vapor_10bar": "#009E73", "vapor_3bar": "#D55E00",
       "energia_eletrica": "#56B4E9"}
CINZA, CINZA_C, TINTA = "#6E6E6E", "#C8C8C8", "#1A1A1A"
REALCE, ALERTA, NEUTRO = COR["fuel_gas"], COR["vapor_3bar"], CINZA_C
MEDIA = COR["vapor_10bar"]
CM = 1 / 2.54
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix", "font.size": 8, "axes.titlesize": 8.5,
    "axes.labelsize": 8, "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5, "axes.linewidth": 0.6, "grid.linewidth": 0.4,
    "lines.linewidth": 1.1, "axes.edgecolor": "#444444", "axes.labelcolor": TINTA,
    "text.color": TINTA, "xtick.color": "#444444", "ytick.color": "#444444",
    "figure.dpi": 200, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
    "pdf.fonttype": 42, "axes.spines.top": False, "axes.spines.right": False})
def pt(x, casas=0):
    return f"{x:,.{casas}f}".replace(",", " ").replace(".", ",")

PARES = ["2020–21", "2021–22", "2022–23", "2023–24", "2024–25"]
GEX, CEX = (1, 1, 1, 1, 0), (0, 1, 1, 1, 1)
LIM = 4

fig = plt.figure(figsize=(15.5 * CM, 7.0 * CM))
gs = fig.add_gridspec(1, 2, width_ratios=[1.36, 1.0], wspace=0.30)

# ---- A: o exemplo, linha a linha ----------------------------------------
ax = fig.add_subplot(gs[0, 0])
linhas = [(r"$G_j$  ganho exclui zero", GEX, REALCE),
          (r"$C_j$  cobertura compatível", CEX, MEDIA),
          (r"$G_jC_j$  ambos no mesmo par",
           tuple(g * c for g, c in zip(GEX, CEX)), TINTA)]
for i, (rot, vec, cor) in enumerate(linhas):
    y = -i * 1.25
    for j, v in enumerate(vec):
        ax.add_patch(Rectangle((j + 0.10, y - 0.34), 0.80, 0.68,
                               facecolor=cor if v else "white",
                               edgecolor=cor if v else CINZA_C, lw=0.8, zorder=3))
        if not v:
            ax.plot([j + 0.28, j + 0.72], [y - 0.16, y + 0.16],
                    color=CINZA_C, lw=0.8, zorder=4)
            ax.plot([j + 0.28, j + 0.72], [y + 0.16, y - 0.16],
                    color=CINZA_C, lw=0.8, zorder=4)
    ax.annotate(rot, (-0.18, y), ha="right", va="center", fontsize=7.4, color=cor)
    tot = sum(vec)
    ok = tot >= LIM
    ax.annotate(rf"$\sum_j = {tot}$", (5.35, y), ha="left", va="center",
                fontsize=7.4, color=cor)
    ax.annotate(rf"$\geq {LIM}$" if ok else rf"$< {LIM}$", (6.85, y), ha="left",
                va="center", fontsize=7.4, color=REALCE if ok else ALERTA)
for j, p in enumerate(PARES):
    ax.annotate(p, (j + 0.5, 0.52), ha="center", va="bottom", fontsize=6.6,
                color=CINZA, rotation=30)
ax.annotate("a regra histórica exige as duas primeiras\n"
            "somas em separado, e aqui cumpre-se",
            (-4.20, -3.25), ha="left", va="top", fontsize=6.5, color=CINZA,
            linespacing=1.4)
ax.set_xlim(-4.30, 8.00); ax.set_ylim(-3.95, 1.35)
ax.set_xticks([]); ax.set_yticks([]); ax.tick_params(length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_title("A  Um exemplo com cinco pares anuais", loc="left")

# ---- B: enumeracao exacta -----------------------------------------------
adm = [v for v in product([0, 1], repeat=5) if sum(v) >= LIM]
adm.sort(key=lambda v: (-sum(v), v))
M = np.array([[1 if sum(g * c for g, c in zip(G, C)) >= LIM else 0
               for C in adm] for G in adm])
ax = fig.add_subplot(gs[0, 1])
for i in range(len(adm)):
    for j in range(len(adm)):
        ax.add_patch(Rectangle((j + 0.06, i + 0.06), 0.88, 0.88,
                               facecolor=REALCE if M[i, j] else NEUTRO,
                               edgecolor="white", lw=0.6, zorder=3))
iG, iC = adm.index(GEX), adm.index(CEX)
ax.add_patch(Rectangle((iC + 0.06, iG + 0.06), 0.88, 0.88, facecolor="none",
                       edgecolor=ALERTA, lw=1.4, zorder=5))
# A moldura assinala o exemplo do painel A; a legenda di-lo, para nao
# atravessar a matriz com uma linha de chamada.
rot = ["".join(str(x) for x in v) for v in adm]
ax.set_xticks(np.arange(len(adm)) + 0.5); ax.set_xticklabels(rot, fontsize=6.4, rotation=90)
ax.set_yticks(np.arange(len(adm)) + 0.5); ax.set_yticklabels(rot, fontsize=6.4)
ax.set_xlim(0, len(adm)); ax.set_ylim(len(adm) + 0.2, -0.2)
ax.set_xlabel(r"vetor de cobertura $C$", labelpad=2)
ax.set_ylabel(r"vetor de ganho $G$")
ax.tick_params(length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_title("B  Todas as configurações que passam a regra", loc="left")
n_ok, n_tot = int(M.sum()), M.size
ax.annotate(f"{n_tot - n_ok} das {n_tot} ({pt(100 * (n_tot - n_ok) / n_tot)} %) não têm\n"
            "quatro sucessos conjuntos",
            (0.02, -0.265), xycoords="axes fraction", ha="left", va="top",
            fontsize=6.4, color=CINZA, linespacing=1.4, annotation_clip=False)

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    TESE, "_revisao", "proto-matf10", "matf10_prototipo.pdf")
fig.savefig(out)
print("ok ->", out)
print("admissiveis:", len(adm), "| pares:", n_tot, "| conjunto>=4:", n_ok,
      "| falham:", n_tot - n_ok)
