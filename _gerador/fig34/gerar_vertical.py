#!/usr/bin/env python3
"""Alternativa à Figura 3.4: dois painéis empilhados à largura da página."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

from gerar import (BLUE, CM, GRAY, HERE, INK, MUTED, SAND, load)


NAMES = {
    "energies": "Energies",
    "journal of cleaner production": "Journal of Cleaner Production",
    "energy": "Energy",
    "Sustainability": "Sustainability",
    "international journal of energy economics and policy":
        "International Journal of Energy Economics and Policy",
    "energy and buildings": "Energy and Buildings",
    "energy efficiency": "Energy Efficiency",
    "Applied Sciences": "Applied Sciences",
    "applied energy": "Applied Energy",
}


def draw(destino=None):
    annual, journal_year, conference_year, counts, frequent = load()
    assert int(counts.artigos.eq(1).sum()) == 83
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.titlesize": 9, "axes.labelsize": 8,
        "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
        "axes.linewidth": .6, "pdf.fonttype": 42,
    })
    fig = plt.figure(figsize=(15.5 * CM, 12.8 * CM))
    ax_time = fig.add_axes((.085, .585, .88, .315))
    ax_journal = fig.add_axes((.43, .15, .535, .315))

    years = annual.index.to_numpy()
    bars = ax_time.bar(years, journal_year, width=.78, color=BLUE, zorder=3,
                       label="Artigos de revista (214)")
    ax_time.bar(years, conference_year, bottom=journal_year, width=.78,
                color=SAND, zorder=3, label="Conferências (117)")
    bars[-1].set_facecolor(GRAY)
    ax_time.set(xlim=(1996.3, 2027.7), ylim=(0, 40),
                ylabel="Publicações")
    ax_time.set_xticks([1997, 2001, 2005, 2009, 2013, 2017, 2021, 2025])
    ax_time.set_yticks([0, 10, 20, 30, 40])
    ax_time.yaxis.grid(True, color="#E7E7E7", linewidth=.45)
    ax_time.set_axisbelow(True)
    for x, label in [(2011.5, "ISO 50001:2011"),
                     (2014.5, "ISO 50006:2014")]:
        ax_time.axvline(x, color="#777777", linewidth=.8,
                        linestyle=(0, (4, 3)), zorder=2)
        ax_time.text(x + .16, 38.8, label, rotation=90, ha="left", va="top",
                     fontsize=7.0, color=MUTED)
    ax_time.legend(frameon=False, loc="upper left", bbox_to_anchor=(.015, .93),
                   fontsize=7.3, borderaxespad=0, labelspacing=.4,
                   handlelength=1.5)
    fig.text(.085, .948, "A  ·  Evolução anual por tipo de documento",
             ha="left", va="center", fontsize=9, color=INK)
    fig.text(.965, .948, "2026: pesquisa até fevereiro; ano incompleto",
             ha="right", va="center", fontsize=7.2, color=MUTED)

    values = frequent.artigos.to_numpy()
    y = np.arange(len(values))
    ax_journal.barh(y, values, height=.65, color=BLUE, zorder=3)
    ax_journal.set_yticks(y, [NAMES.get(title, title) for title in frequent.revista])
    ax_journal.invert_yaxis()
    ax_journal.set(xlim=(0, 27), xlabel="Artigos de revista")
    ax_journal.xaxis.set_major_locator(MultipleLocator(5))
    ax_journal.xaxis.grid(True, color="#E7E7E7", linewidth=.45)
    ax_journal.set_axisbelow(True)
    for yi, n in zip(y, values):
        ax_journal.text(n + .35, yi, str(n), ha="left", va="center",
                        fontsize=7.5, color=INK)
    fig.text(.085, .52, "B  ·  Revistas com pelo menos cinco artigos",
             ha="left", va="center", fontsize=9, color=INK)
    fig.text(.965, .52,
             "9 revistas: 83/214 artigos (38,8%)\n83 das 112 revistas surgem uma só vez",
             ha="right", va="center", fontsize=7.2, color=MUTED)

    for ax in (ax_time, ax_journal):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=2.5, width=.6, color=MUTED)
    ax_journal.tick_params(axis="y", length=0, pad=7)
    fig.text(.085, .055,
             "Corpus A, n=331 · Revistas harmonizadas por ISSN quando verificável",
             ha="left", va="center", fontsize=7, color=MUTED)
    alvo = destino or (HERE / "figura34_vertical.pdf")
    fig.savefig(alvo)
    plt.close(fig)


if __name__ == "__main__":
    draw()
