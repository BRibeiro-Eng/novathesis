# Análise do Capítulo 2 — 2026-09-20

## Resumo

O capítulo liga o enquadramento normativo, as limitações estatísticas e a física do caso de estudo, mas a leitura das normas ainda precisa de correções substantivas.
O problema principal é a passagem de «não se fixa um critério quantitativo obrigatório» para «não existe orientação ou procedimento».
Encontraram-se contraexemplos nas próprias ISO 50006 e ISO 50015 e no tratamento da autocorrelação pela ASHRAE.
Há também desencontros com a seleção do ano de referência descrita no Capítulo 4, com a interpretação dos coeficientes no Capítulo 6 e com as conclusões do Corpus B no Capítulo 3.
A crítica à adequação estatística do método pode manter-se, desde que se delimitem estes pontos e se distinga previsão de comparação contrafactual.
Registam-se **20 achados: 7 erros factuais, 3 contradições entre capítulos, 3 afirmações sem suporte, 6 confusões e 1 dúvida; 0 achados autónomos de redundância**.
Por gravidade: **10 altos, 9 médios e 1 baixo**. As recorrências e as três decisões editoriais são tratadas em secções próprias.
Produziu-se apenas este Markdown; as propostas não foram aplicadas ao LaTeX.

As linhas referem-se à versão atual de [chapter-2-enquadramento.tex](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex). As citações de «Texto atual» são excertos contínuos, exatos e únicos, com 8–30 palavras. Cada proposta substitui apenas esse excerto; preserva-se o texto circundante e os comandos de citação e referência que nele se encontram. Nos fragmentos de tabela, conserva-se a separação das células.

## Achados

### A-01 — A ISO 50006 nomeia testes e indica o que fazer quando o modelo falha

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 126
- **Texto atual:**

~~~latex
não diz \emph{que} testes, \emph{com que limiares}, \emph{com que frequência}, nem \emph{o que fazer} quando falham.
~~~

- **Proposta:**

~~~latex
nomeia testes e recomenda ajustar o EnB ou determinar um novo modelo quando se conclui pela sua invalidade, mas não fixa limiares universais de aceitação nem uma periodicidade única de verificação.
~~~

- **Porquê:** A frase é desmentida pela própria transcrição que se segue no capítulo. A ausência de requisitos vinculativos não equivale à ausência de orientação sobre testes ou resposta à invalidade.
- **Como verificar:** ISO 50006:2014, §4.4.3, p. 16 (página 24 do PDF local); confronto com a linha 147 do capítulo.
- **Coerência com outras ocorrências:** Na linha 126, «sem que lhe corresponda procedimento nenhum» só é defensável se ficar expressamente limitado à separação causal entre erro do modelo e alteração de desempenho.

### A-02 — Existem procedimentos para acompanhar a validade do EnPI e do EnB

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 194
- **Texto atual:**

~~~latex
ou fornece critérios operacionais
para detetar que uma referência deixou de ser válida.
~~~

- **Proposta:**

~~~latex
ou fixa um procedimento estatístico de deteção com desempenho quantificado. Há, contudo, orientação operacional: comparam-se os domínios das variáveis relevantes e identificam-se mudanças dos fatores estáticos (ISO~50006, \S4.6); no plano de M\&V, preveem-se meios de acompanhar a necessidade de ajustamentos não rotineiros e procedimentos para os executar (ISO~50015, \S5.10.2).
~~~

- **Porquê:** A ISO 50006 apresenta verificações concretas; a ISO 50015 inclui a monitorização da necessidade de ajustamento. A lacuna que subsiste é a especificação e avaliação estatística de um detetor, não a inexistência de qualquer mecanismo operacional.
- **Como verificar:** ISO 50006:2014, §4.6, p. 17 (PDF 25); ISO 50015:2014, §5.10.2, pp. 11–12 (PDF 17–18). A própria Tabela 2.4, linha 287, já classifica esta orientação como qualitativa.
- **Coerência com outras ocorrências:** Rever em conjunto a linha 149, as linhas 186–198 e a linha 241 da Tabela 2.3. As expressões «silêncio quanto à validade» e «não contêm o mecanismo» precisam da mesma delimitação; ver as substituições complementares abaixo.

### A-03 — O reporte da incerteza não está ausente da ISO 50015

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 243
- **Texto atual:**

~~~latex
Obrigatoriedade; limiares; reporte junto ao resultado & A incerteza declarada é gerível caso a caso
~~~

- **Proposta:**

~~~latex
Obrigatoriedade; limiares quantitativos de aceitação & A incerteza declarada é gerível caso a caso
~~~

- **Porquê:** A matriz atribui à norma uma omissão que as cláusulas de reporte contradizem. A §4.2 recomenda declarar a exatidão e as medidas de mitigação da incerteza nos resultados; a §6.5 recomenda uma declaração de exatidão ou incerteza no relatório. Mantém-se a distinção entre recomendação e obrigação.
- **Como verificar:** ISO 50015:2014, §4.2, p. 4 (PDF 10), §6.5 e §7, p. 14 (PDF 20). O qualificativo «na medida do praticável» da §7 incide sobre a quantificação das fontes de incerteza.
- **Coerência com outras ocorrências:** A linha 285 da Tabela 2.4 deve distinguir reporte recomendado de quantificação condicionada. A linha 243 da matriz pode conservar a referência à §7; as cláusulas de reporte ficam explicadas em prosa.

### A-04 — A orientação sobre outliers inclui investigação, justificação e prevenção de viés

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 247
- **Texto atual:**

~~~latex
Procedimento e critério de exclusão; efeito sobre $\sigma$
~~~

- **Proposta:**

~~~latex
Limiar quantitativo uniforme de exclusão; efeito sobre $\sigma$
~~~

- **Porquê:** A norma recomenda investigar antes de excluir, documentar a razão e evitar introduzir viés no EnPI ou no EnB. Apresenta também identificação gráfica e um critério baseado num número predeterminado de desvios-padrão, sem fixar esse número. É incorreto resumir isto como ausência de procedimento ou critério.
- **Como verificar:** ISO 50006:2014, §4.2.6.4 e Practical Help Box 4, p. 12 (PDF 20).
- **Coerência com outras ocorrências:** Corrigir também «Rever, sem critério» na linha 281 da Tabela 2.4. Não se propõe qualquer remoção dos dados nem alteração ao filtro usado na dissertação.

### A-05 — A ASHRAE trata explicitamente resíduos autocorrelacionados

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 292
- **Texto atual:**

~~~latex
e todos são omissos quanto à verificação dos pressupostos distribucionais dos seus próprios índices e quanto à não-estacionariedade estrutural.
~~~

- **Proposta:**

~~~latex
mas não se pode generalizar esta crítica a todos os pressupostos: a Guideline~14 aborda a autocorrelação dos resíduos e a correção da incerteza (Anexo~B, \S B4.4).
~~~

- **Porquê:** O contraexemplo invalida a generalização. A Tabela 2.4 já indicava tratamento «Parcial». Deve rever-se também a conclusão seguinte sobre uma lacuna comum a todo o panorama normativo.
- **Como verificar:** [ASHRAE Guideline 14-2014, Anexo B, §B4.4](https://studylib.net/doc/28228372/746559958-ashrae-guideline-14-2014), reprodução do documento original.
- **Coerência com outras ocorrências:** Preservar a citação de Ruiz e Bandera e os exemplos de inconsistência entre índices; a conclusão universal é que excede a evidência.

### A-06 — O limite de exclusão de 25% está atribuído à via errada

- **Categoria:** erro factual
- **Gravidade:** alta
- **Linha:** 261
- **Texto atual:**

~~~latex
a via de simulação calibrada admite exclusões, mas limita-as a $25\,\%$ dos dados medidos e exige a documentação das razões
~~~

- **Proposta:**

~~~latex
a via de desempenho de edifício inteiro limita as exclusões a $25\,\%$ e exige a documentação das razões (\S4.3.2.2\,b)), distinguindo-se da via de simulação calibrada
~~~

- **Porquê:** A §4.3.2.2 b) contém esta regra; a §4.3.2.4 não a enuncia. Conserva-se o número e a citação existente, que passa a identificar a via com que se estabelece a distinção.
- **Como verificar:** [ASHRAE Guideline 14-2014, §4.3.2.2 b) e §4.3.2.4](https://studylib.net/doc/28228372/746559958-ashrae-guideline-14-2014).
- **Coerência com outras ocorrências:** Na linha 281 da Tabela 2.4, atribuir igualmente os 25% à via de desempenho de edifício inteiro.

### A-07 — A atualização anual avaliada não é uma troca automática observada em produção

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Linha:** 477
- **Texto atual:**

~~~latex
e a reestimação anual é a regra de
revisão.
~~~

- **Proposta:**

~~~latex
e estima-se uma reta por ano civil, mantendo-se a seleção do ano de referência. Avalia-se nesta dissertação o uso da reta de um ano no ano seguinte; o histórico das referências selecionadas pela operação não está documentado.
~~~

- **Porquê:** O Capítulo 4 distingue expressamente estimação anual, seleção manual da referência e cenário analisado. O Capítulo 2 volta a apresentar esse cenário como regra de revisão efetivamente utilizada. São afirmações diferentes sobre o objeto de estudo.
- **Como verificar:** [Capítulo 4, linhas 333–341](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:333). O próprio Capítulo 2, linhas 466–467, já menciona a seleção do ano.
- **Coerência com outras ocorrências:** Aplicar a mesma distinção a «recalibração anual por calendário» na linha 154 e a «recalibrada por calendário» na linha 299.

### A-08 — A deriva não está demonstrada apenas na ordenada na origem

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Linha:** 149
- **Texto atual:**

~~~latex
a recalibração anual, que a norma admite como método predeterminado, absorve na ordenada na origem a deriva estrutural que devia alarmar.
~~~

- **Proposta:**

~~~latex
a variação entre referências manifesta-se nos coeficientes das retas anuais, sem identificar por si só a sua causa física nem demonstrar a perda de um alarme real.
~~~

- **Porquê:** O Capítulo 6 mostra variações simultâneas do declive e da ordenada. Distingue ainda comparação dentro do domínio observado de interpretação física do intercepto. A perda de sensibilidade por recalibração é avaliada em simulação, conforme delimita o Capítulo 4.
- **Como verificar:** [Capítulo 6, linhas 315 e 350–368](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:350); [Capítulo 4, linhas 333–341](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:333).
- **Coerência com outras ocorrências:** Corrigir a mesma redução ao intercepto nas linhas 331–332. Não se altera nenhum coeficiente publicado.

### A-09 — Uma referência contrafactual não exige que o desempenho observado permaneça constante

- **Categoria:** confusão
- **Gravidade:** alta
- **Linha:** 106
- **Texto atual:**

~~~latex
São pressupostos de estacionariedade: não da série de consumo, mas da \emph{relação} entre consumo e variáveis relevantes.
~~~

- **Proposta:**

~~~latex
Pressupõe-se que o modelo continua a representar, nas condições de reporte, o consumo correspondente ao desempenho do período de referência. A relação observada pode mudar por melhoria ou degradação do desempenho; essa mudança é precisamente um dos efeitos que se pretende identificar.
~~~

- **Porquê:** O Anexo D apresenta a previsão como consumo que ocorreria sem as ações de melhoria. Exigir invariância da relação efetivamente observada eliminaria o próprio efeito procurado. Deve separar-se validade da comparação contrafactual, estabilidade preditiva e identificação da causa do desvio.
- **Como verificar:** ISO 50006:2014, Anexo D, §D.1, p. 24 (PDF 32), último parágrafo; [Capítulo 1, linhas 214–225](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:214). O Capítulo 1 contém a distinção correta, mas volta depois a aproximá-la da estacionariedade.
- **Coerência com outras ocorrências:** Na linha 202 e na definição compacta de transportabilidade da linha 252, explicitar o mesmo alcance. O problema não é a coluna ser reconstrução do autor; é o significado atribuído à hipótese. Não se propõe mexer na figura.

### A-10 — A descrição do Corpus B conserva uma conclusão que o Capítulo 3 já rejeita

- **Categoria:** contradição entre capítulos
- **Gravidade:** alta
- **Linha:** 406
- **Texto atual:**

~~~latex
mostra que a literatura sobre indicadores e
referências nomeia estas causas raramente: relata o efeito no modelo e
quase nunca o mecanismo no processo.
~~~

- **Proposta:**

~~~latex
distingue a identificação de mecanismos da demonstração dos seus efeitos e da avaliação das respostas propostas. Essa distinção permite situar os mecanismos físicos aqui descritos sem atribuir à literatura uma omissão geral que os resultados da revisão não sustentam.
~~~

- **Porquê:** O Capítulo 3 contabiliza mecanismos em grande parte do corpus e declara expressamente que «raramente» é errado para a ligação entre adaptações e mecanismos. As categorias dessa revisão não autorizam a generalização sobre ausência de mecanismos físicos específicos. Para defender essa leitura mais estreita seria necessária a codificação correspondente.
- **Como verificar:** [Capítulo 3, linhas 748–780 e 919–931](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:919); confrontar a síntese das lacunas a partir da linha 1061.
- **Coerência com outras ocorrências:** Preservar a remissão para a Secção do Corpus B. Não transferir para o Capítulo 2 contagens novas nem confundir menção a um mecanismo com demonstração causal.

### A-11 — Doze meses é uma duração típica, condicionada à variabilidade operacional

- **Categoria:** erro factual
- **Gravidade:** média
- **Linha:** 154
- **Texto atual:**

~~~latex
o período de \emph{baseline} de doze meses, a gestão da incerteza
~~~

- **Proposta:**

~~~latex
a escolha de um período de \emph{baseline} que capture a variabilidade operacional, tipicamente de doze meses quando se pretende abranger um ciclo sazonal, a gestão da incerteza
~~~

- **Porquê:** A síntese transforma uma orientação contextual numa duração geral. A mesma cláusula admite períodos mais curtos ou mais longos. A crítica à escolha do ano civil no caso estudado continua válida, mas deve incidir sobre essa escolha e a sua representatividade.
- **Como verificar:** ISO 50006:2014, §4.4.2 e Practical Help Box 6, p. 15 (PDF 23). Na linha 106 e na linha 233 da matriz, o próprio capítulo já usa «tipicamente».
- **Coerência com outras ocorrências:** Na linha 202, o pressuposto sobre o ciclo anual deve ficar condicionado à escolha dessa janela, não atribuído a qualquer aplicação da norma.

### A-12 — A matriz associa testes a dimensões, sem validar integralmente cada pressuposto

- **Categoria:** confusão
- **Gravidade:** média
- **Linha:** 214
- **Texto atual:**

~~~latex
É esta última coluna que dá ao Capítulo~\ref{cha:diagnostico} rastreabilidade completa norma\,$\to$\,resultado.
~~~

- **Proposta:**

~~~latex
É esta última coluna que liga a leitura das normas às dimensões examinadas no Capítulo~\ref{cha:diagnostico}. A correspondência delimita o alcance de cada resultado: a replicação verifica a reprodução da implementação, o teste de estabilidade incide sobre os declives anuais e a detetabilidade é avaliada em simulação.
~~~

- **Porquê:** E1 verifica igualdade numérica, não validade estatística. E3 testa igualdade de declives, não toda a relação condicional. A detetabilidade real não é estimada. A ressalva posterior é correta, mas «completa» sugere uma cobertura que o protocolo não reivindica.
- **Como verificar:** [Capítulo 4, linhas 434–442 e tabela nas linhas 479–495](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:434); ver também a ressalva já presente na linha 252 do Capítulo 2.
- **Coerência com outras ocorrências:** Conservar os identificadores E1–E6 e a matriz única; não acrescentar outra enumeração de cláusulas.

### A-13 — Seleção de variáveis: ausência de limiar fixo não é ausência de procedimento

- **Categoria:** confusão
- **Gravidade:** média
- **Linha:** 124
- **Texto atual:**

~~~latex
mas não fixa nenhum limiar de decisão, nenhum procedimento de teste e, sobretudo, nenhum teste de \emph{suficiência}:
~~~

- **Proposta:**

~~~latex
mas não fixa um limiar quantitativo geral nem um protocolo obrigatório para a seleção conjunta das variáveis e, sobretudo, para testar a \emph{suficiência} do conjunto:
~~~

- **Porquê:** O parágrafo começa por descrever procedimentos gráficos; mais adiante o capítulo reconhece testes e significância das variáveis. O ponto defensável é a falta de uma regra geral e obrigatória de suficiência, não a ausência de qualquer procedimento.
- **Como verificar:** ISO 50006:2014, §4.2.4 e Anexo D, §D.2; Capítulo 2, linhas 124 e 147. Para o alcance do teste de suficiência da dissertação, Capítulo 4, linha 489.

### A-14 — Meteorologia, ocupação e calendário não são, por si, mudanças da relação

- **Categoria:** confusão
- **Gravidade:** média
- **Linha:** 304
- **Texto atual:**

~~~latex
Num edifício, o que desloca a relação entre consumo e variável explicativa
é quase sempre exterior ao sistema e periódico: a temperatura exterior, a
ocupação, o calendário.
~~~

- **Proposta:**

~~~latex
Na modelação do consumo de edifícios, consideram-se variáveis como a temperatura exterior, a ocupação e o calendário. A variação destas grandezas deve distinguir-se de uma mudança na relação que as liga ao consumo.
~~~

- **Porquê:** A frase confunde deslocamento das variáveis com alteração dos parâmetros da relação e apresenta «quase sempre» sem uma comparação que o sustente. A especificidade dos processos contínuos pode ser demonstrada pelos mecanismos que se seguem, sem postular estabilidade geral nos edifícios.
- **Como verificar:** ISO 50006:2014, §4.3.1, p. 12 (PDF 20), e §4.6; [FEMP M&V Guidelines 4.0](https://www.energy.gov/documents/mvguide40pdf), Opção C, discussão sobre acompanhamento de mudanças nas condições da instalação.
- **Coerência com outras ocorrências:** A continuação «Num processo contínuo de refinação, a relação move-se também por dentro» mantém a passagem para os mecanismos físicos.

### A-15 — Um evento pode ser detetável sem que a sua causa seja identificável

- **Categoria:** confusão
- **Gravidade:** média
- **Linha:** 365
- **Texto atual:**

~~~latex
e nenhuma é visível para um modelo que não receba o registo do
evento.
~~~

- **Proposta:**

~~~latex
e não se identifica a sua causa apenas pela forma do resíduo, sem informação que permita distinguir o evento.
~~~

- **Porquê:** Um degrau no consumo ou no resíduo pode produzir um sinal sem que exista um registo de manutenção. O registo ajuda a explicar o sinal; não é condição necessária para que este exista. A formulação atual confunde deteção e atribuição causal.
- **Como verificar:** [Capítulo 4, linhas 603–616](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:603), enquadramento da simulação; Capítulo 2, linhas 362–367, onde já se reconhece a semelhança dos resíduos.

### A-16 — Estacionariedade não torna dispensável a validação

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Linha:** 299
- **Texto atual:**

~~~latex
Para um processo estacionário e bem comportado, o silêncio é inconsequente.
~~~

- **Proposta:**

~~~latex
A estacionariedade, por si só, não assegura a adequação das variáveis, da forma do modelo ou da escala atribuída aos desvios.
~~~

- **Porquê:** Mesmo sem mudança temporal, um modelo pode omitir variáveis, representar mal a relação ou atribuir cobertura errada às bandas. O capítulo enumera essas dimensões separadamente. «Bem comportado» não está definido e torna a alegada ausência de consequências circular.
- **Como verificar:** Capítulo 2, linha 252, distinção entre suficiência, forma, transportabilidade e calibração; Capítulo 4, tabela do protocolo a partir da linha 479. Trata-se de uma implicação lógica entre conceitos, não de um novo resultado empírico.

### A-17 — A revisão não compara a probabilidade de falha entre unidades

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Linha:** 372
- **Texto atual:**

~~~latex
São também,
pelas razões desta secção, o sítio onde uma referência estática mais
facilmente falha.
~~~

- **Proposta:**

~~~latex
Identificam-se nestas unidades, pelas razões desta secção, mecanismos que podem comprometer o uso de uma referência estática.
~~~

- **Porquê:** A importância energética da destilação está sustentada pela fonte citada; a comparação «mais facilmente» exige evidência entre tipos de unidade. O diagnóstico de uma unidade não estabelece essa ordenação. Mantém-se integralmente a frase anterior e a sua citação.
- **Como verificar:** Capítulo 2, linhas 369–378; âmbito do diagnóstico no Capítulo 6. Para conservar a comparação seria necessária uma análise comparativa de falhas entre unidades — NÃO VERIFICADO nas evidências apresentadas.

### A-18 — A edição usada no SGE não pode ser inferida da edição a que se teve acesso

- **Categoria:** dúvida
- **Gravidade:** média
- **Linha:** 294
- **Texto atual:**

~~~latex
as edições a que houve acesso e, presumivelmente, as que enquadram o método de \emph{baseline} em produção na instalação em estudo.
~~~

- **Proposta:**

~~~latex
as edições a que houve acesso. Não se confirmou qual a edição usada no enquadramento do método de \emph{baseline} em produção na instalação em estudo.
~~~

- **Porquê:** A disponibilidade de uma norma para a dissertação não demonstra a sua utilização na instalação. O próprio ficheiro regista esta confirmação como pendência. A substituição declara a limitação factual, sem atribuir uma edição ao SGE.
- **Como verificar:** Capítulo 2, comentário nas linhas 497–500. Edição efetivamente adotada: NÃO VERIFICADO; confirmar na documentação do SGE ou junto da orientação industrial.
- **Coerência com outras ocorrências:** A existência da edição de 2023 e o título da §8.2 são verificáveis no catálogo e no índice público; o conteúdo integral dessa cláusula não foi verificado.

### A-19 — A comparação demonstra uma diferença documental, não a intenção dos redatores

- **Categoria:** afirmação sem suporte
- **Gravidade:** média
- **Linha:** 265
- **Texto atual:**

~~~latex
A família ISO~50001 escolheu não o fazer. A Tabela~\ref{tab:comparacao-frameworks} sintetiza a comparação.
~~~

- **Proposta:**

~~~latex
Nas edições ISO analisadas não se fixam limiares quantitativos gerais de aceitação de modelos. A Tabela~\ref{tab:comparacao-frameworks} sintetiza a comparação.
~~~

- **Porquê:** Os documentos permitem comparar o que está ou não está prescrito. Não demonstram a deliberação histórica de adotar ou rejeitar uma alternativa. Além disso, a ISO contém orientação sobre tratamento de dados e reporte, que «não o fazer» também abrangia no contexto.
- **Como verificar:** ISO 50006:2014, §4.4.3 e Anexo D; ISO 50015:2014, §§4.2, 6.5 e 7. Intenção do comité: NÃO VERIFICADO; exigiria documentação dos trabalhos de normalização.
- **Coerência com outras ocorrências:** Conservar o argumento da possibilidade de critérios explícitos. Nas linhas 96 e 257, distinguir essa inferência de uma explicação documentalmente provada para as escolhas do comité.

### A-20 — A percentagem excluída deve ficar ligada à amostra

- **Categoria:** confusão
- **Gravidade:** baixa
- **Linha:** 462
- **Texto atual:**

~~~latex
na CDU, $18\,600$~t/d, que deixa de
fora 10,4\% dos dias.
~~~

- **Proposta:**

~~~latex
na CDU, $18\,600$~t/d, que deixa de
fora 10,4\% dos dias candidatos da amostra analisada.
~~~

- **Porquê:** Os 10,4% são uma proporção observada num conjunto de dados, não uma propriedade fixa do limiar. A explicitação do denominador evita que se leia o valor como taxa anual ou característica geral da unidade.
- **Como verificar:** [Capítulo 6, linhas 100 e 124–125](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:124): 251 dos 2 403 dias candidatos. Mantêm-se o limiar e a percentagem.

## Substituições complementares dos mesmos achados

Estas ocorrências repetem os problemas já contabilizados. As propostas seguintes evitam corrigir um parágrafo e conservar a afirmação incompatível noutra passagem. Não alteram a estrutura das tabelas nem constituem novos achados.

### Complemento 1 — A-01, linha 126

**Texto atual:**

~~~latex
e enunciado sem que lhe corresponda procedimento nenhum.
~~~

**Proposta:**

~~~latex
sem que se estabeleça um procedimento específico para separar essas duas causas do resíduo.
~~~

### Complemento 2 — A-02, linha 149

**Texto atual:**

~~~latex
O que nenhum dos gatilhos fornece é um \emph{mecanismo de deteção}: o primeiro é circular
~~~

**Proposta:**

~~~latex
A formulação dos gatilhos, por si só, não define um detetor estatisticamente calibrado: o primeiro exige uma avaliação adicional
~~~

### Complemento 3 — A-02, linha 188

**Texto atual:**

~~~latex
o seu silêncio quanto à \emph{validade}
desses instrumentos.
~~~

**Proposta:**

~~~latex
a menor especificação de critérios quantitativos de \emph{validação estatística}
desses instrumentos.
~~~

### Complemento 4 — A-02, linha 197

**Texto atual:**

~~~latex
as normas analisadas
não contêm o mecanismo que permitiria distinguir uma coisa da outra.
~~~

**Proposta:**

~~~latex
as verificações orientadoras previstas nas normas não substituem a avaliação do desempenho estatístico da implementação.
~~~

### Complemento 5 — A-02, linha 241

**Texto atual:**

~~~latex
Mecanismo de \emph{deteção} de invalidade; gatilho~a) circular & Mudanças invalidantes são conhecidas ou visíveis
~~~

**Proposta:**

~~~latex
Desempenho estatístico do mecanismo de deteção & Mudanças invalidantes são conhecidas ou visíveis
~~~

### Complemento 6 — A-03, linha 285

**Texto atual:**

~~~latex
\enquote{na medida do praticável} (50015 \S7) & Sim (Apêndice~B)
~~~

**Proposta:**

~~~latex
Reporte recomendado (50015 \S4.2, \S6.5); quantificação \enquote{na medida do praticável} (\S7) & Sim (Apêndice~B)
~~~

### Complemento 7 — A-04, linha 281

**Texto atual:**

~~~latex
Rever, sem critério (50006 \S4.2.6.4) & Justificação exigida
~~~

**Proposta:**

~~~latex
Investigar e justificar; evitar viés (50006 \S4.2.6.4) & Justificação exigida
~~~

### Complemento 8 — A-05, linha 292

**Texto atual:**

~~~latex
O \emph{gap} identificado no Capítulo~\ref{cha:revisao} é, portanto, comum a todo o panorama normativo, não exclusivo da família ISO;
~~~

**Proposta:**

~~~latex
O \emph{gap} identificado no Capítulo~\ref{cha:revisao} respeita à avaliação das referências no uso pretendido e não demonstra uma omissão uniforme dos protocolos;
~~~

### Complemento 9 — A-05, linha 292

**Texto atual:**

~~~latex
a família ISO é simplesmente o caso extremo, por não fixar sequer os índices.
~~~

**Proposta:**

~~~latex
na família ISO analisada, essa discussão incide sobretudo na ausência de critérios quantitativos gerais de aceitação.
~~~

### Complemento 10 — A-06, linha 281

**Texto atual:**

~~~latex
Proibidas na via prescritiva; $\leq 25\,\%$, documentadas, na simulação
~~~

**Proposta:**

~~~latex
Proibidas na via prescritiva; $\leq 25\,\%$, documentadas, na via de desempenho de edifício inteiro
~~~

### Complemento 11 — A-07, linha 154

**Texto atual:**

~~~latex
com $\sigma$ estimado a partir dos resíduos de treino; e a recalibração anual por calendário.
~~~

**Proposta:**

~~~latex
com $\sigma$ estimado a partir dos resíduos de treino; e a estimação de uma reta por ano civil, com seleção do ano de referência.
~~~

### Complemento 12 — A-07, linha 299

**Texto atual:**

~~~latex
uma regressão univariada estática, com bandas de $\pm 2\sigma$, recalibrada por calendário
~~~

**Proposta:**

~~~latex
uma regressão univariada estática, com bandas de $\pm 2\sigma$ e referências estimadas por ano civil, selecionáveis pela operação
~~~

### Complemento 13 — A-08, linha 332

**Texto atual:**

~~~latex
modelo reajustado todos os anos absorve-a na ordenada na origem.
~~~

**Proposta:**

~~~latex
modelo reajustado todos os anos pode incorporá-la nos coeficientes da nova referência, alterando a comparação com o desempenho anterior.
~~~

### Complemento 14 — A-09, linha 106

**Texto atual:**

~~~latex
Não são enunciados como pressupostos em parte alguma do texto normativo.
~~~

**Proposta:**

~~~latex
A formulação destes pressupostos é uma interpretação desta dissertação sobre as condições necessárias à comparação.
~~~

### Complemento 15 — A-09, linha 202

**Texto atual:**

~~~latex
não ressalva que a relação estimada à esquerda possa ter deixado de valer à direita.
~~~

**Proposta:**

~~~latex
explicita também que a previsão representa o consumo que ocorreria sem as ações de melhoria. A validade desta comparação continua a depender das variáveis, do domínio de aplicação e das condições de medição.
~~~

### Complemento 16 — A-09, linha 252

**Texto atual:**

~~~latex
\textbf{transportabilidade} (a relação não muda entre treino e aplicação), \textbf{calibração}
~~~

**Proposta:**

~~~latex
\textbf{transportabilidade} (o modelo continua a permitir a comparação pretendida nas condições de reporte), \textbf{calibração}
~~~

### Complemento 17 — A-11, linha 202

**Texto atual:**

~~~latex
o período de referência de doze meses pressupõe que um ciclo anual é representativo;
~~~

**Proposta:**

~~~latex
quando se escolhe um período de referência de doze meses, pressupõe-se que esse ciclo anual é representativo;
~~~

### Complemento 18 — A-19, linha 96

**Texto atual:**

~~~latex
é uma escolha de desenho normativo, não uma impossibilidade técnica.
~~~

**Proposta:**

~~~latex
não resulta de uma impossibilidade técnica de formular critérios explícitos.
~~~

## O que decidi não mudar

- **EnPI/EnB e o parágrafo «Nomenclatura e citações».** Respeitam-se as decisões sobre terminologia, traduções e transcrições; não há benefício em reabri-las.
- **A distinção entre requisitos da ISO 50001 e orientação das ISO 50006/50015.** É necessária e está sustentada. Recomendações de validação não se tornam requisitos certificáveis por serem mais detalhadas do que o capítulo reconhecia.
- **Os sete princípios da ISO 50015 na linha 96.** A enumeração atual corresponde à §4.1, incluindo gestão de dados e planeamento da medição e confidencialidade.
- **As definições de EnPI e EnB na linha 104 e os gatilhos de revisão da linha 149.** Correspondem às cláusulas identificadas. Os problemas aparecem na interpretação posterior, não nesses enunciados.
- **«Mesmo quando válidas, nenhuma delas diz se a referência prevê o período seguinte…», linha 147.** O ajuste e a inferência no treino não demonstram desempenho futuro, cobertura das bandas ou capacidade de deteção. A afirmação forte é defensável.
- **A observação de que o resíduo não distingue, por si, erro de modelação e alteração do desempenho.** A Tabela 2 da ISO 50006 reconhece esta dificuldade; importa preservá-la, delimitando a alegação de ausência de procedimento.
- **A delimitação de que não se faz uma auditoria de conformidade, linhas 156–165.** Evita confundir diagnóstico estatístico da implementação com avaliação do SGE.
- **A matriz única e a declaração de que os pressupostos são reconstrução da dissertação.** Estão explícitas. Corrigem-se conteúdos de células; não se propõe outra matriz, nem se apresenta a reconstrução como texto da norma.
- **Os limiares de calibração e de incerteza citados para a ASHRAE, os doze meses, os nove pontos e a proibição de exclusões da via prescritiva.** Confirmados nas cláusulas indicadas; A-06 corrige a atribuição dos 25%, preservando o valor. [Documento consultado](https://studylib.net/doc/28228372/746559958-ashrae-guideline-14-2014).
- **A correspondência numérica dos limiares de calibração do FEMP com os citados para a ASHRAE e a exigência de demonstrar validade na Opção C.** Confirmam-se na Tabela 4-2 e na §4.4.3 do [FEMP 4.0](https://www.energy.gov/documents/mvguide40pdf). Isto não justifica transportar esses limiares para a refinaria, e o capítulo já o diz.
- **O estatuto secundário de \(R^2 \geq 0{,}75\) no IPMVP.** A limitação está declarada; não se elimina o número nem se promove a recomendação a requisito atual confirmado.
- **A capacidade pública de Sines e o encerramento da refinação em Matosinhos.** A informação é confirmada pela [Galp](https://www.galp.com/corp/en/about-us/what-we-do/industrial-and-midstream); não se propõe suavizar os valores publicados.
- **O limiar de carga, as bandas e as oito regras.** Correspondem à descrição do Capítulo 4. No enquadramento, a repetição do núcleo do método é necessária para o primeiro contacto do leitor.
- **A ressalva de que a detetabilidade real ficou por estimar, linha 252.** Deve manter-se; A-12 antecipa o seu efeito na leitura da matriz.
- **A descrição física da incrustação e a distinção entre desativação de catalisador e a unidade estudada.** Não se propõe acrescentar detalhe industrial. A leitura integral das fontes de processo não foi refeita nesta análise; manter não equivale a certificar todas as generalizações, como se explicita nas dúvidas.
- **As figuras, tabelas, rótulos e ordem das secções.** A sequência pode funcionar sem reorganização. A correção da premissa normativa vem antes de qualquer redesenho.
- **Travessões, termos técnicos ingleses e variação do comprimento das frases.** A aplicação de humanizer/narrativa não justifica uma normalização mecânica do estilo. Os problemas identificados são de conteúdo, alcance e progressão do argumento.

## Três decisões editoriais

### Nota sobre edições na Secção 2.3.3 e «Nomenclatura e citações» na Secção 2.1

**Não se recomenda uma fusão integral.** A Secção 2.1 fixa a convenção de leitura: documentos usados, terminologia e política de citação. A nota da Secção 2.3.3 delimita até onde a comparação permite concluir, sobretudo perante a edição de 2023. Esta limitação é relevante precisamente depois da comparação.

A repetição tem, portanto, uma função. Deve evitar-se voltar a explicar a política de tradução ou a nomenclatura na nota. A intervenção necessária agora é A-18: retirar a inferência sobre a edição usada na instalação. Não se propõe apagar anos, cláusulas, citações ou a referência às limitações para obter um ganho pequeno de extensão.

O [catálogo da ISO](https://www.iso.org/standard/79367.html) confirma a edição de 2023 e o [índice público do documento](https://cdn.standards.iteh.ai/samples/79367/41dbccb95579448bb8d4fe8288e02e67/ISO-50006-2023.pdf) identifica a §8.2 dedicada à incerteza do modelo. **NÃO VERIFICADO:** o conteúdo integral e o seu efeito sobre cada afirmação da análise. A consulta de um índice não resolve essa limitação.

### Método em produção: qual dos capítulos deve encolher?

**A redução deve incidir no comentário repetido do Capítulo 2, conservando a primeira descrição do método e o detalhe reprodutível do Capítulo 4.**

No Capítulo 2, o leitor precisa de saber que se ajusta uma reta à carga, que existe um limiar, que as bandas dependem dos resíduos e que o ano de referência é selecionável. O limiar, a percentagem excluída, as bandas e a menção às oito regras fazem esse trabalho. Não se recomenda suprimi-los. No Capítulo 4, justificam-se o domínio de estimação, as definições dos resíduos, os acumulados, a lista das regras e a distinção entre soma acumulada e detetor calibrado.

A repetição menos produtiva está no parágrafo final das linhas 473–480: volta a enumerar o que a secção acabou de explicar. Se se quiser encurtá-lo, esta é uma **alternativa editorial à aplicação de A-07 nesse parágrafo**, não uma substituição cumulativa. Conserva as três referências existentes e a informação necessária sobre o alcance da comparação:

~~~latex
Os pressupostos da Secção~\ref{sec:assimetria-matriz} confrontam-se aqui com
os mecanismos da Secção~\ref{sec:processos-continuos}. Examina-se o método
replicado de forma exata a partir das tabelas de configuração oficiais
(Secção~\ref{sec:replicacao}), antes de qualquer crítica. A comparação de
cada ano com a reta do anterior é o uso avaliado nesta dissertação; o
histórico das referências selecionadas pela operação não está documentado.
~~~

Mantêm-se as correções A-07 nas outras ocorrências sobre revisão por calendário. Não se recomenda encurtar o Capítulo 4 à custa da capacidade de reproduzir o método.

### Tabela 2.4: vale a pena mexer no formato?

**Não se recomenda alterar agora as larguras só para melhorar a hifenização.** Inspecionou-se a tabela no [PDF existente](/Users/bernardoribeiro/Desktop/Tese/novathesis/template.pdf), página impressa 22, página 49 do ficheiro. O texto é legível, não se veem cortes ou sobreposições, e os valores continuam identificáveis. Há, porém, espaçamento irregular e quebras de palavras que tornam a leitura lenta.

As correções de conteúdo das células têm prioridade. Depois delas, justifica-se uma única verificação visual. Só se essa versão perder legibilidade deve ponderar-se uma intervenção tipográfica local. Não se recomenda diminuir mais o corpo do texto nem alterar larguras e paginação em conjunto. A onze dias da entrega, o ganho cosmético atual é menor do que o risco de criar trabalho de composição. Nesta análise não se alterou nem recompilou a tabela.

## Sugestões de acrescentos

São propostas opcionais, limitadas ao conteúdo já documentado. Não se criaram figuras nem se atribuiu numeração nova. Convém aplicar primeiro os achados; acrescentar todos os blocos abaixo produziria nova repetição.

### Um parágrafo que formule a contribuição depois das correções

**Local sugerido:** no final da formulação da assimetria, articulado com A-02; evitar acumular com as frases que já fazem a mesma conclusão.

Este bloco permite conservar uma crítica incisiva sem depender de omissões inexistentes:

~~~latex
Reconhece-se nas normas orientação para selecionar indicadores, verificar
a adequação das referências, tratar dados e comunicar a incerteza.
Permanece por determinar, para a implementação estudada, se a referência
tem desempenho preditivo fora do treino, se a escala dos desvios permite
interpretar as bandas e se o procedimento de monitorização distingue
alterações relevantes da variabilidade do processo. É neste nível que se
situa o diagnóstico: avaliam-se as propriedades do instrumento utilizado
e o alcance das conclusões que dele se retiram.
~~~

**Base:** ISO 50006:2014, §§4.2.6.4, 4.4.3 e 4.6; ISO 50015:2014, §§4.2, 6.5 e 7; protocolo do Capítulo 4. Não se propõe acrescentar uma nova lista normativa ao corpo do capítulo.

### Uma distinção curta entre prever, comparar e explicar

**Local sugerido:** depois da definição do par EnPI–EnB, como desenvolvimento de A-09. Não se devem usar simultaneamente duas explicações extensas do mesmo ponto.

~~~latex
Distinguem-se três usos da referência. Para prever consumo, interessa
aproximar o valor observado nas condições de aplicação. Para comparar
desempenho, estima-se o consumo que corresponderia ao desempenho do período
de referência, nas condições de reporte. Para explicar um desvio, é
necessária informação que permita separar mudanças de desempenho,
condições não representadas e alterações de medição. Um bom resultado no
primeiro uso não demonstra, por si só, a adequação aos restantes.
~~~

**Base:** sentido contrafactual do Anexo D da ISO 50006 e delimitação já presente nos Capítulos 1 e 4. É a adição com maior utilidade conceptual: resolve a ambiguidade que atravessa estacionariedade, normalização e atribuição causal.

### Um esquema opcional sobre deteção e explicação

**Prioridade baixa.** O capítulo já tem uma cadeia normativa e um esquema da fronteira energética. Não se recomenda acrescentar outra figura normativa nem um segundo esquema industrial. Se a distinção de A-15 continuar pouco clara, pode usar-se um pequeno esquema textual, sem numeração, sem dados e sem alterar qualquer ambiente TikZ:

~~~latex
\begin{quote}
\textbf{Consumo observado e consumo de referência}
\(\longrightarrow\) desvio.\\
\textbf{Desvio e regra de monitorização}
\(\longrightarrow\) avaliação da presença de um sinal.\\
\textbf{Sinal, condições de medição e informação de contexto}
\(\longrightarrow\) investigação da causa.
\end{quote}
~~~

As setas representam etapas de análise, não garantias de deteção ou identificação. Não se acrescentam curvas sintéticas, amplitudes, coeficientes ou novos exemplos da unidade. O parágrafo anterior pode tornar este esquema dispensável.

## Dúvidas para o autor

Estas perguntas não impedem as correções documentais confirmadas acima.

1. **Qual a edição da ISO 50006 efetivamente usada para enquadrar o método na instalação?** NÃO VERIFICADO. Confirmar na documentação do SGE ou com a orientação industrial; não se infere da data do método.
2. **Existe uma fonte primária do IPMVP que sustente, na mesma edição, todas as células da sua coluna?** NÃO VERIFICADO. A ressalva atual cobre a ausência de consulta da edição corrente, mas falta verificar especificamente «Justificação exigida», «Parcial» e «Sim (Apêndice B)» contra o documento ou contra as passagens efetivas de Ruiz e Bandera. Não se deve tratar a verificação de um limiar como verificação de toda a coluna.
3. **A generalização sobre desativação catalítica pretende abranger que processos?** NÃO VERIFICADO na fonte integral nesta análise. Confirmar em Bartholomew (2001), já citado, se a sequência «subir a temperatura → mais energia fornecida por tonelada → dente de serra» é sustentada com esse alcance. Não se pede nem se propõe acrescentar detalhe das unidades da refinaria.
4. **Existe uma classificação da revisão que conte especificamente as causas físicas referidas na Secção 2.4?** Se existir, pode sustentar uma afirmação mais estreita do que a atual. Sem essa evidência, aplica-se A-10. O total de mecanismos do Corpus B não permite, sozinho, contar incrustação, matéria-prima ou intervenções.
5. **A caixa C2-08 já foi resolvida com a orientação industrial?** O estado dessa validação é NÃO VERIFICADO. A caixa permanece no ficheiro; esta análise não a remove, não presume a resposta e não acrescenta detalhe industrial.

## Fontes e limites da verificação

Consultaram-se as passagens normativas relevantes nos PDFs locais:

- [NP EN ISO 50001:2019 — ficheiro identificado como ISO50001_2018.pdf](</Users/bernardoribeiro/Desktop/Tese/bibliografia/seed/Referências/SEED/ISO50001_2018.pdf>).
- [ISO 50006:2014](</Users/bernardoribeiro/Desktop/Tese/bibliografia/seed/Referências/SEED/ISO50006_2014.pdf>).
- [ISO 50015:2014](</Users/bernardoribeiro/Desktop/Tese/bibliografia/seed/Referências/SEED/ISO50015_2014.pdf>).

As páginas indicadas nos achados distinguem a numeração impressa da posição no PDF. A verificação dos capítulos de contexto incidiu nas definições, no protocolo e nas conclusões relevantes para os achados; não corresponde a uma revisão integral desses capítulos.

Para a ASHRAE, consultou-se uma reprodução textual do documento original disponibilizada por terceiro, identificada nos achados; para o FEMP, o PDF oficial. Não se consultou integralmente a ISO 50006:2023, a edição corrente do IPMVP nem toda a bibliografia dos mecanismos físicos. As limitações correspondentes estão declaradas; não se inventaram substitutos bibliográficos.

A leitura editorial segue humanizer e narrativa na precisão das afirmações, na informação dada ao leitor e na utilidade das recorrências. Não se atribui origem automática ao texto nem se impõe uma reescrita de estilo. Mantiveram-se a ordem das secções, a nomenclatura, as referências e as figuras existentes.

## Verificação do próprio relatório

Verificaram-se a ocorrência única e contínua dos excertos, o intervalo de 8–30 palavras, os números de linha, a preservação dos comandos de citação e referência nos excertos substituídos e o equilíbrio das chavetas numa aplicação apenas em memória. Não se executou compilação nem se alterou qualquer ficheiro LaTeX.
