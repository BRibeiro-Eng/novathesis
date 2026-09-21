#!/usr/bin/env python3
"""Mapa de evidência do Corpus B (Cap. 3, figura F05) — PROTÓTIPO para decidir o desenho.

Uma linha por artigo cartografado, agrupada por setor; colunas = o que o estudo declara sobre
fronteira, validade temporal, validação, avaliação de adaptações e partilha. Nível V0 (extração
assistida, sem verificação humana) até existir v1_overrides_*.json.
Regra de agregação por artigo (modelo -> artigo): o nível MAIS declarado entre os modelos.
"""
import argparse, csv, glob, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
V = lambda e: e.get("value") if isinstance(e, dict) else e
CLOSE = {"refinery — model empirically applied there", "petrochemical — model empirically applied there"}
SECT = {"petroleum refining": "Refinação", "petrochemicals": "Petroquímica", "cement, lime, clinker": "Cimento e cal",
        "steel and primary metals": "Aço e metais primários", "pulp & paper": "Pasta e papel", "glass": "Vidro",
        "continuous chemical production": "Química contínua", "industrial gases": "Gases industriais",
        "multiple of the above": "Vários setores", "not one of the registered sectors": "Outro"}
ORDER = ["Refinação", "Petroquímica", "Química contínua", "Gases industriais", "Cimento e cal",
         "Aço e metais primários", "Pasta e papel", "Vidro", "Vários setores", "Outro"]
NA = -1
COLS = [
    ("Fronteira\nmedida", "C5", "exata · alocada · reconhece desvio"),
    ("Re-\nestimação", "C6", "executada · declarada"),
    ("Domínio\nde validade", "C7", "numérico · qualitativo"),
    ("Ajuste\nno treino", "C8", "reportado"),
    ("Fora da\namostra", "C8", "reportada"),
    ("Adaptação\n(estado)", "SQ3", "avaliada · implementada · proposta"),
    ("Dados ou\ncódigo", "C13", "código · dados · dados parciais"),
]


def levels(r):
    models = [m for a in r["applications"] for m in a["models"]]
    b = {"exact": 3, "allocated by rule": 2, "allocated by estimate": 2, "mismatch acknowledged": 1}
    c5 = max([b.get(c.get("boundary_correspondence"), 0) for m in models for c in m.get("C5_measurement") or []] or [0])
    c6 = 0
    for m in models:
        reg, st = V(m["C6_re_estimation"]["regime"]), V(m["C6_re_estimation"]["update_status"])
        if reg not in ("fixed, not mentioned", "not stated"):
            c6 = max(c6, 3 if st == "executed" else 2)
    c7 = max([{"stated with numeric bounds": 3, "stated qualitatively": 2}.get(V(m["C7_validity_envelope"]["statement"]), 0) for m in models] or [0])

    def c8(block, lvl):
        vals = [V(m["C8_metrics"][block]["status"]) for m in models]
        if all(v == "not applicable" for v in vals):
            return NA
        return lvl if "reported" in vals else 0
    ins, oos = c8("in_sample_fit", 2), c8("out_of_sample_validation", 3)
    ad = max([{"evaluated": 3, "implemented": 2, "proposed": 1}[d["status"]] for d in r["adaptations"]] or [0])
    c13 = r["C13_reproducibility"]
    rep = 3 if V(c13["code_available"]) in ("yes", "partial") else 2 if V(c13["data_available"]) == "yes" else 1 if V(c13["data_available"]) == "partial" else 0
    return [c5, c6, c7, ins, oos, ad, rep]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--decisoes")
    ap.add_argument("--out", default=f"{HERE}/mapa_evidencia_PROTOTIPO.png")
    a = ap.parse_args()
    meta = {}
    with open(f"{ROOT}/data/articles.csv", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            k = row["key"] if row["key"].startswith("rayyan-") else f"rayyan-{row['key']}"
            meta[k] = ((row.get("authors") or "?").split(";")[0].split(",")[0].strip(), row.get("year") or "s.d.")
    rows = []
    recs = {os.path.basename(p)[:-5]: json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(f"{ROOT}/production/stage_c/claude/outputs/rayyan-*.json"))}
    if a.decisoes:
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(HERE), "verification_v1"))
        from overlay import effective
        recs, _ = effective(recs, a.decisoes)
    for k, r in recs.items():
        if k in a.exclude:
            continue
        sec = SECT.get(V(r["applications"][0]["sector_registered"]), "Outro")
        close = any(V(x.get("refinery_or_petrochemical_case")) in CLOSE for x in r["applications"])
        au, yr = meta.get(k, ("?", "?"))
        rows.append((ORDER.index(sec), sec, int(yr) if str(yr).isdigit() else 0, f"{au} {yr}", close, levels(r)))
    rows.sort(key=lambda x: (x[0], x[2], x[3]))
    seen = {}
    for r in rows:
        seen[r[3]] = seen.get(r[3], 0) + 1
    cnt = {}
    for i, r in enumerate(rows):
        if seen[r[3]] > 1:
            cnt[r[3]] = cnt.get(r[3], 0) + 1
            rows[i] = r[:3] + (r[3] + "abcdef"[cnt[r[3]] - 1],) + r[4:]

    shade = {0: "#E9E9E9", 1: "#C6DBEF", 2: "#6BAED6", 3: "#08519C"}
    n, m = len(rows), len(COLS)
    groups = [s for s in ORDER if any(r[1] == s for r in rows)]
    gap = 0.6
    fig_h = 1.9 + 0.2 * n + 0.2 * len(groups)
    fig, ax = plt.subplots(figsize=(6.3, fig_h * 0.92))
    ax.set_xlim(-2.9, m); ax.axis("off")
    y, ypos, cur = 0, [], None
    for r in rows:
        if r[1] != cur:
            if cur is not None:
                y += gap
            ax.text(-2.85, y + 0.15, r[1], fontsize=6.4, fontweight="bold", color="#222222", va="center")
            y += 0.95; cur = r[1]
        ypos.append(y); y += 1
    ax.set_ylim(y + 2.2, -3.0)
    for (lab, code, key), j in zip(COLS, range(m)):
        ax.text(j + 0.5, -1.9, lab, ha="center", va="center", fontsize=5.4, color="#222222", fontweight="bold", linespacing=1.0)
        ax.text(j + 0.5, -0.55, code, ha="center", va="center", fontsize=5, color="#666666")
    for yy, r in zip(ypos, rows):
        ax.text(-2.7, yy + 0.5, ("◆ " if r[4] else "   ") + r[3], fontsize=5.6, va="center", color="#222222")
        for j, v in enumerate(r[5]):
            if v == NA:
                ax.add_patch(Rectangle((j + 0.04, yy + 0.06), 0.92, 0.88, facecolor="white", edgecolor="#BBBBBB",
                                       hatch="////", linewidth=0.4))
            else:
                ax.add_patch(Rectangle((j + 0.04, yy + 0.06), 0.92, 0.88, facecolor=shade[v], edgecolor="white", linewidth=1.0))
    # totals
    for j in range(m):
        vals = [r[5][j] for r in rows]
        k2 = sum(v >= 2 for v in vals); na = sum(v == NA for v in vals)
        ax.text(j + 0.5, y + 0.7, f"{k2}/{n - na}", ha="center", fontsize=5.6, color="#222222")
    ax.text(-2.7, y + 0.7, "Nos dois níveis mais escuros", fontsize=5.6, color="#222222")
    lx = -2.7
    for lvl, txt in ((3, "nível mais forte"), (2, "declarado"), (1, "parcial / proposto"), (0, "não reportado"), (NA, "não aplicável")):
        if lvl == NA:
            ax.add_patch(Rectangle((lx, y + 1.45), 0.35, 0.55, facecolor="white", edgecolor="#BBBBBB", hatch="////", linewidth=0.4))
        else:
            ax.add_patch(Rectangle((lx, y + 1.45), 0.35, 0.55, facecolor=shade[lvl], edgecolor="none"))
        ax.text(lx + 0.45, y + 1.75, txt, fontsize=5.0, va="center", color="#444444")
        lx += 0.45 + 0.075 * len(txt) + 0.3

    fig.savefig(a.out, dpi=200, bbox_inches="tight")
    print("ok", a.out, n, "artigos")


if __name__ == "__main__":
    main()
