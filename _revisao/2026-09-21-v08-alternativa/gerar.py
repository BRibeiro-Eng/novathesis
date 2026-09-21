#!/usr/bin/env python3
"""Alternativa à Figura 3.7: composição do protocolo por grupo de norma."""

from collections import Counter, defaultdict
from pathlib import Path
import ast

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


HERE = Path(__file__).resolve().parent
DATA = (Path.home() / "LocalResearch/Screening/level3_extraction/"
        "bibliometrics/results/corpus_a_registado/tables/analysis_dataset.csv")
CM = 1 / 2.54
NONE = "#A9CBDD"
NAMED = "#B87932"
UNKNOWN = "#CFCFCF"
INK = "#1A1A1A"
MUTED = "#666666"


def as_list(value):
    if pd.isna(value):
        return []
    parsed = ast.literal_eval(value)
    return parsed if isinstance(parsed, list) else [parsed]


def counts():
    papers = pd.read_csv(DATA, encoding="utf-8-sig")
    assert len(papers) == 331
    cells = defaultdict(Counter)
    for row in papers.itertuples():
        norms = as_list(row.ems_standard)
        protocols = as_list(row.mv_protocol)
        if not norms:
            norm_group = "Norma por resolver"
        elif any(str(item).startswith("ISO 5000") for item in norms):
            norm_group = "Família ISO 50001"
        elif "none" in norms:
            norm_group = "Nenhuma norma"
        else:
            norm_group = "Outra norma"
        if not protocols:
            protocol_group = "Por resolver"
        elif any(item != "none" for item in protocols):
            protocol_group = "Pelo menos um nomeado"
        else:
            protocol_group = "Nenhum nomeado"
        # Uma publicação conta UMA vez, mesmo que nomeie vários protocolos.
        cells[norm_group][protocol_group] += 1
    assert sum(sum(row.values()) for row in cells.values()) == 331
    assert cells["Família ISO 50001"] == {
        "Nenhum nomeado": 173, "Pelo menos um nomeado": 14, "Por resolver": 4}
    assert cells["Nenhuma norma"] == {
        "Nenhum nomeado": 59, "Pelo menos um nomeado": 5, "Por resolver": 2}
    assert sum(cells["Norma por resolver"].values()) == 73
    assert sum(cells["Outra norma"].values()) == 1
    return cells


def draw():
    cells = counts()
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7.5,
        "ytick.labelsize": 8, "axes.linewidth": .6, "pdf.fonttype": 42,
    })
    fig = plt.figure(figsize=(15.5 * CM, 6.2 * CM))
    ax = fig.add_axes((.245, .36, .55, .42))
    groups = ["Família ISO 50001", "Nenhuma norma"]
    states = [("Nenhum nomeado", NONE),
              ("Pelo menos um nomeado", NAMED),
              ("Por resolver", UNKNOWN)]
    for y, group in zip([1, 0], groups):
        n = sum(cells[group].values())
        left = 0.
        for state, color in states:
            value = cells[group][state]
            width = value / n * 100
            ax.barh(y, width, left=left, height=.53, color=color,
                    edgecolor="white", linewidth=.8)
            left += width
        ax.text(35, y, f"{cells[group]['Nenhum nomeado']}/{n} sem protocolo nomeado",
                ha="center", va="center", fontsize=7.7, color=INK)
    ax.set(xlim=(0, 100), ylim=(-.55, 1.55))
    ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_yticks([1, 0], ["Família ISO 50001 (n=191)",
                             "Nenhuma norma (n=66)"])
    ax.xaxis.grid(True, color="#E8E8E8", linewidth=.45)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0, pad=7)
    ax.tick_params(axis="x", length=2.5, width=.6, color=MUTED)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    fig.text(.245, .91, "Protocolo de M&V invocado segundo a norma declarada",
             fontsize=9, color=INK, ha="left", va="center")
    fig.text(.825, .69, "14/191  (7,3%)", fontsize=9, color=NAMED,
             ha="left", va="center")
    fig.text(.825, .60, "nomeiam protocolo", fontsize=7.5, color=MUTED,
             ha="left", va="center")
    fig.text(.825, .48, "5/66  (7,6%)", fontsize=9, color=NAMED,
             ha="left", va="center")
    fig.text(.825, .39, "nomeiam protocolo", fontsize=7.5, color=MUTED,
             ha="left", va="center")

    from matplotlib.patches import Patch
    legend = [Patch(facecolor=color, label=state)
              for state, color in states]
    fig.legend(handles=legend, loc="lower center", bbox_to_anchor=(.51, .16),
               frameon=False, ncol=3, fontsize=7.1,
               handlelength=1.3, columnspacing=1.7)
    fig.text(.245, .065,
             "Contagem por publicação. Fora da comparação: 73 com norma por resolver e 1 com outra norma.",
             fontsize=7, color=MUTED, ha="left", va="center")
    fig.savefig(HERE / "fig37_barras_condicionais.pdf", bbox_inches="tight", pad_inches=.03)
    fig.savefig(HERE / "fig37_barras_condicionais.png", dpi=270,
                bbox_inches="tight", pad_inches=.03)
    plt.close(fig)


if __name__ == "__main__":
    draw()
