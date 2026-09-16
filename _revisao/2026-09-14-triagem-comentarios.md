# Análise dos comentários de revisão — 2026-09-14

## O que existe

Duas passagens deixaram caixas visíveis no PDF (`\revisaotese`, definida em `0-Config/revisao.tex`; `\mostrarrevisaofalse` esconde tudo, incluindo o Apêndice H de revisão):

- **2026-09-13, 15:12–15:26** — revisão crítica de toda a dissertação: 104 caixas em 20 ficheiros (8 capítulos, 2 resumos, 3 ficheiros de listas, 7 apêndices). 27 P1, 69 P2, 8 P3; 21 são propostas de figura/tabela (F01–F21). Relatório em `_revisao/2026-09-13-avaliacao-critica.md`; JSON em `_revisao/2026-09-13-critica/`; PDF compilado com as caixas (107 pp, 104 visíveis, compilação limpa) em `_revisao/2026-09-13-pdf/`.
- **2026-09-14, 08:39–08:53** — redação das secções 3.1–3.3 do Cap. 3 (5 061 palavras) com 11 caixas de figura (C3-V01–V10 + F04 revista) e 7 entradas novas no `.bib`. Compilação limpa. §3.4 e §3.5 continuam stubs.

Total: 114 identificadores distintos. Os 12 marcadores anteriores (`%% CONFIRMAR`, `%% PENDENTE-REPUBLICACAO`, `%% FIGURA`) continuam nos ficheiros e sobrepõem-se a várias caixas (C5-03 = CONFIRMAR #1 do Cap. 5; C7-12 = PENDENTE-REPUBLICACAO; F01 = FIGURA 1.1 do Cap. 1).

## Natureza da revisão

Não é a passagem `narrativa` + `humanizer` que pediste. É uma crítica científica: estatística, leitura normativa, cronologia do pré-registo, consistência aritmética. A estratégia de estilo ficou ultrapassada pela de substância, o que está certo pela ordem das próprias skills (substância antes de estrutura, estrutura antes de superfície). Mas muda o registo da conversa: a maior parte das caixas não pede «escreve melhor», pede «afirma menos do que estás a afirmar» ou «mostra a evidência que prometes».

## Onde a revisão tem razão sem discussão

Erros verificáveis no texto, que corrigi ou confirmei contra os `.tex`:

1. **C6-09** — vapor 10 bar, 2023→2024: «um e um alarme em 364 dias» (l. 437) contra «2 em 364» (l. 448). Um dos dois está errado; decide-se no lote E4, não na prosa.
2. **C7-17** — sensibilidade do critério: «três em dezasseis» (§7.4) e «três em trinta e dois» (§7.6). Pode ser coerente (3 dos 16 OLS, 0 dos 16 robustos) mas tem de ser dito.
3. **C4-03** — inventário: seis classes enumeradas somam 3 809; o texto anuncia sete classes e 3 862. Faltam 53 ficheiros ou uma classe.
4. **C2-03** — R² não pressupõe normalidade. Erro de facto no Cap. 2 (iii) e na matriz.
5. **C6-05** — autocorrelação não implica perda de cobertura marginal. A perda tem de assentar nos resultados de §6.5, não nesta inferência.
6. **C4-11** — 357/400 (89,25 %) testado contra 0,90 não valida um IC nominal a 95 %; o texto já o admite em §7.6 mas afirma o contrário no local.
7. **C7-13** — cobertura = 1 − taxa de excursão na mesma população; o bloco de saúde propõe uma como se fosse independente da outra.
8. **FR-01/02/03** — siglas, símbolos e glossário ainda são os exemplos do template (`abbrev`, `xpto`, `computer`, `Artho04`). Isto vai para o júri se ninguém tocar.

## Onde a revisão tem razão e o custo é só redação (o bloco maior)

39 caixas pedem **escopo**, não análise nova: «nenhuma das três funções» → por vetor e por uso (C7-02); «modelos vazios» → ganho não demonstrado contra estes comparadores (C6-06); «reajustar é apagar» → atenuação sob este desenho (C7-11); «validação demonstrada» → compatível pelo critério adotado (C7-06); «o método é conforme» → não excluído pelas cláusulas (C2-04); «falso por física» → a estabilidade tem de ser verificada (C1-03); «não existe metodologia» → lacuna delimitada por âmbito, período e fontes (C1-04). São ~2 dias de edições cirúrgicas nos Caps. 6, 7, 2 e 1, e são exactamente as frases que um arguente sublinha.

## Onde discordo ou matizo

- **C1-08** (cortar o Cap. 1 em 25 %): corto ~10 %. A repetição do mecanismo é a recorrência que dá arquitectura ao capítulo; o que sobra é escolha, não descuido.
- **C2-01** (reordenar o Cap. 2 para processo → conceitos → normas): não a 16 dias da entrega. Escrever 2.4/2.5 e remeter para elas resolve 80 % do problema.
- **C7-01** (Cap. 7 mistura métodos e resultados): concordo no diagnóstico; a solução é mover definições de candidatos e simulador para 4.4/Anexo G, não abrir um capítulo. A própria revisão recomenda isso.
- **C1-02** (abertura «generaliza sobre todas as refinarias»): a primeira frase é âncora retórica e fica; a segunda ganha a rotina documentada. «Devia» → «esperado sob a referência» é uma palavra.
- **C6-04, C6-11, C6-03**: correctas em rigor, mas o texto já tem a cautela no corpo; o que falha são títulos e fechos de parágrafo. Edição de meia linha cada.

## O problema de registo, que é a decisão que tens de tomar

Aplicada às cegas, a revisão transforma a tese numa lista de ressalvas. A `narrativa` diz o contrário: compromete-te com a afirmação e nomeia a fraqueza antes do revisor. As duas coisas são compatíveis se a regra for **escopo, não amaciamento**: cada afirmação fica à força que a evidência sustenta, com o domínio explícito na mesma frase («nas cinco transições avaliadas», «sob a política de reajuste anual», «na CDU, 2020–2025»), e sem «pode», «sugere», «parece» à frente de coisas que foram medidas. «A recalibração anual absorve a deriva» fica; «apaga o sinal» sai. «O 24 bar não tem ganho preditivo demonstrado contra a média do treino» fica; «modelo vazio» sai. Se aceitares esta regra, as 39 caixas R fecham-se sem perder o argumento.

## Impacto no Cap. 1 (a v1 que aprovaste)

Oito caixas. Duas P1 são minhas para corrigir: **C1-04** (adoptar já a redacção DECISAO-CAP3 — ver abaixo porquê) e **C1-06** (o «antes de se olhar para um resultado» é mais forte do que a cronologia real: exploração em abril, protocolo selado antes da corrida final; e as revisões adversariais têm de ser declaradas como o que foram — humano ou modelo — no Anexo F). As restantes são escopo (C1-03, C1-07, C1-02) e a tabela objetivo → pergunta → evidência → estado (C1-05), que amplia a Tabela 1.1 que já tinha proposto.

## Cap. 3 de 2026-09-14

Alguém (outra sessão) escreveu 3.1–3.3 com bibliometria do snapshot de 09-13. Dois factos que condicionam o resto: (i) **A=331 e B=42 não são aninhados nos ficheiros de origem** (interseção 40, união 333) — tem de se resolver antes de desenhar o PRISMA (F04) e antes de qualquer contagem no Cap. 1; (ii) os resultados de conteúdo são pré-extrações concordantes **sem verificação humana**. Isto fecha a decisão do Cap. 3: é protocolo + preliminar, e o Cap. 1 deve usar a redacção alternativa em §1.3 e §1.6.

## Plano para os 16 dias (proposta)

| Dias | Frente | Caixas |
|---|---|---|
| 1–2 | Erros verificáveis + escopo nos Caps. 6, 7, 2, 1 (um commit por capítulo) | 8 erros + 39 R |
| 3–5 | Cap. 2 §2.4/2.5 com F02/F03; Cap. 3 §3.4/3.5 como protocolo + piloto; Cap. 8 (C8-01/02) | C2-07, C3-04, F03 |
| 6–8 | Figuras que já existem como SVG/PDF (F04, F11–F14, C3-V02/03/05–08) + F08/F09 (prints) + 4 desenhos próprios (F01, F03, F06, F17) | 22 F |
| 9–11 | Anexos D e G (o corpo remete para eles em todo o lado), A e C; Anexo F com natureza das revisões | AP-* |
| 12–13 | Resumos PT/EN; FR-01/02/03; mover definições do Cap. 7 para 4.4/G (C7-01) | PT-01, EN-01 |
| 14–16 | Compilação limpa, `\mostrarrevisaofalse`, leitura do último terço de cada capítulo, diff final | — |

Fica de fora, declarado em §7.6 e no Cap. 8: covariância caudal × PCI (C4-02), quantificação de imputações (C4-05), cobertura por ano/vetor (C4-04), réplicas independentes de calibração (C7-14), reordenação do Cap. 2 (C2-01), fusão de 2.2/2.3 (C2-05), F15/F16/F18/F21.

## Onze coisas que só tu podes responder (X)

C1-06 natureza das revisões adversariais · C4-07 política real de referência em janeiro · C5-03 evidência do 400/400 · C6-02 origem dos fingerprints (exportados ou recalculados) · C7-09 se o candidato aceite é reta+AR, o MAE é da previsão completa? · C7-04 quais os 3–5 estudos próximos do Corpus B · F05/C3-04/AP-B o que entra do Stage C · F20 se as curvas de deteção existem nos outputs · AP-F o registo das quatro revisões.

---

# Triagem dos comentários de revisão — 2026-09-14

Base: 104 caixas de 2026-09-13 (`_revisao/2026-09-13-critica/comentarios.json`) + 11 caixas C3-V01..V10 de 2026-09-14 (Cap. 3) = **114**. Decisão por caixa, na minha leitura; não substitui a tua.

Códigos: **F** fazer (edição ou inclusão barata) · **R** reformular (dar escopo à afirmação, não amaciar) · **X** depende de facto/decisão tua · **L** declarar como limitação, sem análise nova · **A** adiar para depois da entrega · **D** discordo, em parte.

| Decisão | Total | dos quais P1 | dos quais FIGURA |
|---|---:|---:|---:|
| F — Fazer | 53 | 6 | 22 |
| R — Reformular (escopo) | 39 | 16 | 0 |
| X — Depende de ti | 11 | 4 | 2 |
| L — Declarar limitação | 1 | 1 | 0 |
| A — Adiar | 9 | 0 | 7 |
| D — Discordo (parcial) | 1 | 0 | 0 |

## Tabela completa (ordenada por decisão, depois por capítulo)

| ID | P | Tipo | Ficheiro | Dec. | Nota |
|---|---|---|---|---|---|
| EN-01 | P3 | RESUMO | abstract-en | **F** | abstract EN a partir do PT |
| PT-01 | P2 | RESUMO | abstract-pt | **F** | resumo PT depois de fechar 6/7/8 |
| FR-01 | P3 | APRESENTACAO | acronyms | **F** | obrigatorio: siglas do template ainda la (abbrev, xpto) |
| FR-03 | P3 | APRESENTACAO | glossary | **F** | obrigatorio: glossario com "computer"/Artho04 |
| FR-02 | P3 | NOTACAO | symbols | **F** | obrigatorio: simbolos do template |
| C1-01 | P2 | ESTRUTURA | chapter-1-introducao | **F** | meta; remover a caixa no fim |
| C1-05 | P2 | ESTRUTURA | chapter-1-introducao | **F** | tabela objetivo -> pergunta -> evidencia -> capitulo -> estado (amplia a TABELA 1.1 proposta) |
| F01 | P2 | FIGURA | chapter-1-introducao | **F** | e a FIGURA 1.1 que eu propus; desenho proprio, meia pagina |
| C2-02 | P1 | NORMAS | chapter-2-enquadramento | **F** | P1; declarar no inicio que se analisa a edicao de 2014; comparacao com 2023 so com acesso (senao L) |
| C2-03 | P1 | ESTATISTICA | chapter-2-enquadramento | **F** | P1; erro factual (R2 nao pressupoe normalidade); corrigir (iii) e linha 4 da matriz |
| C2-07 | P2 | CONTEUDO | chapter-2-enquadramento | **F** | parte da 2.5 por escrever; GNE/EII; citar literatura de refinacao |
| F02 | P2 | FIGURA | chapter-2-enquadramento | **F** | tabela mecanismo/efeito/observavel/alternativas; cabe na 2.4, que esta por escrever |
| F03 | P2 | FIGURA | chapter-2-enquadramento | **F** | PRIORIDADE MAXIMA: diagrama CDU + fronteira energetica; desenho proprio |
| C3-01 | P2 | CONTEUDO | chapter-3-revisao | **F** | ID/URL/datas OSF existem (10.17605/OSF.IO/TDW6C) |
| C3-02 | P2 | METODO | chapter-3-revisao | **F** | strings/bases/datas existem no protocolo; vies do recorte ISO -> declarar (L) |
| C3-V01 | P2 | FIGURA | chapter-3-revisao | **F** | esquema pequeno do desenho da revisao |
| C3-V02 | P2 | FIGURA | chapter-3-revisao | **F** | field_status.pdf existe |
| C3-V03 | P2 | FIGURA | chapter-3-revisao | **F** | annual.pdf existe |
| C3-V05 | P2 | FIGURA | chapter-3-revisao | **F** | paper_type + type_of_organisation existem |
| C3-V06 | P2 | FIGURA | chapter-3-revisao | **F** | model types + upset existem; 171 por resolver -> legenda |
| C3-V07 | P2 | FIGURA | chapter-3-revisao | **F** | matriz setor-modelo: responde a SQ1 |
| C3-V08 | P2 | FIGURA | chapter-3-revisao | **F** | ems_standard + mv_protocol existem |
| F04 | P2 | FIGURA | chapter-3-revisao | **F** | prisma_flow.pdf existe; antes: resolver A/B nao aninhados (intersecao 40, uniao 333) |
| C4-01 | P2 | ESTRUTURA | chapter-4-metodos | **F** | seccao inicial "desenho do estudo" (meio dia); mover inventarios para apendice: A |
| C4-03 | P2 | CONSISTENCIA | chapter-4-metodos | **F** | trivial: conferir manifesto (3 809 vs 3 862; 53 ficheiros) |
| C4-06 | P2 | ENERGIA | chapter-4-metodos | **F** | equacoes de conversao + tabela de fatores (698/738/758; 11 820; 0,57) -- dados conhecidos |
| C4-10 | P2 | INFERENCIA | chapter-4-metodos | **F** | tabela por teste (H0/estimando/familia/estatuto) -- quase existe em tab:estimandos/coprimarias |
| F06 | P2 | FIGURA | chapter-4-metodos | **F** | arquitetura de dados com granularidade; desenho proprio; substitui screenshot do modelo |
| F07 | P2 | FIGURA | chapter-4-metodos | **F** | linha temporal dos tres desenhos 2020-2026; desenho simples, alto valor |
| F08 | P2 | FIGURA | chapter-5-plataforma | **F** | barras por versao (OK/vazias/divergentes) -- dados nas notas de validacao de julho |
| F09 | P2 | FIGURA | chapter-5-plataforma | **F** | dois screenshots anotados (prints_dashboard existem); integrais no Anexo E |
| C6-01 | P2 | ESTRUTURA | chapter-6-diagnostico | **F** | abertura com resumo por uso + vocabulario demonstrado/sensivel/NE |
| C6-05 | P1 | ESTATISTICA | chapter-6-diagnostico | **F** | P1; correcao estatistica (autocorrelacao != perda de cobertura marginal) |
| C6-09 | P1 | CONSISTENCIA | chapter-6-diagnostico | **F** | P1; contradicao real (l.437 "um e um" vs l.448 "2 em 364"); conferir lote E4 |
| C6-12 | P1 | SUPORTE | chapter-6-diagnostico | **F** | P1; % de dias fora de [min,max] do treino e barato se o pipeline correr; senao R |
| F10 | P2 | FIGURA | chapter-6-diagnostico | **F** | fluxo da amostra + calendario de disponibilidade; dados nos runs |
| F11 | P2 | FIGURA | chapter-6-diagnostico | **F** | D0 SVGs existem |
| F12 | P2 | FIGURA | chapter-6-diagnostico | **F** | E2_2 forest existe |
| F13 | P2 | FIGURA | chapter-6-diagnostico | **F** | E3_1 existem; compor 4 vetores numa figura a carga comum |
| F14 | P2 | FIGURA | chapter-6-diagnostico | **F** | bundle E4 existe |
| C7-01 | P2 | ESTRUTURA | chapter-7-discussao | **F** | parcial: mover definicoes de candidatos/simulador para 4.4 ou Anexo G (1 dia); sem capitulo novo |
| C7-10 | P2 | POPULACAO | chapter-7-discussao | **F** | 876 dias como fracao dos candidatos por ano/vetor (barato); populacao propria: L |
| C7-12 | P1 | EVIDENCIA | chapter-7-discussao | **F** | P1; retirar a conclusao do lote invalido ate republicacao (= PENDENTE-REPUBLICACAO) |
| C7-17 | P2 | LIMITACOES | chapter-7-discussao | **F** | 3/16 vs 3/32; bloco 60 vs 7; "resposta completa" -> opcoes |
| F17 | P2 | FIGURA | chapter-7-discussao | **F** | esquema referencia/estado/monitor; desenho proprio; central |
| F19 | P2 | FIGURA | chapter-7-discussao | **F** | injecao: tres paineis do lote validado; alto valor |
| C8-01 | P2 | CONTEUDO | chapter-8-conclusoes | **F** | escrever o Cap. 8 (espelho de 1.4) |
| C8-02 | P2 | ESTRUTURA | chapter-8-conclusoes | **F** | tabela falha -> opcao -> dados -> comparador -> criterio; alinhado com 1.5 (grey-box fora) |
| AP-A | P2 | APENDICE | appendix-A-protocolo-sr | **F** | protocolo congelado + cronologia das emendas |
| AP-C | P2 | APENDICE | appendix-C-dicionario | **F** | dicionario: existe no tese-extraccao (Mapeamento_Master) |
| AP-D | P2 | APENDICE | appendix-D-tabelas | **F** | tabelas: existem nos runs; o corpo remete para elas -> obrigatorio |
| AP-E | P2 | APENDICE | appendix-E-manual | **F** | manual: Parte B existe? (CONFIRMAR) |
| AP-G | P2 | APENDICE | appendix-G-matematica | **F** | matematica: esqueleto existe; prioridade -- o corpo remete para ele em todos os instrumentos |
| C1-02 | P2 | CONTEUDO | chapter-1-introducao | **R** | "devia" -> "esperado sob a referencia"; manter a frase de abertura |
| C1-03 | P2 | ARGUMENTO | chapter-1-introducao | **R** | "falso por fisica" -> "a estabilidade tem de ser verificada"; CDU nao tem catalisador |
| C1-04 | P1 | ARGUMENTO | chapter-1-introducao | **R** | P1; usar a redacao DECISAO-CAP3 (protocolo + preliminar); lacuna delimitada por ambito/periodo/fontes |
| C1-07 | P2 | ESTRUTURA | chapter-1-introducao | **R** | retirar "qualquer organizacao"/"qualquer unidade"; condicoes de transferencia numa frase |
| C2-04 | P1 | NORMAS | chapter-2-enquadramento | **R** | P1; "o metodo e conforme" -> "nao excluido pelas clausulas analisadas"; aplicar tambem em 1.2 e 7.2 |
| C2-06 | P2 | FONTES | chapter-2-enquadramento | **R** | R2 >= 0,75 do IPMVP como fonte secundaria por confirmar (ja tem \todo) |
| C3-03 | P2 | ANALISE | chapter-3-revisao | **R** | contagens descrevem cobertura, nao adequacao |
| C4-04 | P1 | METROLOGIA | chapter-4-metodos | **R** | P1; definir "reconciliacao" = harmonizacao de fontes (F); cobertura por ano/vetor: L |
| C4-05 | P1 | DADOS | chapter-4-metodos | **R** | P1; restringir "nao imputa" ao consumo/carga; quantificar imputacoes se o pipeline der (X) |
| C4-08 | P2 | INDICADORES | chapter-4-metodos | **R** | definir e_t; soma vs soma positiva; 2 paragrafos |
| C4-09 | P2 | INDICADORES | chapter-4-metodos | **R** | EII/CO2 como proxy de reporte interno; ligado ao CONFIRMAR do fator CO2 |
| C4-11 | P1 | VALIDACAO | chapter-4-metodos | **R** | P1; "diagnostico, nao validacao"; declarar que o alvo 0,90 foi escolhido a posteriori |
| C4-12 | P2 | REPRODUTIBILIDADE | chapter-4-metodos | **R** | "provar que nao foi editado" -> "detetar divergencias face ao manifesto" |
| C5-01 | P2 | ESTRUTURA | chapter-5-plataforma | **R** | cortar 1-2 paragrafos de inventario repetido do Cap. 4; evidencia de entrega/uso (CONFIRMAR #2) |
| C5-02 | P1 | VALIDACAO | chapter-5-plataforma | **R** | P1; "tres fontes independentes" -> "tres canais com dependencias declaradas" |
| C5-04 | P2 | DADOS | chapter-5-plataforma | **R** | 24 vs 16 unidades; qual Q entra em cada indicador |
| C5-05 | P2 | INTERPRETACAO | chapter-5-plataforma | **R** | ordenacao herda limites das baselines; 2 frases |
| C6-03 | P2 | INTERPRETACAO | chapter-6-diagnostico | **R** | SMD: "populacao distinta nas variaveis observadas" |
| C6-04 | P2 | INTERPRETACAO | chapter-6-diagnostico | **R** | eletricidade: "falta de resolucao temporal", nao impossibilidade |
| C6-06 | P1 | INFERENCIA | chapter-6-diagnostico | **R** | P1; "modelos vazios" -> conclusao delimitada aos comparadores; Lakens ja citado |
| C6-07 | P2 | INFERENCIA | chapter-6-diagnostico | **R** | nao fechar invariancia rejeitada incondicionalmente; MBB 60 dias |
| C6-08 | P1 | INTERPRETACAO | chapter-6-diagnostico | **R** | P1; excursoes != falsos alarmes; uniformizar 0,9545; superior/inferior |
| C6-10 | P2 | METODO | chapter-6-diagnostico | **R** | suficiencia: escopo ao conjunto Z e classe |
| C6-11 | P2 | DIAGNOSTICO | chapter-6-diagnostico | **R** | regimes: titulo e conclusao delimitados |
| C6-13 | P2 | RELATO | chapter-6-diagnostico | **R** | p-values "descritivos" -> ACF/dispersao movel; testes classicos para o Anexo D |
| C6-14 | P1 | SINTESE | chapter-6-diagnostico | **R** | P1; sintese proporcional; linha eletricidade "resolucao mensal"; detetabilidade NE |
| C6-15 | P2 | MECANISMO | chapter-6-diagnostico | **R** | mecanismo: separar projecao algebrica / simulacao / observado (liga a C4-07) |
| C7-02 | P1 | ARGUMENTO | chapter-7-discussao | **R** | P1; "nenhuma das tres funcoes" -> por vetor/uso |
| C7-03 | P2 | ARGUMENTO | chapter-7-discussao | **R** | dicotomia fixa/adaptativa -> "sob as politicas avaliadas" |
| C7-05 | P2 | CRITERIOS | chapter-7-discussao | **R** | 48-72 h como escolha justificada; estado "nao avaliado" |
| C7-06 | P1 | ACEITACAO | chapter-7-discussao | **R** | P1; "compativel pelo criterio adotado", nao "validado" |
| C7-07 | P1 | ACEITACAO | chapter-7-discussao | **R** | P1; justificar 4/5; declarar se o 3/5 e conjunto |
| C7-08 | P2 | MODELOS | chapter-7-discussao | **R** | "condicionais e quantilicas"; anual vs plurianual como sensibilidade |
| C7-11 | P1 | ALGEBRA | chapter-7-discussao | **R** | P1; "reajustar e apagar" -> atenuacao sob este desenho |
| C7-13 | P1 | INTERPRETACAO | chapter-7-discussao | **R** | P1; cobertura = 1 - taxa de excursao; reescrever o paragrafo do bloco de saude |
| C7-14 | P1 | SIMULACAO | chapter-7-discussao | **R** | P1; especificar gerador/escala/onset no Anexo G (F); replicas independentes: L |
| C7-15 | P2 | SIMULACAO | chapter-7-discussao | **R** | gerador linear favorece: titulo e conclusoes |
| C7-16 | P2 | SIMULACAO | chapter-7-discussao | **R** | 0,095 vs 0,05: explicar |
| C7-18 | P1 | ESTIMANDO | chapter-7-discussao | **R** | P1; paragrafo "o que se aceita: preditor/normalizador/detetor" antes da tabela dos candidatos |
| C1-06 | P1 | TRANSPARENCIA | chapter-1-introducao | **X** | P1; cronologia real (exploracao em abril; protocolo selado antes da corrida final); revisoes adversariais foram por modelos? confirmar e declarar no Anexo F |
| C3-04 | P2 | ARGUMENTO | chapter-3-revisao | **X** | fecho da revisao depende de 3.4/3.5 (protocolo + piloto) |
| F05 | P2 | FIGURA | chapter-3-revisao | **X** | mapa de evidencia do Corpus B: so com Stage C; com o piloto de 5 -> versao reduzida ou omitir |
| C4-07 | P1 | CRONOLOGIA | chapter-4-metodos | **X** | P1; politica real de janeiro: so tu/Galp sabem; sem isso, apresentar o mecanismo como consequencia do desenho + simulacao |
| C5-03 | P1 | EVIDENCIA | chapter-5-plataforma | **X** | P1; 400/400 = o teu CONFIRMAR #1; sem evidencia da execucao final, reportar v15.1 como esta |
| C6-02 | P2 | PROVENIENCIA | chapter-6-diagnostico | **X** | origem dos fingerprints (exportados vs recalculados): tu sabes |
| C7-04 | P2 | NORMAS | chapter-7-discussao | **X** | normas (R) + confronto com 3-5 estudos do Cap. 3 (depende do Cap. 3) |
| C7-09 | P1 | ESTIMANDO | chapter-7-discussao | **X** | P1; se o candidato e reta+AR, o MAE tem de ser da previsao completa -- conferir implementacao (pode exigir re-run) |
| F20 | P2 | FIGURA | chapter-7-discussao | **X** | curvas de detecao: existem nos outputs da simulacao? |
| AP-B | P2 | APENDICE | appendix-B-validacao | **X** | depende do Stage C; com piloto: descrever o piloto e a adjudicacao |
| AP-F | P2 | APENDICE | appendix-F-adversarial | **X** | registo das 4 revisoes existe no palace (2026-08-13-adjudicacao); declarar humano/modelo |
| C4-02 | P1 | DADOS | chapter-4-metodos | **L** | escrever a convencao de agregacao (F, 2 h); covariancia caudal x PCI: declarar como limitacao |
| C2-01 | P2 | ESTRUTURA | chapter-2-enquadramento | **A** | nao reordenar o Cap. 2 agora; escrever 2.4/2.5 e remeter para elas ao introduzir os vetores |
| C2-05 | P2 | ESTRUTURA | chapter-2-enquadramento | **A** | fundir 2.2.2/2.2.3/2.3.1 so se sobrar tempo |
| C3-V04 | P2 | FIGURA | chapter-3-revisao | **A** | fontes/dispersao: opcional |
| C3-V09 | P2 | FIGURA | chapter-3-revisao | **A** | rede de palavras so se os grupos forem nomeados por leitura |
| C3-V10 | P2 | FIGURA | chapter-3-revisao | **A** | rede bibliografica -> apendice |
| F15 | P3 | FIGURA | chapter-6-diagnostico | **A** | acoplamento de vapor: opcional |
| F16 | P3 | FIGURA | chapter-6-diagnostico | **A** | SENS matrix existe; opcional |
| F18 | P2 | FIGURA | chapter-7-discussao | **A** | a tabela atual chega; matriz completa no Anexo D |
| F21 | P3 | FIGURA | chapter-7-discussao | **A** | wireframe da ficha: so se sobrar tempo; Anexo E |
| C1-08 | P3 | REDACAO | chapter-1-introducao | **D** | cortar ~10 %, nao 25 %; a recorrencia do mecanismo e deliberada (narrativa) |
