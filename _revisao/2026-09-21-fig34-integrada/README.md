# Protótipo da Figura 3.4 — tempo e revistas

Os dois painéis da Figura 3.4 mostram (A) publicações anuais por tipo de documento e (B) revistas com pelo menos cinco artigos de revista. A curva acumulada foi removida. A figura ainda não foi integrada no texto principal da tese.

- `figura34_temporal_revistas.pdf` / `.png`: primeira composição, painéis lado a lado, 17 × 9 cm.
- `figura34_vertical.pdf` / `.png`: revisão com painéis empilhados, 15,5 × 12,8 cm. Dá espaço aos nomes completos das revistas e às barras, à custa de mais altura na página.

## Dados e convenções

- Corpus A registado: 331 publicações, 214 artigos de revista e 117 comunicações em conferência.
- O painel B usa **apenas os 214 artigos de revista**, para não chamar «revistas» às fontes das comunicações. Depois de harmonizar variantes verificadas por ISSN, há 112 revistas, 83 das quais aparecem uma só vez. As nove com pelo menos cinco artigos reúnem 83/214 (38,8%). A lista integral está em `revistas_harmonizadas.csv`.
- O ano de 2026 está incompleto (pesquisa até fevereiro) e a barra aparece a cinzento.
- Os marcos ISO 50001:2011 e ISO 50006:2014 estão na fronteira **entre barras anuais**; são referências cronológicas, não evidência de causalidade.
- As equivalências por ISSN e DOI usadas para `Sustainability`, `Applied Sciences` e `Proceedings of the Institution of Mechanical Engineers, Part B` estão documentadas em `../2026-09-21-fontes-prototipo/README.md`.

## Se a figura for adotada

O texto da Secção 3.3.3 e a legenda têm de ser alinhados com o gráfico: deixar de falar de «distribuição anual e acumulado»; explicitar que o painel B se restringe aos artigos de revista; retirar `Energy Procedia` do elenco de **revistas** (é uma fonte de comunicações neste corpus). A estatística das 194 designações de fonte refere-se ao corpus inteiro antes das três harmonizações e não é diretamente comparável com as 112 revistas do painel B. A tabela completa de fontes pode permanecer no Apêndice C, sem curva acumulada na figura.

Legenda sugerida:

> Evolução anual e revistas mais frequentes do Corpus A, 1997–2026. (A) Publicações por ano, separadas em artigos de revista e comunicações em conferência. O registo de 2026 aparece a cinzento porque a pesquisa foi executada em fevereiro desse ano. As linhas tracejadas assinalam a publicação da ISO 50001:2011 e da ISO 50006:2014; a figura não estabelece uma relação causal com a evolução observada. (B) Revistas com pelo menos cinco artigos entre os 214 artigos de revista do corpus, após harmonização das variantes confirmadas por ISSN.

Regeneração: `python3 gerar.py` e `python3 gerar_vertical.py`. A fonte é `~/LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables/analysis_dataset.csv` e `annual.csv`.
