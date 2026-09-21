#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Segunda ronda de prototipos para a Figura 3.7.

A primeira ronda (gerar.py) eram tres variacoes da mesma barra horizontal com
uma faixa por cima. Foram rejeitadas e com razao: a forma nao mudou, so ganhou
decoracao. Estes dois partem da pergunta que a subseccao faz -- um racio nao
testa o pressuposto de proporcionalidade, uma regressao pode ser avaliada --
e essa e uma propriedade do modelo, nao uma contagem.

D: pequenos multiplos com a FORMA de cada familia. Mostra a diferenca em vez
   de a descrever. Os paineis sao esquematicos e tem de ser assim ditos.
E: matriz de propriedades. Oito familias contra cinco perguntas metodologicas,
   com a contagem do corpus ao lado. Deixa de descrever o corpus e passa a
   classificar o que cada familia permite fazer.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge

CM = 1 / 2.54
TINTA, CINZA, CINZA_C = "#1A1A1A", "#6E6E6E", "#CFCFCF"
P3 = ["#278CB1", "#65B9E7", "#6FAC74", "#AF6F43"]
AJUSTA, NAO_AJUSTA, FISICO, OUTRO = P3[0], P3[3], P3[2], "#9AA5AC"
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix", "font.size": 8, "axes.titlesize": 8.5,
    "axes.edgecolor": "#B0B0B0", "axes.linewidth": .6,
    "xtick.color": CINZA, "ytick.color": CINZA, "text.color": TINTA,
    "axes.labelcolor": TINTA, "savefig.bbox": "tight", "savefig.pad_inches": .02,
    "pdf.fonttype": 42})
OUT = os.path.dirname(os.path.abspath(__file__))

def grava(fig, nome):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, nome + "." + ext), dpi=200)
    plt.close(fig); print(nome, "ok")

# Nuvem sintetica comum a todos os paineis: carga normalizada contra energia,
# com termo constante claramente nao nulo. E o ponto todo -- e o intercepto
# que separa um racio de uma regressao.
rng = np.random.default_rng(11)
X = np.sort(rng.uniform(.38, 1.0, 34))
A0, B0 = .34, .60
Y = A0 + B0 * X + rng.normal(0, .035, X.size)

def nuvem(ax, cor=CINZA_C, x=None, y=None):
    ax.scatter(X if x is None else x, Y if y is None else y, s=5.5,
               facecolor="white", edgecolor=cor, linewidth=.6, zorder=2)

def moldura(ax, titulo, n, cor):
    ax.set_xlim(0, 1.12); ax.set_ylim(0, 1.16)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_color("#C4C4C4")
    ax.set_title(titulo, loc="left", fontsize=7.3, color=TINTA, pad=3.5)
    # A contagem vai no canto inferior direito, dentro do painel: em cima
    # colidia com os titulos longos.
    ax.annotate("%d" % n, (1.08, .06), ha="right", va="bottom", fontsize=13,
                color=cor, alpha=.90)

# ---------------------------------------------------------------- PROT. D --
def proto_d():
    from matplotlib.lines import Line2D
    fams = [
        (u"R\u00e1cio de intensidade", 74, NAO_AJUSTA, "racio"),
        (u"Regress\u00e3o linear", 48, AJUSTA, "linear"),
        (u"Regress\u00e3o m\u00faltipla", 41, AJUSTA, "multipla"),
        (u"Modelo f\u00edsico", 21, FISICO, "fisico"),
        (u"Ponto de mudan\u00e7a ou CEP", 20, AJUSTA, "mudanca"),
        (u"Aprendizagem autom\u00e1tica", 19, AJUSTA, "ml"),
        (u"M\u00e9dia do consumo espec\u00edfico", 17, NAO_AJUSTA, "media"),
        (u"Outra", 15, OUTRO, "outra")]
    fig, axs = plt.subplots(2, 4, figsize=(15.5 * CM, 9.0 * CM))
    xs = np.linspace(.02, 1.06, 160)
    NOTA = dict(fontsize=5.9, va="top", linespacing=1.3)
    for ax, (nome, n, cor, tipo) in zip(axs.ravel(), fams):
        if tipo == "multipla":
            alto = X > np.median(X)
            nuvem(ax, CINZA_C, X[~alto], Y[~alto] - .045)
            nuvem(ax, CINZA_C, X[alto], Y[alto] + .045)
        else:
            nuvem(ax)
        if tipo in ("racio", "media"):
            k = (Y / X).mean() if tipo == "media" else Y.mean() / X.mean()
            ax.plot(xs, k * xs, color=cor, lw=1.7, zorder=3)
            ax.plot([0], [0], marker="o", ms=3.4, color=cor, zorder=4)
            ax.annotate(u"passa pela origem\npor constru\u00e7\u00e3o", (.05, 1.12),
                        color=cor, **NOTA)
        elif tipo == "linear":
            b, a = np.polyfit(X, Y, 1)
            ax.plot(xs, a + b * xs, color=cor, lw=1.7, zorder=3)
            ax.plot([0, 0], [0, a], color=cor, lw=1.2, ls=(0, (2, 1.6)), zorder=3)
            ax.annotate(u"o termo constante\n\u00e9 estimado", (.05, 1.12), color=cor, **NOTA)
        elif tipo == "multipla":
            b, a = np.polyfit(X, Y, 1)
            ax.plot(xs, a + b * xs - .045, color=cor, lw=1.6, zorder=3)
            ax.plot(xs, a + b * xs + .045, color=cor, lw=1.6, zorder=3)
            ax.annotate(u"uma superf\u00edcie por\nvari\u00e1vel adicional", (.05, 1.12),
                        color=cor, **NOTA)
        elif tipo == "fisico":
            ax.plot(xs, .30 + .78 * xs - .16 * xs ** 2, color=cor, lw=1.7, zorder=3)
            ax.annotate(u"par\u00e2metros de balan\u00e7os,\nn\u00e3o dos dados", (.05, 1.12),
                        color=cor, **NOTA)
        elif tipo == "mudanca":
            xc = .70
            b, a = np.polyfit(X[X <= xc], Y[X <= xc], 1)
            yc = a + b * xc
            ax.plot(xs[xs <= xc], a + b * xs[xs <= xc], color=cor, lw=1.7, zorder=3)
            ax.plot(xs[xs > xc], yc + .30 * (xs[xs > xc] - xc), color=cor, lw=1.7, zorder=3)
            ax.axvline(xc, color=cor, lw=.9, ls=(0, (2, 1.6)), ymax=.62, zorder=3)
            ax.annotate(u"um n\u00f3 onde o\nregime muda", (.05, 1.12), color=cor, **NOTA)
        elif tipo == "ml":
            z = np.polyfit(X, Y, 8)
            ax.plot(X, np.polyval(z, X), color=cor, lw=1.7, zorder=3)
            ax.annotate(u"forma livre, ajustada\nponto a ponto", (.05, 1.12), color=cor, **NOTA)
        else:
            ax.annotate(u"categoria residual;\nsem forma comum", (.05, 1.12), color=cor, **NOTA)
        moldura(ax, nome, n, cor)
    for ax in axs[1]: ax.set_xlabel("carga", fontsize=6.6, labelpad=1.5)
    for ax in axs[:, 0]: ax.set_ylabel("energia", fontsize=6.6, labelpad=1.5)
    fig.tight_layout(h_pad=2.0, w_pad=1.0, rect=(0, .105, 1, 1))
    proxies = [Line2D([], [], color=c, lw=2.2) for c in (AJUSTA, NAO_AJUSTA, FISICO, OUTRO)]
    fig.legend(proxies,
               [u"estima par\u00e2metros dos dados e pode ser avaliado",
                u"n\u00e3o estima nada: o pressuposto n\u00e3o \u00e9 testado",
                u"par\u00e2metros de princ\u00edpios, n\u00e3o dos dados", u"residual"],
               loc="lower center", bbox_to_anchor=(.5, .055), ncol=4, frameon=False,
               fontsize=6.4, handlelength=1.5, columnspacing=1.6, handletextpad=.5)
    fig.text(.5, .005, u"Os pain\u00e9is s\u00e3o esquem\u00e1ticos, sobre a mesma nuvem sint\u00e9tica: mostram a forma de cada fam\u00edlia, n\u00e3o resultados do corpus.\n"
             u"O n\u00famero \u00e9 quantas das 162 publica\u00e7\u00f5es classificadas a declaram; 169 ficaram por resolver e as categorias n\u00e3o s\u00e3o exclusivas.",
             fontsize=6.2, color=CINZA, va="bottom", ha="center", linespacing=1.4)
    grava(fig, "proto-D-formas")

# ---------------------------------------------------------------- PROT. E --
def proto_e():
    from matplotlib.markers import MarkerStyle
    from matplotlib.lines import Line2D
    SIM, PARC, NAO, NA = "sim", "parcial", "nao", "na"
    cols = [u"Estima um termo\nconstante", u"Admite mais do que\numa vari\u00e1vel",
            u"Pode ser avaliado\ncontra os dados", u"Exige ajuste\npor instala\u00e7\u00e3o",
            u"Trata mudan\u00e7a\nde regime"]
    linhas = [
        (u"R\u00e1cio de intensidade", 74, [NAO, NAO, NAO, NAO, NAO]),
        (u"Regress\u00e3o linear", 48, [SIM, NAO, SIM, SIM, NAO]),
        (u"Regress\u00e3o m\u00faltipla", 41, [SIM, SIM, SIM, SIM, NAO]),
        (u"Modelo f\u00edsico", 21, [NA, SIM, PARC, SIM, NAO]),
        (u"Ponto de mudan\u00e7a ou CEP", 20, [SIM, PARC, SIM, SIM, SIM]),
        (u"Aprendizagem autom\u00e1tica", 19, [NA, SIM, SIM, SIM, PARC]),
        (u"M\u00e9dia do consumo espec\u00edfico", 17, [NAO, NAO, NAO, NAO, NAO]),
        (u"Outra", 15, [NA, NA, NA, NA, NA])]
    fig = plt.figure(figsize=(15.5 * CM, 7.8 * CM))
    axb = fig.add_axes((.255, .195, .125, .615))
    axm = fig.add_axes((.415, .195, .555, .615))
    y = np.arange(len(linhas))[::-1]
    axb.barh(y, [r[1] for r in linhas], color="#8FA7B4", height=.48, zorder=3)
    for yy, r in zip(y, linhas):
        axb.annotate(str(r[1]), (r[1] + 2.5, yy), va="center", fontsize=6.8, color=TINTA)
    axb.set_yticks(y); axb.set_yticklabels([r[0] for r in linhas], fontsize=7.3)
    axb.set_xlim(0, 100); axb.set_ylim(-.65, len(linhas) - .35)
    axb.set_xticks([0, 40, 80]); axb.tick_params(labelsize=6.2, length=0)
    axb.grid(True, axis="x", color="#ECECEC", lw=.4, zorder=0); axb.set_axisbelow(True)
    for s in ("top", "right", "left"): axb.spines[s].set_visible(False)
    axb.annotate(u"publica\u00e7\u00f5es", (0, 1.03), xycoords="axes fraction",
                 fontsize=7.0, color=CINZA, va="bottom")
    # zebra primeiro, para ficar por baixo
    for yy in y[1::2]:
        axm.add_patch(Rectangle((-.6, yy - .5), len(cols) + .2, 1., facecolor="#F5F6F7",
                                edgecolor="none", zorder=1))
    # marcadores em scatter: circulos verdadeiros, independentes do aspecto
    M = dict(sim=MarkerStyle("o"), parcial=MarkerStyle("o", fillstyle="left"))
    for j in range(len(cols)):
        for yy, r in zip(y, linhas):
            e = r[2][j]
            if e == SIM:
                axm.scatter([j], [yy], marker=M["sim"], s=74, color=P3[0], zorder=3)
            elif e == PARC:
                axm.scatter([j], [yy], marker=M["parcial"], s=74, facecolor=P3[0],
                            edgecolor=P3[0], linewidth=.9, zorder=3)
            elif e == NAO:
                axm.scatter([j], [yy], marker="o", s=74, facecolor="white",
                            edgecolor=P3[3], linewidth=1.1, zorder=3)
            else:
                axm.plot([j - .1, j + .1], [yy, yy], color="#C0C0C0", lw=1.1, zorder=3)
    axm.set_xlim(-.6, len(cols) - .4); axm.set_ylim(-.65, len(linhas) - .35)
    axm.set_yticks([]); axm.set_xticks(range(len(cols)))
    axm.set_xticklabels(cols, fontsize=6.5, linespacing=1.35)
    axm.xaxis.set_ticks_position("top"); axm.tick_params(length=0, pad=3)
    for s in ("top", "right", "left", "bottom"): axm.spines[s].set_visible(False)
    proxies = [Line2D([], [], ls="", marker=M["sim"], ms=7, color=P3[0]),
               Line2D([], [], ls="", marker=M["parcial"], ms=7, color=P3[0]),
               Line2D([], [], ls="", marker="o", ms=7, mfc="white", mec=P3[3], mew=1.1),
               Line2D([], [], color="#C0C0C0", lw=1.1)]
    fig.legend(proxies, [u"sim", u"depende da formula\u00e7\u00e3o", u"n\u00e3o",
                         u"n\u00e3o se aplica"],
               loc="lower center", bbox_to_anchor=(.55, .085), ncol=4, frameon=False,
               fontsize=6.5, handlelength=1.2, columnspacing=1.8, handletextpad=.5)
    fig.text(.55, .008, u"A barra \u00e9 quantas das 162 publica\u00e7\u00f5es classificadas declaram a fam\u00edlia; 169 ficaram por resolver\n"
             u"e as categorias n\u00e3o s\u00e3o exclusivas. As colunas s\u00e3o propriedades do m\u00e9todo, n\u00e3o do corpus.",
             fontsize=6.2, color=CINZA, va="bottom", ha="center", linespacing=1.4)
    grava(fig, "proto-E-propriedades")

if __name__ == "__main__":
    alvo = sys.argv[1:] or ["d", "e"]
    if "d" in alvo: proto_d()
    if "e" in alvo: proto_e()
