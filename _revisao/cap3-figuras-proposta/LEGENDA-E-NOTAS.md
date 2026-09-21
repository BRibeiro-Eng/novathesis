# Propostas para as figuras do Capítulo 3

## Alternativa com círculos — diagrama de Euler

Proposta revista a pedido do Bernardo: [corpora-euler.pdf](corpora-euler.pdf), com fonte em [corpora-euler-desenho.tex](corpora-euler-desenho.tex). Mantém a tipografia e a paleta da Figura 2.1, substituindo as caixas dos corpora por círculos de inclusão. B e os 13 casos exploratórios estão contidos em A e não se sobrepõem. A SQ1 refere-se à totalidade de A, incluindo B e os casos exploratórios; a SQ2 e a SQ3 associam-se à cartografia de B. A avaliação em Sines permanece numa componente separada. As áreas não são proporcionais às contagens. A legenda proposta abaixo continua aplicável.

## Desenho da revisão

O esquema de conjuntos mostra a pertença e a função de cada corpus: B está dentro de A; os casos exploratórios também estão em A, mas fora de B. A avaliação em Sines fica num painel separado, sem seta causal ou cronológica entre a revisão e as decisões do caso. As áreas não representam proporções.

Pré-visualização: [corpora.pdf](corpora.pdf). Fonte vetorial: [corpora-desenho.tex](corpora-desenho.tex).

Legenda proposta:

~~~latex
Desenho da revisão de âmbito e relação com a componente empírica da dissertação. O Corpus~A reúne 331 publicações elegíveis e sustenta a SQ1. O Corpus~B é um subconjunto de A, com 40 publicações de processos contínuos dos setores pré-registados, das quais 39 foram cartografadas para responder à SQ2 e à SQ3. Os 13 casos exploratórios pertencem a A, mas ficam fora de B e das suas contagens. A avaliação em Sines constitui uma componente distinta. As áreas são esquemáticas, não proporcionais às contagens.
~~~

## PRISMA

Pré-visualização: [prisma.pdf](prisma.pdf). Fonte vetorial: [prisma-desenho.tex](prisma-desenho.tex).

Mantêm-se o percurso vertical, as saídas laterais e todas as contagens. Adotam-se os painéis, as caixas, os números em círculo, a paleta e a tipografia da Figura 2.1. Os 137 relatórios não recuperados e os três duplicados tardios continuam discriminados.

Legenda proposta, conservando a referência ao apêndice e o label existente quando a figura for integrada:

~~~latex
Fluxograma PRISMA~2020 da identificação, triagem e inclusão de publicações. A pesquisa em bola de neve foi registada no protocolo, mas não executada (decisão~D9, Apêndice~\ref{app:protocolo-sr}). O Corpus~B é um subconjunto do Corpus~A, escolhido para cartografia detalhada. Os treze casos exploratórios pertencem ao Corpus~A, mas são tratados à parte e não entram nas contagens do Corpus~B.
~~~

## Correção factual confirmada

A legenda atual diz que os treze casos exploratórios não entram no Corpus A. Essa frase não coincide com a pertença registada: os 13 identificadores da decisão exploratória estão em A e nenhum está em B. A nova proposta corrige a frase, sem acrescentar as 13 publicações aos 331 nem modificar qualquer total.

Verificação: lista de 13 em `/Users/bernardoribeiro/LocalResearch/Screening/level3_extraction/output/fn_census/detector_c/triage/verdicts/_exploratory_decision.json`, cruzada, apenas em leitura, com `rosters()` de `output/corpus_profile.py`. Fluxo e balanços conferidos em `prisma/PRISMA_FLOW_2026-09-17.md`.

## Ficheiros da tese

Implementação autorizada e efetuada em 2026-09-20. O diagrama de Euler foi integrado em `5-Figures/tikz/f03a-desenho-revisao.tex`, substituindo a caixa C3-V01 no Capítulo 3. O PRISMA aprovado substituiu `5-Figures/tikz/f04-prisma.tex`, conservando o label `fig:prisma`. O novo diagrama usa `fig:desenho-revisao`; a numeração e as referências são atualizadas pelo LaTeX. O texto novo e a correção factual da legenda usam a marca de revisão `revisto`. As versões anteriores do capítulo e do PRISMA foram preservadas em `antes-integracao/`, juntamente com o PDF anterior. A Figura 2.1 não foi alterada. As figuras integradas são TikZ nativo e usam o estilo partilhado da tese; os PDF e PNG desta pasta continuam a documentar as propostas aprovadas.


Validação da integração: tese compilada com pdfLaTeX/latexmk, 294 páginas; referências e citações resolvidas. Euler: Figura 3.1, página 34 (página 61 do PDF). PRISMA: Figura 3.2, página 37 (página 64 do PDF). Ambas as páginas foram inspecionadas visualmente. Recorte para consulta: [figuras-integradas.pdf](figuras-integradas.pdf). O auxiliar da skill encontrou um erro de descodificação do log após a compilação; uma chamada direta a latexmk terminou com código 0 e confirmou todos os alvos atualizados.
