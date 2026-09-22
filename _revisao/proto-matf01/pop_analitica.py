#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAT-F01 (prototipo) -- como se forma a populacao analitica da plataforma.

Tres paineis:
  A  cascata de filtros da particao BaselineFit, celula vetor--dia e dia civil;
  B  composicao da linha do agregado, dia a dia;
  C  um mes de eletricidade: total mensal repartido pelos dias, e o que o
     limiar de carga retem.

Contagens recalculadas das tabelas congeladas em baselines-cc/data/raw, com a
mesma precedencia de filtros da particao. Unidade CC.
"""
import os, sys, csv, collections
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Patch

def _first(paths):
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.isdir(p): return p
    raise SystemExit("caminho nao encontrado: " + str(paths))
BC   = _first(["~/LocalResearch/baselines-cc", "~/mnt/LocalResearch/baselines-cc"])
TESE = _first(["~/Desktop/Tese/novathesis", "~/mnt/novathesis"])
RAW  = os.path.join(BC, "data", "raw")

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
def guarda(ax, eixo="both"):
    ax.grid(True, axis=eixo, color="#E6E6E6", lw=0.4, zorder=0)
    ax.set_axisbelow(True)

# --------------------------------------------------------------- dados ----
UNID, THR, VGLOBAL = "CC", 18600.0, {"fuel_gas", "vapor_24bar", "vapor_10bar",
                                     "vapor_3bar", "energia_eletrica", "outros"}
MES, MES_L = "2025-04", "abril de 2025"

def num(x):
    x = (x or "").strip()
    return None if x == "" else float(x)
def ler(nome):
    with open(os.path.join(RAW, nome), encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

carga = {r["ts"]: num(r["carga_ton_d"]) for r in ler("FactCarga_Unified.tsv")
         if r["unidade_id"] == UNID}
ener = [r for r in ler("FactEnergia_Unified.tsv") if r["unidade_id"] == UNID]
CORTE = max(r["ts"] for r in ener)[:10]

def dias(rs): return len({r["ts"] for r in rs})
s = [("calendário candidato", ener)]
s.append(("energia registada",        [r for r in s[-1][1] if num(r["value_gne_d_sem_prod"]) is not None]))
s.append(("energia diferente de zero",[r for r in s[-1][1] if num(r["value_gne_d_sem_prod"]) != 0.0]))
s.append(("dia civil completo",       [r for r in s[-1][1] if r["ts"][:10] <= CORTE]))
s.append(("carga disponível",         [r for r in s[-1][1] if carga.get(r["ts"]) is not None]))
s.append(("carga $\\geq$ 18,6 kt/d",  [r for r in s[-1][1] if carga[r["ts"]] >= THR]))
etapas = [(n, len(rs), dias(rs)) for n, rs in s]

comp = collections.Counter()
for r in s[-1][1]:
    if r["vector_id"] in VGLOBAL: comp[r["ts"]] += 1
composicao = collections.Counter(comp.values())

mes = sorted([r for r in ener if r["vector_id"] == "energia_eletrica"
              and r["ts"][:7] == MES], key=lambda r: r["ts"])
vdia = num(mes[0]["value_gne_d_sem_prod"])
retido = [carga.get(r["ts"]) is not None and carga[r["ts"]] >= THR for r in mes]

# --------------------------------------------------------------- figura ---
fig = plt.figure(figsize=(15.5 * CM, 10.2 * CM))
gs = fig.add_gridspec(2, 2, width_ratios=[1.30, 1.0], height_ratios=[1.0, 1.05],
                      wspace=0.40, hspace=0.95)

# ---- A: cascata ----------------------------------------------------------
ax = fig.add_subplot(gs[:, 0])
y = np.arange(len(etapas))[::-1]
cel = [e[1] for e in etapas]
corta = [i > 0 and cel[i] < cel[i - 1] for i in range(len(cel))]
cores = [REALCE if c else NEUTRO for c in corta]
ax.barh(y, cel, color=cores, height=0.60, zorder=3)
for i, (yy, (nome, c, d)) in enumerate(zip(y, etapas)):
    ax.annotate(f"{pt(c)}  ·  {pt(d)} dias", (c, yy), xytext=(5, 1.5),
                textcoords="offset points", va="center", fontsize=7.2)
    if corta[i]:
        ax.annotate(f"−{pt(cel[i-1]-c)} células, −{pt(etapas[i-1][2]-d)} dias",
                    (c, yy), xytext=(5, -7.5), textcoords="offset points",
                    va="center", fontsize=6.3, color=ALERTA)
ax.set_yticks(y); ax.set_yticklabels([e[0] for e in etapas], fontsize=7.5)
ax.set_xlim(0, max(cel) * 1.42)
ax.set_xlabel("células vetor–dia retidas")
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(v)))
ax.tick_params(length=0)
ax.set_title("A  Cascata de seleção da plataforma", loc="left", fontsize=8.5)
guarda(ax, "x")

# ---- B: composicao do agregado ------------------------------------------
ax = fig.add_subplot(gs[0, 1])
ks = sorted(composicao, reverse=True)
vals = [composicao[k] for k in ks]
cr = [REALCE if k == max(ks) else NEUTRO for k in ks]
b = ax.bar([str(k) for k in ks], vals, color=cr, width=0.60, zorder=3)
for rect, v in zip(b, vals):
    ax.annotate(pt(v), (rect.get_x() + rect.get_width() / 2, v), xytext=(0, 2.5),
                textcoords="offset points", ha="center", fontsize=7.2)
ax.set_ylim(0, max(vals) * 1.26)
ax.set_xlabel("vetores somados no dia", labelpad=2)
ax.set_ylabel("dias")
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(v)))
ax.tick_params(length=0)
ax.set_title("B  Composição da linha do agregado", loc="left", fontsize=8.5)
fora6 = sum(vals) - composicao[max(ks)]
ax.annotate(f"em {pt(fora6)} dos {pt(sum(vals))} dias o agregado\nsoma menos de seis vetores",
            (0.985, 0.90), xycoords="axes fraction", fontsize=6.4, color=CINZA,
            ha="right", va="top", linespacing=1.35)
guarda(ax, "y")

# ---- C: um mes de eletricidade ------------------------------------------
ax = fig.add_subplot(gs[1, 1])
ret = np.array(retido)
x = np.arange(1, len(mes) + 1)
ax.bar(x[ret], [vdia] * ret.sum(), color=COR["energia_eletrica"], width=0.70, zorder=3)
ax.bar(x[~ret], [vdia] * (~ret).sum(), color="white", edgecolor=CINZA,
       hatch="////", lw=0.5, width=0.70, zorder=3)
ax.set_xlim(0.3, len(mes) + 0.7)
ax.set_ylim(0, vdia * 1.95)
ax.set_xticks([1, 5, 10, 15, 20, 25, len(mes)])
ax.set_ylabel("t GNE / dia")
ax.set_xlabel(f"dia de {MES_L}", labelpad=2)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(v)))
ax.tick_params(length=0)
ax.set_title("C  Eletricidade: um total mensal repartido", loc="left", fontsize=8.5)
ax.annotate(f"medido ao mês: {pt(vdia*len(mes), 2)} t GNE "
            f"= {pt(vdia, 2)} × {len(mes)} dias\n"
            f"retido pelo limiar: {pt(vdia*ret.sum(), 2)} t GNE "
            f"(−{pt(100*(~ret).sum()/len(mes), 1)} %)",
            (0.02, 0.97), xycoords="axes fraction", fontsize=6.4, color=CINZA,
            ha="left", va="top", linespacing=1.4)
ax.annotate(f"{(~ret).sum()} dias abaixo\ndo limiar de carga",
            xy=(float(x[~ret].mean()), vdia * 1.04), xycoords="data",
            xytext=(0.985, 0.66), textcoords="axes fraction",
            fontsize=6.3, color=CINZA, ha="right", va="center", linespacing=1.3,
            arrowprops=dict(arrowstyle="-", lw=0.5, color=CINZA,
                            shrinkA=3, shrinkB=2))
guarda(ax, "y")

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    TESE, "_revisao", "proto-matf01", "matf01_prototipo.pdf")
fig.savefig(out)
print("ok ->", out)
print("corte:", CORTE, "| etapas:", [(n, c, d) for n, c, d in etapas])
print("composicao:", dict(sorted(composicao.items(), reverse=True)))
