# Protótipos para a Secção 3.3.3

Gerados em 2026-09-21. São propostas de visualização, ainda não integradas na tese.

## Ficheiros

- `01_evolucao_tipos.pdf` / `.png`: publicações anuais empilhadas por artigo de revista e comunicação em conferência. As linhas tracejadas ficam entre as barras de 2011/2012 e de 2014/2015, no fim dos anos de publicação das normas; assinalam os primeiros anos civis completos seguintes, sem representar o mês exato. A barra cinzenta assinala 2026 parcial. Usa a paleta azul e areia das figuras bibliométricas do capítulo. `01_evolucao_eixo_duplo.*` é a versão anterior, mantida apenas para comparação.
- `02_mapa_marcadores.pdf` / `.png`: país atribuído ao caso. Todos os países recebem o mesmo tratamento; o tamanho do marcador mostra quantas publicações o mencionam, e o tom indica o primeiro ano localizável neste corpus. As duas legendas permitem ler a versão impressa sem caixas sobre o mapa.
- `02_mapa_interativo.html`: versão exploratória em que cada marcador apresenta país, contagens nos corpora A e B, primeiro e último anos, ano mediano e publicações por período.
- `03_mapa_periodos.pdf` / `.png`: quatro cortes temporais, cada qual com o número de publicações que têm país do caso localizável.
- `prototipos.py`: código de geração. `country_points.csv` fixa as coordenadas dos marcadores.

## Dados e leitura

Fonte das contagens: `LocalResearch/Screening/level3_extraction/bibliometrics/results/corpus_a_registado/tables/annual.csv` e `analysis_dataset.csv` (Corpus A, 331 publicações). O país é o **do caso estudado**, não o da afiliação dos autores. O ponto está no centro cartográfico do país, não no local da instalação. As coordenadas vêm do campo `LABEL_X/LABEL_Y` de [Natural Earth Admin 0, 1:110m](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/); Hong Kong tem uma coordenada aproximada própria, pois não está no ficheiro Admin 0 a esta escala.

Na figura temporal, a classificação documental é a do campo `document_type` de `analysis_dataset.csv`: 214 artigos de revista e 117 comunicações em conferência. A proporção de conferências é 42/77 (54,5%) em 2011–2016 e 31/132 (23,5%) em 2021–2025. A mudança descreve este corpus e não demonstra por si a maturação do campo. As datas das normas foram verificadas nas páginas oficiais da [ISO 50001:2011](https://www.iso.org/standard/51297.html) e [ISO 50006:2014](https://www.iso.org/standard/51869.html). A ISO 50006 fornece orientação específica para estabelecer, usar e manter EnPIs e EnBs; a ISO 50001 já enquadrava esses conceitos, pelo que não seria rigoroso atribuir a sua criação à ISO 50006.

Só 120 publicações têm país do caso localizável (36,3% do Corpus A). Há 187 sem resolução, 10 com texto por normalizar e 14 não aplicáveis. Uma publicação pode aparecer em vários países: são 126 atribuições em 45 países para 120 publicações. As extrações concordantes entre modelos não foram integralmente validadas por revisão humana. Assim, estes mapas descrevem apenas os registos com localização atribuída e **não sustentam uma conclusão sobre distribuição ou difusão geográfica global da literatura**. As frações localizáveis também variam entre os quatro períodos; comparar a densidade de pontos entre painéis sem ter isso em conta seria enganador.

O tom do mapa agregado é o **primeiro registo localizável no corpus**, não a data do primeiro estudo realizado em cada país. O mapa não identifica instalações ou localizações exatas. A cor usa uma escala sequencial em vez de transparência: um ponto claro continua visível quando a figura é reduzida ou impressa.

## Recomendação editorial

A figura temporal empilhada substitui melhor a atual Figura 3.4: mantém a produção anual e expõe a mudança do formato documental sem eixo acumulado. Para a geografia, o mapa interativo é útil para explorar e rever casos; para a dissertação impressa, usar um mapa apenas depois da adjudicação das localizações e com o denominador em destaque. Se a cobertura continuar baixa, uma barra de países com a categoria «por resolver» transmite melhor o resultado sem sugerir representatividade espacial.

Para regenerar apenas a figura temporal: `python3 prototipos.py temporal`. Os mapas foram gerados antes de uma atualização da tabela de países do Corpus A; para os regenerar é preciso rever coordenadas e denominadores. Requer pandas, matplotlib, plotly e kaleido; as tabelas do corpus permanecem na localização acima.
