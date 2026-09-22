#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAT-F09 (prototipo, metade de apendice) -- tres bandas no mesmo eixo.

Intervalo de confianca da media, intervalo de predicao e banda de largura
constante: tres objectos que respondem a perguntas diferentes. Exemplo
construido; nenhum valor da refinaria entra nesta figura. A metade empirica
desta caixa ja existe no corpo (cap6-cobertura-bandas).
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy.stats import t as tdist, norm

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
def guarda(ax, eixo="both"):
    ax.grid(True, axis=eixo, color="#E6E6E6", lw=0.4, zorder=0)
    ax.set_axisbelow(True)

# ------------------------------------------------- amostra do exemplo ----
NEX, SIG, ALFA = 40, 1.0, 0.05
rng = np.random.default_rng(20260922)
Q = np.linspace(0.0, 10.0, NEX)
E = 2.0 + 0.8 * Q + rng.normal(0, SIG, NEX)
X = np.column_stack([np.ones(NEX), Q])
beta, *_ = np.linalg.lstsq(X, E, rcond=None)
res = E - X @ beta
s = float(np.sqrt(res @ res / (NEX - 2)))
Qb, Sqq = Q.mean(), float(((Q - Q.mean()) ** 2).sum())
tcrit = float(tdist.ppf(1 - ALFA / 2, NEX - 2))
g = np.linspace(Q.min(), Q.max(), 400)
centro = beta[0] + beta[1] * g
h = 1 / NEX + (g - Qb) ** 2 / Sqq
w_media, w_pred, w_const = tcrit * s * np.sqrt(h), tcrit * s * np.sqrt(1 + h), 2 * s

fig = plt.figure(figsize=(15.5 * CM, 9.0 * CM))
gs = fig.add_gridspec(2, 2, width_ratios=[1.28, 1.0], height_ratios=[1.0, 1.0],
                      wspace=0.36, hspace=0.72)

# ---- A: as tres bandas no mesmo eixo ------------------------------------
ax = fig.add_subplot(gs[:, 0])
ax.fill_between(g, centro - w_pred, centro + w_pred, color=REALCE, alpha=0.16,
                lw=0, zorder=2)
ax.fill_between(g, centro - w_media, centro + w_media, color=MEDIA, alpha=0.40,
                lw=0, zorder=4)
ax.plot(g, centro - w_const, color=ALERTA, lw=1.2, ls=(0, (4, 2)), zorder=5)
ax.plot(g, centro + w_const, color=ALERTA, lw=1.2, ls=(0, (4, 2)), zorder=5)
ax.plot(Q, E, "o", ms=2.8, color=TINTA, alpha=0.55, zorder=6)
ax.plot(g, centro, color=TINTA, lw=1.0, zorder=7)
ax.axvline(Qb, color=CINZA, lw=0.7, ls=(0, (1, 2)), zorder=1)
_lo, _hi = float((centro - w_pred).min()), float((centro + w_pred).max())
ax.set_ylim(_lo - 0.6, _hi + 3.0)
ax.annotate(r"$\bar Q$", (Qb, _hi + 2.8), xytext=(3, 0), textcoords="offset points",
            ha="left", va="top", fontsize=7.0, color=CINZA)
ax.set_xlabel(r"condição $Q$ (unidades arbitrárias)")
ax.set_ylabel(r"consumo $E$ (unidades arbitrárias)")
ax.tick_params(length=0)
ax.set_title("A  Três bandas, o mesmo centro", loc="left")
ax.legend(handles=[
    Patch(facecolor=MEDIA, alpha=0.40, label="intervalo da média"),
    Patch(facecolor=REALCE, alpha=0.16, label="intervalo de predição"),
    Line2D([], [], color=ALERTA, lw=1.2, ls=(0, (4, 2)), label=r"banda $\pm 2s$ da plataforma")],
    loc="upper left", frameon=False, fontsize=6.8, handlelength=1.5,
    borderpad=0.1, labelspacing=0.35)
guarda(ax)

# ---- B: semilargura em unidades de s ------------------------------------
ax = fig.add_subplot(gs[0, 1])
ax.plot(g, w_media / s, color=MEDIA, lw=1.3, zorder=4, label="intervalo da média")
ax.plot(g, w_pred / s, color=REALCE, lw=1.3, zorder=4, label="intervalo de predição")
ax.axhline(2.0, color=ALERTA, lw=1.2, ls=(0, (4, 2)), zorder=4, label=r"banda $\pm 2s$")
ax.axvline(Qb, color=CINZA, lw=0.7, ls=(0, (1, 2)), zorder=1)
ax.set_ylim(0, (w_pred / s).max() * 1.22)
ax.set_xlabel(r"condição $Q$", labelpad=1)
ax.set_ylabel("semilargura / $s$")
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(v, 1)))
ax.tick_params(length=0)
ax.set_title("B  A largura que cada banda tem", loc="left")
ax.annotate("a banda da plataforma não alarga\nquando o dia se afasta de $\\bar Q$",
            (0.5, 0.50), xycoords="axes fraction", ha="center", va="center",
            fontsize=6.4, color=CINZA, linespacing=1.35)
guarda(ax, "y")

# ---- C: cobertura da banda +-2s em funcao de n --------------------------
ax = fig.add_subplot(gs[1, 1])
ns = np.unique(np.round(np.logspace(np.log10(6), np.log10(400), 90)).astype(int))
ns = ns[ns >= 6]
cob_c = np.array([2 * tdist.cdf(2 / np.sqrt(1 + 1 / n), df=n - 2) - 1 for n in ns])
cob_e = np.array([2 * tdist.cdf(2 / np.sqrt(1 + 4 / n), df=n - 2) - 1 for n in ns])
NOM = float(2 * norm.cdf(2) - 1)
ax.axhline(NOM, color=TINTA, lw=0.9, ls=(0, (3, 2)), zorder=4)
ax.plot(ns, cob_c, color=REALCE, lw=1.3, zorder=5, label=r"em $\bar Q$")
ax.plot(ns, cob_e, color=ALERTA, lw=1.3, zorder=5, label="no extremo do treino")
ax.set_xscale("log")
ax.set_xticks([5, 10, 30, 100, 365])
ax.get_xaxis().set_major_formatter(FuncFormatter(lambda v, _: pt(v, 0)))
ax.set_ylim(0.845, 0.982)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(100 * v, 1) + " %"))
ax.set_xlabel("$n$ (observações do ajuste)", labelpad=1)
ax.set_ylabel("cobertura real")
ax.tick_params(length=0)
ax.set_title(r"C  O que a banda $\pm 2s$ cobre", loc="left")
ax.annotate(f"nominal {pt(100 * NOM, 2)} %", (6.2, NOM), xytext=(0, 3),
            textcoords="offset points", ha="left", va="bottom",
            fontsize=6.4, color=CINZA)
for n0 in (30, 365):            # mínimo declarado por vetor e um ano completo
    ax.axvline(n0, color=CINZA_C, lw=0.7, zorder=1)
# Legenda no canto inferior direito: e a unica zona do painel que fica
# vazia, porque ambas as curvas sobem para o nominal.
ax.legend(loc="lower right", frameon=False, fontsize=6.6, handlelength=1.6,
          borderpad=0.1, labelspacing=0.32)
guarda(ax, "y")

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    TESE, "_revisao", "proto-matf09", "matf09_prototipo.pdf")
fig.savefig(out)
print("ok ->", out)
for n0 in (10, 30, 100, 365):
    print(f"n={n0:4d}  centro {100*(2*tdist.cdf(2/np.sqrt(1+1/n0), df=n0-2)-1):.2f} %"
          f"  extremo {100*(2*tdist.cdf(2/np.sqrt(1+4/n0), df=n0-2)-1):.2f} %")
