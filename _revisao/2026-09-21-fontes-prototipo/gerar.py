#!/usr/bin/env python3
"""Protótipo C3-V04: fontes frequentes + percentagem acumulada.

Lê o Corpus A registado e harmoniza apenas variantes verificadas pelo ISSN
dos DOI em Crossref. Não altera as figuras ou o texto da tese.
"""
from pathlib import Path
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd


HERE = Path(__file__).resolve().parent
DATA = Path.home() / "LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables/analysis_dataset.csv"
BLUE = "#2F6D96"
SAND = "#B87932"
INK = "#1A1A1A"
MUTED = "#666666"
CM = 1 / 2.54

# Cada par foi confrontado por DOI e ISSN. Não agregamos edições anuais de
# conferências nem títulos apenas parecidos por nome.
ALIASES = {
    "sustainability (switzerland)": "Sustainability",
    "sustainability": "Sustainability",
    "applied sciences (switzerland)": "Applied Sciences",
    "applied sciences-basel": "Applied Sciences",
    "proceedings of the institution of mechanical engineers, part b: journal of engineering manufacture":
        "Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture",
    "proceedings of the institution of mechanical engineers part b-journal of engineering manufacture":
        "Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture",
}

DISPLAY = {
    "energies": "Energies",
    "journal of cleaner production": "Journal of Cleaner Production",
    "energy": "Energy",
    "energy procedia": "Energy Procedia",
    "procedia cirp": "Procedia CIRP",
    "international journal of energy economics and policy":
        "International Journal of Energy Economics and Policy",
    "energy and buildings": "Energy and Buildings",
    "energy efficiency": "Energy Efficiency",
    "applied energy": "Applied Energy",
}


def dados():
    d = pd.read_csv(DATA, encoding="utf-8-sig")
    assert len(d) == 331 and d.source.nunique() == 194
    canonical = d.source.map(lambda s: ALIASES.get(s, s))
    counts = canonical.value_counts().rename_axis("source").reset_index(name="n")
    counts = counts.sort_values(["n", "source"], ascending=[False, True]).reset_index(drop=True)
    counts.insert(0, "rank", range(1, len(counts) + 1))
    counts["cumulative_pct"] = 100 * counts.n.cumsum() / len(d)
    assert counts.n.sum() == 331 and len(counts) == 191
    return counts


def desenhar(counts):
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.titlesize": 9, "axes.labelsize": 8,
        "xtick.labelsize": 7, "ytick.labelsize": 7,
        "axes.linewidth": .6, "pdf.fonttype": 42,
    })
    frequent = counts[counts.n >= 5].copy()
    k = len(frequent)
    assert k == 11 and int(frequent.n.sum()) == 99
    share = float(counts.cumulative_pct.iloc[k-1])

    fig = plt.figure(figsize=(17.0 * CM, 9.2 * CM))
    gs = fig.add_gridspec(1, 2, left=.365, right=.965, bottom=.18,
                          top=.88, width_ratios=[1.15, .95], wspace=.52)
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    y = range(k)
    ax.barh(y, frequent.n, height=.68, color=BLUE, zorder=3)
    labels = []
    for name in frequent.source:
        display = DISPLAY.get(name, name)
        labels.append(textwrap.fill(display, width=32, break_long_words=False))
    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 28)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.set_xlabel("Publicações")
    ax.set_title("Fontes com ≥5 publicações", loc="left", pad=8)
    for yi, n in zip(y, frequent.n):
        ax.text(n + .55, yi, str(n), va="center", ha="left", fontsize=7.1, color=INK)
    ax.xaxis.grid(True, color="#E8E8E8", linewidth=.4)
    ax.set_axisbelow(True)

    ranks = [0] + counts["rank"].tolist()
    percentages = [0] + counts.cumulative_pct.tolist()
    ax2.plot(ranks, percentages, color=BLUE, lw=1.5, zorder=2)
    ax2.plot(ranks[:k+1], percentages[:k+1], color=SAND, lw=2.0, zorder=3)
    ax2.scatter([k], [share], s=25, facecolor=SAND, edgecolor="white",
                linewidth=.6, zorder=4)
    ax2.axvline(k, color="#999999", linewidth=.6, linestyle=(0, (3, 3)), zorder=1)
    ax2.axhline(share, color="#999999", linewidth=.6, linestyle=(0, (3, 3)), zorder=1)
    ax2.annotate(f"{k} fontes\n{share:.1f}%".replace(".", ","),
                 xy=(k, share), xytext=(37, 19), textcoords="data",
                 color=SAND, fontsize=7.5, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=SAND, lw=.65))
    ax2.set(xlim=(0, 195), ylim=(0, 103), xlabel="Número de fontes",
            ylabel="Publicações acumuladas (%)")
    ax2.set_xticks([0, 50, 100, 150, 191])
    ax2.set_yticks([0, 25, 50, 75, 100])
    ax2.set_title("Dispersão acumulada", loc="left", pad=8)
    ax2.text(.48, .97, "191 fontes\n142 com 1 publicação",
             transform=ax2.transAxes, fontsize=7, color=MUTED,
             ha="center", va="top")
    ax2.yaxis.grid(True, color="#E8E8E8", linewidth=.4)
    ax2.set_axisbelow(True)

    for a in (ax, ax2):
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)
        a.tick_params(length=2.5, width=.6, color=MUTED)
    ax.tick_params(axis="y", length=0)
    fig.text(.365, .055,
             "Corpus A, n=331 · Fontes harmonizadas por ISSN quando verificável · Distribuição descritiva",
             fontsize=7, color=MUTED, va="center")
    fig.savefig(HERE / "fontes_e_dispersao.pdf")
    fig.savefig(HERE / "fontes_e_dispersao.png", dpi=260)
    plt.close(fig)


if __name__ == "__main__":
    counts = dados()
    counts.to_csv(HERE / "fontes_harmonizadas.csv", index=False, float_format="%.4f")
    desenhar(counts)
    print("Gerados 2 painéis; fontes:", len(counts), "; top ≥5:",
          int(counts[counts.n >= 5].n.sum()), "/331")
