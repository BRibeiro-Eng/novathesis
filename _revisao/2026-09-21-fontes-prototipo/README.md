# Protótipo C3-V04 — fontes e dispersão

Figura de dois painéis para a Secção 3.3.3, ainda não integrada na tese.

- `fontes_e_dispersao.pdf` / `.png`: fontes com pelo menos cinco publicações e percentagem acumulada das 331 publicações, por fonte ordenada de forma decrescente. A curva é descritiva; não testa a lei de Bradford.
- `fontes_harmonizadas.csv`: tabela completa das 191 fontes após três fusões documentadas, com posto, contagem e percentagem acumulada. Pode alimentar a tabela do Apêndice C.
- `gerar.py`: regeneração da figura e da tabela a partir de `analysis_dataset.csv` do Corpus A registado.

## Harmonizações verificadas

Só foram unidos os seguintes pares de designações. O ISSN foi confirmado no metadado Crossref dos DOI indicados (um de cada designação):

| Designações no corpus | Fonte harmonizada | ISSN | DOI de verificação |
|---|---|---|---|
| `sustainability (switzerland)` / `sustainability` | Sustainability | 2071-1050 | [10.3390/su17115131](https://api.crossref.org/works/10.3390/su17115131), [10.3390/su11216046](https://api.crossref.org/works/10.3390/su11216046) |
| `applied sciences (switzerland)` / `applied sciences-basel` | Applied Sciences | 2076-3417 | [10.3390/app13031368](https://api.crossref.org/works/10.3390/app13031368), [10.3390/app14209403](https://api.crossref.org/works/10.3390/app14209403) |
| Duas grafias de `Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture` | Mesmo título | 0954-4054 / 2041-2975 | [10.1177/0954405416683427](https://api.crossref.org/works/10.1177/0954405416683427), [10.1177/0954405418789980](https://api.crossref.org/works/10.1177/0954405418789980) |

Edições anuais de conferências e títulos apenas parecidos pelo nome não foram agregados. As tabelas originais tinham 194 designações e as dez primeiras reuniam 92/331 (27,8%). Depois destas fusões, há 191 fontes; 142 surgem uma única vez. Há um empate no corte das dez primeiras, por isso o painel esquerdo mostra as **11 fontes com ≥5 publicações**, que reúnem 99/331 (29,9%).

## Implicação para o texto

Se esta versão for adotada, a frase da Secção 3.3.3 sobre `194 designações` e `27,8% nas dez primeiras` deve ser atualizada. Uma formulação possível:

> Depois de harmonizar três pares de designações pelo ISSN, as 331 publicações repartem-se por 191 fontes; 142 surgem uma única vez. As 11 fontes com pelo menos cinco publicações reúnem 99 publicações (29,9%).

A tabela completa deve ser incluída no Apêndice C ao integrar a figura. O gráfico, isoladamente, não justifica uma interpretação segundo a lei de Bradford.

Regeneração: `python3 gerar.py` (requer pandas e matplotlib; lê a tabela congelada em `~/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables/analysis_dataset.csv`).
