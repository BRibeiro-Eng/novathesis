#!/usr/bin/env python3
"""Prototipos para as caixas de revisao C3-V05, C3-V07 e C3-V08.

Nao altera nada na tese. Fonte: tabelas congeladas do Corpus A.
Paleta e tipografia iguais as figuras 3.3 a 3.6.
"""
import ast, collections, os
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
TABLES = Path.home()/"LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables"
FORTE, CLARO, AREIA, AUSENTE = "#2F6D96", "#5FB0D0", "#C8964A", "#CFCFCF"
TINTA, CINZA = "#1A1A1A", "#6E6E6E"
CM = 1/2.54
PENDENTE = "Por resolver / sem extração"
plt.rcParams.update({"font.family":"serif","font.serif":["STIXGeneral","DejaVu Serif"],
    "font.size":8,"axes.labelsize":8,"xtick.labelsize":7.5,"ytick.labelsize":7.5,
    "axes.linewidth":.6,"pdf.fonttype":42,"savefig.bbox":"tight","savefig.pad_inches":.02})

def lst(v):
    """Celulas escalares vem como texto simples; as multi-valor como lista JSON.
    Um valor por resolver vem vazio."""
    if v is None or (isinstance(v, float) and np.isnan(v)): return []
    t = str(v).strip()
    if t == "" or t.lower() == "nan": return []
    try:
        x = ast.literal_eval(t)
        return x if isinstance(x, list) else [x]
    except Exception:
        return [t]

papers = pd.read_csv(TABLES/"analysis_dataset.csv", encoding="utf-8-sig")
N = len(papers)

# ---------------------------------------------------------------- C3-V05 ---
def v05():
    """Grafico de unidades: cada quadrado e uma publicacao.

    Escolhido em vez das barras empilhadas porque o que a subseccao afirma --
    que a literatura e uma coleccao de casos isolados -- e uma afirmacao sobre
    quantas das 331 publicacoes sao o que, e um quadrado por publicacao torna
    isso literal. O bloco por resolver fica visivel em vez de somido.
    """
    campos = [
        ("Tipo de estudo", "paper_type", {
            "single applied case":"Caso aplicado único","multi-case study":"Estudo multi-caso",
            "review/synthesis":"Revisão ou síntese","tool/software design":"Ferramenta ou software",
            "methodological/theoretical":"Metodológico ou teórico",
            "maturity model or framework":"Modelo de maturidade"}),
        ("Tipo de organização", "type_of_organisation", {
            "discrete manufacturing":"Manufatura discreta","continuous process":"Processo contínuo",
            "buildings":"Edifícios","mixed":"Contextos mistos","services":"Serviços",
            "not specified":"Não especificado"}),
    ]
    COLS = 19
    fig, axs = plt.subplots(1, 2, figsize=(15.5*CM, 9.2*CM))
    for ax, (titulo, campo, rot) in zip(axs, campos):
        c = collections.Counter()
        for v in papers[campo]:
            vals = lst(v)
            c[rot.get(vals[0], vals[0]) if vals else PENDENTE] += 1
        assert sum(c.values()) == N
        ordem = [k for k, _ in c.most_common() if k != PENDENTE] + [PENDENTE]
        # Rampa ordenada em vez de seis matizes a competir: as categorias estao
        # ordenadas por frequencia e os blocos sao contiguos, portanto a cor so
        # tem de dar a ordem. O por resolver nao e um tom da rampa -- e um
        # quadrado vazio, porque ausencia lida melhor como vazio do que como cor
        # (e um cinzento claro seria indistinguivel do ultimo passo da rampa).
        rampa = ["#1F4E6E", "#2F6D96", "#4E8FB5", "#7DB3CF", "#A9CDE0", "#CFE3EE"]
        cor = {k: ("none" if k == PENDENTE else rampa[i % len(rampa)])
               for i, k in enumerate(ordem)}
        bordo = {k: ("#A9A9A9" if k == PENDENTE else "white") for k in ordem}
        seq = [k for k in ordem for _ in range(c[k])]
        for i, k in enumerate(seq):
            x, y = i % COLS, i // COLS
            ax.add_patch(Rectangle((x, -y), .84, .84, facecolor=cor[k],
                                   edgecolor=bordo[k], linewidth=.45))
        linhas = int(np.ceil(N/COLS))
        ax.set_xlim(-.4, COLS+.2); ax.set_ylim(-linhas+.2, 1.4)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(titulo, loc="left", fontsize=8.5, color=TINTA, pad=6)
        y0 = -linhas - .8
        for j, k in enumerate(ordem):
            yy = y0 - j*1.25
            ax.add_patch(Rectangle((0, yy), .84, .84, facecolor=cor[k],
                                   edgecolor=bordo[k], linewidth=.45, clip_on=False))
            ax.text(1.25, yy+.42, "%s — %d" % (k, c[k]), va="center", fontsize=7,
                    color=TINTA if k != PENDENTE else CINZA, clip_on=False)
    fig.savefig(HERE/"v05_unidades.pdf"); fig.savefig(HERE/"v05_unidades.png", dpi=260)
    plt.close(fig); print("v05 ok")

# ---------------------------------------------------------------- C3-V08 ---
def v08():
    """Cruzamento norma x protocolo, em vez de dois paineis marginais.

    Dois paineis separados diriam quantos artigos invocam a norma e quantos
    invocam um protocolo. A pergunta do capitulo e outra: entre os que invocam
    a norma, quantos invocam tambem um protocolo de medicao e verificacao. Isso
    so se ve no cruzamento.
    """
    def grupo_norma(v):
        x = lst(v)
        if not x: return PENDENTE
        if any(str(i).startswith("ISO 5000") for i in x): return "Família ISO 50001"
        if "none" in x: return "Nenhuma norma"
        return "Outra norma nomeada"
    def grupos_prot(v):
        """Devolve TODOS os protocolos nomeados, nao so o primeiro.

        A versao anterior escolhia um por ordem de prioridade e por isso as
        colunas da ASHRAE 14 e do SEP M&V ficavam abaixo das marginais do
        texto (5 e 3 contra 9 e 7): sete publicacoes nomeiam mais do que um
        protocolo. Agora uma publicacao entra em cada coluna que nomeia, as
        linhas nao somam, e a legenda tem de o dizer.
        """
        x = lst(v)
        if not x: return [PENDENTE]
        nomes = [i for i in x if i != "none"]
        if not nomes: return ["Nenhum"]
        conhecidos = {"IPMVP", "ASHRAE 14", "SEP M&V"}
        saida = [n for n in nomes if n in conhecidos]
        if len(saida) < len(nomes): saida.append("Outro nomeado")
        return saida or ["Outro nomeado"]
    linhas = ["Família ISO 50001", "Outra norma nomeada", "Nenhuma norma", PENDENTE]
    cols = ["Nenhum", "IPMVP", "ASHRAE 14", "SEP M&V", "Outro nomeado", PENDENTE]
    M = pd.DataFrame(0, index=linhas, columns=cols)
    for _, r in papers.iterrows():
        for g in grupos_prot(r.mv_protocol):
            M.loc[grupo_norma(r.ems_standard), g] += 1
    # As linhas nao somam 331: uma publicacao pode nomear mais de um protocolo.
    assert M["Nenhum"].sum() + M[PENDENTE].sum() <= N
    fig, ax = plt.subplots(figsize=(15.0*CM, 6.4*CM))
    v = M.values.astype(float)
    ax.imshow(np.sqrt(v), cmap="Blues", vmin=0, vmax=np.sqrt(v.max()), aspect="auto")
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            n = int(v[i, j])
            if n == 0: continue
            ax.text(j, i, str(n), ha="center", va="center", fontsize=8.5,
                    color="white" if np.sqrt(n) > .55*np.sqrt(v.max()) else TINTA)
    ax.set_xticks(range(len(cols)), [c.replace(" / sem extração", "\n/ sem extração") for c in cols],
                  fontsize=7.5)
    ax.set_yticks(range(len(linhas)), linhas, fontsize=7.5)
    ax.set_xlabel("Protocolo de medição e verificação invocado", fontsize=8, labelpad=8)
    ax.set_ylabel("Norma de gestão invocada", fontsize=8)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    linha = M.loc["Família ISO 50001"]
    invoca = int(linha.sum() - linha[PENDENTE] + linha[PENDENTE])  # publicacoes da linha
    invoca = int(papers.apply(lambda r: grupo_norma(r.ems_standard) == "Família ISO 50001", axis=1).sum())
    sem = int(M.loc["Família ISO 50001", "Nenhum"])
    fig.text(.5, -.155, "Das %d publicações que invocam a família ISO 50001, %d (%.0f%%) "
             "não invocam protocolo algum de medição e verificação. Uma publicação "
             "pode nomear mais de um protocolo, pelo que as linhas não somam."
             % (invoca, sem, 100*sem/invoca), ha="center", fontsize=7.5, color=CINZA)
    fig.savefig(HERE/"v08_norma_protocolo.pdf"); fig.savefig(HERE/"v08_norma_protocolo.png", dpi=260)
    plt.close(fig); print("v08 ok — ISO 50001 sem protocolo: %d/%d" % (sem, invoca))
    M.to_csv(HERE/"v08_matriz.csv")

# ---------------------------------------------------------------- C3-V07 ---
def v07():
    """Setor x familia de modelos. Prototipo para decidir, nao para adoptar."""
    fam = {"simple intensity ratio":"Rácio","linear regression":"Regr. linear",
           "multiple regression":"Regr. múltipla","physical model":"Modelo físico",
           "change-point or SPC":"Ponto de mudança","ML":"Aprend. automática",
           "SEC mean":"Média SEC","other":"Outra","composite index":"Índice composto",
           "process integration":"Integração"}
    cont = collections.Counter(); setores = collections.Counter()
    for _, r in papers.iterrows():
        S = [s for s in lst(r.sectors_derived) if s not in
             (PENDENTE, "Por classificar / outro", "Não aplicável", "Não reportado no artigo")]
        F = [fam.get(f, f) for f in lst(r.enpi_enb_model_types)]
        for s in S:
            setores[s] += 1
            for f in F: cont[(s, f)] += 1
    if not cont:
        print("v07: sem dados"); return
    ss = [s for s, _ in setores.most_common(10)]
    ff = list(dict.fromkeys(fam.values()))
    M = pd.DataFrame(0, index=ss, columns=ff)
    for (s, f), n in cont.items():
        if s in ss and f in ff: M.loc[s, f] = n
    cheias = int((M.values > 0).sum()); total = M.size
    print("v07: %d de %d celulas com dados; maximo %d; mediana das nao vazias %.1f"
          % (cheias, total, M.values.max(), np.median(M.values[M.values > 0])))
    fig, ax = plt.subplots(figsize=(15.0*CM, 7.0*CM))
    ax.imshow(np.sqrt(M.values.astype(float)), cmap="Blues", aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            n = M.values[i, j]
            if n: ax.text(j, i, str(n), ha="center", va="center", fontsize=7.5,
                          color="white" if n > .55*M.values.max() else TINTA)
    ax.set_xticks(range(len(ff)), ff, rotation=35, ha="right", fontsize=7)
    ax.set_yticks(range(len(ss)), ss, fontsize=7)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    fig.text(.5, -.20, "%d das %d células têm pelo menos uma publicação." % (cheias, total),
             ha="center", fontsize=7.5, color=CINZA)
    fig.savefig(HERE/"v07_setor_familia.pdf"); fig.savefig(HERE/"v07_setor_familia.png", dpi=260)
    plt.close(fig); M.to_csv(HERE/"v07_matriz.csv")

if __name__ == "__main__":
    v05(); v08(); v07()
