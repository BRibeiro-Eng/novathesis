#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prototipo para substituir o heatmap norma x protocolo (Figura 3.7).

O heatmap tem 24 celulas, 6 a zero e 12 com menos de cinco publicacoes; tres
celulas carregam tudo. A cor nao codifica nada que os numeros impressos nas
celulas nao digam.

A figura passa a comparar duas taxas: entre as publicacoes que invocam a
familia ISO 50001, que fraccao invoca tambem um protocolo de M&V, e a mesma
fraccao entre as que declaram nao invocar norma nenhuma. Sao praticamente
iguais -- e isso e mais forte do que o "173 de 191", porque mostra que a norma
nao traz procedimento de verificacao consigo.

Os intervalos sao de Wilson a 95%. Estao la de proposito: com 14 e 5 casos
nao se pode afirmar ausencia de diferenca, so ausencia de sinal, e o
intervalo e o que impede a figura de dizer mais do que os dados sustentam.
"""
import os, ast, sys, math
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
OUT = os.path.dirname(os.path.abspath(__file__))
CAND = ["~/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado",
        "~/mnt/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado"]
BIB = next(p for p in map(os.path.expanduser, CAND) if os.path.isdir(p))

def pct(x, casas=1):
    return ("%%.%df" % casas % x).replace(".", ",")

def lst(v):
    if v is None or (isinstance(v, float) and np.isnan(v)): return []
    t = str(v).strip()
    if t == "" or t.lower() == "nan": return []
    try:
        x = ast.literal_eval(t); return x if isinstance(x, list) else [x]
    except Exception:
        return [t]

def wilson(k, n, z=1.96):
    """Wilson a 95%. Preferido ao intervalo normal: com k=5 o normal desce
    abaixo de zero e mente sobre a assimetria."""
    if n == 0: return (0., 0., 0.)
    p = k / float(n); a = z * z / n
    c = (p + a / 2.) / (1. + a)
    h = z / (1. + a) * math.sqrt(p * (1 - p) / n + z * z / (4. * n * n))
    return p, max(0., c - h), min(1., c + h)

def dados():
    p = pd.read_csv(os.path.join(BIB, "tables", "analysis_dataset.csv"), encoding="utf-8-sig")
    def gn(v):
        x = lst(v)
        if not x: return "pend"
        if any(str(i).startswith("ISO 5000") for i in x): return "iso"
        if "none" in x: return "nenhuma"
        return "outra"
    def gp(v):
        x = lst(v)
        if not x: return "pend"
        return "com" if [i for i in x if i != "none"] else "sem"
    p["N"] = [gn(v) for v in p.ems_standard]
    p["P"] = [gp(v) for v in p.mv_protocol]
    return p

def proto():
    p = dados()
    # A norma por resolver nao entra no grafico. Nao e um grupo de
    # comparacao, e o campo em falta, e o seu intervalo vai aos 37,6 %: punha
    # as duas linhas que interessam no terco esquerdo do eixo. Vai na legenda.
    grupos = [("iso",     u"Invoca a família ISO 50001", P3[0]),
              ("nenhuma", u"Declara não invocar norma nenhuma", P3[0])]
    linhas = []
    for chave, rot, cor in grupos:
        s = p[p.N == chave]
        n = int((s.P != "pend").sum()); k = int((s.P == "com").sum())
        est, lo, hi = wilson(k, n)
        linhas.append((rot, cor, k, n, est, lo, hi, len(s)))
    fig, ax = plt.subplots(figsize=(15.5 * CM, 3.5 * CM))
    y = np.arange(len(linhas))[::-1]
    for yy, (rot, cor, k, n, est, lo, hi, tot) in zip(y, linhas):
        ax.plot([lo * 100, hi * 100], [yy, yy], color=cor, lw=1.5, alpha=.40,
                solid_capstyle="butt", zorder=3)
        for b in (lo, hi):
            ax.plot([b * 100, b * 100], [yy - .105, yy + .105], color=cor, lw=1.1,
                    alpha=.55, zorder=3)
        ax.plot([est * 100], [yy], marker="o", ms=6.2, color=cor,
                markeredgecolor="white", markeredgewidth=.9, zorder=5)
        ax.annotate(u"%s %%   (%d de %d)" % (pct(est * 100), k, n),
                    (hi * 100 + 1.0, yy), va="center", fontsize=7.2,
                    color=TINTA if cor != "#A7A7A7" else CINZA)
    ax.set_yticks(y); ax.set_yticklabels([r[0] for r in linhas], fontsize=7.8)
    ax.set_ylim(-.58, len(linhas) - .42); ax.set_xlim(0, 26)
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_xticklabels([u"0 %"] + [u"%d %%" % v for v in (5, 10, 15, 20)],
                       fontsize=7)
    ax.set_xlabel(u"publicações que invocam também um protocolo de medição e verificação",
                  fontsize=7.6, labelpad=4)
    ax.grid(True, axis="x", color="#ECECEC", lw=.45, zorder=0); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.spines["bottom"].set_bounds(0, 20)
    ax.annotate(u"ponto: proporção observada   ·   barra: intervalo de Wilson a 95 %",
                (0, 1.16), xycoords="axes fraction", fontsize=6.6, color=CINZA,
                va="bottom", ha="left")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, "proto-taxas." + ext), dpi=200)
    plt.close(fig)
    for r in linhas:
        print("%-38s %2d/%3d  %5.1f%%  [%4.1f, %4.1f]  (grupo n=%d)"
              % (r[0], r[2], r[3], r[4] * 100, r[5] * 100, r[6] * 100, r[7]))
    print("proto-taxas ok")

if __name__ == "__main__":
    proto()
