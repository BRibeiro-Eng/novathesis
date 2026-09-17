#!/usr/bin/env python3
"""Figuras geradas da tese (2026-09-17).

Lê apenas as corridas canónicas pinadas em baselines-cc/config/params.yaml e
config/partc_pins.env, e as tabelas congeladas em data/raw. Não recalcula
resultados: quando uma figura precisa de resíduos, recalcula-os a partir dos
parâmetros oficiais exportados (BaselineFit), que o gate E1 reproduz.

Uso:  /usr/local/bin/python3 _gerador/figuras.py [nome ...]
Saída: 5-Figures/gerado/*.pdf (vetorial).
"""
import os, sys, json
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyArrowPatch

# ---------------------------------------------------------------- caminhos --
def _first(paths):
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.isdir(p): return p
    raise SystemExit("caminho não encontrado: " + str(paths))
BC = _first(["~/LocalResearch/baselines-cc", "~/mnt/LocalResearch/baselines-cc"])
TESE = _first(["~/Desktop/Tese/novathesis", "~/mnt/novathesis"])
OUT = os.path.join(TESE, "5-Figures", "gerado")
os.makedirs(OUT, exist_ok=True)
RUNS = {"E2": "E2/runs/20260828T153423377266Z-7926b7afbe338986221d",
        "E3": "E3/runs/20260829T122639790978Z-aa3e341622b4",
        "E4": "E4/runs/20260829T135121261692Z-2ea18e7390bb",
        "E6": "E6/runs/20260829T153020733605Z-ccd0312d97b3",
        "D": "D1-D9/runs/20260829T182000032463Z-1dde8c0c7d78",
        "SENS": "SENS/runs/20260829T195138387361Z-e068552161d2",
        "T12": "T12/runs/20260830T122854929917Z-459cf49c965c",
        "T13": "T13/runs/20260830T165208669276Z-b583143cacb9",
        "T14": "T14/runs/20260830T165252925802Z-ad4bf78ea405",
        "C8core": "PART_C/C8/runs/20260902T165944891648Z-ae3e8022c6a5",
        "C8stress": "PART_C/C8/runs/20260902T224337596785Z-745ef41d27f7",
        "C5inj": "PART_C/C5/runs/20260903T004416308950Z-2c5caf3d5988"}
def tsv(run, name):
    return pd.read_csv(os.path.join(BC, "outputs", RUNS[run], name), sep="\t")
def raw(name):
    return pd.read_csv(os.path.join(BC, "data", "raw", name), sep="\t")

# ------------------------------------------------------------------ estilo --
COR = {"fuel_gas": "#0072B2", "vapor_24bar": "#B37700",
       "vapor_10bar": "#009E73", "vapor_3bar": "#D55E00",
       "energia_eletrica": "#56B4E9"}
CINZA, CINZA_C, TINTA = "#6E6E6E", "#C8C8C8", "#1A1A1A"
NOME = {"fuel_gas": "Fuel gás", "vapor_24bar": "Vapor 24 bar",
        "vapor_10bar": "Vapor 10 bar", "vapor_3bar": "Vapor 3 bar",
        "energia_eletrica": "Eletricidade"}
VEC4 = ["fuel_gas", "vapor_24bar", "vapor_10bar", "vapor_3bar"]
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
    s = f"{x:,.{casas}f}".replace(",", " ").replace(".", ",")
    return s
def virgula(casas=1):
    return FuncFormatter(lambda v, _: pt(v, casas))
def guarda(ax):
    ax.grid(True, axis="both", color="#E6E6E6", lw=0.4, zorder=0)
    ax.set_axisbelow(True)
def grava(fig, nome):
    p = os.path.join(OUT, nome + ".pdf")
    fig.savefig(p); plt.close(fig)
    print(nome, "->", p)

# ------------------------------------------- dados base (painel congelado) --
def painel():
    e = raw("FactEnergia_Unified.tsv"); k = raw("FactCarga_Unified.tsv")
    e = e[e.unidade_id == "CC"][["ts", "vector_id", "value_gne_d_sem_prod"]]
    k = k[k.unidade_id == "CC"][["ts", "carga_unified_ton_d"]]
    d = e.merge(k, on="ts")
    d["ts"] = pd.to_datetime(d.ts); d["ano"] = d.ts.dt.year
    d = d.rename(columns={"value_gne_d_sem_prod": "E", "carga_unified_ton_d": "Q_ton"})
    d["Q"] = d.Q_ton / 1000.0
    return d
LIMIAR = 18.6  # kt/d, lido de DimUnidade
def fits():
    b = raw("BaselineFit.tsv")
    b = b[(b.unidade_id == "CC")]
    return b

# =============================================================== figuras ====
def f11_dispersao():
    d = painel(); b = fits()
    fig, axs = plt.subplots(3, 2, figsize=(15.5 * CM, 16.0 * CM))
    for ax, v in zip(axs.flat[:4], VEC4):
        x = d[(d.vector_id == v) & (d.ano <= 2025)]
        dentro = (x.Q >= LIMIAR) & (x.E != 0)
        ax.scatter(x.Q[~dentro], x.E[~dentro], s=2.5, c=CINZA_C, lw=0, zorder=2)
        ax.scatter(x.Q[dentro], x.E[dentro], s=2.5, c=COR[v], lw=0, alpha=0.35, zorder=3)
        bb = b[(b.vector_id == v) & (b.ano_baseline <= 2025)].sort_values("ano_baseline")
        qq = np.linspace(LIMIAR, float(x.Q[dentro].max()), 20)
        tons = np.linspace(0.30, 1.0, len(bb))
        for (_, r), t in zip(bb.iterrows(), tons):
            ax.plot(qq, r.slope * qq + r.intercept, color=TINTA, alpha=t, lw=0.9, zorder=4)
            if int(r.ano_baseline) == 2020:
                ax.annotate("2020", (qq[0], r.slope * qq[0] + r.intercept),
                            xytext=(-4, 0), textcoords="offset points", fontsize=6.5,
                            color=TINTA, alpha=0.75, va="center", ha="right")
            if int(r.ano_baseline) == 2025:
                ax.annotate("2025", (qq[-1], r.slope * qq[-1] + r.intercept),
                            xytext=(4, 0), textcoords="offset points", fontsize=6.5,
                            color=TINTA, va="center")
        ax.axvline(LIMIAR, color=CINZA, lw=0.8, ls=(0, (4, 2)), zorder=1)
        ax.set_title(NOME[v], loc="left", color=COR[v])
        ax.set_xlabel("carga (kt/d)"); ax.set_ylabel("consumo (t GNE/d)")
        ax.yaxis.set_major_formatter(virgula(0)); ax.xaxis.set_major_formatter(virgula(0))
        ax.set_xlim(-4, 38); guarda(ax)
    ax = axs.flat[4]
    x = d[(d.vector_id == "energia_eletrica") & (d.ano <= 2025)].sort_values("ts")
    ax.plot(x.ts, x.E, color=COR["energia_eletrica"], lw=0.8)
    ax.annotate("2021--2022: alocação quase nula,\nsó nesta unidade (ver texto)",
                (pd.Timestamp("2022-01-01"), 1.0), xytext=(0, 62), textcoords="offset points",
                fontsize=6.5, color=TINTA, ha="center",
                arrowprops=dict(arrowstyle="-", color=CINZA, lw=0.6))
    ax.set_title("Eletricidade: alocação mensal", loc="left", color=COR["energia_eletrica"])
    ax.set_xlabel("dia"); ax.set_ylabel("consumo alocado (t GNE/d)")
    ax.yaxis.set_major_formatter(virgula(0)); guarda(ax)
    ax = axs.flat[5]
    q = d[(d.vector_id == "fuel_gas") & (d.ano <= 2025)].Q
    ax.hist(q, bins=np.arange(0, 35, 1), color=CINZA_C, lw=0, label="todos os dias")
    ax.hist(q[q >= LIMIAR], bins=np.arange(0, 35, 1), color=TINTA, alpha=0.8, lw=0,
            label="dias acima do limiar")
    ax.axvline(LIMIAR, color=CINZA, lw=0.8, ls=(0, (4, 2)))
    ax.set_title("Carga diária: antes e depois do limiar", loc="left")
    ax.set_xlabel("carga (kt/d)"); ax.set_ylabel("dias")
    ax.xaxis.set_major_formatter(virgula(0)); ax.legend(frameon=False, loc="upper left")
    guarda(ax)
    leg = [Line2D([], [], marker="o", ls="", ms=3.5, color=CINZA_C,
                  label="dias excluídos: carga abaixo do limiar ou consumo nulo"),
           Line2D([], [], color=TINTA, lw=0.9, label="retas anuais oficiais, de 2020 (claro) a 2025 (escuro)"),
           Line2D([], [], color=CINZA, lw=0.8, ls=(0, (4, 2)), label="limiar oficial de carga, 18,6 kt/d")]
    fig.tight_layout(h_pad=1.9, w_pad=2.2, rect=(0, 0.045, 1, 1))
    fig.legend(handles=leg, loc="lower center", ncols=1, frameon=False, bbox_to_anchor=(0.5, 0.0))
    grava(fig, "cap6-dispersao-energia-carga")

def f12_ganho():
    e = tsv("E2", "E2_comparisons.tsv")
    s = tsv("E2", "E2_bootstrap_sensitivity.tsv")
    e = e[(e.null_id == "training_mean") & (e.period_scope == "complete_year")]
    s = s[(s.null_id == "training_mean") & (s.block_length == 60)]
    fig, axs = plt.subplots(1, 4, figsize=(15.5 * CM, 6.2 * CM), sharey=True)
    pares = sorted(e.pair_id.unique())
    for ax, v in zip(axs, VEC4):
        x = e[e.vector_id == v].set_index("pair_id")
        y60 = s[s.vector_id == v].set_index("pair_id")
        for i, p in enumerate(pares):
            if p not in x.index: continue
            r = x.loc[p]
            ax.plot([r.ci_lower, r.ci_upper], [i, i], color=COR[v], lw=2.4, solid_capstyle="round", zorder=3)
            ax.plot([r.delta_mae], [i], "o", ms=4, color=COR[v], mec="white", mew=0.6, zorder=4)
            if p in y60.index:
                q = y60.loc[p]
                ax.plot([q.lower, q.upper], [i + 0.28, i + 0.28], color=CINZA, lw=0.9, zorder=2)
            ax.annotate(f"n={pt(r.n_eval)}", (r.ci_upper, i), xytext=(3, -0.5),
                        textcoords="offset points", fontsize=6, color=CINZA, va="center")
        ax.axvline(0, color=TINTA, lw=0.7, zorder=1)
        ax.set_title(NOME[v], loc="left", color=COR[v])
        ax.set_yticks(range(len(pares)))
        ax.set_yticklabels([p.replace("->", "→") for p in pares])
        ax.invert_yaxis(); ax.set_xlabel(r"$\Delta_{\mathrm{MAE}}$ (t GNE/d)")
        ax.xaxis.set_major_formatter(virgula(0)); guarda(ax)
    axs[0].annotate("modelo melhor →", (0, -0.75), xytext=(4, 0), textcoords="offset points",
                    fontsize=6.5, color=CINZA, va="center")
    leg = [Line2D([], [], color=TINTA, lw=2.4, label="intervalo com o bloco base"),
           Line2D([], [], color=CINZA, lw=0.9, label="intervalo com blocos de 60 dias")]
    fig.legend(handles=leg, loc="lower center", ncols=2, frameon=False, bbox_to_anchor=(0.5, -0.07))
    fig.tight_layout(w_pad=1.4)
    grava(fig, "cap6-ganho-preditivo")

def f13_predicoes():
    p = tsv("E3", "E3_predictions.tsv")
    quants = sorted(p.reference_quantile.unique())
    fig, axs = plt.subplots(1, 4, figsize=(15.5 * CM, 5.6 * CM))
    estilos = {quants[0]: (0, (3, 2)), quants[-1]: "solid"}
    for ax, v in zip(axs, VEC4):
        x = p[p.vector_id == v]
        for q in (quants[0], quants[-1]):
            xx = x[x.reference_quantile == q].sort_values("year")
            ax.fill_between(xx.year, xx.lower, xx.upper, color=COR[v], alpha=0.16, lw=0)
            ax.plot(xx.year, xx.estimate, color=COR[v], ls=estilos[q], marker="o", ms=3)
        ax.set_title(NOME[v], loc="left", color=COR[v])
        ax.set_xlabel("ano da baseline"); ax.set_ylabel("consumo previsto (t GNE/d)")
        ax.yaxis.set_major_formatter(virgula(0))
        ax.set_xticks(sorted(x.year.unique())); ax.tick_params(axis="x", rotation=90)
        guarda(ax)
    leg = [Line2D([], [], color=TINTA, ls=(0, (3, 2)), marker="o", ms=3,
                  label=f"carga no percentil {int(quants[0]*100)} do suporte comum"),
           Line2D([], [], color=TINTA, marker="o", ms=3,
                  label=f"carga no percentil {int(quants[-1]*100)}"),
           Line2D([], [], color=TINTA, lw=6, alpha=0.16, label="intervalo de confiança HAC a 95 %")]
    fig.legend(handles=leg, loc="lower center", ncols=3, frameon=False, bbox_to_anchor=(0.5, -0.1))
    fig.tight_layout(w_pad=1.6)
    grava(fig, "cap6-predicoes-carga-comum")

def f14_cobertura():
    c = tsv("E4", "E4_marginal_coverage.tsv")
    s = tsv("E4", "E4_coverage_sensitivity.tsv")
    c = c[c.band_status != "diagnostic_ytd"]
    fig, axs = plt.subplots(4, 1, figsize=(15.5 * CM, 12.4 * CM), sharex=True)
    for ax, v in zip(axs, VEC4):
        x = c[c.vector_id == v].sort_values("pair_id").reset_index(drop=True)
        for i, r in x.iterrows():
            ax.plot([r.mbb_lower, r.mbb_upper], [i, i], color=COR[v], lw=2.6,
                    solid_capstyle="round", zorder=3)
            ax.plot([r.coverage], [i], "o", ms=4.2, color=COR[v], mec="white", mew=0.6, zorder=4)
            ss = s[(s.vector_id == v) & (s.pair_id == r.pair_id) &
                   (s.block_length.isin([30, 60]))].sort_values("block_length")
            for k, (_, q) in enumerate(ss.iterrows()):
                ax.plot([q.mbb_lower, q.mbb_upper], [i + 0.24 + 0.16 * k] * 2,
                        color=CINZA, lw=0.8, zorder=2)
            ax.annotate(f"{pt(r.n_alarms)}/{pt(r.n_obs)} dias fora", (1.004, i),
                        xycoords=("axes fraction", "data"), fontsize=6.5, color=CINZA, va="center")
        ax.axvline(0.9545, color=TINTA, lw=0.8, zorder=1)
        ax.set_yticks(range(len(x)))
        ax.set_yticklabels([p.replace("->", "\u2192") for p in x.pair_id])
        ax.set_ylim(len(x) - 0.4, -0.7)
        ax.set_title(NOME[v], loc="left", color=COR[v])
        guarda(ax)
    axs[-1].set_xlabel("cobertura da banda de alarme no ano de aplicação")
    axs[-1].set_xlim(0.2, 1.02); axs[-1].xaxis.set_major_formatter(virgula(2))
    axs[0].annotate("0,9545", (0.9545, -0.95), fontsize=6.5, color=TINTA, ha="center")
    leg = [Line2D([], [], color=TINTA, lw=2.6, label="intervalo com o bloco base"),
           Line2D([], [], color=CINZA, lw=0.8, label="intervalos com blocos de 30 e de 60 dias")]
    fig.tight_layout(h_pad=1.2, rect=(0, 0.035, 1, 1))
    fig.legend(handles=leg, loc="lower center", ncols=2, frameon=False, bbox_to_anchor=(0.5, 0.0))
    grava(fig, "cap6-cobertura-bandas")


def _residuos_padronizados():
    """Resíduos padronizados das regressões oficiais, por vetor e ano civil.
    Recalculados dos parâmetros exportados (BaselineFit), que o gate E1 reproduz."""
    d = painel(); b = fits(); out = []
    for v in VEC4:
        for _, r in b[(b.vector_id == v) & (b.ano_baseline <= 2025)].iterrows():
            x = d[(d.vector_id == v) & (d.ano == int(r.ano_baseline)) & (d.Q >= LIMIAR) & (d.E != 0)].copy()
            x["z"] = (x.E - (r.slope * x.Q + r.intercept)) / r.sigma
            out.append(x[["ts", "ano", "vector_id", "z"]])
    return pd.concat(out)

def f15_acoplamento():
    z = _residuos_padronizados()
    w = z.pivot_table(index="ts", columns="vector_id", values="z").dropna(
        subset=["vapor_24bar", "vapor_10bar"])
    d9 = tsv("D", "D9_correlations.tsv")
    d9 = d9[(d9.vector_a == "vapor_24bar") & (d9.vector_b == "vapor_10bar")]
    fig, axs = plt.subplots(1, 2, figsize=(15.5 * CM, 6.2 * CM),
                            gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axs[0]
    m = w[w.index.year == 2025]
    ax.plot(m.index, m["vapor_24bar"], color=COR["vapor_24bar"], lw=0.8, label="Vapor 24 bar")
    ax.plot(m.index, m["vapor_10bar"], color=COR["vapor_10bar"], lw=0.8, label="Vapor 10 bar")
    ax.axhline(0, color=TINTA, lw=0.6)
    ax.set_ylabel("resíduo padronizado"); ax.set_xlabel("dia de 2025")
    ax.legend(frameon=False, ncols=2, loc="upper left")
    ax.set_ylim(-5, 5); ax.yaxis.set_major_formatter(virgula(0)); guarda(ax)
    ax = axs[1]
    anos = sorted(w.index.year.unique())
    cmap = plt.get_cmap("Blues")
    for i, a in enumerate(anos):
        m = w[w.index.year == a]
        ax.scatter(m["vapor_24bar"], m["vapor_10bar"], s=3.5, lw=0, alpha=0.75,
                   color=cmap(0.30 + 0.65 * i / max(1, len(anos) - 1)), label=str(a))
    r = d9[d9.period_scope == "pooled_complete_years"].pearson.iloc[0]
    rmin = d9[d9.period_scope == "complete_year"].pearson.min()
    rmax = d9[d9.period_scope == "complete_year"].pearson.max()
    ax.annotate(f"$r$ agregado = {pt(r,2)}\npor ano, de {pt(rmin,2)} a {pt(rmax,2)}",
                (0.03, 0.03), xycoords="axes fraction", fontsize=7, color=TINTA)
    ax.legend(frameon=False, ncols=3, fontsize=6.5, loc="upper right", handletextpad=0.2,
              columnspacing=0.8, markerscale=1.6)
    ax.set_xlabel("resíduo padronizado, 24 bar"); ax.set_ylabel("resíduo padronizado, 10 bar")
    ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
    ax.xaxis.set_major_formatter(virgula(0)); ax.yaxis.set_major_formatter(virgula(0))
    guarda(ax)
    fig.tight_layout(w_pad=2.0)
    grava(fig, "cap6-acoplamento-vapores")

def f16_sensibilidade():
    g = tsv("SENS", "SENS_grid.tsv")
    g["muda"] = ~g.survives.astype(bool)
    piv = g.pivot_table(index=["endpoint", "vector_id"], columns="cell_id", values="muda", aggfunc="mean")
    n = g.pivot_table(index=["endpoint", "vector_id"], columns="cell_id", values="muda", aggfunc="size")
    ordem = ["0.8x_ano_civil", "1x_ano_civil", "1.2x_ano_civil",
             "0.8x_movel_12m", "1x_movel_12m", "1.2x_movel_12m"]
    piv = piv[ordem]; n = n[ordem]
    fig, ax = plt.subplots(figsize=(15.5 * CM, 9.0 * CM))
    im = ax.imshow(piv.values, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(ordem)))
    ax.set_xticklabels(["0,8$\\times$\nano civil", "1$\\times$\nano civil", "1,2$\\times$\nano civil",
                        "0,8$\\times$\njulho--junho", "1$\\times$\njulho--junho", "1,2$\\times$\njulho--junho"])
    ax.set_yticks(range(len(piv)))
    ax.set_yticklabels([f"{i[0]} · {NOME[i[1]]}" for i in piv.index])
    for i in range(piv.shape[0]):
        for j in range(piv.shape[1]):
            v = piv.values[i, j]
            ax.text(j, i, f"{pt(100*v,0)}%\n({int(n.values[i,j])})", ha="center", va="center",
                    fontsize=6.3, color="white" if v > 0.5 else TINTA)
    ax.axvline(2.5, color="white", lw=2)
    cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
    cb.set_label("rótulos que mudam face à célula de referência")
    cb.ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(100 * v, 0) + "%"))
    cb.outline.set_visible(False)
    ax.set_title("Cada célula: percentagem de conclusões que mudam de rótulo, e o número de reavaliações", loc="left", fontsize=7.5, color=CINZA)
    ax.tick_params(length=0)
    fig.tight_layout()
    grava(fig, "cap6-sensibilidade-convencoes")

def f19_injeccao():
    c = pd.read_csv(os.path.join(BC, "outputs", RUNS["C5inj"], "injection_curves.tsv"), sep="\t")
    c = c[(c.vector_id == "fuel_gas") & (c.model_id == "B08")].copy()
    c["ts"] = pd.to_datetime(c.ts); c = c.sort_values("ts")
    cen = [("step_1sigma", "Degrau de uma escala"), ("ramp_1sigma_90d", "Rampa de uma escala em 90 dias")]
    fig, axs = plt.subplots(3, 2, figsize=(15.5 * CM, 10.4 * CM), sharex="col")
    for j, (cid, titulo) in enumerate(cen):
        x = c[c.scenario == cid].head(150)
        axs[0, j].plot(x.ts, x.injected_delta, color=TINTA, lw=1.0)
        axs[0, j].set_title(titulo, loc="left")
        axs[1, j].plot(x.ts, x.raw_reference_delta, color=COR["fuel_gas"], lw=1.0,
                       label="resíduo da referência congelada")
        axs[1, j].plot(x.ts, x.reference_revision_delta, color=CINZA, lw=1.0,
                       label="parte absorvida pelo reajuste")
        axs[2, j].plot(x.ts, x.innovation_delta, color=COR["vapor_10bar"], lw=1.0)
        for i in range(3):
            axs[i, j].axhline(0, color=TINTA, lw=0.6)
            axs[i, j].yaxis.set_major_formatter(virgula(0)); guarda(axs[i, j])
        axs[2, j].set_xlabel("primeiros 150 dias de aplicação")
        axs[2, j].tick_params(axis="x", rotation=30)
    axs[0, 0].set_ylabel("desvio inserido\n(t GNE/d)")
    axs[1, 0].set_ylabel("desvio medido\n(t GNE/d)")
    axs[2, 0].set_ylabel("inovação do filtro\n(t GNE/d)")
    h, l = axs[1, 0].get_legend_handles_labels()
    fig.tight_layout(h_pad=0.9, w_pad=1.8, rect=(0, 0.05, 1, 1))
    fig.legend(h, l, loc="lower center", ncols=2, frameon=False, bbox_to_anchor=(0.5, 0.0))
    grava(fig, "cap7-injeccao-degrau")

def f20_deteccao():
    core = pd.read_csv(os.path.join(BC, "outputs", "PART_C/C8/runs/20260902T173832448820Z-a57d556e7266",
                                    "core_detection.tsv"), sep="\t")
    stress = pd.read_csv(os.path.join(BC, "outputs", RUNS["C8stress"], "stress_detection.tsv"), sep="\t")
    MON = {"P1": ("resíduo bruto", CINZA), "P3": ("filtro de nível", COR["vapor_10bar"]),
           "P5": ("soma acumulada", COR["fuel_gas"])}
    core = core[(core.channel_role == "primary_level_channel") & (core.bank_id == "mechanistic/LIN_AR06")]
    fig, axs = plt.subplots(1, 3, figsize=(15.5 * CM, 5.6 * CM), sharey=True)
    for ax, fam, titulo in zip(axs[:2], ["STEP", "RAMP"], ["Degrau", "Rampa"]):
        for p, (rot, cor) in MON.items():
            x = core[(core.pipeline == p) & (core.alternative.str.startswith(fam))].copy()
            x["amp"] = x.alternative.str.split("_").str[1].astype(float)
            x = x.sort_values("amp")
            ax.fill_between(x.amp, x.wilson_low, x.wilson_high, color=cor, alpha=0.15, lw=0)
            ax.plot(x.amp, x.observed_rate, color=cor, marker="o", ms=3.2, label=rot)
        ax.axhline(0.5, color=TINTA, lw=0.6, ls=(0, (3, 2)))
        ax.set_title(f"{titulo}, $\\rho = 0{{,}}6$", loc="left")
        ax.set_xlabel("amplitude (em desvios-padrão)"); ax.set_ylim(0, 1.02)
        ax.xaxis.set_major_formatter(virgula(2)); ax.yaxis.set_major_formatter(virgula(1))
        guarda(ax)
    axs[0].set_ylabel("deteção em 90 dias")
    ax = axs[2]
    bancos = [("mechanistic/LIN_AR06", 0.6, core), ("mechanistic/LIN_AR09", 0.9, stress),
              ("mechanistic/LIN_AR095", 0.95, stress)]
    for p, (rot, cor) in MON.items():
        xs, ys, lo, hi = [], [], [], []
        for banco, rho, fonte in bancos:
            x = fonte[(fonte.bank_id == banco) & (fonte.pipeline == p) &
                      (fonte.alternative == "STEP_1.0") & (fonte.channel_role == "primary_level_channel")]
            if not len(x): continue
            xs.append(rho); ys.append(float(x.observed_rate.iloc[0]))
            lo.append(float(x.wilson_low.iloc[0])); hi.append(float(x.wilson_high.iloc[0]))
        ax.fill_between(xs, lo, hi, color=cor, alpha=0.15, lw=0)
        ax.plot(xs, ys, color=cor, marker="o", ms=3.2, label=rot)
    ax.axhline(0.5, color=TINTA, lw=0.6, ls=(0, (3, 2)))
    ax.set_title("Degrau de uma escala, por dependência", loc="left")
    ax.set_xlabel(r"$\rho$ do gerador"); ax.set_xticks([0.6, 0.9, 0.95])
    ax.xaxis.set_major_formatter(virgula(2)); guarda(ax)
    h, l = axs[0].get_legend_handles_labels()
    fig.tight_layout(w_pad=1.6, rect=(0, 0.07, 1, 1))
    fig.legend(h, l, loc="lower center", ncols=3, frameon=False, bbox_to_anchor=(0.5, 0.0))
    grava(fig, "cap7-deteccao-simulacao")

def f08_validacao():
    versoes = ["v13", "v14", "v15", "v15, fev. corrigido", "v15.1"]
    coincidentes = [242, 263, 327, 330, 335]
    divergentes = [94, 73, 8, 5, 0]
    vazias = [64, 64, 65, 65, 65]
    fig, ax = plt.subplots(figsize=(13.0 * CM, 6.4 * CM))
    b1 = ax.bar(versoes, coincidentes, color=COR["fuel_gas"], label="células numéricas coincidentes")
    b2 = ax.bar(versoes, divergentes, bottom=coincidentes, color=COR["vapor_3bar"], label="divergentes")
    b3 = ax.bar(versoes, vazias, bottom=np.add(coincidentes, divergentes), color=CINZA_C,
                label="sem consumo (vazias)")
    for r in b3[-1:]:
        r.set_hatch("///"); r.set_edgecolor("white")
    for r in [b1[-1], b2[-1]]:
        r.set_hatch("///"); r.set_edgecolor("white")
    for i, (c, d) in enumerate(zip(coincidentes, divergentes)):
        ax.annotate(pt(c), (i, c / 2), ha="center", va="center", color="white", fontsize=7)
        if d: ax.annotate(pt(d), (i, c + d / 2), ha="center", va="center", color="white", fontsize=7)
    ax.annotate("esperado,\nnão observado", (4, 200), ha="center", fontsize=6.8, color=TINTA)
    ax.set_ylabel("células unidade--vetor--mês (de 400)")
    ax.set_xlabel("versão da tabela de mapeamento")
    ax.yaxis.set_major_formatter(virgula(0))
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncols=3)
    guarda(fig.axes[0])
    fig.tight_layout()
    grava(fig, "cap5-validacao-progressao")

def f10_amostra():
    d = painel()
    dd = d[d.ts <= pd.Timestamp("2026-07-30")]
    fig, axs = plt.subplots(1, 2, figsize=(15.5 * CM, 6.4 * CM),
                            gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axs[0]
    etapas = ["dias candidatos\n2020-01-01 a 2026-07-30", "observações série--dia\n(5 vetores)",
              "com energia medida", "acima do limiar de carga"]
    vals = [2403, 11955, 11467, 11467 - 744]
    cores = [CINZA_C, CINZA_C, COR["fuel_gas"], COR["fuel_gas"]]
    y = np.arange(len(etapas))[::-1]
    ax.barh(y, vals, color=cores, height=0.6)
    for yy, v in zip(y, vals):
        ax.annotate(pt(v), (v, yy), xytext=(4, 0), textcoords="offset points", va="center", fontsize=7.5)
    ax.set_yticks(y); ax.set_yticklabels(etapas)
    ax.set_xlabel("contagem"); ax.set_xlim(0, 13500)
    ax.xaxis.set_major_formatter(virgula(0)); ax.tick_params(length=0)
    ax.annotate("60 observações em falta\n(eletricidade, 2021-11 e 2026-07)", (11955, y[1]),
                xytext=(0, -20), textcoords="offset points", fontsize=6.5, color=CINZA)
    ax.annotate("744 observações removidas\nem 251 dias (10,4 %)", (11467 - 744, y[3]),
                xytext=(0, -20), textcoords="offset points", fontsize=6.5, color=CINZA)
    guarda(ax)
    ax = axs[1]
    m = dd.copy(); m["mes"] = m.ts.values.astype("datetime64[M]")
    m["retido"] = (m.Q >= LIMIAR) & (m.E != 0) & m.E.notna()
    piv = m.pivot_table(index="vector_id", columns="mes", values="retido", aggfunc="mean")
    ordem = ["fuel_gas", "vapor_24bar", "vapor_10bar", "vapor_3bar", "energia_eletrica"]
    piv = piv.reindex(ordem)
    im = ax.imshow(piv.values, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_yticks(range(len(ordem))); ax.set_yticklabels([NOME[v] for v in ordem])
    cols = pd.DatetimeIndex(piv.columns)
    ticks = [i for i, c in enumerate(cols) if c.month == 1]
    ax.set_xticks(ticks); ax.set_xticklabels([str(cols[i].year) for i in ticks])
    ax.set_title("Fração de dias retidos por mês", loc="left", fontsize=7.5, color=CINZA)
    ax.tick_params(length=0)
    cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
    cb.outline.set_visible(False)
    cb.ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pt(100 * v, 0) + "%"))
    fig.tight_layout(w_pad=2.0)
    grava(fig, "cap6-amostra-e-filtros")


# ------------------------------------------------------------------- F18 --
# Matriz de decisao por candidato e par anual (T13/T14 + T12/T14 coverage).
PARES5 = ["2020->2021", "2021->2022", "2022->2023", "2023->2024", "2024->2025"]
PARES5_L = ["2020–21", "2021–22", "2022–23", "2023–24", "2024–25"]
# estados -> (cor, hachura)
C1_EST = {"positive_excludes_zero": ("#0072B2", None),
          "includes_zero":          ("#C8C8C8", None),
          "negative_excludes_zero": ("#D55E00", None)}
C2_EST = {"reference_within_ci":       ("#0072B2", None),
          "reference_excluded_below":  ("#C8C8C8", None),
          "reference_excluded_above":  ("#B37700", "///")}
NE = ("#FFFFFF", None)
BANDA_L = {"production": "produção",
           "route_a_gaussian": "A gaussiana", "route_a_empirical": "A empírica",
           "route_b_quantile": "B quantílica",
           "marginal_2sigma_rob": "marginal 2$\\sigma$",
           "route_a_gaussian_rob": "A gaussiana"}
EST_L = {"official_ols": "MQO", "huber": "Huber", "theil_sen": "Theil–Sen"}

def _celula(ax, x, y, estado, mapa, lado):
    cor, hat = mapa.get(estado, NE)
    ne = estado not in mapa
    x0 = x - 0.40 if lado == "esq" else x + 0.02
    r = Rectangle((x0, y - 0.38), 0.38, 0.76, facecolor=cor, edgecolor="#FFFFFF",
                  lw=0.5, hatch=hat, zorder=3)
    if hat: r.set_edgecolor("#7A5200")
    ax.add_patch(r)
    if ne:
        r.set_edgecolor(CINZA_C)
        ax.plot([x0 + 0.07, x0 + 0.31], [y - 0.26, y + 0.26], color=CINZA, lw=0.7, zorder=4)
        ax.plot([x0 + 0.07, x0 + 0.31], [y + 0.26, y - 0.26], color=CINZA, lw=0.7, zorder=4)

def f18_matriz():
    e2 = tsv("E2", "E2_bootstrap_sensitivity.tsv")
    e2 = e2[(e2.is_base == True) & (e2.null_id == "training_mean")
            & (e2.pair_id.isin(PARES5))]
    c1_ols = {(r.vector_id, r.pair_id): r.block_interval_status for r in e2.itertuples()}
    t14c1 = tsv("T14", "T14_c1.tsv")
    c1_rob = {(r.vector_id, r.estimator, r.pair_id):
              (r.interval_status if r.status == "estimated" else "NE")
              for r in t14c1.itertuples()}
    t12c = tsv("T12", "T12_coverage.tsv")
    c2 = {(r.vector_id, "official_ols", r.band_id, r.pair_id):
          (r.band_status if r.status == "estimated" else "NE") for r in t12c.itertuples()}
    t14c = tsv("T14", "T14_coverage.tsv")
    for r in t14c.itertuples():
        c2[(r.vector_id, r.estimator, r.band_id, r.pair_id)] = \
            r.band_status if r.status == "estimated" else "NE"

    cand = ([("official_ols", b) for b in
             ["production", "route_a_gaussian", "route_a_empirical", "route_b_quantile"]]
            + [("huber", b) for b in ["marginal_2sigma_rob", "route_a_gaussian_rob"]]
            + [("theil_sen", b) for b in ["marginal_2sigma_rob", "route_a_gaussian_rob"]])

    linhas = []          # (vetor, est, banda)
    for v in VEC4:
        for e, b in cand: linhas.append((v, e, b))
    nl = len(linhas)
    alt = 0.42 * nl + 3.4
    fig, ax = plt.subplots(figsize=(15.5 * CM, alt * CM))
    ax.set_xlim(-0.6, 9.05); ax.set_ylim(nl - 0.5 + 1.1, -1.9)
    ax.axis("off")

    for i, (v, e, b) in enumerate(linhas):
        if i % len(cand) == 0:                      # faixa do vetor
            ax.add_patch(Rectangle((-0.6, i - 0.5), 9.7, len(cand),
                                   facecolor="#F4F4F4" if (i // len(cand)) % 2 else "#FFFFFF",
                                   edgecolor="none", zorder=0))
            ax.text(-0.55, i - 0.5 + len(cand) / 2, NOME[v], va="center", ha="left",
                    rotation=90, fontsize=7.5, color=TINTA, zorder=2)
        ax.text(1.05, i, EST_L[e], va="center", ha="right", fontsize=6.6, color=TINTA, zorder=2)
        ax.text(1.15, i, BANDA_L[b], va="center", ha="left", fontsize=6.6, color=CINZA, zorder=2)
        n1 = n2 = 0
        for j, p in enumerate(PARES5):
            x = 3.4 + j
            s1 = c1_ols[(v, p)] if e == "official_ols" else c1_rob.get((v, e, p), "NE")
            s2 = c2.get((v, e, b, p), "NE")
            _celula(ax, x, i, s1, C1_EST, "esq")
            _celula(ax, x, i, s2, C2_EST, "dir")
            n1 += s1 == "positive_excludes_zero"
            n2 += s2 == "reference_within_ci"
        ax.text(8.62, i, f"{n1}/5 · {n2}/5", va="center", ha="right",
                fontsize=6.6, color=TINTA, zorder=2)
        for k, (n, xx) in enumerate(((n1, 8.72), (n2, 8.84))):
            ax.add_patch(Rectangle((xx, i - 0.22), 0.09, 0.44, zorder=3,
                                   facecolor="#0072B2" if n >= 4 else "#FFFFFF",
                                   edgecolor=CINZA if n < 4 else "#0072B2", lw=0.5))

    for j, p in enumerate(PARES5_L):
        ax.text(3.4 + j, -0.95, p, ha="center", va="bottom", fontsize=7, color=TINTA)
        ax.text(3.4 + j - 0.21, -0.62, "G", ha="center", va="bottom", fontsize=6, color=CINZA)
        ax.text(3.4 + j + 0.21, -0.62, "B", ha="center", va="bottom", fontsize=6, color=CINZA)
    ax.text(1.05, -0.95, "candidato", ha="right", va="bottom", fontsize=7, color=TINTA)
    ax.text(8.62, -0.95, "G · B", ha="right", va="bottom", fontsize=7, color=TINTA)
    ax.text(8.78, -0.95, "4/5", ha="center", va="bottom", fontsize=6.6, color=TINTA)
    ax.plot([-0.6, 9.05], [-0.5, -0.5], color="#444444", lw=0.6)

    leg = [("G: ganho demonstrado (IC $>$ 0)", "#0072B2", None),
           ("G: inconclusivo (IC contém 0)", "#C8C8C8", None),
           ("G: adverso (IC $<$ 0)", "#D55E00", None),
           ("B: cobertura compatível", "#0072B2", None),
           ("B: cobertura abaixo do nominal", "#C8C8C8", None),
           ("B: cobertura acima do nominal", "#B37700", "///"),
           ("não estimável", "#FFFFFF", "x")]
    y0 = nl + 0.30
    for k, (t, c, h) in enumerate(leg):
        cx = -0.55 + 3.15 * (k % 3); cy = y0 + 0.62 * (k // 3)
        r = Rectangle((cx, cy - 0.18), 0.30, 0.36, facecolor=c, lw=0.5,
                      edgecolor="#7A5200" if h == "///" else CINZA_C,
                      hatch=h if h == "///" else None, clip_on=False)
        ax.add_patch(r)
        if h == "x":
            ax.plot([cx + 0.05, cx + 0.25], [cy - 0.12, cy + 0.12], color=CINZA, lw=0.7, clip_on=False)
            ax.plot([cx + 0.05, cx + 0.25], [cy + 0.12, cy - 0.12], color=CINZA, lw=0.7, clip_on=False)
        ax.text(cx + 0.40, cy, t, va="center", ha="left", fontsize=6.6, color=TINTA, clip_on=False)
    ax.text(-0.55, y0 + 1.95, "Nenhum dos 32 candidatos reúne 4/5 nos dois critérios; "
            "com a regra de sensibilidade (3/5) também nenhum.",
            va="center", ha="left", fontsize=6.8, color=CINZA, clip_on=False)
    fig.tight_layout()
    grava(fig, "cap7-matriz-decisao")


# ------------------------------------------------- dependência residual --
def fdep_dependencia():
    a = tsv("D", "D1_dependence_functions.tsv")
    a = a[(a.period_scope == "complete_year") & (a.acf_status == "estimable") &
          (a.lag_days <= 21)]
    fig, axs = plt.subplots(2, 2, figsize=(15.5 * CM, 9.0 * CM), sharex=True, sharey=True)
    anos = sorted(a.year.unique())
    for ax, v in zip(axs.flat, VEC4):
        x = a[a.vector_id == v]
        for i, an in enumerate(anos):
            y = x[x.year == an].sort_values("lag_days")
            if not len(y): continue
            t = 0.28 + 0.72 * i / max(1, len(anos) - 1)
            ax.plot(y.lag_days, y.acf, color=COR[v], alpha=t, lw=1.0,
                    label=str(an) if v == "fuel_gas" else None)
        n = float(x.n_pairs.median())
        lim = 1.96 / np.sqrt(n)
        ax.axhspan(-lim, lim, color=CINZA_C, alpha=0.45, lw=0, zorder=0)
        ax.axhline(0, color=TINTA, lw=0.6)
        ax.set_title(NOME[v], loc="left", color=COR[v])
        ax.set_ylim(-0.25, 1.0); ax.set_xlim(0.5, 21.5)
        ax.yaxis.set_major_formatter(virgula(1)); guarda(ax)
    for ax in axs[1]: ax.set_xlabel("desfasamento (dias)")
    for ax in axs[:, 0]: ax.set_ylabel("autocorrelação do resíduo")
    h, l = axs.flat[0].get_legend_handles_labels()
    h.append(Rectangle((0, 0), 1, 1, color=CINZA_C, alpha=0.45))
    l.append("faixa compatível com independência")
    fig.tight_layout(h_pad=1.2, w_pad=2.0, rect=(0, 0.07, 1, 1))
    fig.legend(h, l, loc="lower center", ncols=len(l), frameon=False,
               bbox_to_anchor=(0.5, 0.0), handlelength=1.6, columnspacing=1.2)
    grava(fig, "cap6-dependencia-residuos")

# --------------------------------------------- rajadas e episódios -------
def _z_fora_amostra(v, treino, aplica):
    """Resíduos padronizados do ano de aplicação face à reta do ano de treino.
    Reproduz exatamente a banda de produção (2 sigma): verificado contra E4."""
    d = painel(); b = fits()
    r = b[(b.vector_id == v) & (b.ano_baseline == treino)].iloc[0]
    x = d[(d.vector_id == v) & (d.ano == aplica) & (d.Q >= LIMIAR) & (d.E != 0)].copy()
    x["z"] = (x.E - (r.slope * x.Q + r.intercept)) / r.sigma
    return x.sort_values("ts")

def f14b_rajadas():
    casos = [("fuel_gas", 2020, 2021), ("vapor_3bar", 2021, 2022)]
    ar = tsv("E4", "E4_alarm_runs.tsv")
    ar = ar[ar.scope == "confirmatory"]
    fig = plt.figure(figsize=(15.5 * CM, 11.0 * CM))
    gs = fig.add_gridspec(3, 1, height_ratios=[1, 1, 1.45], hspace=0.68)
    for k, (v, tr, ap) in enumerate(casos):
        ax = fig.add_subplot(gs[k])
        x = _z_fora_amostra(v, tr, ap)
        fora = x.z.abs() > 2
        ax.axhspan(-2, 2, color=CINZA_C, alpha=0.40, lw=0, zorder=0)
        ax.plot(x.ts, x.z, color=CINZA, lw=0.7, zorder=2)
        ax.scatter(x.ts[fora], x.z[fora], s=5, color=COR[v], lw=0, zorder=3)
        ax.axhline(0, color=TINTA, lw=0.6)
        ax.set_title(f"{NOME[v]}: referência de {tr} aplicada a {ap} — "
                     f"{pt(int(fora.sum()))} de {pt(len(x))} dias fora da banda",
                     loc="left", fontsize=8)
        ax.set_ylabel("resíduo\npadronizado")
        ax.yaxis.set_major_formatter(virgula(0)); guarda(ax)
    ax = fig.add_subplot(gs[2])
    for v in VEC4:
        y = ar[ar.vector_id == v]
        ax.scatter(y.independence_mean_run_length, y.mean_run_length, s=18,
                   color=COR[v], lw=0.4, edgecolor="white", zorder=3, label=NOME[v])
        for _, r in y.iterrows():
            if r.mean_run_length >= 4.5:
                dir = r.independence_mean_run_length > 2.2
                ax.annotate(f"{r.pair_id.replace('->', '→')} (máx. {pt(r.max_run_length)} d)",
                            (r.independence_mean_run_length, r.mean_run_length),
                            xytext=(-6 if dir else 6, 0), textcoords="offset points",
                            fontsize=6.2, color=CINZA, va="center",
                            ha="right" if dir else "left")
    ax.plot([1.0, 3.3], [1.0, 3.3], color=TINTA, lw=0.7, ls=(0, (3, 2)), zorder=1)
    ax.annotate("igualdade: alarmes isolados", (3.25, 3.25), xytext=(0, 5),
                textcoords="offset points", fontsize=6.5, color=CINZA, ha="right")
    ax.set_xlim(0.9, 3.45); ax.set_ylim(0.6, 9.4)
    ax.set_xlabel("comprimento médio de sequência esperado sob independência (dias)")
    ax.set_ylabel("comprimento médio\nobservado (dias)")
    ax.xaxis.set_major_formatter(virgula(1)); ax.yaxis.set_major_formatter(virgula(0))
    ax.legend(frameon=False, ncols=4, fontsize=7, loc="upper center",
              bbox_to_anchor=(0.5, -0.30))
    guarda(ax)
    fig.tight_layout()
    grava(fig, "cap6-rajadas-e-episodios")

FIGS = {"f08": f08_validacao, "f10": f10_amostra, "f11": f11_dispersao, "f12": f12_ganho,
        "f13": f13_predicoes, "f14": f14_cobertura, "f15": f15_acoplamento,
        "f16": f16_sensibilidade, "f18": f18_matriz, "fdep": fdep_dependencia, "f14b": f14b_rajadas, "f19": f19_injeccao, "f20": f20_deteccao}
if __name__ == "__main__":
    alvos = sys.argv[1:] or list(FIGS)
    for a in alvos: FIGS[a]()
