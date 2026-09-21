#!/usr/bin/env python3
"""Protótipo F da Figura 3.7: cobertura + coocorrência de duas famílias."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from gerar import CM, OUT, dados, tabela


BLUE = "#2F6D96"
SAND = "#B87932"
GREEN = "#6FAC74"
PALE = "#A9CEDD"
GRAY = "#CFCFCF"
INK = "#1A1A1A"
MUTED = "#666666"


def draw():
    classified, unresolved, groups, ratio_only, _ = tabela(dados())
    assert len(classified) == 162 and unresolved == 169 and ratio_only == 47
    assert groups[(True, False)] == 59 and groups[(True, True)] == 31
    assert groups[(False, False)] == 23 and groups[(False, True)] == 49

    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.linewidth": .6, "pdf.fonttype": 42,
    })
    fig = plt.figure(figsize=(15.5 * CM, 7.7 * CM))
    fig.text(.06, .95, "A  ·  Cobertura da classificação de modelos",
             fontsize=9, color=INK, va="center")

    # Cobertura: só dois estados de extração; nenhum dos 169 é tratado como
    # ausência da família ou incluído no denominador da matriz.
    ax_cover = fig.add_axes((.06, .82, .88, .075))
    ax_cover.barh([0], [162], left=[0], height=.85, color=BLUE)
    ax_cover.barh([0], [169], left=[162], height=.85, color=GRAY)
    ax_cover.text(81, 0, "162 concordantes (49%)", ha="center", va="center",
                  color="white", fontsize=8)
    ax_cover.text(162 + 84.5, 0, "169 por resolver (51%)", ha="center",
                  va="center", color=INK, fontsize=8)
    ax_cover.set(xlim=(0, 331), ylim=(-.5, .5))
    ax_cover.axis("off")

    fig.text(.06, .74, "B  ·  Famílias declaradas nas 162 concordantes",
             fontsize=9, color=INK, va="center")
    fig.text(.375, .675, "Regressão linear ou múltipla", ha="center",
             va="center", fontsize=7.7, color=INK)
    ax = fig.add_axes((.31, .21, .40, .40))
    ax.set(xlim=(0, 2), ylim=(0, 2))
    ax.axis("off")
    # Linhas: rácio/média sim, não. Colunas: regressão não, sim.
    cells = [
        (0, 1, 59, SAND, "white"),
        (1, 1, 31, GREEN, "white"),
        (0, 0, 23, PALE, INK),
        (1, 0, 49, BLUE, "white"),
    ]
    for x, y, count, fill, foreground in cells:
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor=fill,
                               edgecolor="white", linewidth=2))
        ax.text(x + .5, y + .5, str(count), ha="center", va="center",
                fontsize=17, color=foreground)
    ax.text(.5, 2.07, "não", ha="center", va="bottom", fontsize=8,
            color=INK, clip_on=False)
    ax.text(1.5, 2.07, "sim", ha="center", va="bottom", fontsize=8,
            color=INK, clip_on=False)
    ax.text(-.06, 1.5, "rácio ou\nmédia: sim", ha="right", va="center",
            fontsize=8, color=INK, clip_on=False)
    ax.text(-.06, .5, "rácio ou\nmédia: não", ha="right", va="center",
            fontsize=8, color=INK, clip_on=False)

    # O número-chave é um subconjunto preciso da célula 59: publicações que
    # não declaram mais nenhuma família, não apenas as sem regressão.
    fig.text(.79, .52, "47", ha="left", va="center", fontsize=22,
             color=SAND)
    fig.text(.79, .41, "declaram apenas\nrácio ou média",
             ha="left", va="top", fontsize=8, color=INK,
             linespacing=1.25)
    fig.text(.79, .27, "dentro das 59 sem\nregressão declarada",
             ha="left", va="top", fontsize=7.1, color=MUTED,
             linespacing=1.25)

    fig.text(.06, .075,
             "Contagens de publicações, não de modelos. Outras famílias podem coexistir em cada célula;",
             ha="left", va="center", fontsize=7, color=MUTED)
    fig.text(.06, .045,
             "«sem regressão» não significa «sem modelo ajustado». As 169 por resolver não entram na matriz.",
             ha="left", va="center", fontsize=7, color=MUTED)
    fig.savefig(f"{OUT}/proto-F-matriz-cruzada.pdf", bbox_inches="tight", pad_inches=.03)
    fig.savefig(f"{OUT}/proto-F-matriz-cruzada.png", dpi=260,
                bbox_inches="tight", pad_inches=.03)
    plt.close(fig)


if __name__ == "__main__":
    draw()
