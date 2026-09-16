# Crítica do Apêndice G (matemática) — 2026-09-16

Ficheiro: `3-BackMatter/appendix-G-matematica.tex` (ex-rascunho de 2026-09-15, activado hoje; esqueleto arquivado em `3-BackMatter/_arquivo/`).
Build: compila, 0 referências ou citações indefinidas. O PDF passou de 122 para 159 páginas: **o apêndice ocupa ~37 páginas**.
Dimensão: 12 745 palavras (wc), 84 equações numeradas, 3 TikZ, 3 algoritmos, 23 caixas (18 P1).

## Veredicto

A matemática está certa nos pontos verificados. O problema não são as fórmulas. São quatro coisas:

1. **Registo de memorando de auditoria, não de tese.** 25 ocorrências de «consultado/a» («a implementação consultada», «a regra consultada», «na Parte C consultada») e 80 de «deve/devem». Um apêndice declara o que a dissertação fez e com que convenção; não recomenda a si próprio o que deveria fazer. Metade da extensão vem daqui.
2. **Convenções por fechar dentro do texto que iria para o júri**, fora das caixas: legenda da Tabela das regras («requerem harmonização com a implementação»), «segundo a definição de lateralidade adotada», «a dimensão do desvio [...] permanece por quantificar», «deve fixar-se se uma lacuna interrompe o episódio».
3. **Instrumentos previstos descritos ao lado dos executados, sem os distinguir.** §Auditoria da revisão formaliza a auditoria SRS n=40 do Nível A e a divergência entre duas extracções; a extracção final foi numa superfície e sem verificação humana por ocorrência. Equivalência/não inferioridade e as famílias ARMA/partilha parcial/grey-box são propostas.
4. **18 P1.** Dois fecham-se já com fontes (MAT-02, MAT-07). Um é uma falha metodológica real que tem de subir ao corpo (MAT-08).

## 1. Fórmulas verificadas (corretas)

OLS e escala com n−p; Huber c=1,345 e MAD 1,4826; Theil–Sen com intercepto `separate` (SciPy); HAC com núcleo quadrático-espectral e largura de Andrews (1,3221·(nα̂₂)^{1/5}, α̂₂ correcto); Wald; BH e BY (c_m harmónico); Clopper–Pearson; limite para zero erros (n=40: 7,2 % unilateral, 8,8 % bilateral — conferido); Wilson; Cook; G₁/G₂ com correcção amostral; E[max(r,0)]=σ/√(2π); nível local de Kalman e crescimento dv_η na lacuna; gerador AR(1) estacionário; variância da soma; 2Φ(2)−1=0,9545; TF-IDF suavizado (sklearn); modularidade; identidade da covariância no produto de agregados; conversão eléctrica 860,4/(11 820×0,57) dimensionalmente coerente.

## 2. Âmbito — o que o corpo usa

Contagem de menções nos Caps. 3–8 (grep). Quase tudo o que o apêndice formaliza é usado:

| secção do G | usada em | leitura |
|---|---|---|
| Notação, populações | 4, 6 | manter |
| Grandezas físicas, GNE, CE, EII | 4 (EII 1×) | manter GNE/CE; **cortar balanços material/energia genéricos e API/°F/mmHg** (sem uso fora da correlação Solomon) |
| Bibliometria e redes (TF-IDF, NMF, modularidade, acoplamento) | 3 | manter, comprimido |
| Auditoria da revisão | 3 (planeada) | **só o que foi executado**; o resto sai ou passa a «previsto, não executado» no Apêndice B |
| Regressão, Huber, Theil–Sen, GAM | 6, 7 | manter; **cortar §famílias futuras** (ARMA, partilha parcial, grey-box → Cap. 8) |
| Avaliação temporal, perdas | 4, 6, 7 | manter |
| HAC, Wald, BH/BY, MBB, bootstrap nulo | 4, 6, 7 | manter |
| Diagnósticos | 6 (SMD, OVL, DW, BP, ARCH, k-means, DBSCAN, silhouette) | manter os usados; **cortar Cook, RESET, Ljung–Box, Pearson/Spearman** (0 menções) |
| Bandas, cobertura, regras, AR, quantílica | 4, 6, 7 | manter; reescrever regras com a convenção DAX (MAT-07) |
| Aceitação 4/5 | 4, 7 | manter; **equivalência/não inferioridade → Cap. 7/8** como proposta |
| Referência/estado/CUSUM/monitores | 4, 6, 7 | manter; **estados operacionais → Apêndice F (manual) ou Cap. 7** |
| Simulação, MDD | 7 | manter |

Alvo realista: **~8 000–9 000 palavras (~22–24 pp.)**, sobretudo por reescrita do registo; os cortes de tópico valem ~1 500 palavras.

## 3. Inconsistências com o corpo detectadas

- **Cobertura 357/400 do bootstrap:** o Cap. 4 (l. ~479) diz que foi adjudicada por teste binomial exacto (Clopper–Pearson); o Cap. 7 (l. ~1051) reporta intervalo de Wilson 0,86–0,92. Mesmo resultado, dois procedimentos. Escolher um e alinhar os dois capítulos.
- **Regras de sequência:** o apêndice formula-as sobre dias civis; a plataforma aplica-as sobre dias válidos ordenados (ver MAT-07). O Cap. 4 (l. ~344) descreve «oito consecutivos» sem dizer consecutivos em quê.
- **Regra 4/5:** o Cap. 4 (l. ~519) diz «cada um em pelo menos quatro dos cinco pares» — contagens separadas. Correcto e coerente com o apêndice, mas admite só três pares com ambos os critérios (exemplo do apêndice). O Cap. 7 tem de o dizer.
- **Fuel gás/coque:** a regra da plataforma é `sum_flow_x_pci_intra` (produto horário caudal×PCI, `_Parametros_Vector`). O apêndice diz que a transformação consultada combina caudal agregado e PCI médio diário. Uma das duas cadeias (Power BI ou `baselines-cc`) faz outra coisa, ou o apêndice leu mal. Liga ao C4-02 do Cap. 4.

## 4. Triagem das caixas

| caixa | P | estado | acção |
|---|---|---|---|
| MAT-00 | P1 | meta | sai com a versão final |
| MAT-01 | P1 | verificar | DAX: carga **≥** limiar (inclusivo), resíduo não vazio. Confirmar a sequência de filtros no Python e publicar contagens por filtro (liga ao Apêndice E) |
| **MAT-02** | P1 | **fechada** | `Mapeamento_Master_v22.xlsx`, folha `_Parametros_Global`: PCI_ref 11 820 kcal/kg («Standard Galp»); vapor 3,5 bar **698**, 10,5 bar **738**, 24 bar **758** kcal/kg («tabelas de vapor saturado»); 860,4 Mcal/MWh (a coluna «unidade» diz kcal/MWh — erro de rótulo na fonte); 0,57 «convenção Galp». 10 bar é saldo (cons − prod) |
| MAT-03 | P1 | decisão | não transcrever a correlação Solomon (metodologia licenciada a terceiros; a confidencialidade da tese não resolve licenças). Fica a estrutura do EII. Cortar §transformações |
| MAT-04 | P1 | verificar | mínimo de observações admissível em `config/params.yaml` vs cálculo com 3 pontos |
| MAT-05 | P1 | trabalho de lote | contrato inferencial por tabela — faz-se ao construir o Apêndice E |
| MAT-06 | P1 | decisão | quais os valores p descritivos que ficam; cortar os diagnósticos sem uso |
| **MAT-07** | P1 | **fechada** | medida DAX `Card_Regras_CC_HTML`: janelas sobre **dias válidos ordenados** (`RANKX`), não dias civis — lacunas e dias abaixo do limiar são saltados; regra 4 = 8 pontos, desigualdade estrita (zero quebra); regra 5 = 6 pontos, 5 incrementos estritos; regra 6 = 14 pontos, empate conta como descida; regra 7 = 15 pontos com \|z\|<1; regra 8 = 8 pontos com \|z\|>1 **sem exigir mesmo lado nem ambos os lados**; contagem por fim de janela (janelas sobrepostas contam repetidamente); população = `ALLSELECTED(Calendario[Date])`, logo as contagens mudam com o filtro de datas. A plataforma não define episódio |
| **MAT-08** | P1 | **falha real** | no quadro histórico, o ganho usa a previsão anual E2 e a cobertura usa o centro AR: a decisão combina dois objectos. Não se resolve no apêndice — declarar no Cap. 7 (limitações do critério de aceitação) |
| MAT-09 | P1 | trabalho de lote | associar cada cenário de simulação a lote e manifesto — Apêndice E |
| MAT-10 | P2 | fim | remissões com `_revisao/2026-09-15-rascunho-anexo-G/remissoes.csv` |
| MAT-F01…F12 | 8×P1 | cortar | 12 propostas de figura. Com 14 dias: nenhuma figura nova aqui além dos 3 TikZ existentes; F06/F09/F12 só se os lotes existirem, e então no Cap. 6/7 |

## 5. Ordem proposta (≤ 1 dia)

1. Aplicar MAT-02 e MAT-07 (factos fechados acima).
2. Reescrever em indicativo: «a implementação consultada usa» → «usa-se»; «deve» → a convenção adoptada ou sai.
3. Cortes da §2.
4. Resolver as quatro inconsistências da §3 nos capítulos.
5. MAT-08 para o Cap. 7.
6. Remissões no fim, quando os capítulos estiverem estáveis.
