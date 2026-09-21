# Protótipos para as caixas de revisão da Secção 3.3

Gerados a 2026-09-21. Não alteram nada na tese. `python3 gerar.py` regenera tudo.
Fonte: `analysis_dataset.csv` do Corpus A registado (331 publicações).

## C3-V05 — `v05_unidades.*` — **recomendo adoptar**

A caixa pedia uma figura com `paper_type` e `type_of_organisation` mantendo a
categoria por resolver. Em vez de barras empilhadas, um **gráfico de unidades**:
cada um dos 331 quadrados é uma publicação.

A razão é o que a subsecção afirma — que a literatura é uma colecção de casos
isolados. Isso é uma afirmação sobre quantas das 331 são o quê, e um quadrado
por publicação torna-a literal: o bloco de 153 casos aplicados únicos ocupa
quase metade do painel. Barras empilhadas diriam o mesmo em abstracto.

O «por resolver» não é um tom da rampa, é um **quadrado vazio**. Ausência lê-se
melhor como vazio do que como cor, e um cinzento claro seria indistinguível do
último passo da rampa (ΔE 5,4 em visão normal — verificado). Os dois painéis
são directamente comparáveis porque ambos têm exactamente 331 quadrados.

## C3-V08 — `v08_norma_protocolo.*` — **recomendo adoptar, e é a mais forte**

A caixa pedia dois painéis com as marginais de `ems_standard` e `mv_protocol`.
Fiz o **cruzamento** em vez das marginais, porque a pergunta do capítulo não é
quantos artigos invocam a norma e quantos invocam um protocolo, é quantos dos
que invocam a norma invocam também um protocolo.

Resultado: **das 191 publicações que invocam a família ISO 50001, 173 (91%) não
invocam protocolo algum de medição e verificação.** IPMVP em 8, ASHRAE 14 em 3,
SEP M&V em 3.

É a demonstração empírica, dentro do corpus, do que a Secção 2.3.3 argumenta a
partir do texto das normas: a norma de gestão diz o que fazer e não diz como
validar, e a literatura que a invoca faz o mesmo. Dois painéis marginais não
conseguiriam dizer isto.

Cuidado com a formulação, como a caixa avisa: isto é o que o artigo **invoca**,
não a certificação da organização nem a conformidade do modelo.

## C3-V07 — `v07_setor_familia.*` — **não adoptar; confirma o apêndice**

A caixa dizia para só inserir se a normalização do sector fosse revista. Foi
revista hoje (186 → 130 por classificar), por isso valia a pena ver. Vi:

**58 das 100 células têm dados, o máximo é 16 e a mediana das células não vazias
é 2.** A única linha com substância é «Edifícios / serviços públicos». Os
sectores de processo contínuo que interessam à tese — petroquímica, cimento,
refinação — são uns e dois. A matriz não sustenta leitura por sector, tal como
a caixa suspeitava. Fica no Apêndice C, e o protótipo serve de prova da decisão.

## C3-V09 e C3-V10 — não prototipei

A V09 pede o mapa temático **só depois de nomear os grupos pela leitura dos
artigos**, e avisa que os rótulos automáticos trocaram entre execuções. Isso é
trabalho de leitura, não de desenho: não o posso resolver com um gráfico.

A V10 pede uma rede bibliográfica. Redes deste tamanho dão novelos com pouca
informação por centímetro. Antes de desenhar uma, é preciso decidir que
pergunta ela responde — e nenhuma secção da 3.3 tem hoje uma pergunta que
precise dela. Faço o protótipo se disseres qual é a pergunta.
