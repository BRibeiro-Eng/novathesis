"""Generate the editorial map; never edits the thesis or research outputs."""
from pathlib import Path
import csv
import hashlib
import json
import re
from collections import Counter

ROOT = Path('/Users/bernardoribeiro/Desktop/Tese/novathesis')
OUT = Path(__file__).parent
BASE = Path('/Users/bernardoribeiro/LocalResearch/baselines-cc')
SCREEN = Path('/Users/bernardoribeiro/LocalResearch/Screening/level3_extraction')
EXTRACT = Path('/Users/bernardoribeiro/tese-extraccao')
CHAPTERS = [ROOT / '2-MainMatter' / f for f in (
    'chapter-1-introducao.tex', 'chapter-2-enquadramento.tex',
    'chapter-3-revisao.tex', 'chapter-4-metodos.tex',
    'chapter-5-plataforma.tex', 'chapter-6-diagnostico.tex',
    'chapter-7-discussao.tex', 'chapter-8-conclusoes.tex')]
APPENDICES = sorted((ROOT / '3-BackMatter').glob('appendix-[A-G]-*.tex'))
SOURCE_FILES = CHAPTERS + APPENDICES
LABELS = {}
for file in SOURCE_FILES:
    for line, text in enumerate(file.read_text().splitlines(), 1):
        for label in re.findall(r'\\label\{([^}]+)\}', text):
            LABELS[label] = (file, line)

SOURCES = {
    'V': (SCREEN / 'VALIDATION_PROTOCOL_C.md', '## 4. Audit design'),
    'VP': (SCREEN / 'PROTOCOL.md', '## 16. Snowballing entry path'),
    'BF': (SCREEN / 'bibliometrics/biblio/analysis.py', 'def frequencies'),
    'BN': (SCREEN / 'bibliometrics/biblio/networks.py', 'def projection'),
    'PBI': (EXTRACT / 'medidas/_TODAS_AS_MEDIDAS.dax', 'Feii_kBTU_bbl ='),
    'GNE': (EXTRACT / 'power_query/FactEnergia_Tags.m', 'ComPCI ='),
    'DAX': (EXTRACT / 'particoes/BaselineFit__BaselineFit.dax', 'VAR _Result'),
    'OLS': (BASE / 'src/baselines/replication.py', 'def fit_ols'),
    'CFG': (BASE / 'config/params.yaml', 'inferencia:'),
    'INF': (BASE / 'src/baselines/inference.py', 'def moving_block_indices'),
    'REF': (BASE / 'src/baselines/partc/reference.py', 'def _block_errors'),
    'LIN': (BASE / 'src/baselines/partc/models/__init__.py', '_LINEAR_DEFINITIONS:'),
    'GAM': (BASE / 'src/baselines/partc/models/additive.py', 'def _fit_ridge'),
    'MON': (BASE / 'src/baselines/partc/models/monitors.py', 'def monitor_cusum'),
    'SIM': (BASE / 'src/baselines/partc/simulation.py', 'def generate_noise'),
    'STATE': (BASE / 'src/baselines/partc/models/state.py', 'def fit_state_space'),
    'JOINT': (BASE / 'src/baselines/partc/joint.py', 'def innovation_covariance'),
}

# title | status | priority | depth | origin labels | supporting sources | specification
# T: in active thesis; C: clarified by inspected implementation; P: planned;
# F: future only. None is a claim of scientific validation or completed execution.
GROUPS = [
('01', 'Notação, populações e operações sobre dados', 'sec:mat-notacao-dados', r'''
Índices, vetores e unidades|T|P1|Definição|sec:metricas,sec:perfil-dados||Definir dia civil t, ano y, unidade u, vetor v, observação i, réplica b; separar E, carga Q, covariáveis Z, densidade e autocorrelação. Fixar dimensões de cada símbolo e convenção de sinal.
Populações e máscaras de seleção|T|P1|Algoritmo|sec:fontes,sec:perfil-dados,sec:referencia-congelada|DAX,REF|Definir candidatos, elegíveis, retidos, completos, em suporte e pontuáveis. Publicar ordem dos filtros e denominadores; distinguir dias únicos de células série–dia e interseção entre modelos.
Estimando, estimador e quantidade observada|T|P1|Definição|sec:protocolo-baselines,sec:leitura-integrada||Dar o alvo de cada análise, população, comparador e condicionamento; distinguir previsão temporal, normalização, deteção e poupanças verificadas. Um resultado deve indicar a pergunta que mede.
Agregação horária e calendário civil|T|P1|Equação + algoritmo|sec:fontes|GNE|Formalizar soma de incrementos, integração de caudal e média ponderada pelo tempo; horas válidas, fuso, dias de 23/25 horas e dias incompletos. A validade física da regra executada permanece por confirmar.
Alocação mensal em dias e reagregação|T|P1|Equação|sec:fontes,sec:perfil-dados,sec:cobertura||Explicitar E_dia=E_mês/n_dias e conservação do total; distinguir resolução de apresentação e de medição. Formalizar média mensal versus total mensal e impedir pseudorreplicação dos dias alocados.
Janelas móveis, acumulados e exposição|T|P1|Equação|sec:metricas,sec:dashboard,sec:referencia-fixa||Definir intervalos civis, inclusão do dia atual, mínimo de observações, denominador efetivo e reinício. Uma janela de 30 dias não significa as últimas 30 observações retidas.
Faltas, zeros, imputação e seleção pela resposta|T|P1|Definição + algoritmo|sec:fontes,sec:modelo-dimensional,sec:guidelines|GNE,DAX|Distinguir zero físico, ausente, valor propagado/default e exclusão; LOCF e backfill, fração imputada e informação futura. A máscara altera a população; mecanismo de falta não é identificado só pela série.
Precedência de fontes, pesos e conservação|T|P1|Equação|sec:modelo-dimensional,sec:validacao-dados||Representar seleção de canal por função por partes; soma de componentes com pesos 0, 1, −1 ou fracionários; vigência e ausência de dupla contagem. Separar harmonização de reconciliação estatística por balanços.
Concordância numérica e tolerâncias|C|P1|Equação|sec:replicacao,sec:validacao-dados|OLS,CFG|Distinguir comparação de dados por máximo de tolerâncias absoluta/relativa e replicação por atol+rtol×módulo da referência. Definir zero, valores com sinal, unidades e igualdade do conjunto de datas; um hash não mede exatidão física.
Estatística descritiva e completude|T|P2|Definição|sec:perfil-dados,sec:corpus-a||Média, mediana, quantis, variância, desvio-padrão, IQR, amplitude, proporção disponível e denominador por campo. Definir convenção amostral e quantis quando usados por filtros, bandas ou estratos.
'''),
('02', 'Grandezas físicas e indicadores energéticos', 'sec:mat-energia', r'''
Balanços materiais e definição de carga|P|P1|Equação + esquema|sec:caso-estudo,sec:metricas,sec:validacao-dados||Formalização a acrescentar: fronteira, entradas, saídas e acumulação; carga fresca versus reprocessada, componentes e retornos. Fundamentar Q com a definição efetivamente usada; o caso físico no Cap. 2 ainda está incompleto.
Balanço energético e significado de eficiência|P|P1|Equação + esquema|sec:processos-continuos,sec:caso-estudo||Acrescentar apenas as relações necessárias à CDU: energia de combustível, dever térmico, recuperação e perdas. Q térmico deve ter símbolo distinto da carga. Não apresentar GNE, EII ou resíduo como eficiência termodinâmica ou exergia.
Combustíveis em gás natural equivalente|T|P1|Equação + unidades|sec:metricas|GNE|Escrever massa×PCI/PCI_ref por combustível, somas por unidade e período, bases mássica/volúmica e distinção PCI/PCS. Relacionar t de combustível, kcal/kg e t GNE; declarar fonte e vigência dos fatores.
Produto de médias versus energia integrada|C|P1|Derivação curta|sec:fontes,sec:metricas|GNE|A implementação consultada combina caudal agregado e PCI médio ao dia. Comparar soma horária de massa×PCI com produto dos agregados; explicitar o termo de covariância e a condição em que desaparece. Não inventar a dimensão do erro nos dados.
Vapor por nível de pressão e energia equivalente|T|P1|Equação + unidades|sec:modelo-dimensional,sec:metricas||Massa de vapor×equivalente entálpico/PCI_ref; identificar 24/10/3 bar, referência de entalpia, condensados e convenção contabilística. Distinguir consumo bruto, produção creditada e saldo líquido negativo.
Eletricidade e rendimento de conversão|T|P1|Equação + unidades|sec:metricas||MWh→energia térmica→t GNE, com 860,4 Mcal/MWh, 11 820 kcal/kg e rendimento 0,57 segundo o texto. Explicar conversões de milhar e significado de energia final versus combustível equivalente; verificar origem dos parâmetros.
Massa, volume, densidade e barris|C|P1|Equação + unidades|sec:metricas|PBI|Explicitar V=m/densidade, t↔kt, m³↔bbl e densidade relativa; a conversão e a temperatura de referência devem preceder fórmulas com API e fatores por barril.
Transformações API, temperatura, pressão e rendimentos|C|P1|Equação + condições|sec:metricas,sec:suficiencia|PBI|Mapear API a partir da densidade, °C/°F, pressão manométrica/absoluta e mmHg, rendimento mássico/volúmico. O ramo CC consultado usa flash já em °F e logaritmo de pressão convertido à unidade convencionada; conferir antes de transcrever.
Consumo específico e média ponderada|C|P1|Derivação curta|sec:enb-cadeia,sec:metricas,sec:dashboard|PBI|Rácio de totais sobre os mesmos dias operacionais; mostrar equivalência à média dos rácios diários ponderada pela carga, e diferença da média aritmética. Derivar E/Q=a+b/Q+erro/Q para ligar rácio e regressão.
Normalização energética e desvio à referência|T|P1|Equação + exemplo|sec:enb-par,sec:metricas,sec:leitura-integrada||Definir consumo esperado à carga observada, comparação a condições comuns, desvio absoluto e relativo. Fixar qual normalização é efetivamente usada; nenhuma regressão histórica define por si consumo ótimo ou poupança causal.
EII: razão, energia padrão e função da CDU|C|P1|Equação + algoritmo|sec:metricas,sec:dashboard|PBI|EII=100×consumo/energia padrão; energia padrão por carga×fator; ramo CDU dependente de densidade, API, flash e resíduo, com teto por partes. Transcrever convenção executada e verificar separadamente conformidade com documentação Solomon.
Agregação de EII, quartis e decomposição por vetor|C|P2|Equação|sec:metricas,sec:dashboard|PBI|Rácio de somas, ponderação por energia padrão, contributos aditivos por vetor e guardas de dias válidos. Distinguir quartis externos de quantis da amostra; a média simples de índices não substitui o índice agregado.
Emissões calculadas e âmbito dos fatores|C|P1|Equação + unidades|sec:metricas,sec:dashboard|PBI|Soma do GNE líquido por vetor×fator de emissão e conversão t→kt. Declarar unidades e fonte dos fatores e o âmbito das emissões atribuídas; a expressão computacional não demonstra equivalência a inventário físico de CO₂.
'''),
('03', 'Contagens, bibliometria e redes', 'sec:mat-bibliometria', r'''
Conjuntos de publicações e fluxo PRISMA|T|P1|Equação + esquema|sec:pesquisa,sec:corpus-a||A, B, união, interseção, diferenças, cardinalidades e inclusão–exclusão; identidade única da publicação. B previsto como subconjunto e B observado são objetos distintos; fluxos de seleção precisam de denominadores e exclusões disjuntas.
Recuperação de textos e disponibilidade por grupo|T|P1|Equação|sec:pesquisa,sec:corpus-a||Taxa de recuperação condicionada a DOI/classificação e cobertura de metadados por fornecedor. A diferença entre grupos descreve seleção observada; não identifica elegibilidade nem taxa de erro dos textos não recuperados.
Frequências multirrótulo e cruzamentos|C|P1|Equação + exemplo|sec:corpus-a|BF|Matriz publicação×categoria, soma de indicadores, denominadores total/disponível/comum e contagem uma vez por célula. Percentagens podem somar mais de 100%; dado ausente difere de ausência explícita da característica.
Interseções exatas e contagem fracionada|C|P1|Equação + exemplo|sec:corpus-a|BF|Combinações exatas no UpSet versus coocorrência inclusiva. No aluvial, cada publicação distribui peso 1 pelas combinações setor×modelo×norma; demonstrar conservação de massa e explicitar agrupamento em Outros.
Matrizes de incidência e projeções de rede|C|P2|Equação|sec:corpus-a|BN|Nós, arestas, direção, peso, diagonal e contagem binária por publicação. Coocorrência de termos e coautoria/afiliação como projeções; distinguir número de publicações, ligações, grau e força ponderada.
Citação direta, acoplamento e cocitação|C|P2|Equação + esquema|sec:corpus-a|BN|Distinguir as três relações; acoplamento por referências comuns normalizado pela raiz do produto dos tamanhos das listas, mínimo duas partilhadas na implementação. Delimitar cobertura das referências indexadas e recortes das projeções.
Modularidade e comunidades|C|P2|Equação + algoritmo|sec:corpus-a|BN|Objetivo de modularidade ponderada e otimização gulosa; resolução, limiares de ocorrência e poda de nós. Comunidades e posições no layout não são categorias metodológicas validadas nem distâncias físicas.
TF–IDF e fatorização não negativa de tópicos|C|P2|Equação + algoritmo|sec:corpus-a|BN|A exploração de tópicos mencionada no texto usa TF–IDF e NMF no código consultado. Especificar vocabulário, n-gramas, pesos, normalização, matriz≈W×H e atribuição dominante; verificar se estes resultados entrarão na versão final.
Evolução temporal, citações e concentração|T|P2|Definição|sec:corpus-a|BF,BN|Contagens anuais e por janelas fixas, concentração nas fontes mais frequentes, mediana de citações à data da consulta. Não comparar ano parcial a ano completo sem qualificação nem fundir contagens de fornecedores.
'''),
('04', 'Auditoria da revisão e controlo da extração', 'sec:mat-auditoria-revisao', r'''
Taxas de divergência, alteração e fundamentação|P|P1|Equação|sec:pesquisa,app:validacao|V|Desenvolver D_v/N_v, alterações após revelação, discrepâncias humano–IA e taxa de grounding com denominador por instrumento/campo. O protocolo existe; a tese ainda não documenta a execução completa. Concordância não equivale a acerto.
União de detetores, censos e fecho iterativo|P|P1|Conjuntos + algoritmo|sec:pesquisa,app:validacao|V|União de sinalizações de modelos, léxico e passagem de recall; candidatos novos, verificação humana e fecho. Censo exaure a união definida, não falsos negativos invisíveis; contagens censitárias ficam separadas da amostra.
Amostragem aleatória de artigos e erro por campo|P|P1|Equação + algoritmo|app:validacao|V|SRS de 40 publicações no protocolo C-2.3; unidade sorteada é artigo e unidade de erro é célula. Definir n_v elegível, concordante e não censado, erros e_v e casos n_v=0. Não usar e_v/40 quando o campo tem menos casos.
Erro binário e dados multisseleção|P|P1|Definição|app:validacao|V|Comparação após normalização; enum/bool, conjunto de etiquetas, texto substantivo, null e não aplicável. Uma diferença de conjunto conta como um erro do campo; não é F1 nem número de etiquetas erradas.
Modelo binomial, intervalo Clopper–Pearson e população finita|P|P1|Equação + pressupostos|app:validacao,sec:protocolo-baselines|V|Intervalo exato por campo sob modelo binomial; discutir amostragem sem reposição e referência hipergeométrica. CP referido pelo protocolo não deve ser apresentado como cobertura simultânea nem como limite determinista de erros por encontrar.
Zero erros, limite unilateral e tamanho amostral|P|P1|Derivação curta|app:validacao|V|Distinguir limite unilateral 1−α^(1/n) de limite bilateral 1−(α/2)^(1/n); regra de três apenas aproximada. Zero erros em 40 implica limites diferentes (~7,2% e ~8,8%), não certificação de erro zero.
Gatilhos de revisão e probabilidade de acionamento|P|P2|Equação|app:validacao|V|Regra e_v≥3, denominador, custo e P(Bin(n_v,p)≥3); distinguir regra de ação de teste de aceitação. Não agregar censos dirigidos e SRS numa taxa única.
Repetição, instabilidade e limites do recall|P|P2|Equação + algoritmo|app:validacao,app:protocolo-sr|V,VP|Taxas de flip canary e teste–reteste; M/S e gatilho M/S>0,10 ou M≥5 no snowballing, caso S=0 e fecho sem novos incluídos. São instrumentos diferentes; nenhum certifica recall global ou elimina erro humano.
'''),
('05', 'Regressão, estimação e modelos comparadores', 'sec:mat-regressao', r'''
Modelo linear, matriz de desenho e mínimos quadrados|C|P1|Equação + derivação|sec:enb-cadeia,sec:replicacao,sec:suficiencia|OLS,LIN|E=Xβ+ε, função objetivo, solução de mínimos quadrados, posto e identificabilidade; regressão anual com intercepto e unidade dos coeficientes. Distinguir algoritmo numérico de propriedades probabilísticas do estimador.
RSS, TSS, R² e R² fora do treino|C|P1|Equação + condições|sec:enb-cadeia,sec:replicacao,sec:poder-preditivo|OLS|Definir somas de quadrados e coeficiente de determinação, variância nula e possibilidade de R² negativo em avaliação. R² não exige normalidade para ser calculado e não mede calibração/deteção; distinguir R² centrado e não centrado.
Escala residual e graus de liberdade|C|P1|Equação|sec:replicacao,sec:metricas|OLS,DAX|Sigma residual=sqrt(RSS/(n−2)) na regressão simples consultada; generalização pelo posto p. Separar desvio residual, RMSE, escala robusta, escala cross-fit e escala de inovação. Verificar mínimos de cálculo versus mínimos de utilização.
Reta pela origem, constante e rácio específico|C|P1|Derivação curta|sec:corpus-a,sec:referencia-fixa|LIN|Média histórica, regressão com intercepto e OLS pela origem são comparadores distintos. Mostrar a_pela_origem=sum(QE)/sum(Q²), diferente de sum(E)/sum(Q) e da mediana de E/Q. Identificar os cinco normalizadores citados.
Modelos encaixados e valor incremental de covariáveis|T|P1|Equação|sec:suficiencia,sec:guidelines||Modelo Q e modelo Q+Z no mesmo treino e teste completos; transformação determinista API/densidade, redundância e multicolinearidade. Mais regressores reduzem RSS de treino sob o mesmo domínio, sem garantir melhoria temporal.
Huber, perda robusta e escala MAD|T|P1|Equação + algoritmo|sec:guidelines,sec:demo-robustos||Funções de perda e influência, constante 1,345, MAD e fator de consistência, atualização iterativa e convergência. Confirmar variante exata do código e distinguir robustez a resíduos extremos de resistência a alavancagem.
Theil–Sen e convenção do intercepto|T|P2|Equação + algoritmo|sec:guidelines,sec:demo-robustos||Mediana de declives entre pares com cargas distintas, empates, intercepto e escala residual. Conferir implementação exata antes de escrever; não chamar a todo o procedimento livre de pressupostos.
GAM, bases spline, penalização e graus de liberdade efetivos|C|P1|Equação + algoritmo|sec:verdade-conhecida|GAM|Modelo aditivo por funções suaves, bases e penalidade, hiperparâmetros escolhidos no treino, interação por produto tensorial. O GAM já participa na simulação, embora também apareça no roteiro futuro; documentar a variante citada.
Erro de medição, endogeneidade e causalidade|T|P1|Definição + exemplo|sec:suficiencia,sec:limitacoes||Explicitar regressão como associação condicional; erro na carga, variáveis omitidas, reação da operação e covariável mediadora. Uma equação de limitação basta; não acrescentar modelos causais ou correções não executadas.
'''),
('06', 'Avaliação temporal, perdas e comparação', 'sec:mat-avaliacao-temporal', r'''
Treino, aplicação e informação disponível|T|P1|Conjuntos + algoritmo|sec:protocolo-baselines,sec:poder-preditivo||Definir cinco pares anuais, corte de 2026, afinação interna e informação disponível no instante t. Separar aplicação à carga contemporânea observada de previsão ex ante e de validação independente da seleção metodológica.
Referências triviais e respetivos domínios|C|P1|Equação + algoritmo|sec:poder-preditivo|CFG|Média de treino, mesmo dia civil do ano anterior, média dos 30 dias civis anteriores; ano bissexto e janela completa. Para eletricidade, média mensal, mês homólogo e mês anterior; cada comparador pode ter população diferente.
MAE, RMSE, viés, NMBE e CV(RMSE)|T|P1|Equação + unidades|sec:assimetria-comparacao,sec:poder-preditivo||Fixar sinais e denominadores; métricas empíricas versus convenções de graus de liberdade em protocolos de M&V. Normalização pela média exige denominador admissível; as variantes normativas carecem de edição/cláusula antes de transcrição.
Diferença emparelhada de perdas e skill|T|P1|Equação + exemplo|sec:poder-preditivo,sec:suficiencia,sec:demo-robustos||Definir d_t=perda_comparador−perda_modelo, delta=média(d_t) e skill relativo; direção favorável, unidades e comparador com perda zero. Manter os mesmos dias por par; número de vitórias não equivale a ganho agregado.
Cross-fitting em blocos e estimação de escala|C|P1|Algoritmo|sec:protocolo-baselines,sec:referencia-fixa|REF|Seis blocos contíguos de 2020, reestimar nos restantes e reunir erros omitidos. Distinguir esta rotação da validação cronológica, buffers e famílias adaptativas; declarar condicionamento nos hiperparâmetros e suporte do ajuste de cada bloco.
Referência fixa, reajustes móveis e janela expansiva|T|P1|Equação + cronologia|sec:referencia-fixa||Formalizar que parâmetros/escala/estado ficam fixos, origens de refit e janelas de 6/12/24 meses. Resultados de lotes assinalados como não finais continuam pendentes; descrever desenho sem promover conclusões qualitativas inválidas.
Grelha de sensibilidade e mudança de estimando|T|P1|Conjuntos + algoritmo|sec:protocolo-baselines,sec:sintese-modos-falha||Produto de limiares e âncoras anuais; distinguir perturbação da seleção, mudança de período e variação Monte Carlo da semente. Reportar efeitos/IC além de rótulos; âncora julho–junho também muda meses incluídos no caso atual.
'''),
('07', 'Inferência sob dependência e multiplicidade', 'sec:mat-inferencia', r'''
Intervalos de confiança, hipóteses e valores p|T|P1|Definição + exemplo|sec:enb-cadeia,sec:protocolo-baselines,sec:limitacoes||Nível de confiança, hipótese nula, estatística e referência; erro tipo I, potência e precisão. Não rejeição difere de equivalência; intervalo largo que contém a referência não demonstra adequação.
Covariância HAC e kernel quadrático-espectral|C|P1|Equação + algoritmo|sec:protocolo-baselines,sec:estabilidade|INF,CFG|Matriz sandwich, produtos de scores por desfasamento civil, kernel QS, largura Andrews AR(1), correção finita e sensibilidades. Documentar tratamento de lacunas e condições da aproximação; HAC não corrige quebras arbitrárias.
Wald empilhado, contrastes de declive e nível|T|P1|Equação + algoritmo|sec:estabilidade||Desenho por interações ano×carga, matriz de restrições, W e graus de liberdade; famílias separadas de declive/nível. Mostrar predições a carga comum com incerteza; não interpretar intercepto extrapolado como carga térmica de base.
Benjamini–Hochberg, Benjamini–Yekutieli e FDR|T|P1|Equação + algoritmo|sec:protocolo-baselines,sec:estabilidade||Definir família, ordenação dos valores p, valores ajustados e FDR. Distinguir condições BH, proteção BY e inferência por contraste fora dessas famílias; contar IC individuais não cria uma conclusão simultânea.
Bootstrap de blocos móveis em calendário irregular|C|P1|Algoritmo + equação|sec:protocolo-baselines,sec:poder-preditivo|INF|Blocos candidatos definidos por duração civil, retendo observações disponíveis; sorteio, concatenação até n e truncagem final. O código consultado não exige que cada bloco tenha observações em todos os dias: documentar número variável de pontos por bloco.
Intervalos percentil, objeto reamostrado e condicionamento|T|P1|Equação + algoritmo|sec:protocolo-baselines,sec:calibracao||Quantis das réplicas, número B, semente e emparelhamento; perdas/indicadores de modelos fixos versus reestimação de treino. Não apresentar IC condicional como incerteza de todo o processo de construção e seleção.
Bootstrap residual sob hipótese nula|T|P1|Algoritmo|sec:estabilidade||Ajuste restrito, resíduos, blocos, reconstrução da resposta, reestimação e máximo de contrastes; esclarecer diferença de alvo relativamente ao bootstrap de perdas e critérios da rota alternativa de estabilidade.
Cobertura simulada de intervalos e erro Monte Carlo|T|P1|Equação + exemplo|sec:protocolo-baselines,sec:limitacoes|SIM|Cobertura empírica, Wilson/CP conforme objetivo, MCSE e incerteza finita; separar 400 réplicas de avaliação de 2 000 reamostragens. O ensaio 357/400 não demonstra cobertura nominal de 95% nem valida o bloco base a partir de bloco 60.
'''),
('08', 'Diagnóstico de resíduos, suporte e influência', 'sec:mat-diagnosticos', r'''
Diferença padronizada de médias|T|P1|Equação|sec:perfil-dados||Definir SMD e denominador de dispersão usados para retidos/removidos; sinais, módulo e variância quase nula. Separação estatística não identifica regime físico; confirmar fórmula no produtor dos resultados.
ACF, PACF e dimensão amostral efetiva|C|P1|Equação + algoritmo|sec:perfil-dados,sec:diagnosticos-desc|CFG|Desfasamentos civis exatos, pares disponíveis, PACF e convenções; dimensão efetiva apenas ilustrativa e específica do estimando. Dependência altera sequências e precisão, não implica automaticamente perda de cobertura marginal.
Durbin–Watson e Ljung–Box|C|P2|Equação + pressupostos|sec:diagnosticos-desc|CFG|Estatísticas e referências clássicas, lag civil versus linhas adjacentes, graus de liberdade ajustados. Reportar como contraste técnico quando a calibração inferencial não é defensável; um valor p inválido não se reabilita por se chamar descritivo.
Heterocedasticidade, Breusch–Pagan/Koenker e ARCH|C|P2|Equação + pressupostos|sec:diagnosticos-desc|CFG|Variância condicional, regressões auxiliares, estatísticas e lags; desvio móvel de 30 dias com mínimo de pontos. Diferenciar heterogeneidade com carga e dependência temporal dos quadrados dos resíduos.
Assimetria, curtose e diagnóstico de forma|C|P2|Equação|sec:diagnosticos-desc|CFG|Momentos normalizados, excesso de curtose com correção amostral, caudas e RESET com potência quadrática. Separar descrição marginal, forma da média e inferência; conferir eventual inclusão de testes de normalidade apenas no código.
Sazonalidade mensal e eta quadrado|C|P2|Equação|sec:diagnosticos-desc|CFG|Decomposição de variância entre/dentro de meses e eta²; efeito descritivo em dias disponíveis, com meses e denominadores. Não atribuir validade de ANOVA iid a séries dependentes.
Padronização, PCA e distância no espaço operacional|C|P2|Equação + algoritmo|sec:diagnosticos-desc|CFG|Z-scores com parâmetros de ajuste, matriz de covariância/correlação, autovetores e variância explicada; o código configura quatro componentes e agrupamento em três. Tornar explícita a transformação que precede os clusters.
k-means, DBSCAN e silhouette|C|P2|Equação + algoritmo|sec:diagnosticos-desc|CFG|Objetivo intra-cluster, centroides, distância, vizinhança/densidade e ruído; seleção de k e silhouette. Descrever parâmetros e estabilidade; grupos geométricos não equivalem a regimes operacionais.
KDE, sobreposição de densidades e suporte|C|P1|Equação + algoritmo|sec:diagnosticos-desc,sec:referencia-fixa|CFG,REF|Densidades por kernel, bandwidth Scott, integral do mínimo, intervalo min–max e suporte central. Diferenciar overlap marginal, caixa multivariada e região conjunta bem amostrada; quantificar fração fora do suporte.
Alavancagem, Cook e remoção de semanas|C|P2|Equação + algoritmo|sec:diagnosticos-desc|CFG|Diagonal da matriz de projeção, distância de Cook e limiar heurístico; refit omitindo semanas ISO, variação da previsão a cargas comuns e mudanças de sinal. Influência no declive quase nulo difere de impacto operacional grande.
Correlação entre vetores e simultaneidade|C|P1|Equação|sec:diagnosticos-desc,sec:verdade-conhecida|CFG,JOINT|Pearson, Spearman, amostra comum, padronização anual e número de vetores em excursão; lateralidade. Distinguir dependência de sinais, magnitude absoluta, causalidade e número de evidências independentes.
'''),
('09', 'Bandas, cobertura e regras de alarme', 'sec:mat-bandas', r'''
Intervalo da média, intervalo preditivo e banda de alarme|T|P1|Equação + exemplo|sec:metricas,sec:calibracao,sec:demo-bandas||Distinguir objeto aleatório, centro, largura e nível; explicar termo adicional de variância do erro numa predição individual e influência da carga. Banda constante não é automaticamente intervalo preditivo clássico.
Banda marginal normal e nominal 2 sigma|T|P1|Equação|sec:calibracao,sec:demo-bandas||Centro f(Q), limites ±2s, referência 2Φ(2)−1≈0,9545 e diferença de 95%. Declarar incerteza de parâmetros e escala; separar cobertura marginal de cobertura condicionada no passado.
Cobertura, excursões e intervalos da cobertura|T|P1|Equação + exemplo|sec:calibracao,sec:implicacoes-plataforma||Indicador de estar dentro da banda, n/N, excursões superior/inferior e IC MBB. Na mesma população, cobertura=1−fração fora; ambas exigem contexto externo para separar mudança real e defeito da banda.
Cobertura condicional e largura das bandas|T|P1|Equação|sec:calibracao,sec:demo-bandas,sec:referencia-fixa||Estratos por tercis de carga/semestre, cortes de treino, denominadores pequenos e meia-largura relativa. Comparar centro, população e nível; nitidez deve ser apreciada em conjunto com calibração.
Rajadas, episódios e regras de sequência|T|P1|Algoritmo|sec:metricas,sec:dashboard,sec:calibracao||Formalizar as oito regras efetivamente descritas, lado, limiares, comprimento, monotonia, alternância e sobreposição de janelas. Contar dias, violações e episódios separadamente; conferir convenção 8/9 pontos e regra de lacunas antes de chamar Nelson.
Resíduos AR(p), centro condicional e BIC|T|P1|Equação + algoritmo|sec:demo-bandas||Reta mais previsão AR dos resíduos; ordem 1–7 por BIC no treino, amostra comum de comparação, inovação e previsão a um passo. A rota muda o centro; o MAE do candidato completo tem de corresponder à mesma previsão.
Bandas de inovação e fallback marginal|T|P1|Equação + algoritmo|sec:demo-bandas||Limites gaussianos ou quantis empíricos das inovações; histórico admissível, desfasamentos exatos e fallback quando faltam lags. Publicar fração de dias em fallback e desempenho nas mesmas datas.
Regressão quantílica, perda assimétrica e não cruzamento|T|P1|Equação + algoritmo|sec:guidelines,sec:demo-bandas||Definir quantil condicional, pinball loss, dois quantis-alvo e regra de recusa por cruzamento. Distinguir rejeitar cruzamento de impor restrições; afinação, convergência e escassez de observações de cauda em janela anual.
Envelopes fixos e quantis móveis|T|P1|Equação + algoritmo|sec:referencia-fixa||Origem dos quantis e da escala em 2020; controlo de 90 dias anteriores com mínimo de 60 erros, disponibilidade e população comum. Separar envelope da referência e adaptação ao passado de aplicação.
'''),
('10', 'Critérios de aceitação e materialidade', 'sec:mat-aceitacao', r'''
Candidato, finalidade e decisão não estimável|T|P1|Definição + tabela|sec:guidelines,sec:demo-gate||Definir estimador, domínio, centro, banda e uso; enumerar oito combinações por vetor que produzem 32 decisões, sem sugerir fatorial completo. Separar NE, inconclusivo e rejeitado; normalizador, preditor e detetor precisam de alvos próprios.
Regra histórica quatro em cinco|T|P1|Equação + exemplo|sec:guidelines,sec:demo-gate||Indicadores de ganho e de compatibilidade de cobertura por par; duas somas ≥4 versus soma de sucessos conjuntos ≥4. A regra descrita pode ter só três pares com ambos; preservar resultado histórico e explicitar a diferença.
Compatibilidade, equivalência e não inferioridade|P|P1|Equação + pressupostos|sec:guidelines,sec:limitacoes||Separar regra já usada de proposta futura com margens materiais, precisão mínima e inconclusão. IC que contém nominal não prova calibração; margens carecem de definição anterior à nova avaliação e não serão escolhidas para aprovar candidatos.
Potência, erros de decisão e dependência entre pares|P|P1|Equação + desenho|sec:demo-gate,sec:limitacoes||Avaliar aceitação/rejeição sob cenários declarados, com dependência dos pares e seleção de candidatos. Cinco transições não são cinco ensaios Bernoulli independentes por construção; análise de custo/benefício continua futura.
'''),
('11', 'Referência, estado e monitorização sequencial', 'sec:mat-monitorizacao', r'''
Resíduo, excesso positivo e acumulado líquido|T|P1|Equação + derivação|sec:metricas,sec:dashboard||e=observado−referência; soma(e), soma(max(e,0)), ritmo por dia e Pareto. Excesso positivo cresce com ruído mesmo com erro centrado; não é estimador de desperdício ou poupança. Somar inclui exposição e fronteiras.
Referência congelada, estado e inovação|T|P1|Equação + esquema|sec:leitura-integrada,sec:referencia-congelada||Separar f_ref(X), r_ref, estado previsto/filtrado e inovação; a informação que cada canal conserva. Distinguir escala residual, escala da referência, erro do estado e variância de inovação.
Espaço de estados e filtro de Kalman|C|P1|Equação + algoritmo|sec:referencia-fixa,sec:verdade-conhecida|STATE|Equações de observação/transição, nível e eventual tendência, ruídos de processo/medição, previsão, ganho e atualização; estado inicial, parametrização e passos civis com lacunas. Transcrever só famílias efetivamente citadas.
Monitor de resíduo e lateralidade|C|P1|Equação|sec:verdade-conhecida|MON|Estatística z ou módulo de z, limiar e conjunto pontuável; unilateral superior versus bilateral. O vapor líquido de 10 bar requer a lateralidade declarada; sinal de consumo não pode ser perdido por normalização percentual.
CUSUM tabular, estado e reinício|C|P1|Equação + algoritmo|sec:detetabilidade,sec:verdade-conhecida|MON|Recorrências S+ e S− com k, limiar h e estado inicial. Na Parte C consultada usa resíduos padronizados, conserva estado em dia não pontuável e não reinicia após cruzamento; distinguir do CUSUM sobre inovações planeado em E5.
Monitores de carga, estratos e escala|T|P1|Equação + algoritmo|sec:verdade-conhecida|MON,STATE|Definir estatística que reage a mudança de resposta à carga e a alargamento da dispersão; regressão local/estratos, janelas, mínimos, normalização e lateralidade. Não reduzir a designação genérica canais de carga e escala.
Preservação de sinal e projeção do reajuste|T|P1|Derivação + algoritmo|sec:sintese-modos-falha,sec:referencia-fixa||Definir controlo/injetado, canal, janela e denominador. Para OLS no mesmo desenho, diferença residual=(I−H)δ; degrau uniforme pode estar no espaço do intercepto, mas mudança parcial não desaparece universalmente.
Branqueamento e atenuação de uma mudança|T|P1|Derivação curta|sec:verdade-conhecida||Distinguir filtro AR fixo e filtro adaptativo; para AR(1), contribuição do sinal na inovação é δ_t−ρδ_(t−1). Não equiparar atenuação de inovação a impossibilidade de deteção por monitor sequencial.
Estados operacionais da baseline e transições|P|P2|Algoritmo + esquema|sec:implicacoes-plataforma||Alarme, investigação, suspensão, recalibração e verificação; separar evento de estado persistente, fora de domínio e não pontuável. Anexo G define regra matemática; manual E guarda operação, responsabilidades e aprovação.
'''),
('12', 'Simulação, falsos sinais e detetabilidade', 'sec:mat-simulacao', r'''
Gerador de dados e verdade conhecida|T|P1|Equação + algoritmo|sec:verdade-conhecida||Relação de referência, covariáveis fixas/reamostradas, treino, aplicação, máscara, instante inicial do desvio e cenários. Separar gerador linear, bancos não lineares e factos observados da refinaria.
Ruído AR(1) com variância marginal fixa|C|P1|Equação + derivação|sec:verdade-conhecida|SIM|ε_t=ρ ε_(t−1)+σ_marg sqrt(1−ρ²) ξ_t, inicialização estacionária e simulação em todos os dias, incluindo ocultos. Aumentar ρ preserva dispersão marginal nesta construção e altera memória.
Degrau, rampa, recuperação, carga e escala|T|P1|Equação + desenho|sec:referencia-fixa,sec:verdade-conhecida||Amplitude em unidades da escala, onset, duração, plateau, sentido e retorno; alternativas multiplicativas para variância ou interação com carga. Separar injeção em dados reais e geração sintética completa.
Calibração de limiar por horizonte|T|P1|Equação + algoritmo|sec:verdade-conhecida||Probabilidade de pelo menos um sinal sob H0 durante H dias versus taxa diária e ARL0; máximo de trajetória, limiar, quantis discretos e réplicas separadas de calibração/verificação. Declarar orçamento por canal e sistema.
Probabilidade de deteção, atraso e censura|T|P1|Equação|sec:detetabilidade,sec:verdade-conhecida||Tempo do primeiro cruzamento após onset, dias civis versus pontuáveis, deteção até H e não deteções censuradas. ARL0 e atraso condicional só aos detetados são quantidades diferentes; não usar uma pela outra.
Desvio mínimo detetável e curva de potência|T|P1|Equação + algoritmo|sec:verdade-conhecida||Amplitude para atingir probabilidade-alvo (50% no relato), grelha, interpolação/monotonicidade, IC da curva e censura aberta quando não há cruzamento. Converter em percentagem apenas com referência positiva admissível; não aplicar a fluxo líquido com sinal.
Contrastes emparelhados por réplica e MCSE|T|P1|Equação + algoritmo|sec:verdade-conhecida||Diferença dos indicadores de deteção dentro da mesma réplica, média e MCSE=sd(diferenças)/sqrt(R); bootstrap por réplica independente. Distinguir esta reamostragem iid do MBB temporal; separar oito co-primárias e secundárias.
Ruído multivariado, coocorrência e deteção conjunta|C|P1|Equação + algoritmo|sec:diagnosticos-desc,sec:verdade-conhecida|JOINT|Matriz de correlação/covariância, eventual regularização, inovações correlacionadas, regra conjunta e lateralidade. Calibrar orçamento conjunto; correlação negativa não impede excursões bilaterais simultâneas.
Agregação temporal e correlações em acumulados|T|P1|Derivação + simulação|sec:verdade-conhecida||Somas semanais/mensais e acumulados preservando calendário; variância da soma inclui autocovariâncias. Mostrar mecanismo e distribuição entre réplicas, sem transformar uma realização com R² alto em teorema universal.
Stress, máscaras e âmbito de generalização|T|P1|Desenho + algoritmo|sec:verdade-conhecida,sec:limitacoes||Sensibilidade a ρ, dimensão, máscara, não linearidade e tipo de desvio; comparação justa mantém denominadores/orçamentos declarados. Lotes com populações ou calendário incorretos não suportam sequer ordenações qualitativas finais.
'''),
]

ROWS = []
for number, title, label, raw in GROUPS:
    for index, entry in enumerate(raw.strip().splitlines(), 1):
        fields = entry.split('|')
        assert len(fields) == 7, (number, entry)
        concept, status, priority, depth, origins, sources, detail = fields
        ROWS.append(dict(id=f'M{number}.{index:02}', bloco=f'G.{int(number)}',
                         secao=title, label_proposto=label, conceito=concept,
                         estado=status, prioridade=priority, profundidade=depth,
                         origens=origins, fontes_apoio=sources, desenvolver=detail))

def source_link(key):
    path, needle = SOURCES[key]
    line = next(i for i, s in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1) if needle in s)
    return f'[{key}](<{path}:{line}>)'

def origin_link(label):
    file, line = LABELS[label]
    chapter = re.search(r'chapter-(\d)', file.name)
    short = f'Cap. {chapter[1]}' if chapter else 'Ap. ' + file.name.split('-')[1]
    return f'[{short} · {label}](<{file}:{line}>)'

for row in ROWS:
    for label in row['origens'].split(','):
        assert label in LABELS, (row['id'], label)
    for key in filter(None, row['fontes_apoio'].split(',')):
        assert key in SOURCES

with (OUT / 'inventario.csv').open('w', encoding='utf-8-sig', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=list(ROWS[0]))
    writer.writeheader()
    writer.writerows(ROWS)

HEADER = r'''# Mapa dos conceitos matemáticos da tese

**Versão de trabalho — 15 de setembro de 2026.** Objetivo: desenhar um anexo transversal que permita remissões precisas a partir de toda a dissertação. Este é um levantamento editorial fundamentado nos ficheiros atuais, não a redação final do anexo nem uma validação dos resultados.

## 1. Proposta de organização

Recomenda-se ampliar o atual **«Definições matemáticas dos instrumentos de avaliação»** para **«Fundamentos e formulações matemáticas da dissertação»**, conservando o identificador `app:matematica`. A sequência começa nas grandezas e nos dados, passa pela revisão e pela modelação e termina na monitorização e na simulação.

O corpo da tese deve conservar a definição operacional, a equação essencial, a unidade e o critério necessário para compreender o resultado. O anexo recebe a derivação, os pressupostos, as variantes, os casos-limite e o pseudocódigo. Uma remissão não pode substituir a definição daquilo que se mede.

**Cobertura desta primeira passagem:** os oito capítulos ativos e os apêndices A–G, identificados em `0-Config/4_files.tex`; consulta dirigida dos protocolos atuais da revisão, de módulos de bibliometria, de configuração/implementação estatística e da extração M/DAX. Não foram tratados como capítulos ativos os ficheiros de exemplo, a proposta alternativa de estilo do Cap. 3, cópias de revisão ou o apêndice H desativado.

As Secções 2.4/2.5, 3.4/3.5, o Cap. 8 e os apêndices ainda têm partes em esqueleto. A completude do mapa é relativa à versão atual: conceitos que surgirem quando essas partes forem escritas terão de ser acrescentados. A consulta ao código foi dirigida, sem reexecução dos estudos e sem auditoria integral dos lotes canónicos.

### Como ler o inventário

- **T — texto:** conceito efetivamente usado ou discutido no corpo ativo; a formulação pode ainda estar por verificar.
- **C — código consultado:** a consulta dirigida à implementação/configuração esclareceu o conceito ou a convenção. Não significa correspondência já auditada com o lote citado pela tese.
- **P — previsto:** consta de protocolo, comentário de revisão ou conteúdo ainda a desenvolver. Não é tratado como resultado executado.
- **P1:** necessário para interpretar um resultado, evitar uma ambiguidade substantiva ou reproduzir uma operação central.
- **P2:** aprofundamento técnico ou diagnóstico de apoio. A prioridade é de escrita, não a gravidade de um erro.

Uma entrada pode agrupar conceitos inseparáveis na exposição; a contagem não pretende contar objetos matemáticos atómicos. Os códigos `M01.01`, etc., são identificadores do mapa. Os `sec:mat-*` abaixo são **labels propostos, ainda não inseridos na tese**. Todas as ligações de origem apontam para labels que existem na versão lida; as linhas são uma fotografia desta data.

'''

text = HEADER
text += f'**Inventário: {len(ROWS)} entradas, em {len(GROUPS)} blocos.** '
counts = Counter(r['estado'] for r in ROWS)
text += '; '.join(f'{n} em estado {s}' for s, n in sorted(counts.items())) + '.\n\n'
text += '| Secção proposta | Conteúdo | Entradas | Label proposto |\n|---|---|---:|---|\n'
for number, title, label, _ in GROUPS:
    text += f'| G.{int(number)} | {title} | {sum(r["bloco"] == f"G.{int(number)}" for r in ROWS)} | `{label}` |\n'

text += r'''
### Relação com os restantes apêndices

| Local | Responsabilidade editorial |
|---|---|
| Corpo principal | Pergunta, equação essencial, população, resultado, interpretação e limite. |
| G — Matemática | Definições reutilizáveis, equações completas, pressupostos, algoritmos e casos-limite. |
| A — Protocolo da revisão | Estratégia literal, cronologia, emendas e regras de seleção; remete para G para a matemática dos conjuntos/indicadores. |
| B — Validação da extração | Desenho efetivamente executado, adjudicação, denominadores e resultados da auditoria; remete para G para amostragem e intervalos. |
| C — Dicionário | Tags/campos, unidades, fatores, fontes, vigência e fronteiras concretas. As fórmulas comuns ficam em G; não as manter duplicadas em versões divergentes. |
| D — Tabelas | Resultados completos, amostras, sensibilidades e proveniência. G explica como se calculam, D mostra quanto deram. |
| E — Manual | Utilização da plataforma, filtros, ações e estados; remete para G nas regras de cálculo. |
| F — Revisão adversarial | Decisões e alterações de metodologia. Métodos substituídos ficam documentados aqui/B, sem regressarem ao núcleo matemático ativo. |

O projeto configura G como `appendix` e não usa `annex`. Convém uniformizar a designação portuguesa «Apêndice»/«Anexo» na revisão editorial; o identificador pode manter-se em qualquer opção.

## 2. Inventário com origem e conteúdo a desenvolver

'''
for number, title, label, _ in GROUPS:
    text += f'### G.{int(number)} — {title}\n\nDestino proposto: `{label}`.\n\n'
    text += '| ID · estado · prioridade | Conceito e profundidade | Origem | Conteúdo a desenvolver |\n|---|---|---|---|\n'
    for row in (r for r in ROWS if r['bloco'] == f'G.{int(number)}'):
        origins = '<br>'.join(origin_link(l) for l in row['origens'].split(','))
        supporting = ' '.join(source_link(k) for k in filter(None, row['fontes_apoio'].split(',')))
        if supporting:
            origins += '<br>Apoio: ' + supporting
        text += f'| **{row["id"]}** · {row["estado"]} · {row["prioridade"]} | **{row["conceito"]}**<br>{row["profundidade"]} | {origins} | {row["desenvolver"]} |\n'
    text += '\n'

TAIL = r'''
## 3. Mapa de remissões por capítulo

| Zona do texto | Remissão principal | O que deve continuar no corpo |
|---|---|---|
| Cap. 1 — problema, objetivos e âmbito | G.1, G.6 e G.11, só quando indispensável | Separação entre referência, previsão e deteção; âmbito das afirmações. Evitar sobrecarregar a introdução com notas técnicas. |
| Cap. 2 — EnPI/EnB e tipologia | G.2 e G.5 | Rácio versus modelo ajustado; consumo esperado versus ótimo; fronteira e variáveis. |
| Cap. 2 — critérios normativos | G.6 e G.7 | Nome da métrica, sentido, edição, via de aplicação e limiar discutido. A matemática não resolve por si a exatidão das afirmações normativas. |
| Cap. 2 — processo/CDU | G.2 | Esquema físico, fronteira material/energética e hipótese de mecanismo. |
| Cap. 3 — corpora, recuperação e contagens | G.3 | Unidade publicação, conjunto usado e denominador de cada número. |
| Cap. 3 — auditoria da extração | G.4, articulado com B | Procedimento executado, referência humana, campos e publicações verificados. |
| Cap. 3 — redes e tópicos | G.3 | Significado de nó/aresta, peso e recorte; nomear TF–IDF/NMF se os resultados entrarem. |
| Cap. 4 — ingestão, reconciliação e métricas | G.1 e G.2 | Equações de conversão, unidades, bruto/líquido, seleção e rácio de totais. |
| Cap. 4 — protocolo estatístico | G.5–G.10 e G.12 | Tabela de estimandos, cronologia, comparadores, IC, famílias e critérios. |
| Cap. 5 — validação dos dados | G.1 | Regra de tolerância com unidade, denominador e estatuto de casos vazios. |
| Cap. 5 — dashboard | G.2, G.9 e G.11 | Sinal do desvio, referência selecionada, janela, significado de excesso/alarme. |
| Cap. 6 — replicação e perfil | G.1, G.5 e G.8 | Modelo anual, n, escala residual, filtros e domínio observado. |
| Cap. 6 — perdas, estabilidade e cobertura | G.6, G.7 e G.9 | Delta com sinal favorável, hipótese de igualdade, cobertura n/N e sensibilidade que altera a conclusão. |
| Cap. 6 — covariáveis e diagnóstico | G.5 e G.8 | Conjunto Z, amostra comum e interpretação estritamente delimitada. |
| Cap. 7 — candidatos e aceitação | G.5, G.9 e G.10 | Definição completa do candidato e regra histórica com limites; equação do centro AR. |
| Cap. 7 — referência e simulação | G.6, G.11 e G.12 | Esquema referência→resíduo→estado/inovação→monitor; equação do gerador, orçamento de falso sinal e definição de deteção. |
| Cap. 8 — roteiro | Apenas secções que já expliquem componentes usados; outros conceitos condicionais | Ligação falha→opção→dados→critério. Não introduzir uma cadeia de modelos supostamente necessária. |

### Estratégia de referência no texto

Remeter para a **subsecção ou equação concreta**, em vez de repetir apenas «ver Anexo G». Reservar nota de rodapé para um esclarecimento secundário; usar remissão no próprio texto quando o detalhe sustenta a interpretação do resultado. Usar `\ref` para referências internas e `\cite` para fontes bibliográficas; o anexo não substitui a citação original do método.

Exemplos para inserir **depois de as secções existirem**:

```latex
O consumo específico é calculado pelo rácio dos totais nos mesmos
dias operacionais; a relação com a média ponderada dos rácios diários
é apresentada na Secção~\ref{sec:mat-energia}.

Os intervalos são obtidos por reamostragem de blocos de dias civis,
com o algoritmo e o condicionamento descritos na
Secção~\ref{sec:mat-inferencia}.

O excesso positivo acumulado é uma estatística descritiva do desvio.\footnote{
As diferenças entre excesso positivo, desvio líquido e CUSUM de deteção
são formalizadas na Secção~\ref{sec:mat-monitorizacao}.}
```

Na redação, subdividir os labels largos acima em destinos como `sec:mat-gne`, `sec:mat-consumo-especifico`, `sec:mat-mbb`, `sec:mat-wald-hac`, `sec:mat-cusum` e `sec:mat-mdd`. A numeração de G.1–G.12 é proposta; as remissões não devem codificar os números à mão.

## 4. Notação a fixar antes de escrever

| Objeto | Proposta | Atenção |
|---|---|---|
| Dia, ano, unidade e vetor | t, y, u, v | Data civil não é posição da linha depois de filtrar. |
| Carga processada | Q_t, em kt/d | Manter conversão explícita de limiar dado em t/d. |
| Energia equivalente diária | E_t, em t GNE/d | Distinguir quantidade no dia de caudal; somas de taxas exigem a duração adotada. |
| Calor/dever térmico | H_t ou dot(H)_t, a escolher | Evitar Q, já usado para carga. |
| Densidade da carga | rho_carga,t | Reservar rho_e para autocorrelação; verificar densidade absoluta versus relativa. |
| Variáveis explicativas e padrão estatístico | x_t=(1,Q_t,Z_t), z_t para resíduo padronizado | Z vetorial e z escalar precisam de distinção tipográfica. |
| Coeficientes anuais | beta_y=(b_y,a_y,gamma_y) | a em t GNE/kt quando Q está em kt/d; não sobra /d. |
| Erro do modelo e resíduo calculado | epsilon_t e e_t | O primeiro não é observado; o segundo depende do modelo ajustado. |
| Escalas | s_OLS, s_MAD, s_ref, s_inov | «Sigma» isolado deixa de chegar quando há quatro construções. |
| Cobertura e probabilidade de sinal | c; p_FA,H | Diferenciar nível nominal da banda e confiança do IC de cobertura. |
| Estado e inovação | ell_(t|t−1), ell_(t|t), nu_t | Explicitar informação disponível antes e depois da observação. |
| CUSUM, constante de referência e limiar | S_t^+, S_t^−; k; h | Não confundir com soma simples dos resíduos. |
| Réplicas de simulação e de bootstrap | R e B_boot | Separar 400 trajetórias de 2 000 reamostragens; Corpus B usa contexto distinto. |

Esta notação é uma proposta editorial, não uma renomeação já aplicada ao código. A lista de símbolos da tese ainda contém exemplos do template; deve ser preenchida em conjunto com o anexo, depois de fechar as convenções.

## 5. Pontos que precisam de resolução antes de fechar o anexo

### 5.1 Verificações reveladas pela consulta desta sessão

1. **Tolerância de replicação:** `within_tolerance` usa `abs(local−produção) <= atol + rtol*abs(produção)`, com ambos os parâmetros a 10⁻⁶ na configuração consultada. A frase «tolerância de 10⁻⁶» é incompleta. A tolerância da reconciliação de dados descrita no Cap. 5 é outro operador, o máximo de dois limites.
2. **Mínimo de observações:** o texto declara um parâmetro de 30 observações; a tabela DAX exportada consultada calcula os coeficientes a partir de 3, e a função de replicação também. Confirmar onde 30 bloqueia utilização/apresentação ou se a descrição está errada; não alterar o número por inferência.
3. **MBB e lacunas:** a rotina atual sorteia janelas de duração civil com número variável de observações; não exige blocos totalmente preenchidos. Concatenar esses blocos e truncar em n não é a mesma coisa que reamostrar apenas segmentos completos. Confirmar a versão usada por cada lote antes de formalizar.
4. **Escala residual:** a replicação consultada usa n−2. A Parte C acrescenta escala por cross-fitting; a simulação AR(1) mantém a variância marginal através do fator sqrt(1−rho²). São três definições que não podem aparecer como um único sigma.
5. **CUSUM da Parte C:** usa o resíduo padronizado da referência; não reinicia após cruzamento e transporta o estado nos dias não pontuáveis. O protocolo E5 planeia CUSUM de inovações e menciona ARL0. Exigem descrições distintas, com estatuto executado/previsto.
6. **Bibliometria:** a exploração de tópicos é TF–IDF/NMF e a deteção de comunidades usa modularidade gulosa; a contagem aluvial é fracionada. Não basta colocar «redes bibliométricas» no índice matemático.
7. **Protocolo da revisão:** a versão C-2.3 separa SRS por artigo, erro por campo, censos e gatilhos; substitui métodos anteriores. O anexo deve explicar o protocolo atual e manter as alternativas abandonadas no histórico.
8. **Conversões do dashboard:** o canal de tags consultado agrega caudal e PCI separadamente antes do produto. O EII da CDU envolve conversões, um logaritmo e uma função por partes. A origem física dos fatores e a conformidade com Solomon ainda precisam de confronto documental.

Estas verificações dizem respeito aos ficheiros consultados nesta data. Não certificam que o código corrente corresponde aos commits que produziram cada resultado citado em agosto/setembro.

### 5.2 Questões já assinaladas na revisão da tese, que o desenho do anexo deve resolver

- **Nominais distintos:** 0,954, 0,9545 e 0,95 não devem alternar sem explicação; separar referência gaussiana de ±2 sigma, banda de 95% e IC de 95%.
- **Centro AR e critério:** a previsão reta+AR difere da reta anual; a avaliação do candidato tem de corresponder ao centro efetivamente usado.
- **Regra 4/5:** esclarecer dois sucessos marginais versus sucesso conjunto; compatibilidade pelo IC não significa calibração demonstrada. O anexo deve preservar a regra histórica e identificar qualquer sucessora como proposta.
- **Dependência e cobertura:** autocorrelação não implica por si só má cobertura marginal; não rejeição não é equivalência; ausência de eventos impede identificar falsos alarmes reais.
- **Calendário e suporte:** separar datas civis de linhas retidas, suporte marginal de conjunto, população de cada modelo de população comum e validação fora do treino de avaliação independente da escolha metodológica.
- **Energia, excesso e eficiência:** fronteiras, saldo líquido, carga reprocessada e denominadores percentuais têm consequências matemáticas. Excesso positivo não é poupança; referência histórica não é ótimo.
- **Lotes não finais:** a redação de G.6/G.11/G.12 deve distinguir desenho pretendido, algoritmo corrigido e resultados efetivamente republicados. O mapa não resolve essa pendência.

## 6. Conteúdo condicional e conteúdo a deixar fora

| Conceito | Decisão nesta fase |
|---|---|
| ARMA e modelos de estado mais gerais | Explicar a variante já usada quando necessária ao Cap. 7. Deixar o restante como roteiro, sem derivação enciclopédica. |
| Ridge polinomial, interações e modelos não lineares adicionais | Existem no código consultado/localizado, mas não estão identificados individualmente no relato corrente. Acrescentar ao núcleo apenas se os respetivos resultados passarem a integrar a tese; não inferir uso a partir da existência de um módulo. |
| Pooling parcial e modelos hierárquicos multiunidade | Só roteiro do Cap. 8; definição curta se permanecer no texto, sem apresentar como executado. |
| Grey-box, modelos de fouling e estado físico de degradação | Só proposta futura; os balanços físicos básicos necessários ao caso CDU entram em G.2. Não introduzir cinética de fouling, pinch ou exergia sem uso efetivo na tese. |
| Mann–Kendall corrigido e Pettitt | Surgem como trabalho futuro de eventos na configuração; não os listar como testes executados no diagnóstico. |
| Cohen κ, PABAK, AC1, captura–recaptura e índice composto de erro residual | Substituídos no protocolo da revisão. Podem merecer uma nota justificativa no histórico, não um capítulo de métodos ativos. |
| F1 e métricas de classificação | Só se forem reportadas em componente ativa. A auditoria atual define erro por campo e não as usa como substituto. |
| Reconciliação estatística por mínimos quadrados sujeita a balanços | Não foi identificada no método descrito; harmonização de fontes não autoriza atribuir esta técnica à plataforma. |
| Testes de equivalência, limites de materialidade e custo/benefício | Propostas de desenvolvimento. Formalizar o desenho após fixar margens/objetivos, sem recalcular o estudo atual para obter aprovação. |
| Funções hash e pormenores de publicação de corridas | Proveniência em C/F e documentação técnica. Basta explicar no corpo o que a verificação garante; não é necessário ensinar criptografia no anexo matemático. |

## 7. Modelo de cada unidade do anexo

Cada subseção deve poder ser lida isoladamente, com sete elementos curtos:

1. **Finalidade e uso na tese:** a pergunta que o instrumento responde.
2. **Entradas, população e notação:** unidades, calendário, critérios de elegibilidade e informação disponível.
3. **Definição ou equação:** fórmula com cada termo definido; mostrar a derivação só quando esclarece uma distinção importante.
4. **Pressupostos e casos-limite:** denominador zero, falta de suporte, não convergência, dependência ou amostra insuficiente.
5. **Algoritmo e convenções:** para procedimentos que uma equação isolada não reproduz; parâmetros no treino, tratamento de lacunas e reestimação.
6. **Interpretação e limites:** o que o número permite e não permite concluir.
7. **Fonte e ligação à implementação:** referência metodológica original, edição/variante e função/configuração/lote correspondente. Código não substitui fundamento científico e referência teórica não identifica a variante implementada.

Pseudocódigos prioritários: **um par anual de treino–aplicação**, **MBB em calendário com lacunas**, **auditoria por campo**, **construção de banda AR**, **referência/estado/CUSUM** e **uma réplica de simulação com calibração separada**.

## 8. Ordem recomendada de redação

1. **Fixar as convenções transversais:** notação, unidade, sinal, calendário, população, escala e nominal. Resolver as divergências identificadas em 5.1 antes de as cristalizar em equações.
2. **Escrever G.1/G.2 e o núcleo G.5/G.6:** os dados, a energia e o modelo que geram os números. Isto dá suporte também aos Caps. 2, 4 e 5.
3. **Escrever G.3/G.4:** matemática da bibliometria e da auditoria segundo C-2.3, identificando o que já foi executado e o que ainda está previsto.
4. **Escrever G.7/G.9/G.10:** inferência, bandas e regra de aceitação, sem transferir para o anexo as interpretações incorretas já marcadas no corpo.
5. **Escrever G.11/G.12 e completar G.8:** referência, monitores, simulação e diagnósticos de apoio, após confrontar variantes e lotes.
6. **Inserir remissões específicas no corpo:** rever redundância, completar símbolos e verificar links/compilação. Só nessa fase alterar o atual G e o texto que o cita.

**Critério de fecho do mapa:** cada fórmula, transformação quantitativa, métrica ou algoritmo referido na versão final da tese tem um destino identificado ou uma justificação explícita para ficar fora. Cada resultado tem população, escala, comparador e regra de incerteza rastreáveis. Não é necessário reproduzir funções completas nem formalizar matemática elementar sem aplicação.

## 9. Ficheiros e verificação desta entrega

- `mapa-conceitos.md`: proposta de índice, inventário comentado, remissões, notação e pendências.
- `inventario.csv`: o mesmo inventário em formato filtrável por bloco, estado, prioridade e origem.
- `manifesto.json`: hashes dos ficheiros da tese lidos e dos apoios consultados, para identificar a fotografia documental.
- `construir_mapa.py`: gera o mapa e verifica a existência dos labels/ficheiros de origem; não altera capítulos, apêndices ou resultados.

As referências de apoio abaixo são locais e servem a rastreabilidade do levantamento. A bibliografia matemática do anexo final ainda deve ser conferida contra as fontes primárias e variantes utilizadas; esta sessão não fez uma revisão bibliográfica nova nem verificou normas e documentação Solomon.

'''
text += TAIL
text += '| Código | Fonte local |\n|---|---|\n'
for key in SOURCES:
    text += f'| {key} | {source_link(key)} — `{SOURCES[key][0].name}` |\n'
(OUT / 'mapa-conceitos.md').write_text(text)

all_sources = sorted(set(SOURCE_FILES + [ROOT / '0-Config/4_files.tex', ROOT / '1-FrontMatter/symbols.tex'] + [p for p, _ in SOURCES.values()]))
manifest = {
    'date': '2026-09-15',
    'scope': 'Mapa editorial; consulta dirigida; sem reexecução de estudos ou edição da tese.',
    'entries': len(ROWS), 'groups': len(GROUPS), 'status_counts': dict(counts),
    'sources': [{ 'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                 'bytes': p.stat().st_size } for p in all_sources],
    'checks': {'all_origin_labels_exist': True, 'all_support_files_exist': True,
               'unique_entry_ids': len({r['id'] for r in ROWS}) == len(ROWS)},
}
(OUT / 'manifesto.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'entries':len(ROWS), 'groups':len(GROUPS), 'status_counts':dict(counts), 'markdown_bytes':len(text.encode()), 'path':str(OUT / 'mapa-conceitos.md')}, ensure_ascii=False))
