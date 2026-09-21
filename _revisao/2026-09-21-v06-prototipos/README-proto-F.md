# Protótipo F — alternativa à Figura 3.7

Esta figura substitui o ranking de famílias por uma pergunta que o texto da secção realmente discute: quantas publicações declaram rácio/média, regressão, ambas ou nenhuma destas famílias. O ranking completo permanece no texto. É um protótipo, ainda não integrado na tese.

## Leitura

- Painel A: cobertura do campo de famílias de modelos no Corpus A. Das 331 publicações, 162 têm uma classificação **concordante entre as duas extrações automáticas** e 169 ficam por resolver; não foi feita validação humana integral.
- Painel B: cruzamento **apenas nas 162 concordantes**. Linhas: presença de rácio de intensidade simples ou média do consumo específico. Colunas: presença de regressão linear ou múltipla. Células: 59 com rácio/média sem regressão, 31 com ambos, 23 sem nenhum destes dois grupos, 49 com regressão sem rácio/média. As células são mutuamente exclusivas neste cruzamento, mas as publicações podem declarar outras famílias.
- Destaque: 47 das 59 publicações da célula «rácio/média sim, regressão não» não declaram **qualquer outra família**.

O eixo diz explicitamente «regressão», porque a divisão usada nos protótipos A–C contava apenas regressões linear e múltipla. Chamar a outra coluna «sem modelo ajustado» seria incorreto: nela podem estar modelos de aprendizagem automática, pontos de mudança ou outras famílias. O protótipo F não faz afirmações sobre a qualidade dos modelos, nem transforma famílias declaradas em métodos efetivamente validados.

Dados: `analysis_dataset.csv` do Corpus A registado. Código: `gerar3.py`, que reutiliza a leitura e a contagem de `gerar.py`. Regeneração: `python3 gerar3.py`.
