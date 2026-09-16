# Rascunho do apêndice matemático

15 de setembro de 2026.

## Entrega e âmbito

O ficheiro `3-BackMatter/appendix-G-matematica-rascunho.tex` contém o texto desenvolvido do apêndice **Fundamentos e formulações matemáticas da dissertação**, com o identificador `app:matematica`. Foi escrito ao lado do esqueleto anterior. A configuração principal ainda seleciona esse esqueleto; a cópia em `projeto-compilacao` seleciona o rascunho para permitir a sua leitura no contexto da tese.

O texto cobre as 107 entradas do inventário anterior, em 12 secções, com 63 subsecções e 84 equações numeradas. Acrescenta uma passagem sobre ARMA, partilha parcial entre unidades e modelos com estrutura física, famílias que já aparecem no esqueleto do trabalho futuro. As propostas sem estudo apresentado são identificadas como tal.

Inclui três esquemas TikZ, três algoritmos e doze propostas de figuras. Os esquemas mostram os pares anuais, os canais referência–estado–inovação e a separação entre calibração e avaliação de deteção. As propostas usam `\revisaotese`, com a categoria `FIGURA`, e especificam conteúdo, dados, eixos ou legendas a preparar. Os gráficos de resultados ficam dependentes de lotes consolidados.

## Acesso e remissões

`remissoes.csv` liga cada conceito às suas origens no corpo da tese, à subsecção do rascunho e ao respetivo identificador LaTeX. Pode ser usado como lista de trabalho para inserir remissões sem reler o apêndice inteiro.

Exemplos:

```latex
O consumo específico é calculado como razão de totais
(equação~\ref{eq:mat-consumo-especifico}).

A incerteza do ganho é estimada por blocos civis,
conforme a Secção~\ref{sec:mat-mbb}.

...\footnote{A contribuição esperada do ruído para o excesso positivo
é desenvolvida na equação~\ref{eq:mat-excesso-ruido}.}
```

Na configuração final, selecionar **apenas uma** versão do apêndice G. O rascunho mantém `app:matematica` para preservar as remissões existentes. As novas remissões devem usar os identificadores `sec:mat-*`, `eq:mat-*`, `fig:mat-*` e `tab:mat-*`. A numeração resolve-se na compilação.

## Aplicação de narrativa

Skill: `/Users/bernardoribeiro/Desktop/Mind Palace/.agents/skills/narrativa/SKILL.md`, com a referência de não ficção.

Modo aplicar, adequado a um texto de consulta. O leitor chega a partir de uma expressão, cálculo ou resultado do corpo da tese. A estrutura de acesso começa na pergunta, apresenta a definição ou equação e depois as hipóteses e os limites. A sequência global vai das grandezas às decisões, mas as secções são autónomas para permitir leitura descontínua. Não se usa suspense nem uma progressão artificial de complexidade.

A notação repete três distinções porque elas mudam a interpretação: população efetivamente avaliada; origem da escala; informação disponível no instante do cálculo. Os exemplos algébricos de consumo específico, quatro em cinco, excesso positivo e atenuação AR tornam essas distinções verificáveis sem inventar observações da refinaria.

## Aplicação de humanizer

Skill: `/Users/bernardoribeiro/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/humanizer/SKILL.md`.

`primeira-versao.tex` conserva a versão anterior à passagem final. A revisão priorizou factos e convenções, seguida de coerência linguística e de leitura.

1. **Substância:** explicitou a reta B09 por mínimos quadrados, os conjuntos B03/B08, o divisor de variância na SMD, a normalização global da ACF civil, a adaptação de Durbin–Watson e Ljung–Box, a correção HAC e a padronização do monitor por estratos. O estado previsto no esquema recebe desvios anteriores. Mantiveram-se como pendentes os fatores físicos e a correlação Solomon sem fonte conferida.
2. **Português:** revisão em português europeu AO90, incluindo a leitura do último terço. Foram mantidos os termos técnicos que identificam métodos: bootstrap, cross-fitting, CUSUM e grey-box, sempre explicados no contexto. “Realização” identifica a simulação independente e “réplica” a reamostragem.
3. **Voz e estrutura:** definições diretas, sem elogios ao método, conclusões cerimoniais ou resultados implícitos. As reservas acompanham a expressão a que se aplicam. O texto distingue o que é calculado, o que é assumido e o que continua proposto.

## Questões científicas e editoriais por fechar

Estas questões estão localizadas nas caixas MAT-01 a MAT-10 e nas propostas MAT-F01 a MAT-F12:

- Fronteiras da unidade, carga fresca/retornos e integração das tags por duração válida.
- Fonte, vigência e unidades dos fatores de GNE, vapor, eletricidade e emissões; correspondência dos três equivalentes entálpicos aos níveis de pressão.
- Conferência da correlação CC/Solomon com a fonte oficial antes de publicar os coeficientes. O rascunho fornece a estrutura do EII e as transformações necessárias.
- Diferença entre mínimo computacional de observações e admissibilidade metodológica.
- Correspondência de cada formulação consultada com o lote efetivamente citado, incluindo pesos HAC, estatística do bootstrap nulo, calendário e graus de liberdade.
- Convenções das regras de sequência: oito/nove pontos, ambos os lados na regra 8, empates, lacunas e episódios.
- Ganho preditivo do centro completo em rotas AR; significado da regra histórica de quatro em cinco; margens materiais numa avaliação futura.
- Estado dos lotes de simulação, censura, famílias de contrastes e independência entre calibração e verificação.
- Completar as fontes primárias dos diagnósticos que forem conservados; o conjunto de referências existente não foi objeto de uma auditoria bibliográfica integral nesta tarefa.

## Fontes de convenções computacionais

As fontes locais e respetivos hashes estão no manifesto. As convenções documentadas publicamente foram consultadas nas páginas oficiais:

- [SciPy — Theil–Sen e convenção do intercepto](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.theilslopes.html).
- [statsmodels — ajuste RLM e estimação da escala](https://www.statsmodels.org/stable/generated/statsmodels.robust.robust_linear_model.RLM.fit.html).
- [scikit-learn — TF–IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html).
- [scikit-learn — NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html).
- [NetworkX — modularidade](https://networkx.org/documentation/networkx-3.2/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html).

As citações académicas do rascunho usam 30 chaves já presentes na bibliografia da tese. As notas com documentação informática fundamentam convenções de implementação; a identificação exata do ambiente executado pertence ao manifesto do estudo.

## Nota sobre o mapa anterior

O mapa inicial descreveu o apêndice H como desativado por não aparecer em `0-Config/4_files.tex`. A leitura de `0-Config/revisao.tex` mostrou que H é acrescentado condicionalmente quando a revisão está visível. A compilação deste rascunho respeita esse mecanismo. H contém notas de revisão das listas preliminares e não acrescenta uma família matemática ao inventário.

## Verificação

Foram verificados a cobertura das 107 entradas, a unicidade dos identificadores do rascunho, a existência das chaves bibliográficas e a resolução estática das remissões. A compilação e a verificação do PDF ficam registadas em `compilacao.json` e `verificacao.json`. Estes controlos verificam o documento; os estudos empíricos não foram reexecutados nesta tarefa.
