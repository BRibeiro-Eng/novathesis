#!/usr/bin/env python3
"""Protótipo da Figura 3.4: evolução anual e revistas mais frequentes."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator


HERE = Path(__file__).resolve().parent
TABLES = (Path.home() / "LocalResearch/Screening/level3_extraction/"
          "bibliometrics/results/corpus_a_registado/tables")
CM = 1 / 2.54
BLUE = "#2F6D96"
SAND = "#B87932"
GRAY = "#CFCFCF"
INK = "#1A1A1A"
MUTED = "#666666"

# Apenas equivalências de títulos confirmadas por ISSN dos DOI.
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

LABELS = {
    "energies": "Energies",
    "journal of cleaner production": "Journal of Cleaner\nProduction",
    "energy": "Energy",
    "Sustainability": "Sustainability",
    "international journal of energy economics and policy":
        "Int. J. Energy Economics\nand Policy",
    "energy and buildings": "Energy and Buildings",
    "energy efficiency": "Energy Efficiency",
    "Applied Sciences": "Applied Sciences",
    "applied energy": "Applied Energy",
}


def load():
    papers = pd.read_csv(TABLES / "analysis_dataset.csv", encoding="utf-8-sig")
    annual = pd.read_csv(TABLES / "annual.csv", encoding="utf-8-sig", index_col=0)
    annual.index = annual.index.astype(int)
    assert len(papers) == 331
    cross = pd.crosstab(papers.year, papers.document_type).reindex(
        annual.index, fill_value=0)
    journal_year = cross["journal article"].to_numpy()
    conference_year = cross["conference proceedings"].to_numpy()
    assert journal_year.sum() == 214 and conference_year.sum() == 117
    assert np.array_equal(journal_year + conference_year, annual.n.to_numpy())

    journals = papers.loc[papers.document_type.eq("journal article"), "source"]
    normalized = journals.map(lambda title: ALIASES.get(title, title))
    counts = (normalized.value_counts().rename_axis("revista")
              .reset_index(name="artigos")
              .sort_values(["artigos", "revista"], ascending=[False, True])
              .reset_index(drop=True))
    counts.insert(0, "posto", np.arange(1, len(counts) + 1))
    assert len(counts) == 112 and counts.artigos.sum() == 214
    frequent = counts[counts.artigos >= 5]
    assert len(frequent) == 9 and frequent.artigos.sum() == 83
    return annual, journal_year, conference_year, counts, frequent


def draw(annual, journal_year, conference_year, frequent):
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.titlesize": 9, "axes.labelsize": 8,
        "xtick.labelsize": 7.2, "ytick.labelsize": 7.2,
        "axes.linewidth": .6, "pdf.fonttype": 42,
    })
    fig = plt.figure(figsize=(17.0 * CM, 9.0 * CM))
    # O espaço entre painéis pertence aos nomes das revistas.
    ax_time = fig.add_axes((.072, .20, .43, .65))
    ax_journal = fig.add_axes((.76, .20, .205, .65))

    years = annual.index.to_numpy()
    bars_j = ax_time.bar(years, journal_year, width=.78, color=BLUE,
                         label="Artigos de revista (214)", zorder=3)
    ax_time.bar(years, conference_year, bottom=journal_year, width=.78,
                color=SAND, label="Conferências (117)", zorder=3)
    bars_j[-1].set_facecolor(GRAY)
    ax_time.set(xlim=(1996.3, 2027.7), ylim=(0, 40),
                xlabel="Ano de publicação", ylabel="Publicações")
    ax_time.set_xticks([1997, 2002, 2007, 2012, 2017, 2022, 2026])
    ax_time.set_yticks([0, 10, 20, 30, 40])
    ax_time.set_title("A  ·  Evolução anual por tipo de documento", loc="left", pad=9)
    ax_time.yaxis.grid(True, color="#E7E7E7", linewidth=.45)
    ax_time.set_axisbelow(True)
    # Os anos são barras civis; cada marco fica exatamente ENTRE barras.
    for x, label in [(2011.5, "ISO 50001:2011"),
                     (2014.5, "ISO 50006:2014")]:
        ax_time.axvline(x, color="#777777", linewidth=.8,
                        linestyle=(0, (4, 3)), zorder=2)
        ax_time.text(x + .12, 39, label, rotation=90, ha="left", va="top",
                     fontsize=6.8, color=MUTED)
    ax_time.legend(frameon=False, loc="upper left", bbox_to_anchor=(.015, .82),
                   fontsize=7.0, borderaxespad=0, labelspacing=.35,
                   handlelength=1.5)
    ax_time.text(1, 1.11, "2026: pesquisa até fevereiro; ano incompleto",
                 transform=ax_time.transAxes, ha="right", va="bottom",
                 fontsize=6.9, color=MUTED)

    values = frequent.artigos.to_numpy()
    positions = np.arange(len(frequent))
    ax_journal.barh(positions, values, height=.63, color=BLUE, zorder=3)
    ax_journal.set_yticks(positions, [LABELS.get(s, s) for s in frequent.revista])
    ax_journal.invert_yaxis()
    ax_journal.set(xlim=(0, 27.5), xlabel="Artigos de revista")
    ax_journal.xaxis.set_major_locator(MultipleLocator(5))
    ax_journal.set_title("B  ·  Revistas com ≥5 artigos", loc="left", pad=9)
    ax_journal.xaxis.grid(True, color="#E7E7E7", linewidth=.45)
    ax_journal.set_axisbelow(True)
    for y, count in zip(positions, values):
        ax_journal.text(count + .45, y, str(count), ha="left", va="center",
                        fontsize=7.2, color=INK)
    ax_journal.text(1, 1.005, "9 revistas · 83/214 artigos (38,8%)",
                    transform=ax_journal.transAxes, ha="right", va="top",
                    fontsize=6.9, color=MUTED)

    for ax in (ax_time, ax_journal):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=2.5, width=.6, color=MUTED)
    ax_journal.tick_params(axis="y", length=0, pad=5)

    fig.text(.072, .055,
             "Corpus A, n=331 · Revistas harmonizadas por ISSN quando verificável · 2026 parcial",
             fontsize=7, color=MUTED, va="center")
    fig.savefig(HERE / "figura34_temporal_revistas.pdf")
    fig.savefig(HERE / "figura34_temporal_revistas.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    annual, journal_year, conference_year, counts, frequent = load()
    counts.to_csv(HERE / "revistas_harmonizadas.csv", index=False)
    draw(annual, journal_year, conference_year, frequent)
    print(f"331 publicações = {journal_year.sum()} artigos + {conference_year.sum()} conferências")
    print(f"{len(counts)} revistas; {len(frequent)} revistas com ≥5 artigos = {frequent.artigos.sum()}/214")
