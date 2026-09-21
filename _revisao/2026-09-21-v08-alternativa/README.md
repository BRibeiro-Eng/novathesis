# Alternativa à Figura 3.7 — norma e protocolo

Protótipo para substituir o mapa de calor da Figura 3.7. Ainda não está integrado na tese.

## Decisão visual

O argumento da Secção 3.3.5 pergunta quantas publicações que invocam a família ISO 50001 também nomeiam um protocolo de medição e verificação. O heatmap atual cruza quatro grupos de norma com seis etiquetas de protocolo, mas a sua escala de cor é dominada por 173, 59 e 54 e dificulta comparar os protocolos nomeados (células de 1 a 8). Uma publicação pode nomear mais de um protocolo, pelo que somar as células de uma linha pode contá-la duas vezes.

O protótipo usa dois grupos de norma com interpretação clara e estados de protocolo **mutuamente exclusivos por publicação**: nenhum nomeado, pelo menos um nomeado, ou campo por resolver. As barras são percentuais para permitir comparação entre grupos de tamanhos diferentes; as frações sobre os totais aparecem junto das barras.

| Norma declarada | Nenhum protocolo nomeado | Pelo menos um nomeado | Protocolo por resolver | Total |
|---|---:|---:|---:|---:|
| Família ISO 50001 | 173 | 14 | 4 | 191 |
| Nenhuma norma | 59 | 5 | 2 | 66 |

Ficam fora desta comparação 73 publicações cujo campo de norma está por resolver e uma que nomeia apenas outra norma. A frequência de protocolo nomeado é 14/191 (7,3%) no primeiro grupo e 5/66 (7,6%) no segundo. A diferença é apenas descritiva; a figura não sustenta uma inferência sobre associação ou causalidade. «Nenhum protocolo nomeado» não significa ausência de medição. As classificações são concordantes entre extrações automáticas, sem validação humana integral.

O script `gerar.py` lê o `analysis_dataset.csv` do Corpus A registado e gera PDF vetorial e PNG. Uma publicação conta uma vez mesmo quando declara vários protocolos.
