# Análise do corpo da tese — 2026-09-20

## Resumo

Analisaram-se integralmente os Capítulos 3–8, usando o Capítulo 1 como referência e a revisão já feita do Capítulo 2 como contexto.
O encadeamento revisão → métodos → plataforma → diagnóstico → proposta → conclusões funciona e não precisa de uma reorganização.
O principal problema é a perda de precisão nas sínteses: resultados condicionais tornam-se, por vezes, afirmações sobre ausência de relação, calibração demonstrada ou comportamento real da operação.
Há erros verificáveis nas contagens do Corpus B, no sinal de um contraste e na legenda da matriz de aceitação.
Persistem duas questões documentais: o fecho efetivamente observado da validação e a implementação da sua repetição mensal.
Registam-se **42 achados: 10 erros factuais, 13 contradições entre capítulos, 9 afirmações sem suporte, 8 confusões e 2 dúvidas; 0 achados autónomos de redundância**.
Por gravidade: **9 altos, 29 médios e 4 baixos**; acrescentam-se 13 substituições complementares para propagar as mesmas correções.
Produziu-se apenas este Markdown: não se editaram ficheiros LaTeX, figuras, scripts ou dados, nem se compilou a tese.

Os excertos são contínuos, exatos e únicos no ficheiro indicado, com 8–30 palavras. Cada proposta substitui apenas o excerto citado, mantendo o texto circundante. Nos fragmentos de tabela, mantêm-se os separadores de células; os comandos de referência e citação existentes são preservados. As linhas foram atualizadas depois das alterações externas aos Capítulos 5, 6 e 8 ocorridas durante esta análise. As propostas não estão aplicadas.

Esta revisão aplica o protocolo de análise de afirmações e coerência ao restante corpo da tese. Não é uma nova execução dos ensaios, uma auditoria integral dos dados industriais nem uma nova extração humana dos 39 artigos. Quando se confirmou uma transcrição contra um ficheiro de resultados, essa confirmação não equivale a revalidar o estudo que produziu o ficheiro.

## Achados

### A-01 — A regra de três em cinco altera efetivamente a decisão

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:468>) — Capítulo 7
- **Linha:** 468
- **Texto atual:**

~~~latex
Nenhum candidato a cumpre nos dois critérios, e a regra de sensibilidade de três em cinco não altera essa conclusão.
~~~

- **Proposta:**

~~~latex
Nenhum candidato cumpre os dois critérios com a regra de quatro em cinco. Com três em cinco, seriam aceites três dos dezasseis candidatos de mínimos quadrados; os robustos não foram recontados.
~~~

- **Porquê:** A legenda contradiz a discussão do próprio capítulo e as conclusões. O erro também está impresso dentro da figura, pelo que corrigir apenas a legenda deixaria duas versões do resultado na mesma página. O resultado primário de zero em 32 mantém-se.
- **Como verificar:** Cap. 7, parágrafo «O que o zero em trinta e dois significa» e Tabela \ref{tab:gate}; Cap. 8, «Prescrever». Corrida T13: outputs/T13/runs/20260830T165208669276Z-b583143cacb9/T13_gate.tsv. Em _gerador/figuras.py, a função da matriz escreve também «com a regra de sensibilidade (3/5) também nenhum»: corrigir essa anotação na futura aplicação, preservando nome e numeração da figura.

### A-02 — A síntese recupera contagens antigas do Corpus B

- **Categoria:** erro factual
- **Gravidade:** alta
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:1081>) — Capítulo 3
- **Linha:** 1081
- **Texto atual:**

~~~latex
Só 27 de 140 modelos têm um regime de
reestimação declarado, 22 um domínio de validade e 13 uma validação fora da
amostra;
~~~

- **Proposta:**

~~~latex
Só 23 de 140 modelos têm um regime de reestimação declarado, 19 um domínio de validade e 13 uma validação fora da amostra;
~~~

- **Porquê:** A secção detalhada dá 23 regimes declarados e 8 + 11 = 19 domínios. O ficheiro de resultados de 18 de setembro confirma esses valores. A síntese e a linha da tabela de lacunas conservaram 27 e 22, anteriores à revisão da codificação.
- **Como verificar:** Cap. 3, «Fronteira, validade temporal e validação». Ficheiro stage_c/figuras_cap3/tabelas_cap3_2026-09-18.json, campos c6_regime e c7, no repositório de extração. Na Tabela \ref{tab:gap}, harmonizar também «27 de 140 modelos (9 artigos)» e «22»: o corpo reporta 23 modelos em oito artigos e 19 domínios. A contagem de oito artigos deve manter a deduplicação por publicação.

### A-03 — As normas dão orientações de validação que a discussão omite

- **Categoria:** erro factual
- **Gravidade:** alta
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:135>) — Capítulo 7
- **Linha:** 135
- **Texto atual:**

~~~latex
as três dizem \emph{o que} deve existir e são quase omissas sobre
\emph{como validar} o que existe
~~~

- **Proposta:**

~~~latex
os referenciais estabelecem objetivos e orientações de validação, mas não especificam um protocolo completo para avaliar a transportabilidade temporal e a deteção sob a dependência observada neste caso
~~~

- **Porquê:** A ISO 50006:2014 indica testes estatísticos em 4.4.3 e verificações de validade na aplicação em 4.6. A lacuna defendida pode ser a ausência do protocolo específico proposto, mas não uma omissão quase total de como validar. «As três» também fica ambíguo depois de enumerar quatro referenciais.
- **Como verificar:** ISO 50006:2014, pp. impressas 15–17, §§4.4.3 e 4.6; PDF local ISO50006_2014.pdf, páginas físicas 23–25. Harmonizar também, nesta secção, «sem fixar como a fazer» e «a norma não os traz», distinguindo orientações existentes de critérios operacionais que a dissertação acrescenta.

### A-04 — Não rejeitar não demonstra que não exista relação

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Ficheiro:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:51>) — Capítulo 8
- **Linha:** 51
- **Texto atual:**

~~~latex
O vapor de
24~bar passa os testes de estabilidade e de calibração precisamente por não
haver relação a mudar;
~~~

- **Proposta:**

~~~latex
No vapor de 24~bar, não se rejeita a igualdade dos declives e a cobertura é compatível com a nominal; estes resultados não demonstram estabilidade nem ausência de relação com a carga;
~~~

- **Porquê:** O Capítulo 6 explica expressamente que o teste não distingue uma constante de uma relação fraca que muda. As conclusões transformam essa indeterminação numa causa estabelecida. Não é uma reserva genérica: a interpretação atual contradiz a interpretação dos próprios testes.
- **Como verificar:** Cap. 6, «Estabilidade dos parâmetros», parágrafo posterior à Tabela \ref{tab:declives-anuais}; Cap. 7, limitações do critério de aceitação. Há formulações equivalentes a corrigir em «essa calibra razoavelmente» (Cap. 6), «estável e calibrado» e «uma banda suportada sem modelo por trás» (Cap. 7). Uma média é um modelo e pode ser uma referência útil.

### A-05 — A banda usa dispersão residual, não erros-padrão clássicos

- **Categoria:** erro factual
- **Gravidade:** alta
- **Ficheiro:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:59>) — Capítulo 8
- **Linha:** 59
- **Texto atual:**

~~~latex
os resíduos têm autocorrelação de primeira ordem
entre 0,46 e 0,90, o que invalida os erros-padrão clássicos em que a banda
se apoia;
~~~

- **Proposta:**

~~~latex
os resíduos têm autocorrelação de primeira ordem entre 0,46 e 0,90, o que compromete a inferência sob independência e aumenta a incerteza da cobertura estimada da banda;
~~~

- **Porquê:** A banda descrita é ±2 desvios-padrão residuais, não ±2 erros-padrão de um coeficiente. A dependência também não implica, por si, perda de cobertura marginal. O Capítulo 6 já faz corretamente ambas as distinções; a síntese deve conservá-las.
- **Como verificar:** Cap. 4, «Resíduos, bandas e acumulados»; Cap. 6, «Os resíduos são fortemente dependentes»; Apêndice E, definição da banda constante e da sua cobertura. Preservam-se os valores 0,46 e 0,90; este achado não pretende recertificar o seu arredondamento.

### A-06 — O estatuto do fecho da validação não é coerente

- **Categoria:** dúvida
- **Gravidade:** alta
- **Ficheiro:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:122>) — Capítulo 5
- **Linha:** 122
- **Texto atual:**

~~~latex
Cada barra é um estado verificado célula a célula; a última corresponde à correção das cinco divergências que restavam, nas referências de fuel gás dos enxofres.
~~~

- **Proposta:**

~~~latex
As barras distinguem os estados da validação; a última representa o fecho esperado após a correção das cinco divergências que restavam, nas referências de fuel gás dos enxofres.
~~~

- **Porquê:** O Capítulo 7 diz que o fecho de 400 em 400 é esperado, não observado; o Capítulo 5 fala de atualização sem divergências e a figura mostra 335 coincidências e 65 vazios como verificadas. A nota de julho localizada documenta apenas a expectativa. NÃO VERIFICADO: não se encontrou aqui uma grelha final que decida entre as versões. A proposta corresponde ao estado documental comprovável e deve ser substituída por «observado» se existir essa grelha.
- **Como verificar:** Cap. 7, limitações «Dos dados»; Cap. 5, «O fecho»; _gerador/figuras.py, f08_validacao, valores fixos da última barra. Nota salas/tese/notas-chat/2026-07-03-validacao-veredicto-final.md, no Mind Palace, regista «400/400 esperado». Confirmar no export e na grelha célula a célula posteriores à v15.1, com data. Manter os 400 casos e todas as contagens; identificar o estatuto da última barra também visualmente.

### A-07 — O sinal do efeito primário está invertido na tabela

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:483>) — Capítulo 4
- **Linha:** 483
- **Texto atual:**

~~~latex
média das diferenças diárias de perda absoluta, modelo $-$ nulo, no ano de aplicação
~~~

- **Proposta:**

~~~latex
média das diferenças diárias de perda absoluta, nulo $-$ modelo, no ano de aplicação
~~~

- **Porquê:** A definição de ΔMAE nos resultados é MAE do nulo menos MAE do modelo: positivo favorece a baseline. A tabela metodológica escreve o contrário, alterando o sentido do efeito e do critério de aceitação.
- **Como verificar:** Cap. 6, «Desempenho preditivo contra referências triviais», equação de \Delta_{\mathrm{MAE}} e legenda da figura de ganho preditivo. A proposta altera apenas o conteúdo da célula e preserva o ambiente xltabular.

### A-08 — O cenário anual não é o histórico observado da operação

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:320>) — Capítulo 6
- **Linha:** 320
- **Texto atual:**

~~~latex
A recalibração anual do método de produção pressupõe que cada ano de dados
reestima \emph{a mesma} relação física entre energia e carga, a menos de ruído
amostral.
~~~

- **Proposta:**

~~~latex
Na avaliação encadeada, testa-se se as retas anuais do método de produção reestimam \emph{a mesma} relação entre energia e carga, a menos de ruído amostral.
~~~

- **Porquê:** O Capítulo 4 esclarece que o ano de referência é escolhido num seletor e que não está documentado o histórico das escolhas. A análise ano y → y+1 é legítima, mas não demonstra que a operação tenha substituído a referência anualmente nem que tenha absorvido degradação real.
- **Como verificar:** Cap. 4, linhas 332–340, parágrafo do seletor de ano de referência. Manter a distinção também na leitura integrada do Cap. 7 e na conclusão sobre deriva acomodada: propriedade do ajuste e cenário simulado, não episódio operacional identificado.

### A-09 — A falha inferencial do vapor de 3 bar não resiste a todas as rotas

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:62>) — Capítulo 7
- **Linha:** 62
- **Texto atual:**

~~~latex
a relação anual muda de forma robusta no
vapor de 3~bar
~~~

- **Proposta:**

~~~latex
a igualdade dos declives anuais é rejeitada no vapor de 3~bar sob BH e BY, mas não na sensibilidade com blocos de 60 dias
~~~

- **Porquê:** O Capítulo 6 reporta que nenhum teste de declive mantém p < 0,05 na rota de bootstrap com blocos de 60 dias. «Robusta» sem qualificação volta a apagar a limitação que os resultados conservaram. A resistência a BY não é resistência à modelação da dependência.
- **Como verificar:** Cap. 6, fim de «Estabilidade dos parâmetros», parágrafo que começa «A leitura operacional». Rever igualmente «falha de forma robusta no vapor de 3~bar», na secção normativa do Cap. 7, e o adjetivo «robusta» na síntese do Cap. 6; manter a rejeição sob BH/BY explicitamente.

### A-10 — O comprimento base efetivo é de sete ou oito dias

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:531>) — Capítulo 4
- **Linha:** 531
- **Texto atual:**

~~~latex
comprimento base é $\lceil n^{1/3}\rceil$ observações, sete dias nas amostras
anuais,
~~~

- **Proposta:**

~~~latex
comprimento base é $\lceil n^{1/3}\rceil$ dias civis, sete ou oito nas amostras anuais avaliadas,
~~~

- **Porquê:** O código aplica o teto da raiz cúbica ao número de observações e usa o resultado como comprimento civil. As corridas E4 têm sete dias para n = 301 e oito para n = 355 ou 364. Portanto, «sete» não descreve todas as análises; «observações» também contradiz a definição de blocos civis com lacunas.
- **Como verificar:** baselines-cc/src/baselines/inference.py, default_block_length, linha 152; outputs/E4/runs/20260829T135121261692Z-2ea18e7390bb/E4_marginal_coverage.tsv, colunas n_obs e block_length. Corrigir a mesma simplificação em «Da inferência», no Cap. 7, para «sete ou oito dias»; não alterar a grelha de sensibilidades predefinida.

### A-11 — O fingerprint não é uma validação independente dos dias do Power BI

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:701>) — Capítulo 4
- **Linha:** 701
- **Texto atual:**

~~~latex
A identidade das observações
selecionadas pela \emph{baseline} de produção é guardada como
\emph{fingerprints} de referência.
~~~

- **Proposta:**

~~~latex
A identidade das observações selecionadas pela replicação do método de produção é guardada como \emph{fingerprints} de referência; não foi comparada com uma lista independente de dias exportada do Power BI.
~~~

- **Porquê:** O Capítulo 6 declara que os fingerprints foram construídos pela própria análise e que a lista de seleção do modelo original não estava disponível. Servem para detetar alterações posteriores da amostra, mas não provam, por confronto independente, a igualdade das datas selecionadas.
- **Como verificar:** Cap. 6, «Replicação como porta de entrada», parágrafo que limita a proveniência dos fingerprints; Cap. 7, limitações «Do estudo». Harmonizar a frase «é comparada por fingerprint do conjunto» na descrição da porta de replicação do Cap. 4.

### A-12 — A aceitação não certifica uma banda calibrada

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:676>) — Capítulo 4
- **Linha:** 676
- **Texto atual:**

~~~latex
e uma banda calibrada sob a hipótese de que
nada mudou.
~~~

- **Proposta:**

~~~latex
e uma banda cuja cobertura não se mostrou incompatível com a nominal pelo critério adotado.
~~~

- **Porquê:** O critério inclui o nominal no intervalo, mas não testa equivalência nem impõe precisão mínima. O Capítulo 7 reconhece que intervalos largos facilitam a aceitação. «Calibrada» atribui ao procedimento uma certificação que a tese expressamente lhe retira.
- **Como verificar:** Cap. 7, três defeitos declarados do critério de aceitação, especialmente o primeiro. Ver também Lakens2017, referência já existente, sobre a distinção entre ausência de diferença demonstrada e equivalência; não é necessário acrescentar chave bibliográfica.

### A-13 — A investigação da anomalia elétrica não identifica automaticamente a causa

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:181>) — Capítulo 6
- **Linha:** 181
- **Texto atual:**

~~~latex
se o relatório oficial também traz o valor baixo, a repartição
mudou na fonte;
~~~

- **Proposta:**

~~~latex
se o relatório oficial também traz o valor baixo, a anomalia já está presente a montante da ingestão, sem que isso identifique a sua causa;
~~~

- **Porquê:** A concordância com a fonte localiza a anomalia na cadeia de processamento; não distingue uma alteração de repartição de erro de origem ou mudança real. O próprio texto apresenta a repartição apenas como hipótese concorrente.
- **Como verificar:** Cap. 6, parágrafo da anomalia elétrica de 2021 e 2022. Confirmar os relatórios originais desses anos e o histórico de regras de alocação; a causa permanece NÃO VERIFICADO enquanto esse confronto não existir.

### A-14 — A eletricidade ainda não foi confrontada com o relatório original

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:174>) — Capítulo 6
- **Linha:** 174
- **Texto atual:**

~~~latex
a
plataforma reproduziu o valor oficial sem o assinalar
~~~

- **Proposta:**

~~~latex
a plataforma apresentou o valor da série exportada sem assinalar esta anomalia
~~~

- **Porquê:** O mesmo parágrafo pede depois a consulta do relatório oficial para decidir onde se encontra a anomalia. Até esse confronto, é demonstrável o que consta da exportação, mas não a sua concordância com o documento original.
- **Como verificar:** Cap. 6, anomalia da eletricidade, comparação proposta com os relatórios de 2021 e 2022; Cap. 5, validação documental limitada a janeiro–maio de 2026. A proposta preserva todos os consumos e percentagens do parágrafo.

### A-15 — A frequência das famílias é conhecida apenas no subconjunto concordante

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:17>) — Capítulo 3
- **Linha:** 17
- **Texto atual:**

~~~latex
Nas 331 publicações elegíveis, o rácio de intensidade
energética é a família de modelo mais frequente.
~~~

- **Proposta:**

~~~latex
Das 331 publicações elegíveis, 162 têm classificação concordante das famílias de modelos; nesse subconjunto, o rácio de intensidade energética é a família mais frequente.
~~~

- **Porquê:** Há 169 publicações por resolver neste campo. O resultado observado em 162 não estabelece a ordenação nas 331, sobretudo quando o número desconhecido excede o classificado. A secção detalhada respeita este denominador, mas a abertura e as conclusões generalizam-no.
- **Como verificar:** Cap. 3, «Cobertura dos campos extraídos» e «Famílias de modelos e enquadramento normativo»; aplicar a mesma precisão ao início do parágrafo «A revisão» do Cap. 8, preservando 331 e as contagens normativas.

### A-16 — A causa física não deve ser resumida por «quase nunca»

- **Categoria:** confusão
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:22>) — Capítulo 3
- **Linha:** 22
- **Texto atual:**

~~~latex
Os estudos relatam o que corre mal
ao modelo, mas quase nunca a causa física no processo.
~~~

- **Proposta:**

~~~latex
Das 130 ocorrências extraídas sobre o que corre mal ao modelo, 89 não nomeiam uma causa física ou operacional; esta contagem depende da cobertura da extração e das categorias de codificação.
~~~

- **Porquê:** O segundo eixo não é vazio: há 25 ocorrências nas categorias específicas e 16 em «outra». A formulação atual omite esse resultado e a hipótese, discutida no capítulo, de a taxonomia não captar bem outros setores. A substituição usa as contagens existentes, sem presumir uma ausência na literatura.
- **Como verificar:** Cap. 3, SQ2, parágrafo «O segundo eixo»; ficheiro tabelas_cap3_2026-09-18.json, campo cause. Harmonizar a frase correspondente no Cap. 8. Não confundir este eixo causal com as 130 ocorrências de efeitos nem com as 43 adaptações ligadas a mecanismos.

### A-17 — As ausências não verificadas não são limites inferiores de ausência

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:1050>) — Capítulo 3
- **Linha:** 1050
- **Texto atual:**

~~~latex
e por isso todos os ``não reportado'' são limites inferiores do
que os artigos contêm.
~~~

- **Proposta:**

~~~latex
pelo que as ocorrências identificadas podem subcontar o que os artigos contêm, enquanto as classificações ``não reportado'' podem sobrestimar as ausências.
~~~

- **Porquê:** O sentido do limite está invertido: uma extração incompleta tende a perder presenças e a produzir mais «não reportado». Além disso, os erros positivos ainda possíveis impedem tratar estes limites como garantias estatísticas.
- **Como verificar:** Cap. 3, «Extração assistida e níveis de verificação», distingue verificação de valores positivos e ausência de revisão das ausências; «Alcance e limites desta síntese» deve manter a mesma distinção.

### A-18 — O Capítulo 6 não compara as três famílias anunciadas

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:455>) — Capítulo 3
- **Linha:** 455
- **Texto atual:**

~~~latex
as três primeiras ---
  rácio, regressão linear e regressão múltipla --- são as que o
  Capítulo~\ref{cha:diagnostico} avalia no caso real.
~~~

- **Proposta:**

~~~latex
as três primeiras --- rácio, regressão linear e regressão múltipla --- enquadram o caso real; o Capítulo~\ref{cha:diagnostico} compara as regressões simples e múltipla, além dos comparadores triviais.
~~~

- **Porquê:** Nos resultados, o nulo primário é a média do consumo do treino; os secundários são o dia homólogo e a média móvel. Nenhum destes equivale a um modelo de consumo específico constante multiplicado pela carga. A legenda promete uma comparação de rácios que não é apresentada.
- **Como verificar:** Cap. 6, «Desempenho preditivo contra referências triviais» e «Suficiência da variável explicativa»; Cap. 4, tabela do contrato inferencial. Não se propõe executar uma análise nova para preencher essa promessa.

### A-19 — A ordem temporal de Hamedi passa de desconhecida a violada

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:175>) — Capítulo 7
- **Linha:** 175
- **Texto atual:**

~~~latex
\textcite{Hamedi2019} e \textcite{Moghadasi2025} validam fora
da amostra, com partições que não respeitam a ordem do tempo,
~~~

- **Proposta:**

~~~latex
\textcite{Hamedi2019} e \textcite{Moghadasi2025} validam fora da amostra: no primeiro, a ordem temporal da partição não está descrita; no segundo, a partição é aleatória,
~~~

- **Porquê:** O Capítulo 3 distingue explicitamente partição aleatória de ordem temporal não descrita. A discussão transforma falta de informação em demonstração de que Hamedi não respeita a ordem. A proposta conserva ambos os estudos e limita a conclusão ao que foi extraído.
- **Como verificar:** Cap. 3, «Fronteira, validade temporal e validação», frase «cuja ordem temporal não é descrita». Se se quiser uma afirmação mais forte, conferir a secção de divisão dos dados no texto integral de Hamedi2019; essa violação permanece NÃO VERIFICADO nesta análise.

### A-20 — Calcular um rácio não pressupõe, por si, proporcionalidade

- **Categoria:** confusão
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:439>) — Capítulo 3
- **Linha:** 439
- **Texto atual:**

~~~latex
Um rácio divide o consumo pela produção e assume, sem o testar,
que a relação passa pela origem e não tem termo constante.
~~~

- **Proposta:**

~~~latex
Um rácio divide o consumo pela produção. Usá-lo como normalizador invariável à carga pressupõe proporcionalidade entre as duas grandezas, sem termo constante relevante; a mera divisão não testa esse pressuposto.
~~~

- **Porquê:** O indicador E/Q pode ser calculado e descrito mesmo quando E = aQ + b, ficando E/Q = a + b/Q. O pressuposto de proporcionalidade pertence ao seu uso como normalização independente da carga, não à existência matemática do rácio. A crítica ao uso inadequado mantém-se.
- **Como verificar:** ISO 50006:2014, §4.5.1, p. 16, distingue rácio com uma variável e pequeno consumo de base de modelos com várias variáveis ou consumo de base elevado; identidade algébrica E/Q = a + b/Q.

### A-21 — A exclusão de outliers não é a adaptação implementada mais comum

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:917>) — Capítulo 3
- **Linha:** 917
- **Texto atual:**

~~~latex
contra dez exclusões de valores atípicos, que são a adaptação
implementada mais comum e a que menos muda o modelo.
~~~

- **Proposta:**

~~~latex
contra dez exclusões de valores atípicos, uma das adaptações implementadas mais frequentes, embora retirar observações possa alterar o ajuste sem alterar a sua forma funcional.
~~~

- **Porquê:** A tabela conta onze implementações de variáveis adicionais e onze em «outra», contra dez exclusões. «A que menos muda o modelo» também não foi medido: excluir observações pode alterar bastante os coeficientes e a população representada.
- **Como verificar:** Cap. 3, Tabela \ref{tab:b-adaptacoes}, coluna «Impl.»; tabelas_cap3_2026-09-18.json, campo adaptations. Mantém-se a contagem de dez e distingue-se forma funcional de parâmetros ajustados.

### A-22 — O acumulado não demonstrou deteção mais precoce na operação

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:341>) — Capítulo 5
- **Linha:** 341
- **Texto atual:**

~~~latex
que mostra um desvio persistente
antes de a banda diária o assinalar;
~~~

- **Proposta:**

~~~latex
que permite acompanhar a acumulação de desvios persistentes, sem que tenha sido medida a sua antecedência face ao alarme diário;
~~~

- **Porquê:** O Capítulo 4 apresenta um acumulado descritivo, distinto de um CUSUM calibrado; os Capítulos 6 e 7 dizem que não há eventos reais rotulados para medir atraso de deteção. A observação visual e o ensaio simulado não demonstram que este painel se antecipe na operação.
- **Como verificar:** Cap. 4, distinção entre acumulado e monitor sequencial; Cap. 6, «Detetabilidade». Corrigir também a legenda do painel 4 da página de baselines, que repete «antes de a banda diária o assinalar», sem retirar a figura ou a referência.

### A-23 — Diferenças com sinal constante são um indício, não prova de causa estrutural

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:232>) — Capítulo 5
- **Linha:** 232
- **Texto atual:**

~~~latex
se a diferença tem sempre o mesmo sinal e nunca é nula, é
estrutural, por mais pequena que seja.
~~~

- **Proposta:**

~~~latex
se a diferença mantém o mesmo sinal e nunca é nula, investiga-se a possibilidade de um desvio sistemático, mesmo que esteja abaixo da tolerância.
~~~

- **Porquê:** O caso do medidor omitido foi explicado pelo confronto das referências e dos valores; não apenas pelo sinal em cinco meses. A regra geral anunciada é mais forte do que essa demonstração: erros dependentes ou aleatórios podem manter o sinal numa amostra finita.
- **Como verificar:** Cap. 5, «Erros no mapeamento»: a identificação do medidor explica os cinco défices e a coincidência a 0,1 t. Preservar esses dados como prova da causa concreta; a regra proposta apenas define quando investigar.

### A-24 — A ISO 50006 não trata a escolha da janela como neutra

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:873>) — Capítulo 6
- **Linha:** 873
- **Texto atual:**

~~~latex
Para um método que a ISO 50006 trata como neutro, é um resultado
central:
~~~

- **Proposta:**

~~~latex
A ISO 50006 orienta a escolha do período pela variabilidade operacional; a sensibilidade aqui observada torna essa escolha um resultado central:
~~~

- **Porquê:** A cláusula 4.4.2 pede um período adequado à natureza da operação e suficientemente longo para captar a variabilidade, discutindo durações inferiores e superiores a um ano. Pode criticar-se a falta do ensaio de sensibilidade aqui proposto, mas não atribuir neutralidade à norma.
- **Como verificar:** ISO 50006:2014, §4.4.2 e Practical Help Box 6, p. 15; PDF local, página física 23. Mantêm-se os 133 de 312 e a distinção entre mudança de partição e mudança do período coberto.

### A-25 — A referência fixa não é a única que mede desvios

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:839>) — Capítulo 7
- **Linha:** 839
- **Texto atual:**

~~~latex
A Secção~\ref{sec:referencia-fixa} mostrou que só a segunda
mede o desvio;
~~~

- **Proposta:**

~~~latex
A Secção~\ref{sec:referencia-fixa} mostrou que a segunda conserva um termo de comparação fixo entre anos;
~~~

- **Porquê:** O Capítulo 6 demonstra que o desvio aparece ao aplicar a reta do ano anterior e só se absorve a parte projetada no ajuste quando se muda de referência. «Só a segunda» contradiz essa distinção e exagera o resultado da experiência de injeção.
- **Como verificar:** Cap. 6, «Um mecanismo comum», separação das afirmações algébrica, observada e simulada; Cap. 7, «Um desvio inserido», que limita a absorção ao período usado no reajuste. A vantagem demonstrada é conservar o mesmo termo de comparação.

### A-26 — O resultado do gerador não prevê a detetabilidade na refinaria

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:776>) — Capítulo 7
- **Linha:** 776
- **Texto atual:**

~~~latex
Estes valores são propriedades do
gerador a $\rho = 0{,}6$; na refinaria, e nos vapores, o parágrafo anterior
diz o que se pode esperar.
~~~

- **Proposta:**

~~~latex
Estes valores são propriedades do gerador a $\rho = 0{,}6$; o parágrafo anterior mostra a sua sensibilidade à dependência, sem estimar a detetabilidade real na refinaria.
~~~

- **Porquê:** A simulação fixa, além de rho, a relação de referência, distribuição do ruído, máscaras, amplitude, horizonte e forma do desvio. Aproximar a autocorrelação observada não valida todos esses elementos para a unidade. O próprio capítulo diz expressamente que a simulação não é um facto sobre a refinaria.
- **Como verificar:** Cap. 7, descrição do gerador e limitações «Da simulação»; Cap. 6, não estimabilidade da deteção real. Conservar integralmente os desvios mínimos, percentagens e valores de rho, mas com o seu estimando correto.

### A-27 — O critério não testou a classe de modelos mais complexos

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:156>) — Capítulo 8
- **Linha:** 156
- **Texto atual:**

~~~latex
o critério de aceitação mostrou que um modelo mais
complexo sem as condições de avaliação não seria mais aceitável do que o
atual.
~~~

- **Proposta:**

~~~latex
o critério de aceitação recusou as combinações avaliadas; a aceitação de modelos mais complexos continua a exigir uma avaliação própria segundo critérios previamente declarados.
~~~

- **Porquê:** A demonstração adjudicou um conjunto delimitado de estimadores e bandas. Não testou os modelos hierárquicos, físicos ou com estado enunciados na frase anterior. A exigência de avaliação é uma recomendação justificada, mas o seu desfecho não foi demonstrado.
- **Como verificar:** Cap. 4, classe de candidatos; Cap. 7, «O que o zero em trinta e dois significa»; Cap. 8, tabela do roteiro. Mantém-se a recomendação de não equiparar complexidade a qualidade.

### A-28 — A não linearidade do vapor de 3 bar permanece uma hipótese

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:193>) — Capítulo 8
- **Linha:** 193
- **Texto atual:**

~~~latex
Vapor de 3~bar: relação provavelmente não linear, covariáveis úteis
~~~

- **Proposta:**

~~~latex
Vapor de 3~bar: ganhos das covariáveis dependentes do período; não linearidade por testar
~~~

- **Porquê:** A oscilação dos declives e dos ganhos é compatível com várias causas, incluindo variáveis omitidas, mudança de regime e deslocação de suporte. O estudo não compara, nos dados reais desse vetor, modelos lineares e não lineares para estimar a probabilidade da hipótese. As covariáveis foram também prejudiciais num par.
- **Como verificar:** Cap. 6, Tabela \ref{tab:covariaveis-incremental} e hipóteses concorrentes discutidas depois dela. Manter o modelo aditivo na coluna «Opção»: faz sentido como teste futuro, não como solução para uma causa já identificada.

### A-29 — A reconciliação histórica exigida não foi integralmente demonstrada

- **Categoria:** confusão
- **Gravidade:** média
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:197>) — Capítulo 7
- **Linha:** 197
- **Texto atual:**

~~~latex
Nenhuma \emph{baseline} se
estima sobre dados que não passaram a validação de fontes do
Capítulo~\ref{cha:plataforma}:
~~~

- **Proposta:**

~~~latex
Para aplicação em produção, exige-se a validação de fontes descrita no Capítulo~\ref{cha:plataforma} para o período usado; nesta demonstração, a validação documental cobre apenas janeiro a maio de 2026:
~~~

- **Porquê:** A recomendação surge como condição já cumprida pela demonstração de todas as linhas orientadoras, mas os modelos usam 2020–2025 e a validação documental cobre 2026. As limitações reconhecem que mudanças de contabilização históricas não foram excluídas. É necessário separar requisito proposto de requisito efetivamente verificado.
- **Como verificar:** Cap. 7, limitações «Dos dados»; Cap. 5, último período de «O fecho»; Cap. 4, origem das séries dos quatro vetores. A proposta não exige divulgar mais dados industriais nem invalida a replicação dos valores exportados.

### A-30 — A repetição mensal da validação precisa de um estado confirmado

- **Categoria:** dúvida
- **Gravidade:** média
- **Ficheiro:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:237>) — Capítulo 5
- **Linha:** 237
- **Texto atual:**

~~~latex
é um teste de
aceitação permanente, que a plataforma repete a cada fecho mensal,
~~~

- **Proposta:**

~~~latex
deve constituir um teste de aceitação a repetir em cada fecho mensal,
~~~

- **Porquê:** O Capítulo 8 coloca a repetição mensal no trabalho futuro, enquanto aqui se afirma que já é executada pela plataforma. NÃO VERIFICADO: não foi identificado nesta análise um registo de execução mensal ou uma rotina que demonstre essa periodicidade. A proposta exprime o requisito até se confirmar o estado efetivo.
- **Como verificar:** Comparar Cap. 5, «O que a validação ensinou», com Cap. 8, parágrafo posterior à tabela do roteiro. Confirmar rotina, responsável, saídas e datas dos fechos executados; se já estiver implementada, conservar a afirmação no Cap. 5 e atualizar o trabalho futuro.

### A-31 — Uma quebra não faz desaparecer a quantidade média do período

- **Categoria:** confusão
- **Gravidade:** média
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:513>) — Capítulo 4
- **Linha:** 513
- **Texto atual:**

~~~latex
a série reamostrada já não tem um valor
esperado único e o intervalo deixa de apontar a uma quantidade fixa;
~~~

- **Proposta:**

~~~latex
a média pode variar no tempo, comprometendo a justificação estacionária do intervalo, embora continue definida uma média para o período avaliado;
~~~

- **Porquê:** Se a distribuição muda a meio do ano, a média do período continua matematicamente definida; o problema é a validade do procedimento usado para quantificar a sua incerteza. A frase atual confunde a existência do estimando com a justificação do estimador de incerteza.
- **Como verificar:** Cap. 4, contrato inferencial: os efeitos E2/E4 são definidos para um ano de aplicação; a decomposição semestral do Cap. 6 mostra médias locais distintas. Não se propõe aceitar a cobertura nominal do bootstrap após uma quebra nem alterar resultados.

### A-32 — A diferença entre integrações é proporcional à covariância

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:76>) — Capítulo 4
- **Linha:** 76
- **Texto atual:**

~~~latex
A diferença entre os dois cálculos é a covariância
intradiária entre caudal e poder calorífico
~~~

- **Proposta:**

~~~latex
A diferença entre os dois cálculos é proporcional à covariância intradiária entre caudal e poder calorífico
~~~

- **Porquê:** A equação citada dá a diferença entre soma de produtos e produto de agregados como H vezes a covariância, para H intervalos iguais e divisor H. O texto elimina esse fator. A correção mantém a interpretação e não acrescenta coeficientes industriais.
- **Como verificar:** Apêndice E, Equação \eqref{eq:mat-covariancia-agregacao}: soma(m_h c_h) − soma(m_h) média(c) = H Cov_H(m,c), linhas 182–191. A magnitude real do efeito continua por quantificar.

### A-33 — A legenda atribui toda a incerteza ao bootstrap e omite HAC

- **Categoria:** contradição entre capítulos
- **Gravidade:** média
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:215>) — Capítulo 6
- **Linha:** 215
- **Texto atual:**

~~~latex
os erros-padrão e os
   $p$-values clássicos não são usados neste capítulo e toda a incerteza é
   estimada por reamostragem em blocos.
~~~

- **Proposta:**

~~~latex
os erros-padrão e os $p$-values clássicos não sustentam a inferência neste capítulo; usam-se covariâncias HAC nos testes de estabilidade e reamostragem em blocos nos contrastes de perdas e coberturas.
~~~

- **Porquê:** O teste principal de estabilidade usa Wald com covariância HAC, e a figura de predições a carga comum apresenta intervalos HAC. A legenda confunde o princípio comum — considerar dependência — com um único procedimento de estimação.
- **Como verificar:** Cap. 6, «Estabilidade dos parâmetros» e legenda da figura de predições a carga comum; Cap. 4, tabela do contrato inferencial. A presença de diagnósticos clássicos no apêndice é explicitamente descritiva.

### A-34 — A duração das mudanças do processo não foi estimada

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:79>) — Capítulo 7
- **Linha:** 79
- **Texto atual:**

~~~latex
um processo cujo
comportamento muda mais devagar do que um ano e mais depressa do que a
recalibração o assinala.
~~~

- **Proposta:**

~~~latex
um processo em que se observam diferenças entre anos, sem se terem identificado as datas e as causas das mudanças.
~~~

- **Porquê:** Os testes comparam anos, mas não estimam uma duração física de mudança nem um atraso de deteção da recalibração. Sem calendário de eventos, a frase atribui uma escala temporal e uma sequência operacional que a própria tese declara não ter medido.
- **Como verificar:** Cap. 6, «Detetabilidade» e limitação da data da alteração no vapor de 10 bar em 2026; Cap. 4, seletor manual do ano de referência. A experiência simulada não identifica a duração das mudanças reais.

### A-35 — Ausência de código disponível não prova impossibilidade de reprodução

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:1096>) — Capítulo 3
- **Linha:** 1096
- **Texto atual:**

~~~latex
o que impede, na prática, que
outro autor reproduza uma referência a partir de um artigo.
~~~

- **Proposta:**

~~~latex
o que limita a reprodução independente e exige verificar, caso a caso, se a informação publicada permite reconstruir a referência.
~~~

- **Porquê:** O mesmo capítulo reporta equações completas em 24 artigos e coeficientes em 12, além de informação parcial. Falta de código não impede necessariamente reimplementação; falta de dados limita a reprodução dos resultados. O efeito depende da combinação destes campos por artigo, que não é demonstrada pela frase.
- **Como verificar:** Cap. 3, «Limitações, barreiras e reprodutibilidade»; tabelas_cap3_2026-09-18.json, campo c13. Preservar também o caso de código parcialmente disponível na síntese e na tabela, em vez de deixar «zero» ser lido como ausência absoluta.

### A-36 — «Adaptação mais proposta» não corresponde à tabela

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:1076>) — Capítulo 3
- **Linha:** 1076
- **Texto atual:**

~~~latex
melhorar
a medição é a adaptação mais proposta e menos feita.
~~~

- **Proposta:**

~~~latex
melhorar a medição é proposto seis vezes e implementado uma vez.
~~~

- **Porquê:** A tabela dá vinte propostas na categoria «outra» e seis para medição melhorada. Existem outras categorias com apenas uma implementação. O resultado relevante é o contraste entre seis propostas e uma implementação, não um máximo ou mínimo que a tabela não demonstra.
- **Como verificar:** Cap. 3, Tabela \ref{tab:b-adaptacoes} e campo adaptations do ficheiro de resultados de 18 de setembro. As contagens seis e uma já constam do texto e da tabela de lacunas.

### A-37 — A tabela dos estudos próximos diverge da codificação atualizada

- **Categoria:** erro factual
- **Gravidade:** média
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:987>) — Capítulo 3
- **Linha:** 987
- **Texto atual:**

~~~latex
exata em parte & por evento & qualitativo & n.r.
~~~

- **Proposta:**

~~~latex
exata em parte & por evento & n.r. & n.r.
~~~

- **Porquê:** A decisão do autor de 18 de setembro, nos itens MOD-015, MOD-017 e MOD-019, distingue a definição da função de um domínio de validade e fixa «not stated» para Beisheim2020. A tabela conserva «qualitativo». Ikeyama2017 também mantém «contínua», embora MOD-060 e a tabela de resultados tenham sido corrigidos para «not stated». Não é necessário reabrir essas decisões: falta propagá-las ao texto.
- **Como verificar:** decisoes_2026-09-17.json, decisao_autor/data = 2026-09-18 e itens MOD-015, MOD-017, MOD-019 e MOD-060; tabelas_cap3_2026-09-18.json, close13/Beisheim2020/envelope e close13/Ikeyama2017/regime. Alterar também «contínua» para «n.r.» na linha Ikeyama2017; conferir se o mapa de evidência usa a mesma versão.

### A-38 — A fronteira agregada não demonstra impossibilidade de normalização

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Ficheiro:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:605>) — Capítulo 6
- **Linha:** 605
- **Texto atual:**

~~~latex
Nenhuma covariável de processo da coluna a corrige,
porque a omissão não está no modelo --- está na definição do indicador.
~~~

- **Proposta:**

~~~latex
A agregação pode introduzir variáveis de atividade não representadas no modelo; a sua contribuição para o erro e o valor de covariáveis adicionais exigem avaliação.
~~~

- **Porquê:** A fronteira define a grandeza a explicar, mas não prova que ela não possa ser modelada. Como contraexemplo algébrico, uma contribuição auxiliar constante pode ser absorvida no intercepto; uma contribuição relacionada com variáveis observadas pode ser modelada. A tese ainda não quantificou a contribuição das secções nem comparou referências por secção. O Capítulo 8 coloca precisamente essa avaliação no trabalho futuro.
- **Como verificar:** Adição sobre a fronteira no Cap. 6, «Suficiência da variável explicativa»; nova linha da Tabela do roteiro no Cap. 8. No Cap. 2 há uma formulação absoluta semelhante, «nenhuma reestimação da reta corrige», que deve ser confrontada com a mesma distinção. Preservar a fronteira declarada e não apresentar a ausência de relação com a carga como resultado medido.

### A-39 — O sentido dos 28% deve ficar explícito

- **Categoria:** confusão
- **Gravidade:** baixa
- **Ficheiro:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:903>) — Capítulo 3
- **Linha:** 903
- **Texto atual:**

~~~latex
2,82~GWh, contra 2,03~GWh com uma
referência constante, uma diferença de 28\%.
~~~

- **Proposta:**

~~~latex
2,82~GWh, contra 2,03~GWh com uma referência constante; este último valor é 28\% inferior ao primeiro.
~~~

- **Porquê:** A fonte calcula a redução da estimativa constante face à estimativa ajustada: (2,82 − 2,03)/2,82. A frase atual pode ser lida como aumento de 28% ao passar da constante à ajustada, que teria outro denominador.
- **Como verificar:** Velazquez_2013.pdf, página física 8, p. impressa 224, parágrafo sobre a Figura 7. Confirmado no PDF local; os dois consumos, a percentagem e a citação existente são preservados.

### A-40 — Motor, mapeamento e relatório não são as três fontes de dados

- **Categoria:** confusão
- **Gravidade:** baixa
- **Ficheiro:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:129>) — Capítulo 5
- **Linha:** 129
- **Texto atual:**

~~~latex
sete causas, e o resultado mais instrutivo da validação é onde essas
causas estavam: em todas as três fontes.
~~~

- **Proposta:**

~~~latex
sete causas, e o resultado mais instrutivo da validação é onde essas causas estavam: no motor de ingestão, no mapeamento e no relatório oficial.
~~~

- **Porquê:** As três fontes foram definidas como historiador, balanços e relatórios de eletricidade. Motor e mapeamento são etapas da transformação. A alternância de sentido torna a conclusão sobre a independência das fontes mais difícil de acompanhar.
- **Como verificar:** Cap. 4, «Fontes»; Cap. 5, três parágrafos seguintes. Fazer a mesma correção no Cap. 8, «As causas estavam nas três fontes», sem alterar a enumeração dos sistemas de origem.

### A-41 — A regra de exclusão do intervalo precisa de dizer que conclusão sustenta

- **Categoria:** confusão
- **Gravidade:** baixa
- **Ficheiro:** [chapter-4-metodos.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:556>) — Capítulo 4
- **Linha:** 556
- **Texto atual:**

~~~latex
Uma
conclusão existe apenas quando o intervalo exclui o valor de referência;
nunca por comparação de pontos.
~~~

- **Proposta:**

~~~latex
Uma conclusão de diferença estatística exige que o intervalo exclua o valor de referência; a compatibilidade usada na aceitação é uma decisão distinta, não uma prova de equivalência.
~~~

- **Porquê:** O critério C2 decide pela inclusão do nominal e os diagnósticos contêm resultados descritivos, logo nem toda a conclusão obedece à frase universal. Especificar «diferença estatística» evita contradizer o procedimento apresentado no mesmo capítulo.
- **Como verificar:** Cap. 4, contrato inferencial e «O que o critério aceita»; Cap. 7, limitações explícitas da regra de compatibilidade. Não se alteram o critério nem os intervalos.

### A-42 — Há uma discordância simples na ligação ao desenho comum

- **Categoria:** confusão
- **Gravidade:** baixa
- **Ficheiro:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:76>) — Capítulo 7
- **Linha:** 76
- **Texto atual:**

~~~latex
os
quatro vetores diários partilham um desenho, e é sobre ela que a
proposta deste capítulo se constrói:
~~~

- **Proposta:**

~~~latex
os quatro vetores diários partilham um desenho, sobre o qual se constrói a proposta deste capítulo:
~~~

- **Porquê:** O antecedente é «desenho», masculino. A frase pode ficar impessoal e mais direta sem perder qualquer elemento do argumento.
- **Como verificar:** Cap. 7, parágrafo «Modos de falha distintos, um desenho comum». Correção estritamente linguística.

## Substituições complementares

Estas passagens propagam os achados anteriores; não são novos achados nem novas conclusões. Aplicar a correção numa conclusão e deixar a formulação antiga numa legenda manteria a contradição.

### C-01 — Contagens na tabela de lacunas

- **Ficheiro e linha:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:1122>), linha 1122.
- **Texto atual:**

~~~latex
Regime de reestimação em 27 de 140 modelos (9 artigos); domínio de
    validade em 22 (numérico em 11, 3 artigos);
~~~

- **Proposta:**

~~~latex
Regime de reestimação em 23 de 140 modelos (8 artigos); domínio de validade em 19 (numérico em 11, 3 artigos);
~~~

### C-02 — Frequência das famílias nas conclusões

- **Ficheiro e linha:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:96>), linha 96.
- **Texto atual:**

~~~latex
Nas 331 publicações elegíveis, o rácio de
intensidade é a família de modelo mais frequente,
~~~

- **Proposta:**

~~~latex
Entre as 162 publicações com classificação concordante das famílias de modelos, de um total de 331 elegíveis, o rácio de intensidade é a família mais frequente,
~~~

### C-03 — Ausência de ganho não é ausência de informação

- **Ficheiro e linha:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:49>), linha 49.
- **Texto atual:**

~~~latex
Nos três níveis de vapor, a carga não traz informação
utilizável de um ano para o seguinte:
~~~

- **Proposta:**

~~~latex
Nos três níveis de vapor, não se demonstrou um ganho preditivo consistente da reta anual sobre a média do treino:
~~~

### C-04 — Compatibilidade da banda no Capítulo 6

- **Ficheiro e linha:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:424>), linha 424.
- **Texto atual:**

~~~latex
a banda de um modelo sem
relação a proteger é uma banda em torno de uma média, e essa calibra
razoavelmente.
~~~

- **Proposta:**

~~~latex
uma banda em torno de uma relação fraca pode apresentar cobertura compatível com a nominal, sem que isso demonstre calibração ou ausência de relação.
~~~

### C-05 — A média continua a ser um modelo

- **Ficheiro e linha:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:509>), linha 509.
- **Texto atual:**

~~~latex
protege um modelo sem
relação a proteger: é o espelho do fuel gás, uma banda suportada sem modelo
por trás.
~~~

- **Proposta:**

~~~latex
acompanha uma reta sem ganho preditivo consistente sobre a média. O contraste com o fuel gás separa os dois critérios, sem retirar à média o estatuto de modelo.
~~~

### C-06 — Comprimento base nas limitações

- **Ficheiro e linha:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:918>), linha 918.
- **Texto atual:**

~~~latex
O intervalo de
confiança por \emph{bootstrap} de blocos usa um bloco base de sete dias
~~~

- **Proposta:**

~~~latex
O intervalo de confiança por \emph{bootstrap} de blocos usa um bloco base de sete ou oito dias
~~~

### C-07 — Antecedência não medida na legenda do dashboard

- **Ficheiro e linha:** [chapter-5-plataforma.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:366>), linha 366.
- **Texto atual:**

~~~latex
soma acumulada dos resíduos, que revela o
  desvio persistente antes de a banda diária o assinalar.
~~~

- **Proposta:**

~~~latex
soma acumulada dos resíduos, que permite acompanhar a persistência dos desvios; não foi medida a sua antecedência face ao alarme diário.
~~~

### C-08 — Causas nas conclusões da plataforma

- **Ficheiro e linha:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:30>), linha 30.
- **Texto atual:**

~~~latex
As causas estavam nas três fontes: no
motor de ingestão, no mapeamento e no próprio relatório oficial.
~~~

- **Proposta:**

~~~latex
As causas distribuíam-se pelo motor de ingestão, pelo mapeamento e pelo próprio relatório oficial.
~~~

### C-09 — Causas físicas nas conclusões da revisão

- **Ficheiro e linha:** [chapter-8-conclusoes.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:102>), linha 102.
- **Texto atual:**

~~~latex
Os estudos relatam o efeito
sobre o modelo e quase nunca a causa física no processo
~~~

- **Proposta:**

~~~latex
Na extração dos mecanismos, 89 das 130 ocorrências não nomeiam uma causa física ou operacional, resultado condicionado pela cobertura e pela codificação
~~~

### C-10 — Robustez qualificada no Capítulo 6

- **Ficheiro e linha:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:382>), linha 382.
- **Texto atual:**

~~~latex
a evidência
inferencial de que a relação muda é robusta no vapor de 3~bar
~~~

- **Proposta:**

~~~latex
a rejeição da igualdade dos declives resiste a BY no vapor de 3~bar, mas não à sensibilidade com blocos de 60 dias
~~~

### C-11 — Robustez qualificada na discussão normativa

- **Ficheiro e linha:** [chapter-7-discussao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:140>), linha 140.
- **Texto atual:**

~~~latex
falha de forma robusta no vapor
de 3~bar, falha de forma dependente do método no fuel gás e no de 10~bar,
~~~

- **Proposta:**

~~~latex
a igualdade dos declives é rejeitada sob BH e BY no vapor de 3~bar, mas não com blocos de 60 dias; no fuel gás e no de 10~bar, a rejeição também depende do método,
~~~

### C-12 — Regime de reestimação de Ikeyama2017

- **Ficheiro e linha:** [chapter-3-revisao.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:991>), linha 991.
- **Texto atual:**

~~~latex
n.r. & contínua & não declarado & n.r.
~~~

- **Proposta:**

~~~latex
n.r. & n.r. & não declarado & n.r.
~~~

### C-13 — Dependência da carga nas secções agregadas

- **Ficheiro e linha:** [chapter-6-diagnostico.tex](</Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:604>), linha 604.
- **Texto atual:**

~~~latex
cujo consumo não responde à
tonelagem de crude.
~~~

- **Proposta:**

~~~latex
cujo consumo pode depender de variáveis adicionais à tonelagem de crude.
~~~

## Apreciação por capítulo

| Capítulo | Apreciação | Trabalho prioritário |
|---|---|---|
| 3 — Revisão de âmbito | A distinção entre corpus, extração e evidência é explícita e permite ao leitor avaliar as limitações. A abertura e a síntese ainda não acompanham inteiramente a versão revista dos resultados. | Propagar as decisões de 18 de setembro; corrigir contagens e denominadores; manter «não reportado» distinto de ausência comprovada. |
| 4 — Métodos | É o capítulo de consulta técnica. Define comparadores, populações e estimandos com detalhe suficiente para orientar os resultados. | Corrigir o sinal de E2, os sete/oito dias e o alcance dos fingerprints; distinguir compatibilidade de calibração. |
| 5 — Plataforma | Os erros concretos e a sua resolução dão substância ao contributo de engenharia. O texto explica bem por que coincidência contabilística não prova medição física. | Fechar o estatuto documental da última barra da validação; confirmar a execução mensal; retirar a promessa de antecedência do acumulado. |
| 6 — Diagnóstico | É onde a evidência está mais cuidadosamente delimitada: comparadores, sensibilidade e resultados não estimáveis aparecem junto dos números. | Fazer as sínteses e legendas respeitarem essas delimitações; separar o cenário anual do histórico da operação; corrigir a interpretação normativa. |
| 7 — Discussão | A separação entre previsão, referência e monitor é útil, e o resultado negativo está explicado. Algumas frases retóricas excedem o que os próprios parágrafos de limitações permitem concluir. | Corrigir a Figura 7.2 e as afirmações de robustez, ausência de relação e exclusividade da referência fixa; distinguir recomendação de condição já satisfeita. |
| 8 — Conclusões | Retoma os objetivos e distingue o bloco de saúde proposto do que foi entregue. É o capítulo que mais precisa de recuperar as condições dos resultados resumidos. | Corrigir a interpretação dos testes, a banda e a generalização dos modelos complexos; manter cada conclusão ligada ao seu estimando. |

O contributo defensável não depende de provar que toda a classe linear falha, que a norma não dá orientação ou que a refinaria sofreu uma degradação identificada. Está na plataforma rastreável, na replicação do método avaliado, no diagnóstico por vetor e período e na explicitação de um procedimento de decisão com limitações conhecidas. Corrigir as afirmações excessivas protege esse contributo.

## Decisões editoriais e redundância

### O que deve ficar em cada capítulo

O Capítulo 3 deve sustentar o mapa da literatura e as lacunas dentro do corpus. O Capítulo 4 deve conservar as definições completas, o desenho dos ensaios e as condições de reprodução. Os Capítulos 5 e 6 devem mostrar a evidência. O Capítulo 7 deve explicar as consequências e delimitar as prescrições. O Capítulo 8 deve responder aos objetivos.

Não proponho trocar secções nem deslocar tabelas. A função de cada capítulo já é reconhecível. As repetições que merecem atenção são sobretudo as que mudam o sentido: «não se rejeita» no resultado, «passa» na síntese e «não há relação» na conclusão não são três versões equivalentes.

### Métodos e resultados: o que pode encolher

Na futura revisão de extensão, o primeiro candidato a encurtar é a repetição do mecanismo geral de reajuste entre a leitura integrada do Capítulo 7 e o início da exploração com referência congelada. A explicação algébrica completa já está no Capítulo 6. No Capítulo 7 basta retomá-la para distinguir o que a injeção mede do que é identidade matemática.

Conservar, porém, junto de cada resultado: população avaliada, comparador, sinal do efeito, estatuto do intervalo e limitação que altera a interpretação. Remeter tudo para os métodos tornaria figuras e tabelas menos autónomas. Não se propõe apagar números, citações ou referências para reduzir páginas.

O Capítulo 8 pode ser mais curto, mas não à custa de retirar «sob o gerador», «no subconjunto concordante» ou «não demonstra equivalência». São condições do resultado, não ressalvas decorativas. Nesta análise não se identificou uma passagem cuja remoção isolada, sob as restrições do pedido, fosse preferível a uma correção localizada; por isso não há achados autónomos de redundância.

### Figuras, tabelas e paginação

Inspecionaram-se no primeiro PDF consultado, sem recompilar, as páginas físicas 77, 100, 137 e 153, correspondentes às páginas impressas 50, 73, 110 e 126. Depois de uma atualização externa do documento, conferiu-se também o roteiro nas páginas físicas 154–156, impressas 127–129, do PDF de 294 páginas.

- **Figura 5.1 — progressão da validação:** o problema prioritário é o estatuto da última barra, não a paleta. Se for uma projeção, distingui-la por contorno ou padrão e uma indicação «esperado»; se for observada, ligar a contagem à grelha final. Manter as contagens e não converter vazios em sucessos.
- **Figura 7.2 — matriz de decisão:** corrigir a frase errada dentro da imagem, além da legenda. A própria matriz mostra 4/5 e 3/5 nas três primeiras combinações de fuel gás; portanto, o erro é verificável na figura. A anotação inferior é pequena: pode ganhar legibilidade quando for corrigida, mantendo os painéis e o estilo.
- **Tabela 3.6 — estudos próximos:** é densa, mas cabe na página e não apresenta a hifenização que justificaria uma reestruturação urgente. Corrigir primeiro as células que ficaram desatualizadas. Não acrescentar colunas.
- **Tabela 8.2 — roteiro:** a nova linha sobre a fronteira levou a uma conversão externa para uma tabela repartida. Na versão atual, o conteúdo ocupa as páginas impressas 127–128, mas a página 128 anuncia continuação e a 129 apresenta apenas o fecho, sem nova linha de conteúdo. Esta continuação vazia merece correção tipográfica no fecho da paginação; manter a estrutura, os dados e a numeração da tabela. A hipótese sobre a fronteira requer também a precisão de A-38. Não acrescentar uma figura que repita o roteiro.

As decisões específicas da análise anterior — nota sobre edições, divisão da apresentação do método entre os Capítulos 2 e 4 e tratamento da tabela normativa — permanecem no [relatório do Capítulo 2](/Users/bernardoribeiro/Desktop/Tese/novathesis/_revisao/2026-09-20-cap2-analise.md). Não se reabrem a nomenclatura, a política de citações nem a matriz única de cláusulas.

## Adições opcionais, com função definida

Estas adições não exigem resultados novos, não substituem os achados e não devem ser todas inseridas por acumulação. Recomenda-se no máximo uma intervenção onde resolver uma dificuldade concreta de leitura.

### 1. Explicitar o limite entre a validação de 2026 e o diagnóstico histórico

No final da secção de validação do Capítulo 5, depois da delimitação dos meses, pode substituir-se uma repetição mais genérica por esta ligação:

~~~latex
Esta validação verifica a contabilização no período observado. Na avaliação histórica, replica-se o método aplicado à série exportada; não se dispõe de uma verificação documental equivalente para todos os anos. Uma mudança entre anos pode, por isso, refletir alterações do processo, da medição ou da contabilização, que a replicação numérica, por si só, não distingue.
~~~

A informação já está nos Capítulos 4 e 7. A utilidade é impedir que o leitor transporte a validação documental de cinco meses para seis anos de dados.

### 2. Encerrar a interpretação dos testes sem voltar a explicar toda a inferência

Na síntese do Capítulo 6, apenas se as correções localizadas não forem suficientes:

~~~latex
A interpretação conserva três distinções: não rejeitar a igualdade dos declives não demonstra estabilidade; incluir a cobertura nominal no intervalo não demonstra calibração; e observar um desvio não identifica a sua causa operacional. O diagnóstico quantifica as diferenças e a sua sensibilidade, sem substituir a informação externa necessária para as explicar.
~~~

Este parágrafo usa distinções já estabelecidas no capítulo. Evitar repeti-lo também nas conclusões: aí bastam formulações corretas de cada resultado.

### 3. Dizer exatamente o que a demonstração deixa pronto

No Capítulo 7, junto da especificação para a plataforma, se for necessário uma transição mais curta:

~~~latex
Distingue-se o procedimento demonstrado dos requisitos para entrada em produção. A demonstração permite rastrear os resultados e aplicar o critério declarado; a utilização operacional exige ainda as margens materiais, a informação de eventos e a verificação prospetiva que aqui não ficaram disponíveis.
~~~

Não acrescentar um novo diagrama de referência, estado e monitor: a figura existente já cumpre essa função. Para explicar o estatuto dos entregáveis, a Tabela 8.1 também já é suficiente.

## O que decidi não mudar

1. **A replicação das 30 células vetor–ano e a ordem do erro numérico.** É um resultado distinto da validação física ou inferencial. Corrige-se o alcance dos fingerprints, sem retirar a replicação.
2. **O ganho de 30–40% do fuel gás em quatro transições.** Está delimitado pelo comparador, pelos pares favoráveis e pelos intervalos; não necessita de ser diluído por cautela genérica.
3. **As coberturas muito baixas e muito altas das bandas.** As contagens e proporções documentam a heterogeneidade. Não transformar as excursões em falsos alarmes, mas também não apagar a sua gravidade operacional.
4. **O resultado primário de zero candidatos aceites em 32.** A tabela, o critério 4/5 e a adjudicação sustentam-no. Corrigir a sensibilidade 3/5 não apaga esse resultado.
5. **A explicação dos defeitos do critério de aceitação.** A preferência involuntária por intervalos largos, a dependência entre pares e a exclusão de referências constantes estão bem identificadas; não substituir essa discussão por «o critério é robusto».
6. **A diferença entre a banda AR e uma simples mudança de largura.** O Capítulo 7 reconhece que o centro também muda e que o ganho desse preditor completo não foi adjudicado. Essa precisão é necessária.
7. **A distinção entre quantílica recomendada e quantílica efetivamente ensaiada.** O texto admite que a versão anual não testa a recomendação plurianual; não reporta o resultado negativo como impossibilidade da rota.
8. **A deteção real não estimável e a simulação com verdade conhecida.** São dois resultados com estatutos diferentes, já bem apresentados. Corrigem-se apenas as frases que os voltam a fundir.
9. **Os ganhos de 32–49 pontos percentuais ao trocar o monitor no gerador primário.** O resultado tem comparações emparelhadas e gerador declarado. A sua força mantém-se dentro desse desenho.
10. **A exclusão da eletricidade da inferência diária.** A alocação mensal não fornece a resolução necessária para localizar desvios intramensais. A causa da anomalia de dois anos é que continua por fechar.
11. **A anticorrelação entre vapores como associação, com hipóteses concorrentes.** O Capítulo 6 evita uma seta causal sem fundamento; não acrescentar um mecanismo físico como se tivesse sido identificado.
12. **A sensibilidade julho–junho.** O texto já separa mudança da partição de mudança do período coberto. Não descrever os 43% como efeito isolado da data de início do ano.
13. **As limitações do bootstrap e o resultado 357/400.** Estão explicitados, incluindo a diferença entre o bloco usado na simulação de validação e o bloco base. Corrigir sete/oito dias não resolve nem esconde a limitação.
14. **As unidades de análise da revisão e o caráter não aleatório do Corpus B.** Publicações, aplicações, modelos e ocorrências são objetos distintos; as contagens não têm de somar entre si.
15. **A incidência de adaptações em 36 dos 39 artigos e as 43 ligações em 88 ocorrências.** São resultados que contrariam as expectativas iniciais, e o texto assume essa discordância. Não os substituir por uma narrativa de escassez geral.
16. **A decisão de não responder à SQ4 e a cronologia das decisões metodológicas.** A revisão posterior não deve ser apresentada como origem de decisões anteriores. A tese faz bem em documentar isso.
17. **A ressalva sobre os dados de fuel gás e as fontes dependentes.** Coincidência entre processamentos não equivale a uma medição independente; esta limitação deve permanecer junto da validação.
18. **A distinção entre entrega da plataforma e bloco de saúde proposto.** A Tabela 8.1 é útil e evita atribuir implementação a requisitos ainda especificados.
19. **A regra de não identificar ineficiência sem informação operacional.** O facto de um desvio ser estatisticamente convincente não identifica a sua causa. Conservar a separação sem diminuir os resultados medidos.
20. **As escolhas já fixadas de nomenclatura e citação.** Não se propõem novas traduções de EnPI/EnB, nem alterações à política normativa, nem mais detalhe confidencial sobre a unidade.

## Dúvidas para o autor

Estas perguntas ficam registadas para o fecho documental; não impediram a análise nem exigem repetir decisões já adjudicadas.

1. **Fecho da validação:** existe a grelha completa ou export que documente o estado final depois da v15.1, com data e classificação das 400 células? **NÃO VERIFICADO.** Uma atualização sem erros de execução não basta, por si, para demonstrar coincidência célula a célula. A resposta decide A-06 e a redação correspondente nos Capítulos 5, 7 e 8.
2. **Validação mensal:** a comparação a três leituras já corre em cada fecho, por rotina automática ou procedimento humano, e existem saídas registadas? **NÃO VERIFICADO.** A resposta decide se se corrige o estado atual do Capítulo 5 ou o trabalho futuro do Capítulo 8.
3. **Anomalia elétrica:** foi entretanto possível consultar os relatórios cumulativos de dezembro dos anos afetados? **NÃO VERIFICADO.** Se não, manter a anomalia identificada e a causa por fechar; não escolher entre ingestão, repartição e erro de origem por eliminação verbal.
4. **Reinspeção científica da exploração com referência congelada:** existe um relatório posterior que encerre os lotes ainda em correção? **NÃO VERIFICADO nesta análise.** Os Capítulos 4 e 7 conservam um estado de trabalho em curso. Só uma reinspeção datada permite mudar esse estado ou usar os lotes excluídos; não se presume que estejam aprovados.
5. **Versão de entrega do pacote reprodutível:** manter-se-á o estado de trabalho futuro ou existe já um pacote público com código, ambiente e dados sintéticos que possa ser identificado? **NÃO VERIFICADO nesta análise.** A tese atual assume que ainda é trabalho futuro; conservar essa formulação até haver o artefacto.

Não se pede nova decisão sobre R1/R4, sobre a amostra de dez confirmações ou sobre o domínio de Beisheim2020: o ficheiro de adjudicação regista as decisões de 18 de setembro, incluindo que a amostra de controlo não foi lida. O trabalho necessário é refletir o estado existente no texto e preservar a limitação.

## Fontes e verificação desta análise

Leram-se integralmente os seis ficheiros dos Capítulos 3–8. O Capítulo 1 foi usado para confrontar objetivos, contribuições e estados dos entregáveis; o Capítulo 2 e a sua revisão serviram para a coerência normativa. Os apêndices foram consultados nos pontos matemáticos e metodológicos indicados, sem se apresentar isso como uma revisão integral dos apêndices.

As principais verificações adicionais foram:

- [Tabelas do Corpus B — 18 de setembro](/Users/bernardoribeiro/LocalResearch/Screening/level3_extraction/stage_c/figuras_cap3/tabelas_cap3_2026-09-18.json): contagens de modelos, reestimação, domínio, adaptações e reprodutibilidade.
- [Decisões de extração, incluindo adjudicação do autor de 18 de setembro](/Users/bernardoribeiro/LocalResearch/Screening/level3_extraction/stage_c/verification_v1/verificacao_modelo/decisoes_2026-09-17.json): propagação das correções MOD-015/017/019/060.
- [Cobertura marginal E4](/Users/bernardoribeiro/LocalResearch/baselines-cc/outputs/E4/runs/20260829T135121261692Z-2ea18e7390bb/E4_marginal_coverage.tsv) e [cálculo do bloco base](/Users/bernardoribeiro/LocalResearch/baselines-cc/src/baselines/inference.py:152): comprimentos efetivos de sete ou oito dias.
- [Adjudicação T13](/Users/bernardoribeiro/LocalResearch/baselines-cc/outputs/T13/runs/20260830T165208669276Z-b583143cacb9/T13_gate.tsv) e [resumo da corrida](/Users/bernardoribeiro/LocalResearch/baselines-cc/outputs/T13/runs/20260830T165208669276Z-b583143cacb9/T13_summary.json): critério primário e ausência de candidatos aceites nesse critério.
- [Gerador das figuras](/Users/bernardoribeiro/Desktop/Tese/novathesis/_gerador/figuras.py): contagens fixas da Figura 5.1 e anotação contraditória da Figura 7.2. Nenhum gerador foi executado.
- [Apêndice matemático](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-E-matematica.tex): identidade da covariância na agregação e distinção entre dispersão residual, intervalo de predição e incerteza dos parâmetros.
- [Registo da validação de julho](</Users/bernardoribeiro/Desktop/Mind Palace/salas/tese/notas-chat/2026-07-03-validacao-veredicto-final.md>): documenta o fecho esperado; não substitui a grelha final.
- PDFs locais ISO50006_2014.pdf, §§4.4.2, 4.4.3, 4.5.1 e 4.6, e Velazquez_2013.pdf, p. 224, nas páginas especificadas nos achados. A confirmação normativa não introduz uma nova edição nem reabre a política de tradução.
- [Lakens, 2017 — Equivalence Tests](https://doi.org/10.1177/1948550617697177), referência já citada pela tese: não rejeição de diferença não demonstra equivalência. [NIST — Statistical Process Monitoring for Autocorrelated Data](https://www.nist.gov/publications/statistical-process-monitoring-autocorrelated-data): a dependência requer tratamento próprio na monitorização. Estas fontes apoiam distinções metodológicas; não certificam os intervalos concretos da dissertação.

Os excertos e as linhas foram verificados contra os ficheiros consultados. A primeira comparação dos hashes de 290 ficheiros .tex não detetou alterações; durante a redação final ocorreram alterações externas, cujas diferenças relevantes foram relidas. Atualizaram-se as linhas e acrescentou-se o achado sobre a fronteira agregada. Esta análise escreveu apenas este Markdown. A inspeção visual usou exclusivamente os PDFs existentes em cada momento, sem produzir novos ficheiros de imagem.
