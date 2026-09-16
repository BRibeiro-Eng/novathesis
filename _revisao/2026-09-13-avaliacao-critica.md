**Avaliação crítica da dissertação — 13 de setembro de 2026**

A tese tem uma contribuição identificável: integrar fontes industriais, verificar a implementação existente e avaliar as baselines por várias propriedades, distinguindo previsão de monitorização. A proveniência dos resultados, a comparação com referências simples e o relato de sensibilidades são partes que vale a pena conservar. **A versão atual ainda não sustenta todas as conclusões que apresenta.** O principal problema é a distância entre a força da narrativa e a evidência disponível, agravada por capítulos e apêndices ainda vazios.

Foram inseridos **104 comentários em 20 ficheiros LaTeX**, dos quais **21 especificam figuras, esquemas, gráficos ou tabelas**, nos locais de utilização. Não são 21 figuras obrigatórias: algumas consolidam sugestões já existentes, outras são complementares ou pertencem aos apêndices. Os blocos são identificados por `% [REV-2026-09-13]`. Na atualização desta revisão, foram convertidos em caixas visíveis no PDF através de `\revisaotese`. O interruptor está em `0-Config/revisao.tex`: `\mostrarrevisaotrue` mostra as notas e `\mostrarrevisaofalse` oculta-as. As três notas das listas preliminares aparecem num apêndice de revisão, porque os ficheiros de definições são carregados no preâmbulo.

Prioridades: **P1** — corrigir uma afirmação ou decisão que afeta a validade da interpretação (27); **P2** — desenvolver conteúdo, estrutura, evidência ou apresentação visual (69); **P3** — aperfeiçoamento editorial ou complemento visual (8). Os identificadores mantêm-se úteis mesmo quando a numeração de capítulos mudar.

**O que resolver primeiro**

1. **Definir o objeto que se está a aceitar.** Uma baseline usada para prever, uma referência que preserva desvios e um detetor não se validam pelo mesmo critério. A demonstração rejeita cobertura baixa no ano seguinte, mas a referência congelada valoriza essa queda como sinal de mudança. Sem eventos externos, não se separa completamente mudança real de erro do modelo. A regra de aceitação tem ainda dois problemas: incluir a nominal num IC largo não demonstra calibração; a construção AR altera o centro, enquanto o ganho preditivo é adjudicado com a reta original. Preservar os resultados do protocolo original, qualificá-los e propor a revisão como desenvolvimento posterior, sem escolher novas margens para obter candidatos aceites. [C7-18](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:389), [C7-06](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:318), [C7-07](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:331), [C7-09](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:525).

2. **Corrigir implicações estatísticas incorretas.** R² não exige normalidade para ser calculado. Autocorrelação não implica, sozinha, perda de cobertura marginal. Não-rejeição não prova ausência de relação, equivalência ou adequação. Cobertura e taxa de dias fora da banda são complementares na mesma população. Estas correções mudam a leitura de vários resultados e devem entrar onde aparecem, não apenas nas limitações. [C2-03](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:130), [C6-05](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:178), [C6-06](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:202), [C7-13](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:972).

3. **Delimitar a crítica normativa.** O texto reconhece que a ISO exige adequação dos indicadores, mas depois afirma que a conformidade certifica apenas existência. Ausência de limiares universais não demonstra conformidade de uma implementação inválida. Além disso, uma análise centrada em 2014 não sustenta sem comparação o que se afirma sobre o quadro atual. O catálogo oficial identifica a ISO 50006:2023 como segunda edição publicada e a de 2014 como retirada; não foi feita nesta revisão uma auditoria das cláusulas do texto integral. [C2-02](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:26), [C2-04](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:150). [Catálogo ISO](https://www.iso.org/standard/79367.html).

4. **Fechar as provas de validação e a cronologia.** O resultado 400/400 aparece como observado, mas um comentário anterior diz que era esperado. As três fontes podem partilhar balanços e medidores: consistência de processamento não é exatidão física. Explicitar também o que já se conhecia dos dados em cada versão do protocolo e qual era a política real de referência em janeiro. [C5-03](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:184), [C5-02](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:96), [C4-04](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:206), [C1-06](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:324), [C4-07](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:292).

5. **Dar mais peso ao processo e às fronteiras energéticas.** A CDU e os mecanismos físicos estão por desenvolver, enquanto a discussão estatística ocupa grande parte do documento. Explicar utilidades, consumo/produção, reprocessamento, variáveis operacionais e conversões GNE antes de interpretar coeficientes. Identificar a parcela observada, a alocada, a propagada e a selecionada. A interseção de 876 dias e os diferentes denominadores precisam de uma leitura explícita. [C2-01](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:12), [F03](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:292), [C4-02](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:48), [C4-05](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:234), [C4-06](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:257), [C7-10](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:656).

6. **Completar a literatura e os elementos que sustentam o texto.** Capítulo 3, conclusões, resumos, caso físico e apêndices não podem continuar apenas como promessas enquanto a Introdução afirma entregas completas. A revisão tem de mostrar que trabalhos próximos existem e qual lacuna delimitada permanece; não assumir inexistência universal de metodologia. PRISMA-ScR orienta o relato, não certifica a revisão nem substitui o protocolo. [C1-01](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:28), [C1-04](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:211), [C3-04](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:90), [C8-01](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:14), [AP-D](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-D-tabelas.tex:11), [AP-G](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-G-matematica.tex:13). [PRISMA-ScR](https://www.prisma-statement.org/scoping).

Há também contradições verificáveis no próprio texto: as classes de ficheiros enumeradas somam 3 809, não 3 862; as contagens de excursões no vapor de 10 bar divergem entre parágrafos; a sensibilidade do gate é descrita como 3/16 e depois 3/32. Os comentários pedem confronto com os artefactos de origem, sem inventar a correção. [C4-03](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:122), [C6-09](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:420), [C7-17](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:1014).

**Estrutura recomendada**

| Parte | Alteração proposta |
|---|---|
| Introdução | Encurtar repetições; distinguir perguntas empíricas das SQ da revisão; apresentar contribuições efetivamente demonstradas. |
| Enquadramento | Dar entrada ao processo e à fronteira energética; explicar conceitos; consolidar crítica normativa numa matriz. |
| Revisão | Protocolo e formação dos corpora; mapa de métodos/validação; síntese crítica que justifica decisões do estudo. |
| Métodos | Reunir desenho temporal, estimandos, candidatos, critérios e simulador; deslocar inventário e histórico técnico para apêndices. |
| Plataforma | Evidência de entrega, reconciliação quantificada, duas capturas anotadas e limitações de âmbito. |
| Diagnóstico | Organizar por perguntas, com efeitos/IC e qualificações próximas; preservar incerteza e sensibilidade na síntese. |
| Discussão/proposta | Reduzir repetição, confrontar com literatura, mostrar demonstração essencial e separar previsão, referência e deteção. |
| Conclusões/futuro | Responder às perguntas; ordenar trabalho futuro por falha/dados/critério, sem uma escada automática de complexidade. |

Não recomendo aumentar já o número de capítulos. Primeiro deslocaria os métodos do Cap. 7 para o Cap. 4 e o detalhe de implementação para apêndices. Um capítulo autónomo para a simulação só se esta ficar como contribuição central depois de fechada a evidência.

**Plano visual**

Começar pelas figuras do processo, da amostra e dos resultados centrais. Usar desenhos vetoriais próprios para arquitetura e processo, gráficos gerados dos lotes identificados para resultados, e capturas reais para a plataforma. Uma imagem decorativa da refinaria acrescenta menos que uma fronteira energética legível. Cores consistentes por vetor; distinguir dados observados, esquemas conceptuais e simulação em todas as legendas.

As sugestões especificam posição, conteúdo, unidades/denominadores e cautelas diretamente no LaTeX. Não foram geradas novas figuras nesta revisão. Confirmei a existência dos SVG de efeito do limiar, forest plot E2, previsões de referência E3 e matriz SENS nos diretórios das corridas referidas; isso não substitui conferir a sua concordância científica com a versão final da prosa.

| ID | Local exato e proposta | Utilização |
|---|---|---|
| F01 | [Priorizar o esquema das duas camadas](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:111) | Complemento / consolidar com outra figura |
| F02 | [Quadro físico de mecanismos e variáveis observáveis](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:274) | Complemento / consolidar com outra figura |
| F03 | [Diagrama de processo e fronteira energética da CDU](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:292) | Prioridade no corpo |
| F04 | [Fluxo PRISMA com a formação dos dois corpora](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:47) | Prioridade no corpo |
| F05 | [Mapa de evidência que sustenta a lacuna](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:73) | Complemento / consolidar com outra figura |
| F06 | [Arquitetura de dados com granularidade e proveniência](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:151) | Prioridade no corpo |
| F07 | [Linha temporal dos três desenhos de avaliação](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:499) | Prioridade no corpo |
| F08 | [Prova visual da reconciliação antes e depois](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:120) | Prioridade no corpo |
| F09 | [Dois screenshots anotados no corpo, quatro páginas no manual](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:245) | Complemento / consolidar com outra figura |
| F10 | [Amostra e filtros precisam de um fluxo e de um calendário](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:96) | Prioridade no corpo |
| F11 | [Distribuição operacional e relação energia-carga](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:107) | Prioridade no corpo |
| F12 | [Forest plot do ganho preditivo com a sensibilidade visível](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:214) | Prioridade no corpo |
| F13 | [Predições a carga comum em vez de quatro figuras repetidas](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:305) | Prioridade no corpo |
| F14 | [Cobertura, excursões e persistência numa leitura única](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:396) | Prioridade no corpo |
| F15 | [Acoplamento de vapor com hipótese física explícita](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:703) | Complemento / consolidar com outra figura |
| F16 | [Sensibilidade dos efeitos, não apenas dos rótulos](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:854) | Complemento / consolidar com outra figura |
| F17 | [Esquema central: referência, estado e monitor](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:129) | Prioridade no corpo |
| F18 | [Matriz de decisão por candidato e por par anual](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:537) | Complemento / consolidar com outra figura |
| F19 | [Visualizar quanto sinal cada componente preserva](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:701) | Prioridade no corpo |
| F20 | [Curvas de deteção e atraso sob o mesmo falso sinal](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:849) | Prioridade no corpo |
| F21 | [Protótipo da ficha e diagrama de estados](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:936) | Complemento / consolidar com outra figura |

**Âmbito e verificação desta revisão**

A leitura incidiu nos oito capítulos ativos definidos em `0-Config/4_files.tex`, nos dois resumos, nos sete apêndices ativos e nos ficheiros de glossário/siglas/símbolos. Foram examinadas as referências relevantes para os problemas identificados e consultadas fontes públicas primárias para pontos metodológicos/normativos selecionados; não foi feita validação integral de todas as entradas bibliográficas ou das citações de normas pagas. A distinção entre não-rejeição e equivalência está também explicada no artigo já citado na tese. [Lakens, 2017](https://doi.org/10.1177/1948550617697177).

Não foram reexecutadas as análises estatísticas, auditado integralmente o código Power BI/Python ou validadas as medições industriais. Os achados distinguem erros lógicos demonstráveis no texto, contradições internas, informação ainda necessária e sugestões de investigação. As sugestões que dependem de dados novos não são apresentadas como resultados já obtidos.

Na primeira versão foram inseridos apenas comentários `%`, com recuperação byte a byte dos originais verificada. Na atualização para o PDF, as notas passaram a chamadas `\revisaotese`, colocadas em limites de parágrafo para não interromper frases. O corpo anterior da tese mantém-se recuperável removendo os blocos de revisão. As listas preliminares conservam as notas nos ficheiros de definição e mostram-nas num apêndice próprio em modo de revisão. O PDF foi recompilado; os registos da compilação e da verificação ficam em `_revisao/2026-09-13-pdf/`.

**Índice completo dos comentários**

Os links apontam para as linhas nesta revisão; se o texto for editado entretanto, procurar o identificador do comentário.

| ID | Prioridade | Tipo | Comentário no LaTeX |
|---|---|---|---|
| EN-01 | P3 | RESUMO | [Alinhar a versão inglesa com os estimandos finais](/Users/bernardoribeiro/Desktop/Tese/novathesis/1-FrontMatter/abstract-en.tex:7) |
| PT-01 | P2 | RESUMO | [Resumo quantitativo apenas depois de fechar o argumento](/Users/bernardoribeiro/Desktop/Tese/novathesis/1-FrontMatter/abstract-pt.tex:11) |
| FR-01 | P3 | APRESENTACAO | [Substituir as siglas de exemplo pelas usadas na tese](/Users/bernardoribeiro/Desktop/Tese/novathesis/1-FrontMatter/acronyms.tex:12) |
| FR-03 | P3 | APRESENTACAO | [Remover conteúdo demonstrativo e fixar termos operacionais](/Users/bernardoribeiro/Desktop/Tese/novathesis/1-FrontMatter/glossary.tex:11) |
| FR-02 | P3 | NOTACAO | [Definir a notação física e estatística com unidades](/Users/bernardoribeiro/Desktop/Tese/novathesis/1-FrontMatter/symbols.tex:10) |
| C1-01 | P2 | ESTRUTURA | [Estado da dissertação e ordem de revisão](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:28) |
| C1-02 | P2 | CONTEUDO | [Abertura e definição de fiabilidade](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:44) |
| F01 | P2 | FIGURA | [Priorizar o esquema das duas camadas](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:111) |
| C1-03 | P2 | ARGUMENTO | [Não tornar a não-estacionariedade uma impossibilidade universal](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:163) |
| C1-04 | P1 | ARGUMENTO | [Delimitar a lacuna que a revisão ainda tem de demonstrar](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:211) |
| C1-05 | P2 | ESTRUTURA | [Alinhar perguntas da tese com perguntas da revisão](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:264) |
| C1-06 | P1 | TRANSPARENCIA | [Especificado antes da execução não significa dados nunca vistos](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:324) |
| C1-07 | P2 | ESTRUTURA | [Contribuições demonstradas e extensão a outros processos](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:350) |
| C1-08 | P3 | REDACAO | [Reduzir repetição entre abertura, contribuições e roteiro](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-1-introducao.tex:465) |
| C2-01 | P2 | ESTRUTURA | [Dar base de engenharia ao argumento estatístico](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:12) |
| C2-02 | P1 | NORMAS | [Edição histórica versus enquadramento atual](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:26) |
| C2-03 | P1 | ESTATISTICA | [R² não é um teste com pressuposto de normalidade](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:130) |
| C2-04 | P1 | NORMAS | [Adequação normativa não se reduz à existência do instrumento](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:150) |
| C2-05 | P2 | ESTRUTURA | [Fundir passagens repetidas e separar texto normativo de interpretação](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:173) |
| C2-06 | P2 | FONTES | [Comparar vias e edições sem extrapolar os limiares](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:222) |
| F02 | P2 | FIGURA | [Quadro físico de mecanismos e variáveis observáveis](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:274) |
| F03 | P2 | FIGURA | [Diagrama de processo e fronteira energética da CDU](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:292) |
| C2-07 | P2 | CONTEUDO | [Contextualizar seleção da unidade e energia equivalente](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-2-enquadramento.tex:305) |
| C3-01 | P2 | CONTEUDO | [Fechar a revisão com estado verificável](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:14) |
| C3-02 | P2 | METODO | [Tornar a revisão reprodutível e limitar o viés do corpus ISO](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:30) |
| F04 | P2 | FIGURA | [Fluxo PRISMA com a formação dos dois corpora](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:47) |
| C3-03 | P2 | ANALISE | [Contagem bibliométrica não demonstra adequação metodológica](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:57) |
| F05 | P2 | FIGURA | [Mapa de evidência que sustenta a lacuna](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:73) |
| C3-04 | P2 | ARGUMENTO | [Fecho da revisão tem de ligar evidência e decisões do estudo](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-3-revisao.tex:90) |
| C4-01 | P2 | ESTRUTURA | [Separar método reproduzível da história do desenvolvimento](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:17) |
| C4-02 | P1 | DADOS | [Agregação diária e conversão energética precisam de equações](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:48) |
| C4-03 | P2 | CONSISTENCIA | [O inventário não fecha aritmeticamente](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:122) |
| F06 | P2 | FIGURA | [Arquitetura de dados com granularidade e proveniência](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:151) |
| C4-04 | P1 | METROLOGIA | [Consistência documental, reconciliação e exatidão física](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:206) |
| C4-05 | P1 | DADOS | [Imputação, zeros e seleção na variável resposta](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:234) |
| C4-06 | P2 | ENERGIA | [Escrever o balanço de conversão e justificar constantes](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:257) |
| C4-07 | P1 | CRONOLOGIA | [Precisar o que acontece efetivamente em janeiro](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:292) |
| C4-08 | P2 | INDICADORES | [Excesso positivo não estima desperdício ou poupança](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:321) |
| C4-09 | P2 | INDICADORES | [Delimitar o EII e as emissões derivados da plataforma](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:352) |
| C4-10 | P2 | INFERENCIA | [Definir população, alvo inferencial e limites de HAC/MBB](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:431) |
| C4-11 | P1 | VALIDACAO | [O alvo nominal de 95% não foi validado pelo teste a 90%](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:442) |
| F07 | P2 | FIGURA | [Linha temporal dos três desenhos de avaliação](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:499) |
| C4-12 | P2 | REPRODUTIBILIDADE | [Integridade não certifica correção científica](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-4-metodos.tex:538) |
| C5-01 | P2 | ESTRUTURA | [Separar resultado entregue de características da implementação](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:30) |
| C5-02 | P1 | VALIDACAO | [As três leituras podem partilhar o mesmo erro](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:96) |
| F08 | P2 | FIGURA | [Prova visual da reconciliação antes e depois](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:120) |
| C5-03 | P1 | EVIDENCIA | [400/400 aparece como facto e como resultado por confirmar](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:184) |
| C5-04 | P2 | DADOS | [A definição de carga interfere diretamente no diagnóstico](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:207) |
| F09 | P2 | FIGURA | [Dois screenshots anotados no corpo, quatro páginas no manual](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:245) |
| C5-05 | P2 | INTERPRETACAO | [A ordenação do dashboard herda os limites das baselines](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-5-plataforma.tex:266) |
| C6-01 | P2 | ESTRUTURA | [Resultado principal e pergunta efetivamente respondida](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:23) |
| C6-02 | P2 | PROVENIENCIA | [Qual é a fonte independente dos fingerprints?](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:61) |
| F10 | P2 | FIGURA | [Amostra e filtros precisam de um fluxo e de um calendário](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:96) |
| F11 | P2 | FIGURA | [Distribuição operacional e relação energia-carga](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:107) |
| C6-03 | P2 | INTERPRETACAO | [Diferenças de distribuição não identificam o regime físico](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:128) |
| C6-04 | P2 | INTERPRETACAO | [Alocação mensal não torna todo o evento curto indetetável](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:156) |
| C6-05 | P1 | ESTATISTICA | [Autocorrelação e cobertura marginal são propriedades distintas](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:178) |
| C6-06 | P1 | INFERENCIA | [Ganho não demonstrado não equivale a modelo vazio](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:202) |
| F12 | P2 | FIGURA | [Forest plot do ganho preditivo com a sensibilidade visível](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:214) |
| C6-07 | P2 | INFERENCIA | [Instabilidade depende do teste, suporte e precisão](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:293) |
| F13 | P2 | FIGURA | [Predições a carga comum em vez de quatro figuras repetidas](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:305) |
| C6-08 | P1 | INTERPRETACAO | [Excursões observadas não identificam falsos alarmes](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:384) |
| F14 | P2 | FIGURA | [Cobertura, excursões e persistência numa leitura única](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:396) |
| C6-09 | P1 | CONSISTENCIA | [Contagens de excursões contraditórias](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:420) |
| C6-10 | P2 | METODO | [Valor incremental não testa toda a suficiência física](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:519) |
| C6-13 | P2 | RELATO | [Substituir p-values inválidos por evidência descritiva legível](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:609) |
| C6-11 | P2 | DIAGNOSTICO | [Dois algoritmos sem separação clara não excluem regimes](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:652) |
| C6-12 | P1 | SUPORTE | [Overlap de densidades não prova ausência de extrapolação](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:675) |
| F15 | P3 | FIGURA | [Acoplamento de vapor com hipótese física explícita](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:703) |
| C6-14 | P1 | SINTESE | [A síntese está mais categórica que os resultados](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:757) |
| C6-15 | P2 | MECANISMO | [Separar projeção algébrica, simulação e evento observado](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:825) |
| F16 | P3 | FIGURA | [Sensibilidade dos efeitos, não apenas dos rótulos](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-6-diagnostico.tex:854) |
| C7-01 | P2 | ESTRUTURA | [O capítulo mistura discussão, métodos e novos resultados](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:28) |
| C7-02 | P1 | ARGUMENTO | [A discussão amplia indevidamente o veredicto do diagnóstico](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:62) |
| C7-03 | P2 | ARGUMENTO | [Evitar a dicotomia fixa = deteta / adaptativa = esconde](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:101) |
| F17 | P2 | FIGURA | [Esquema central: referência, estado e monitor](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:129) |
| C7-04 | P2 | NORMAS | [Reformular a consequência normativa e discutir literatura](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:181) |
| C7-05 | P2 | CRITERIOS | [Não converter escolhas prudentes em regras universais](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:246) |
| C7-06 | P1 | ACEITACAO | [Compatibilidade por não-rejeição não valida uma banda](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:318) |
| C7-07 | P1 | ACEITACAO | [A regra 4/5 precisa de justificação e avaliação conjunta](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:331) |
| C7-18 | P1 | ESTIMANDO | [O critério de aceitação tem de corresponder ao uso da baseline](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:389) |
| C7-08 | P2 | MODELOS | [Nomear a construção e tratar a quantílica anual como sensibilidade](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:458) |
| C7-09 | P1 | ESTIMANDO | [O candidato com AR muda a previsão; o ganho tem de corresponder](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:525) |
| F18 | P2 | FIGURA | [Matriz de decisão por candidato e por par anual](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:537) |
| C7-10 | P2 | POPULACAO | [A interseção de 876 dias altera a população de interesse](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:656) |
| F19 | P2 | FIGURA | [Visualizar quanto sinal cada componente preserva](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:701) |
| C7-11 | P1 | ALGEBRA | [Reajustar não apaga universalmente o sinal de mudança](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:712) |
| C7-12 | P1 | EVIDENCIA | [Um lote inválido também não sustenta uma conclusão qualitativa](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:742) |
| C7-14 | P1 | SIMULACAO | [Tornar o gerador e a calibração de falsos sinais comparáveis](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:769) |
| C7-15 | P2 | SIMULACAO | [O gerador linear favorece a comparação pontual adotada](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:822) |
| F20 | P2 | FIGURA | [Curvas de deteção e atraso sob o mesmo falso sinal](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:849) |
| C7-16 | P2 | SIMULACAO | [Exemplos simulados não são teoremas universais](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:888) |
| F21 | P3 | FIGURA | [Protótipo da ficha e diagrama de estados](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:936) |
| C7-13 | P1 | INTERPRETACAO | [Cobertura e taxa de excursões são complementares](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:972) |
| C7-17 | P2 | LIMITACOES | [Corrigir contradições internas e preservar o alcance real](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-7-discussao.tex:1014) |
| C8-01 | P2 | CONTEUDO | [Fechar perguntas com resultados e limites, sem novo manifesto](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:14) |
| C8-02 | P2 | ESTRUTURA | [Trocar escada de complexidade por decisões guiadas pelo diagnóstico](/Users/bernardoribeiro/Desktop/Tese/novathesis/2-MainMatter/chapter-8-conclusoes.tex:31) |
| AP-A | P2 | APENDICE | [Protocolo público e cronologia das emendas](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-A-protocolo-sr.tex:11) |
| AP-B | P2 | APENDICE | [Validação da extração assistida e adjudicação humana](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-B-validacao.tex:11) |
| AP-C | P2 | APENDICE | [Dicionário que permita reproduzir as fronteiras e conversões](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-C-dicionario.tex:11) |
| AP-D | P2 | APENDICE | [Publicar as tabelas que sustentam os qualificadores](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-D-tabelas.tex:11) |
| AP-E | P2 | APENDICE | [Manual operacional e proposta futura devem ser distinguíveis](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-E-manual.tex:11) |
| AP-F | P2 | APENDICE | [Revisão adversarial como registo verificável, não selo de validade](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-F-adversarial.tex:11) |
| AP-G | P2 | APENDICE | [A matemática essencial não pode permanecer num apêndice vazio](/Users/bernardoribeiro/Desktop/Tese/novathesis/3-BackMatter/appendix-G-matematica.tex:13) |
