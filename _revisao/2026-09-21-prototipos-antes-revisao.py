#!/usr/bin/env python3
"""Protótipos para a secção 3.3.3; não altera as figuras usadas na tese.

Fonte: tabelas congeladas do Corpus A em LocalResearch/Screening.
Coordenadas: LABEL_X/LABEL_Y do Natural Earth Admin 0, 1:110m.
"""
from __future__ import annotations

import ast
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


HERE = Path(__file__).resolve().parent
TABLES = Path.home() / "LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables"
BLUE = "#2F6D96"
CYAN = "#5FB0D0"
SAND = "#B87932"
GRAY = "#CFCFCF"
INK = "#1A1A1A"
MUTED = "#666666"
EXCLUDE = {"Não aplicável", "Por normalizar: localização em texto"}


def data():
    annual = pd.read_csv(TABLES / "annual.csv", encoding="utf-8-sig", index_col=0)
    annual.index = annual.index.astype(int)
    papers = pd.read_csv(TABLES / "analysis_dataset.csv", encoding="utf-8-sig")
    points = pd.read_csv(HERE / "country_points.csv")
    by_country = defaultdict(list)
    by_period = defaultdict(Counter)
    for row in papers.itertuples():
        countries = ast.literal_eval(row.countries_case)
        for country in countries:
            if country not in EXCLUDE:
                by_country[country].append(int(row.year))
                by_period[period(int(row.year))][country] += 1
    assert len(papers) == 331
    assert len(by_country) == 45 and sum(map(len, by_country.values())) == 126
    assert len(set(by_country).difference(points.country)) == 0
    return annual, papers, points, by_country, by_period


def period(year):
    if year <= 2010:
        return "1997–2010"
    if year <= 2015:
        return "2011–2015"
    if year <= 2020:
        return "2016–2020"
    return "2021–2025"


def temporal(annual, papers):
    """Publicações anuais empilhadas por formato documental."""
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5, "pdf.fonttype": 42,
    })
    counts = pd.crosstab(papers.year, papers.document_type).reindex(
        annual.index, fill_value=0)
    journal = counts["journal article"].to_numpy()
    conference = counts["conference proceedings"].to_numpy()
    assert journal.sum() == 214 and conference.sum() == 117
    assert np.array_equal(journal + conference, annual.n.to_numpy())
    fig, ax = plt.subplots(figsize=(15 / 2.54, 7.2 / 2.54))
    years = annual.index.to_numpy()
    journal_bars = ax.bar(years, journal, width=.78, color=BLUE, zorder=3,
                          label="Artigos de revista (214)")
    ax.bar(years, conference, bottom=journal, width=.78, color=SAND,
           zorder=3, label="Comunicações em conferência (117)")
    journal_bars[-1].set_facecolor(GRAY)
    ax.set(xlim=(1996.3, 2027.8), ylim=(0, 40), ylabel="Publicações por ano",
           xlabel="Ano de publicação")
    ax.set_xticks([1997, 2001, 2005, 2009, 2013, 2017, 2021, 2025])
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.yaxis.grid(True, lw=.45, color="#E4E4E4")
    ax.set_axisbelow(True)
    # As barras agregam anos civis. As marcas ficam na fronteira após o ano
    # de publicação: 2012 e 2015 são os primeiros anos completos seguintes.
    for x, label in [(2011.5, "ISO 50001:2011"),
                     (2014.5, "ISO 50006:2014")]:
        ax.axvline(x, color="#777777", lw=.8, linestyle=(0, (4, 3)), zorder=2)
        ax.text(x + .11, 38.9, label, rotation=90, fontsize=7,
                color=MUTED, ha="left", va="top")
    ax.legend(frameon=False, loc="upper left", ncol=1,
              bbox_to_anchor=(.015, .91), fontsize=7.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="x", length=0, pad=5)
    fig.text(.965, .98, "2026: pesquisa até fevereiro; ano incompleto", color=MUTED,
             fontsize=7, ha="right", va="top")
    fig.subplots_adjust(left=.105, right=.965, bottom=.16, top=.88)
    fig.savefig(HERE / "01_evolucao_tipos.pdf")
    fig.savefig(HERE / "01_evolucao_tipos.png", dpi=260)
    plt.close(fig)


def geo_style(fig, *, domain=None):
    opts = dict(
        projection_type="natural earth", showcountries=True,
        countrycolor="#A5A5A5", countrywidth=.55,
        showcoastlines=False, showland=True, landcolor="#F6F7F7",
        showocean=True, oceancolor="white", showframe=False,
        lataxis_range=[-60, 85], lonaxis_range=[-180, 180],
        bgcolor="white",
    )
    if domain:
        opts["domain"] = domain
    fig.update_geos(**opts)


def marker_sizes(n):
    return [6 + 2.6 * np.sqrt(v) for v in n]


def map_overview(papers, points, by_country):
    p = points.copy()
    p["n"] = p.country.map(lambda c: len(by_country[c]))
    p["first"] = p.country.map(lambda c: min(by_country[c]))
    p["last"] = p.country.map(lambda c: max(by_country[c]))
    p["median"] = p.country.map(lambda c: float(np.median(by_country[c])))
    b_count = Counter()
    for row in papers.itertuples():
        if row.in_corpus_b:
            for country in ast.literal_eval(row.countries_case):
                if country not in EXCLUDE:
                    b_count[country] += 1
    p["b"] = p.country.map(lambda c: b_count[c])
    windows = [(1997, 2010), (2011, 2015), (2016, 2020), (2021, 2025)]

    def hover(row):
        counts = [sum(a <= y <= b for y in by_country[row.country])
                  for a, b in windows]
        breakdown = (f"1997–2010: {counts[0]} · 2011–2015: {counts[1]}"
                     f"<br>2016–2020: {counts[2]} · 2021–2025: {counts[3]}")
        return (f"<b>{row.country_pt}</b><br>Corpus A: {row.n} publicação(ões)"
                f"<br>Corpus B: {row.b}"
                f"<br>Primeiro / último registo: {row['first']} / {row['last']}"
                f"<br>Ano mediano: {row['median']:g}"
                f"<br>Publicações por período:<br>{breakdown}<extra></extra>")

    p["hover"] = p.apply(hover, axis=1)
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=p.lon, lat=p.lat, mode="markers", text=p.hover,
        hovertemplate="%{text}", showlegend=False,
        marker=dict(size=marker_sizes(p.n), color=p["first"],
                    colorscale=[[0, "#B9E4EC"], [.32, "#78BBD1"],
                                [.68, "#2F6D96"], [1, "#163D62"]],
                    cmin=1997, cmax=2025, opacity=.92,
                    line=dict(color="#2B5670", width=.55),
                    colorbar=dict(title=dict(text="Primeiro registo localizável", side="top",
                                             font=dict(size=12, color=MUTED)),
                                  orientation="h", x=.43, xanchor="center", y=-.055,
                                  len=.42, thickness=11, outlinewidth=0,
                                  tickvals=[1997, 2005, 2013, 2020, 2025],
                                  tickfont=dict(size=12, color=MUTED)))))
    for n in (1, 5, 15):
        fig.add_trace(go.Scattergeo(
            lon=[None], lat=[None], mode="markers", name=str(n),
            showlegend=True, hoverinfo="skip",
            marker=dict(size=marker_sizes([n])[0], color=BLUE,
                        line=dict(color="#2B5670", width=.55))))
    geo_style(fig)
    fig.update_layout(
        width=1200, height=630, margin=dict(l=24, r=24, t=95, b=76),
        paper_bgcolor="white", font=dict(family="STIXGeneral, Georgia, serif", size=14, color=INK),
        showlegend=True,
        legend=dict(title=dict(text="Publicações", font=dict(size=13, color=MUTED)),
                    x=.89, xanchor="left",
                    y=.97, yanchor="top", bgcolor="rgba(255,255,255,.75)",
                    font=dict(size=13, color=MUTED),
                    borderwidth=0),
        title=dict(text="Países atribuídos aos casos — Corpus A", x=.03, y=.975, font=dict(size=24)),
    )
    fig.add_annotation(
        x=.03, y=1.025, xref="paper", yref="paper", showarrow=False,
        text="Tamanho do ponto = publicações no país  ·  Tom = primeiro ano localizável neste corpus",
        xanchor="left", font=dict(size=14, color=MUTED))
    fig.add_annotation(
        x=.03, y=-.08, xref="paper", yref="paper", showarrow=False,
        text="120/331 publicações (36,3%) com país localizável · 126 atribuições em 45 países · Ponto = país, não instalação",
        xanchor="left", font=dict(size=12, color=MUTED))
    fig.write_image(HERE / "02_mapa_marcadores.pdf")
    fig.write_image(HERE / "02_mapa_marcadores.png", scale=2)
    fig.write_html(HERE / "02_mapa_interativo.html", include_plotlyjs=True,
                   full_html=True)


def map_periods(papers, points, by_period):
    labels = ["1997–2010", "2011–2015", "2016–2020", "2021–2025"]
    fig = make_subplots(rows=2, cols=2, specs=[[{"type": "geo"}, {"type": "geo"}],
                                              [{"type": "geo"}, {"type": "geo"}]],
                        horizontal_spacing=.02, vertical_spacing=.12)
    for i, label in enumerate(labels):
        counts = by_period[label]
        p = points[points.country.isin(counts)].copy()
        p["n"] = p.country.map(counts)
        p["hover"] = p.apply(lambda r: f"<b>{r.country_pt}</b><br>{r.n} publicação(ões) em {label}<extra></extra>", axis=1)
        row, col = divmod(i, 2)
        fig.add_trace(go.Scattergeo(
            lon=p.lon, lat=p.lat, mode="markers", text=p.hover,
            hovertemplate="%{text}", showlegend=False,
            marker=dict(size=marker_sizes(p.n), color=BLUE, opacity=.86,
                        line=dict(color="white", width=.5))), row=row+1, col=col+1)
        window = papers[papers.year.between(*map(int, label.split("–")))]
        located = sum(bool(ast.literal_eval(s)) and ast.literal_eval(s)[0] not in EXCLUDE
                      for s in window.countries_case)
        fig.add_annotation(x=[.255, .745][col], y=[.94, .44][row],
                           xref="paper", yref="paper", showarrow=False,
                           text=f"<b>{label}</b>  ·  país atribuído: {located}/{len(window)}",
                           font=dict(size=15, color=INK))
    geo_style(fig)
    for name in ("geo", "geo2"):
        fig.layout[name].domain.y = [.55, .88]
    for name in ("geo3", "geo4"):
        fig.layout[name].domain.y = [.06, .39]
    fig.update_layout(
        width=1500, height=890, margin=dict(l=20, r=20, t=70, b=65),
        title=dict(text="Países dos casos ao longo do período do Corpus A", x=.03, y=.98,
                   font=dict(size=23)),
        font=dict(family="STIXGeneral, Georgia, serif", size=13, color=INK),
        paper_bgcolor="white",
    )
    fig.add_annotation(x=.03, y=.012, xref="paper", yref="paper", showarrow=False,
                       xanchor="left", text="A cobertura geográfica difere entre períodos; 2026 excluído (apenas um registo, sem país atribuído).",
                       font=dict(size=12, color=MUTED))
    fig.write_image(HERE / "03_mapa_periodos.pdf")
    fig.write_image(HERE / "03_mapa_periodos.png", scale=2)


if __name__ == "__main__":
    if sys.argv[1:] == ["temporal"]:
        annual = pd.read_csv(TABLES / "annual.csv", encoding="utf-8-sig", index_col=0)
        annual.index = annual.index.astype(int)
        papers = pd.read_csv(TABLES / "analysis_dataset.csv", encoding="utf-8-sig")
        temporal(annual, papers)
    else:
        annual, papers, points, by_country, by_period = data()
        temporal(annual, papers)
        map_overview(papers, points, by_country)
        map_periods(papers, points, by_period)
    print("Protótipos gerados em", HERE)
