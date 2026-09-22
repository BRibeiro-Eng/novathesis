#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAT-F07 (prototipo) -- o bootstrap de blocos moveis no calendario civil.

Figura de apendice: explica o mecanismo, nao apresenta resultados. Todos os
numeros sao sinteticos. O painel C corre um MBB sobre uma serie AR(1) gerada
com semente fixa; nao ha um unico valor da refinaria nesta figura.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

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
# Papéis não-vetoriais. As figuras de vetores usam COR[vector]; esta figura não
# é sobre vetores, por isso nomeia o papel e não o vetor. Mesmos hexes.
REALCE, ALERTA, NEUTRO = COR["fuel_gas"], COR["vapor_3bar"], CINZA_C

def pt(x, casas=0):
    return f"{x:,.{casas}f}".replace(",", " ").replace(".", ",")

# ------------------------------------------------- calendário do exemplo --
T0, T1, ELL = 1, 22, 5
FALTA = {10, 11, 12, 13}
OBS = [t for t in range(T0, T1 + 1) if t not in FALTA]
N = len(OBS)
def bloco(s): return [t for t in OBS if s <= t < s + ELL]
DESTAQUE = [2, 9, 14]
SEQ = [2, 9, 14, 6, 17]          # sorteio ilustrativo, fixado à mão

fig = plt.figure(figsize=(15.5 * CM, 8.4 * CM))
gs = fig.add_gridspec(2, 2, width_ratios=[1.50, 1.0], height_ratios=[1.12, 1.0],
                      wspace=0.30, hspace=0.75)

# ---- A: blocos candidatos no calendário ---------------------------------
ax = fig.add_subplot(gs[0, 0])
for t in range(T0, T1 + 1):
    if t in FALTA:
        ax.plot(t, 0, marker="o", ms=4.6, mfc="white", mec=CINZA, mew=0.8, zorder=4)
        ax.plot(t, 0, marker="x", ms=3.0, color=CINZA, mew=0.8, zorder=5)
    else:
        ax.plot(t, 0, marker="o", ms=4.6, color=TINTA, zorder=4)
for k, s in enumerate(DESTAQUE):
    b = bloco(s)
    yy = -(k + 1) * 0.92
    cor = ALERTA if len(b) < ELL else REALCE
    ax.add_patch(plt.Rectangle((s - 0.42, yy - 0.26), ELL - 0.16, 0.52,
                               facecolor=cor, alpha=0.16, edgecolor=cor, lw=0.7, zorder=2))
    for t in b:
        ax.plot(t, yy, marker="o", ms=4.0, color=cor, zorder=4)
    ax.annotate(f"$\\mathcal{{B}}_{{{s}}}$", (s - 0.62, yy), ha="right", va="center",
                fontsize=7.4, color=cor)
    ax.annotate(f"$|\\mathcal{{B}}_{{{s}}}|={len(b)}$", (s + ELL - 0.6, yy),
                xytext=(6, 0), textcoords="offset points", ha="left", va="center",
                fontsize=7.0, color=cor)
ax.annotate("dias sem registo", (11.5, 0.18), xytext=(0, 9), textcoords="offset points",
            ha="center", va="bottom", fontsize=6.5, color=CINZA,
            arrowprops=dict(arrowstyle="-", lw=0.5, color=CINZA, shrinkA=1, shrinkB=3))
ax.set_xlim(T0 - 2.6, T1 + 2.2); ax.set_ylim(-3.55, 1.45)
ax.set_xticks([T0, 5, 10, 15, 20, T1])
ax.set_yticks([]); ax.tick_params(length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_xlabel("dia civil", labelpad=1)
ax.set_title(f"A  Blocos candidatos no calendário  ($\\ell={ELL}$, $n={N}$)",
             loc="left", fontsize=8.5)

# ---- B: concatenação de uma réplica -------------------------------------
ax = fig.add_subplot(gs[1, 0])
pos, juntas = 0, []
for s in SEQ:
    b = bloco(s)
    cor = ALERTA if len(b) < ELL else REALCE
    for j, _ in enumerate(b):
        x = pos + j
        dentro = x < N
        ax.add_patch(plt.Rectangle((x + 0.08, 0.08), 0.84, 0.84,
                                   facecolor=cor if dentro else "white",
                                   edgecolor=cor, lw=0.7,
                                   alpha=1.0 if dentro else 1.0,
                                   hatch=None if dentro else "////", zorder=3))
    ax.annotate(f"$\\mathcal{{B}}_{{{s}}}$", (pos + len(b) / 2, 1.08),
                ha="center", va="bottom", fontsize=6.8, color=cor)
    pos += len(b)
    if pos < 22: juntas.append(pos)
for j in juntas[:-1]:
    ax.plot([j, j], [-0.06, 1.06], color=TINTA, lw=0.8, zorder=5)
ax.plot([N, N], [-0.42, 1.00], color=CINZA, lw=0.8, ls=(0, (3, 2)), zorder=5)
ax.annotate(f"trunca em $n={N}$", (N, -0.42), xytext=(4, 0), textcoords="offset points",
            ha="left", va="bottom", fontsize=6.5, color=CINZA)
ax.annotate("as junções são artificiais", (0, -0.42), xytext=(0, 0),
            textcoords="offset points", ha="left", va="bottom", fontsize=6.5, color=CINZA)
ax.set_xlim(-0.6, pos + 0.6); ax.set_ylim(-0.95, 1.75)
ax.set_xticks([]); ax.set_yticks([]); ax.tick_params(length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_title("B  Uma réplica: sortear, concatenar, truncar", loc="left", fontsize=8.5)

# ---- C: largura do intervalo em função de ell ---------------------------
# Media sobre M series AR(1) independentes: uma so realizacao da uma curva
# ruidosa e o mecanismo -- a largura cresce com l e estabiliza -- deixa de
# se ler. Nada aqui vem da refinaria.
rng = np.random.default_rng(20260922)
NS, RHO, B, M = 240, 0.6, 800, 120
ells = np.arange(1, 21)
larg = np.zeros(len(ells))
for _ in range(M):
    e = np.empty(NS); e[0] = rng.normal()
    for t in range(1, NS):
        e[t] = RHO * e[t - 1] + np.sqrt(1 - RHO**2) * rng.normal()
    for i, L in enumerate(ells):
        starts = rng.integers(0, NS - L + 1, size=(B, int(np.ceil(NS / L))))
        idx = (starts[:, :, None] + np.arange(L)[None, None, :]).reshape(B, -1)[:, :NS]
        q = np.quantile(e[idx].mean(axis=1), [0.025, 0.975])
        larg[i] += q[1] - q[0]
larg /= M
ESTIM = 0.0
ax = fig.add_subplot(gs[:, 1])
ax.fill_between(ells, ESTIM - larg / 2, ESTIM + larg / 2, color=REALCE,
                alpha=0.20, lw=0, zorder=2)
ax.plot(ells, ESTIM - larg / 2, color=REALCE, lw=1.1, zorder=3)
ax.plot(ells, ESTIM + larg / 2, color=REALCE, lw=1.1, zorder=3)
ax.plot(ells, ESTIM - larg / 2, "o", ms=2.2, color=REALCE, zorder=4)
ax.plot(ells, ESTIM + larg / 2, "o", ms=2.2, color=REALCE, zorder=4)
ax.axhline(ESTIM, color=TINTA, lw=0.9, ls=(0, (3, 2)), zorder=4)
L0 = int(np.ceil(NS ** (1 / 3)))
ax.axvline(L0, color=CINZA, lw=0.7, ls=(0, (1, 2)), zorder=2)
top = larg.max() / 2 * 1.42
ax.set_ylim(-top, top); ax.set_xlim(0.4, 20.6)
ax.annotate(f"$\\ell_0=\\lceil n^{{1/3}}\\rceil={L0}$", (L0, top), xytext=(4, -3),
            textcoords="offset points", ha="left", va="top", fontsize=6.5, color=CINZA)
ax.annotate("a estimativa pontual não se move", (20.4, ESTIM), xytext=(0, 3),
            textcoords="offset points", ha="right", va="bottom", fontsize=6.5, color=CINZA)
ax.annotate(f"em $\\ell=1$ o bootstrap ignora a dependência\ne o intervalo sai {pt(100*(1-larg[0]/larg[L0-1]), 0)} % mais estreito que em $\\ell_0$",
            (1.15, -larg[0] / 2), xytext=(0.03, 0.045), textcoords="axes fraction",
            ha="left", va="bottom", fontsize=6.5, color=CINZA, linespacing=1.35)
ax.set_xlabel("comprimento do bloco $\\ell$ (dias civis)")
ax.set_ylabel("intervalo de percentil a 95 %, centrado")
ax.set_xticks([1, 5, 10, 15, 20])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(v, 2)))
ax.tick_params(length=0)
ax.grid(True, axis="y", color="#E6E6E6", lw=0.4, zorder=0); ax.set_axisbelow(True)
ax.set_title("C  Sensibilidade à dependência", loc="left", fontsize=8.5)

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    TESE, "_revisao", "proto-matf07", "matf07_prototipo.pdf")
fig.savefig(out)
print("ok ->", out)
print("blocos:", [(s2, len(bloco(s2))) for s2 in DESTAQUE], "| n =", N)
print("replica:", [(s2, len(bloco(s2))) for s2 in SEQ], "total", sum(len(bloco(s2)) for s2 in SEQ))
print("larguras: l=1", round(larg[0], 4), "| l0", round(larg[L0-1], 4),
      "| l=20", round(larg[-1], 4))
