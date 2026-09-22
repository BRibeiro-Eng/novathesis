#!/usr/bin/env python3
"""Tabelas do Apendice C a partir das corridas canonicas de baselines-cc (2026-09-17).
Le apenas os TSV pinados em config/params.yaml; nao recalcula nada. Escreve apC-t*.tex."""
import os, sys, pandas as pd, numpy as np

_c = [os.path.expanduser(x) for x in ("~/LocalResearch/baselines-cc/outputs", "~/mnt/LocalResearch/baselines-cc/outputs")]
R = next(x for x in _c if os.path.isdir(x))
_o = [os.path.expanduser(x) for x in ("~/Desktop/Tese/novathesis/3-BackMatter", "~/mnt/novathesis/3-BackMatter")]
OUT = next(x for x in _o if os.path.isdir(x))
RUNS = {"E2": "E2/runs/20260828T153423377266Z-7926b7afbe338986221d",
        "E3": "E3/runs/20260829T122639790978Z-aa3e341622b4",
        "E4": "E4/runs/20260829T135121261692Z-2ea18e7390bb",
        "E6": "E6/runs/20260829T153020733605Z-ccd0312d97b3",
        "D": "D1-D9/runs/20260829T182000032463Z-1dde8c0c7d78",
        "SENS": "SENS/runs/20260829T195138387361Z-e068552161d2"}
VEC = {"fuel_gas": "Fuel gás", "vapor_24bar": "Vapor 24 bar", "vapor_10bar": "Vapor 10 bar",
       "vapor_3bar": "Vapor 3 bar", "energia_eletrica": "Eletricidade"}
NULL = {"training_mean": "média do treino", "seasonal_persistence": "mesmo dia do ano anterior",
        "moving_average_30d": "média móvel 30 d", "training_month_mean": "média mensal do treino",
        "same_month_previous_year": "mês homólogo", "previous_month": "mês anterior"}
STAT = {"positive_excludes_zero": "+", "negative_excludes_zero": "$-$", "includes_zero": "0",
        "not_estimable": "NE", "reference_excluded_below": "sub", "reference_excluded_above": "sobre",
        "reference_within_interval": "inclui", "estimable": "", "degenerate": "deg.",
        "diagnostic_only": "diag.", "diagnostic_ytd": "diag.", "incremental_confirmed": "+",
        "incremental_negative": "$-$", "no_incremental_evidence": "0",
        "not_estimable_threshold": "NE", "insufficient_data": "n.d."}
def st(x):
    if not isinstance(x, str): return "---"
    return STAT.get(x, x.replace("_", " "))
def f(x, n=2):
    if x is None or (isinstance(x, float) and not np.isfinite(x)): return "---"
    s = f"{abs(x):,.{n}f}".replace(",", "\\,").replace(".", ",")
    return ("$-$" if x < 0 else "") + s
def pair(p): return p.replace("->", "$\\to$")
def ic(lo, hi, n=2):
    if lo is None or hi is None or not np.isfinite(lo) or not np.isfinite(hi): return "---"
    return "[" + f(lo, n) + "; " + f(hi, n) + "]"
def tsv(run, name): return pd.read_csv(os.path.join(R, RUNS[run], name), sep="\t")
def write(fn, head, body, caption, label, colspec, short=None, size="footnotesize"):
    L = [f"%% Gerado por _gerador/apendice_c.py (2026-09-17) das corridas canonicas. Nao editar a mao.",
         "{\\" + size, f"\\begin{{xltabular}}{{\\linewidth}}{{{colspec}}}",
         f"\\caption[{short or caption[:60]}]{{{caption}}}\\label{{{label}}}\\\\",
         "\\toprule", head, "\\midrule", "\\endfirsthead", "\\toprule", head, "\\midrule", "\\endhead",
         "\\bottomrule", "\\endfoot"] + body + ["\\end{xltabular}", "}"]
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(fn, len(body))

# ---- C1: parametros anuais oficiais (D8) --------------------------------------
d = tsv("D", "D8_physical_plausibility.tsv")
d = d[d.period_scope == "complete_year"].sort_values(["vector_id", "year"])
body = [f"{VEC[r.vector_id]} & {int(r.year)} & {int(r.n_obs)} & {f(r.slope,3)} & {f(r.intercept,1)} & {f(r.sigma,2)} & {f(r.r2,3)} & {f(r.q_min,1)}--{f(r.q_max,1)} \\\\"
        for r in d.itertuples()]
write("apC-t1.tex", "Vetor & Ano & $n$ & $\\hat a$ & $\\hat b$ & $\\hat\\sigma$ & $R^2$ & Carga (kt/d) \\\\", body,
      "Parâmetros das \\emph{baselines} oficiais replicadas, por vetor e ano civil completo (2020--2025). $\\hat a$ em t~GNE/d por kt/d, $\\hat b$ e $\\hat\\sigma$ em t~GNE/d. Corrida canónica dos diagnósticos descritivos.",
      "tab:apC-parametros", "@{}lrrrrrrr@{}", "Parâmetros anuais das baselines oficiais")

# ---- C2: E2 poder preditivo ---------------------------------------------------
e = tsv("E2", "E2_comparisons.tsv")
e = e.sort_values(["resolution", "vector_id", "pair_id", "null_id"])
body = []
for r in e.itertuples():
    ci = "---" if not np.isfinite(r.ci_lower) else f"[{f(r.ci_lower)}; {f(r.ci_upper)}]"
    body.append(f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {NULL[r.null_id]} & {int(r.n_eval)} & {f(r.model_mae)} & {f(r.null_mae)} & {f(r.delta_mae)} & {ci} & {f(r.skill_mae,3)} & {st(r.interval_status)} \\\\")
write("apC-t2.tex", "Vetor & Par & Comparador & $n$ & MAE mod. & MAE nulo & $\\Delta$MAE & IC 95\\% & \\emph{skill} & Est. \\\\", body,
      "Poder preditivo (E2): diferença emparelhada de perda absoluta entre o modelo do ano de treino e cada comparador, no ano seguinte, com intervalo percentil por \\emph{bootstrap} de blocos móveis (bloco base). Est.: $+$ o intervalo exclui zero pelo lado positivo, $-$ pelo negativo, 0 contém zero, NE não estimável. As últimas linhas são a resolução mensal da eletricidade. Unidades: t~GNE/d (MWh na eletricidade).",
      "tab:apC-e2", "@{}llp{2.6cm}rrrrlrl@{}", "Poder preditivo por vetor, par e comparador")

# ---- C3: E2 sensibilidade a blocos -------------------------------------------
s = tsv("E2", "E2_bootstrap_sensitivity.tsv")
s["st"] = s.block_interval_status.map(st)
p = s.pivot_table(index=["vector_id", "pair_id", "null_id"], columns="block_length", values="st", aggfunc="first")
def cell(v):
    v = str(v)
    return "---" if v in ("nan", "None", "") else v
body = [f"{VEC[i[0]]} & {pair(i[1])} & {NULL[i[2]]} & " + " & ".join(cell(p.loc[i, c]) for c in p.columns) + " \\\\" for i in p.index]
write("apC-t3.tex", "Vetor & Par & Comparador & " + " & ".join(f"{c}~d" for c in p.columns) + " \\\\", body,
      "Sensibilidade do intervalo do ganho preditivo ao comprimento do bloco do \\emph{bootstrap} (E2). Mesma convenção de estatuto da Tabela~\\ref{tab:apC-e2}. As colunas de 6 e 8 dias são blocos base, que dependem do número de observações do par ($\\lceil n^{1/3}\\rceil$); ``---'' significa que esse comprimento não se aplica ao par.",
      "tab:apC-e2-blocos", "@{}llp{2.6cm}" + "c" * len(p.columns) + "@{}", "Ganho preditivo: sensibilidade ao bloco")

# ---- C4: E3 testes e sensibilidades ------------------------------------------
t = tsv("E3", "E3_tests.tsv")
body = [f"{VEC[r.vector_id]} & {'declives' if 'slope' in r.hypothesis else 'níveis'} & {f(r.statistic,1)} & {f(r.p_value,4)} & {f(r.p_bh,4)} & {f(r.p_by,4)} \\\\" for r in t.sort_values(['hypothesis','vector_id']).itertuples()]
write("apC-t4.tex", "Vetor & Família & $W$ & $p$ & $q_{\\mathrm{BH}}$ & $q_{\\mathrm{BY}}$ \\\\", body,
      "Estabilidade (E3): testes de Wald com covariância HAC para a igualdade dos declives e dos níveis anuais, 2020--2025, com correção de Benjamini--Hochberg dentro de cada família e Benjamini--Yekutieli como verificação.",
      "tab:apC-e3", "@{}llrrrr@{}", "Testes de igualdade dos declives e dos níveis")
bw = tsv("E3", "E3_bandwidth_sensitivity.tsv")
body = [f"{VEC[r.vector_id]} & {f(r.multiplier,1)} & {f(r.bandwidth,2)} & {f(r.slope_statistic,1)} & {f(r.slope_p_value,4)} & {f(r.level_statistic,1)} & {f(r.level_p_value,4)} \\\\" for r in bw.itertuples()]
write("apC-t5.tex", "Vetor & Mult. & Largura & $W$ declives & $p$ & $W$ níveis & $p$ \\\\", body,
      "Sensibilidade dos testes de estabilidade à largura de banda HAC (multiplicadores $0{,}5\\times$ e $2\\times$ da regra de Andrews).",
      "tab:apC-e3-hac", "@{}lrrrrrr@{}", "Estabilidade: sensibilidade à largura de banda")
bs = tsv("E3", "E3_bootstrap_sensitivity.tsv")
p = bs.pivot_table(index=["vector_id", "hypothesis"], columns="block_length", values="p_value", aggfunc="first")
body = [f"{VEC[i[0]]} & {'declives' if 'slope' in i[1] else 'níveis'} & " + " & ".join(f(p.loc[i, c], 3) for c in p.columns) + " \\\\" for i in p.index]
write("apC-t6.tex", "Vetor & Família & " + " & ".join(f"{c}~d" for c in p.columns) + " \\\\", body,
      "Estabilidade: valor $p$ por \\emph{bootstrap} de blocos sob a hipótese nula, por comprimento de bloco. Sem ajustamento de multiplicidade.",
      "tab:apC-e3-blocos", "@{}ll" + "r" * len(p.columns) + "@{}", "Estabilidade: sensibilidade ao bloco")

# ---- C5: E4 cobertura marginal ------------------------------------------------
c = tsv("E4", "E4_marginal_coverage.tsv")
body = [f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {int(r.n_obs)} & {int(r.n_alarms)} & {f(r.coverage,3)} & " +
        ("---" if not np.isfinite(r.mbb_lower) else f"[{f(r.mbb_lower,3)}; {f(r.mbb_upper,3)}]") + " & " +
        ("---" if not np.isfinite(r.binomial_lower) else f"[{f(r.binomial_lower,3)}; {f(r.binomial_upper,3)}]") +
        f" & {st(r.band_status)} \\\\" for r in c.itertuples()]
write("apC-t7.tex", "Vetor & Par & $n$ & Alarmes & Cobertura & IC MBB & IC binomial & Estatuto \\\\", body,
      "Calibração (E4): cobertura marginal da banda $\\pm2\\hat\\sigma$ do ano de treino aplicada ao ano seguinte, com intervalo por \\emph{bootstrap} de blocos e intervalo binomial (publicado só como contraste, porque assume independência). Estatuto face à referência de $0{,}9545$. As linhas 2025$\\to$2026 são diagnósticas.",
      "tab:apC-e4", "@{}llrrrlll@{}", "Cobertura marginal das bandas de alarme")
cc = tsv("E4", "E4_conditional_coverage.tsv")
cc = cc[cc.stratum_family != "load_tercile_x_semester"]
p = cc.pivot_table(index=["vector_id", "pair_id"], columns="stratum_id", values="coverage", aggfunc="first")
body = [f"{VEC[i[0]]} & {pair(i[1])} & " + " & ".join(f(p.loc[i, c], 3) for c in p.columns) + " \\\\" for i in p.index]
write("apC-t8.tex", "Vetor & Par & " + " & ".join(p.columns) + " \\\\", body,
      "Cobertura condicional (E4) por tercil de carga (T1--T3) e por semestre (S1, S2). A cobertura cruzada tercil$\\times$semestre está na corrida canónica.",
      "tab:apC-e4-cond", "@{}ll" + "r" * len(p.columns) + "@{}", "Cobertura condicional por tercil e semestre")
ar = tsv("E4", "E4_alarm_runs.tsv")
body = [f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {int(r.n_alarms)} & {f(r.alarm_rate,3)} & {int(r.n_runs)} & {f(r.mean_run_length,1)} & {int(r.max_run_length)} & {f(r.median_alarm_gap_days,1)} & {f(r.independence_mean_run_length,2)} \\\\" for r in ar.itertuples()]
write("apC-t9.tex", "Vetor & Par & Alarmes & Taxa & Rajadas & Compr.\\ médio & Máx. & Intervalo mediano & Compr.\\ sob indep. \\\\", body,
      "Rajadas de alarme (E4): número de sequências de dias consecutivos fora da banda, comprimento médio e máximo, intervalo mediano entre alarmes e comprimento médio esperado se os dias fossem independentes.",
      "tab:apC-e4-rajadas", "@{}llrrrrrrr@{}", "Rajadas de alarme")
bsh = tsv("E4", "E4_band_shape.tsv")
body = [f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {f(r.sigma_train,2)} & {f(r.constant_half_width,2)} & {f(r.half_width_q_min,2)} & {f(r.half_width_q_median,2)} & {f(r.half_width_q_max,2)} \\\\" for r in bsh.itertuples()]
write("apC-t10.tex", "Vetor & Par & $\\hat\\sigma$ & Banda constante & \\multicolumn{3}{c}{Intervalo de predição (mín., mediana, máx.\\ da carga)} \\\\", body,
      "Forma da banda (E4): meia-largura da banda constante $\\pm2\\hat\\sigma$ contra a meia-largura de um intervalo de predição clássico, que cresce com a distância à carga média do treino. O intervalo de predição é um comparador homocedástico e independente, não uma banda validada.",
      "tab:apC-e4-forma", "@{}llrrrrr@{}", "Forma da banda contra o intervalo de predição")

# ---- C6: E6 covariaveis -------------------------------------------------------
sk = tsv("E6", "E6_skill.tsv")
body = [f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {int(r.n_obs)} & {f(r.mae_baseline)} & {f(r.mae_augmented)} & {f(r.delta_mae)} & {ic(r.delta_lower, r.delta_upper)} & {f(r.skill_fraction,3)} & {st(r.skill_status)} \\\\" for r in sk.itertuples()]
write("apC-t11.tex", "Vetor & Par & $n$ & MAE $Q$ & MAE $Q+Z$ & $\\Delta$MAE & IC 95\\% & fração & Est. \\\\", body,
      "Valor incremental das covariáveis (E6): erro absoluto médio no ano seguinte com carga apenas e com carga mais densidade e condições de \\emph{flash}, nos mesmos dias, com intervalo por \\emph{bootstrap} de blocos.",
      "tab:apC-e6", "@{}llrrrrlrl@{}", "Valor incremental das covariáveis")
cs = tsv("E6", "E6_coverage_secondary.tsv")
body = [f"{VEC[r.vector_id]} & {pair(r.pair_id)} & {f(r.coverage_baseline,3)} & {f(r.coverage_augmented,3)} & {f(r.delta_coverage,3)} & {ic(r.delta_lower, r.delta_upper, 3)} \\\\" for r in cs.itertuples()]
write("apC-t12.tex", "Vetor & Par & Cobertura $Q$ & Cobertura $Q+Z$ & $\\Delta$ & IC 95\\% \\\\", body,
      "Comparação secundária de cobertura (E6): cobertura da banda dos dois modelos encaixados nos mesmos dias.",
      "tab:apC-e6-cobertura", "@{}llrrrl@{}", "Cobertura das bandas dos modelos encaixados")
mo = tsv("E6", "E6_models.tsv")
body = [f"{VEC[r.vector_id]} & {int(r.train_year)} & {'$Q$' if r.model_id=='q_only' else '$Q+Z$'} & {int(r.n_obs)} & {f(r.sigma,2)} & {f(r.intercept,1)} & {f(r.coef_q,3)} & {f(r.coef_ro_carga,1)} & {f(r.coef_fz_temp,3)} & {f(r.coef_fz_press,2)} \\\\" for r in mo.sort_values(['vector_id','train_year','model_id']).itertuples()]
write("apC-t13.tex", "Vetor & Treino & Modelo & $n$ & $\\hat\\sigma$ & $\\hat b$ & $Q$ & densidade & temp.\\ \\emph{flash} & pressão \\emph{flash} \\\\", body,
      "Coeficientes estimados dos modelos encaixados (E6), por vetor e ano de treino. Os coeficientes das covariáveis mudam de sinal entre anos em vários vetores.",
      "tab:apC-e6-coef", "@{}lllrrrrrrr@{}", "Coeficientes dos modelos com covariáveis", size="scriptsize")

# ---- C7: diagnosticos descritivos --------------------------------------------
d1 = tsv("D", "D1_serial_metrics.tsv"); d2 = tsv("D", "D2_variance_metrics.tsv"); d3 = tsv("D", "D3_distribution.tsv")
m = d1.merge(d2, on=["vector_id", "year", "period_scope"], suffixes=("", "_v")).merge(d3, on=["vector_id", "year", "period_scope"], suffixes=("", "_d"))
m = m[m.period_scope == "complete_year"].sort_values(["vector_id", "year"])
body = [f"{VEC[r.vector_id]} & {int(r.year)} & {int(r.n_obs)} & {f(r.rho1,2)} & {f(r.durbin_watson,2)} & {f(r.ljung_box_7_p_value_descriptive,3)} & {f(r.bp_p_value_descriptive,3)} & {f(r.arch_p_value_descriptive,3)} & {f(r.skewness,2)} & {f(r.kurtosis_excess,2)} \\\\" for r in m.itertuples()]
write("apC-t14.tex", "Vetor & Ano & $n$ & $\\rho_1$ & DW & LB(7) & BP & ARCH & assim. & curtose \\\\", body,
      "Diagnósticos descritivos dos resíduos (D1--D3), por vetor e ano civil completo: autocorrelação de primeira ordem em desfasamento civil, estatística de Durbin--Watson, e valores $p$ de Ljung--Box, Breusch--Pagan e ARCH. Estes valores $p$ são calculados sob independência, que os próprios diagnósticos mostram não valer: são contraste técnico, sem interpretação inferencial.",
      "tab:apC-d123", "@{}lrrrrrrrrr@{}", "Diagnósticos descritivos dos resíduos")
d6 = tsv("D", "D6_support.tsv")
FEAT = {"Q": "carga", "ro_carga": "densidade", "fz_temp": "temp.\\ \\emph{flash}", "fz_press": "pressão \\emph{flash}"}
d6 = d6[d6.period_scope == "complete_year"] if "complete_year" in set(d6.period_scope) else d6
body = [f"{FEAT.get(r.feature, r.feature.replace('_',' '))} & {pair(r.pair_id)} & {int(r.n_train)} & {int(r.n_apply)} & {f(r.density_overlap,3)} & [{f(r.density_overlap_mbb_lower,3)}; {f(r.density_overlap_mbb_upper,3)}] & {f(r.application_fraction_in_train_central,3)} \\\\" for r in d6.sort_values(['feature','pair_id']).itertuples()]
write("apC-t15.tex", "Variável & Par & $n$ treino & $n$ aplicação & \\emph{Overlap} & IC 95\\% & Fração na zona central \\\\", body,
      "Suporte entre anos (D6): índice de sobreposição das densidades de cada variável explicativa entre o ano de treino e o de aplicação, e fração dos dias de aplicação dentro do intervalo central do treino.",
      "tab:apC-d6", "@{}llrrrlr@{}", "Sobreposição de suporte entre anos")
d9 = tsv("D", "D9_correlations.tsv")
d9 = d9[d9.period_scope == "complete_year"] if "complete_year" in set(d9.period_scope) else d9
body = [f"{VEC.get(r.vector_a, r.vector_a)} & {VEC.get(r.vector_b, r.vector_b)} & {str(r.scope_id).replace('_',' ')} & {int(r.n_obs)} & {f(r.pearson,2)} & {f(r.spearman,2)} \\\\" for r in d9.itertuples()]
write("apC-t16.tex", "Vetor A & Vetor B & Âmbito & $n$ & Pearson & Spearman \\\\", body,
      "Correlação cruzada dos resíduos padronizados entre vetores (D9), por ano e no agregado dos anos completos.",
      "tab:apC-d9", "@{}lllrrr@{}", "Correlação dos resíduos entre vetores")

# ---- C8: sensibilidade --------------------------------------------------------
sg = tsv("SENS", "SENS_grid.tsv")
g = sg.groupby(["endpoint", "cell_id"]).agg(n=("survives", "size"), muda=("survives", lambda x: int((~x.astype(bool)).sum()))).reset_index()
def celula(cid):
    mult, _, jan = cid.partition("_")
    mult = mult.replace("x", "").replace(".", ",")
    jan = "ano civil" if jan == "ano_civil" else "janela móvel de 12 meses"
    return f"${mult}\\times$, {jan}"
body = [f"{r.endpoint} & {celula(r.cell_id)} & {int(r.n)} & {int(r.muda)} \\\\" for r in g.itertuples()]
write("apC-t17.tex", "\\emph{Endpoint} & Célula & Reavaliações & Mudam de rótulo \\\\", body,
      "Grelha de sensibilidade: número de reavaliações por \\emph{endpoint} e célula (limiar de carga $\\times$ esquema de janela) e quantas mudam de rótulo face à célula de referência ($1\\times$, ano civil).",
      "tab:apC-sens", "@{}llrr@{}", "Grelha de sensibilidade às convenções")
