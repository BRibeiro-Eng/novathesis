import sys,io,re
ROOT=sys.argv[1]
def patch(path,pairs):
    s=open(path,encoding="utf-8").read()
    for old,new in pairs:
        n=s.count(old)
        assert n==1,(path,n,old[:70])
        s=s.replace(old,new)
    open(path,"w",encoding="utf-8").write(s)
    print(path.split('/')[-1],len(pairs),"inserções")

C4=[
("A plataforma é um modelo tabular em esquema em estrela, em modo de\nimportação,",
 "A plataforma é um modelo tabular em esquema em estrela~\\cite{KimballRoss2013}, em modo de\nimportação,"),
("o modelo estima por mínimos quadrados a relação\n$E = a\\,Q + b$ entre o consumo diário",
 "o modelo estima por mínimos quadrados a relação\n$E = a\\,Q + b$ (o modelo estatístico de \\emph{baseline} que a ISO~50006\ntipifica~\\cite{ISO50006_2014}) entre o consumo diário"),
("(o gráfico de CUSUM do\n\\emph{dashboard})","(o gráfico de CUSUM~\\cite{Page1954} do\n\\emph{dashboard})"),
("painel de regras de carta de controlo verifica oito regras clássicas\nsobre os resíduos padronizados",
 "painel de regras de carta de controlo verifica oito regras clássicas de\ncausas especiais, na linha das de Nelson~\\cite{Nelson1984}, sobre os resíduos padronizados"),
("O protocolo foi escrito\nantes de qualquer execução --- perguntas,",
 "O protocolo foi escrito\nantes de qualquer execução, no sentido do pré-registo~\\cite{Nosek2018} --- perguntas,"),
("do ano anterior e média móvel de trinta dias como secundários), medido\npela diferença emparelhada de perda absoluta diária;",
 "do ano anterior e média móvel de trinta dias como secundários~\\cite{HyndmanKoehler2006}), medido\npela diferença emparelhada de perda absoluta diária~\\cite{DieboldMariano1995,HarveyLeybourneNewbold1997};"),
("por um teste de Wald sobre uma regressão empilhada com\ninterações ano$\\times$carga;",
 "por um teste de Wald sobre uma regressão empilhada com\ninterações ano$\\times$carga, na linha do teste de Chow~\\cite{Chow1960};"),
("erros-padrão\nrobustos à heterocedasticidade e à autocorrelação (\\emph{kernel}\nquadrático-espectral com largura de banda de Andrews) para os testes de\nigualdade,",
 "erros-padrão\nrobustos à heterocedasticidade e à autocorrelação~\\cite{NeweyWest1987}\n(\\emph{kernel} quadrático-espectral com largura de banda de\nAndrews~\\cite{Andrews1991}) para os testes de igualdade,"),
("e intervalos percentil por \\emph{bootstrap} de blocos móveis\n--- bloco base de $\\lceil n^{1/3}\\rceil$ dias com desfasamentos civis\nexatos,",
 "e intervalos percentil~\\cite{Efron1979,EfronTibshirani1993} por\n\\emph{bootstrap} de blocos móveis~\\cite{Kunsch1989,Lahiri2003} --- bloco\nbase de $\\lceil n^{1/3}\\rceil$ dias~\\cite{HallHorowitzJing1995} com\ndesfasamentos civis exatos,"),
("(Benjamini--Hochberg, com\nBenjamini--Yekutieli como verificação)",
 "(Benjamini--Hochberg~\\cite{BenjaminiHochberg1995}, com\nBenjamini--Yekutieli~\\cite{BenjaminiYekutieli2001} como verificação)"),
("o resultado foi adjudicado por teste binomial exato depois de\nconhecido",
 "o resultado foi adjudicado por teste binomial exato~\\cite{ClopperPearson1934}\ndepois de conhecido"),
("foi substituída, por decisão datada, por\nvalidação temporal encadeada, porque 2025 já tinha informado o\ndiagnóstico",
 "foi substituída, por decisão datada, por\nvalidação temporal encadeada~\\cite{Tashman2000,BergmeirHyndmanKoo2018},\nporque 2025 já tinha informado o diagnóstico"),
("escala (por validação cruzada em seis blocos contíguos) e o seu estado",
 "escala (por validação cruzada em seis blocos contíguos~\\cite{BergmeirHyndmanKoo2018})\ne o seu estado"),
("qualquer número citado nesta dissertação tem de poder ser refeito, e tem\nde ser possível provar que não foi editado depois de produzido.",
 "qualquer número citado nesta dissertação tem de poder ser refeito, e tem\nde ser possível provar que não foi editado depois de\nproduzido~\\cite{Peng2011,Sandve2013}."),
]
C7=[
("A ISO~50001 obriga a monitorizar, medir e analisar o desempenho energético;\na ISO~50006 operacionaliza-o em indicadores e \\emph{baselines}, com variáveis\nrelevantes, fatores estáticos e normalização; a ISO~50015 e o IPMVP tratam\nda medição e verificação de poupanças.",
 "A ISO~50001~\\cite{ISO50001_2018} obriga a monitorizar, medir e analisar o\ndesempenho energético; a ISO~50006~\\cite{ISO50006_2014} operacionaliza-o em\nindicadores e \\emph{baselines}, com variáveis relevantes, fatores estáticos\ne normalização; a ISO~50015 e o IPMVP~\\cite{ISO50015_2014,IPMVP_2022} tratam\nda medição e verificação de poupanças."),
("selecionar sobre a variável\nresposta trunca a distribuição do erro e enviesa o modelo.",
 "selecionar sobre a variável\nresposta trunca a distribuição do erro e enviesa o modelo~\\cite{Heckman1979}."),
("existe o degrau que a ISO~50006 e o\nIPMVP sancionam: a regressão linear múltipla",
 "existe o degrau que a ISO~50006 e o\nIPMVP sancionam~\\cite{ISO50006_2014,IPMVP_2022}: a regressão linear múltipla"),
("um estimador-M de Huber com constante de\nafinação fixa ($c = 1{,}345$) e escala pela mediana dos desvios absolutos ---",
 "um estimador-M de Huber~\\cite{Huber1964,HuberRonchetti2009} com constante\nde afinação fixa ($c = 1{,}345$~\\cite{HollandWelsch1977}) e escala pela\nmediana dos desvios absolutos ---"),
("porque um estimador de Huber não resiste a pontos de\nalavancagem elevada.",
 "porque um estimador de Huber não resiste a pontos de\nalavancagem elevada~\\cite{RousseeuwLeroy1987}."),
("O estimador de Theil--Sen serve de referência livre de\ndistribuição em regressão simples.",
 "O estimador de Theil--Sen~\\cite{Sen1968} serve de referência livre de\ndistribuição em regressão simples."),
("um processo autorregressivo\nsobre os resíduos, com desfasamentos civis exatos e ordem escolhida só no\ntreino ---",
 "um processo autorregressivo\nsobre os resíduos~\\cite{BoxJenkins2015}, com desfasamentos civis exatos e\nordem escolhida só no treino ---"),
("A rota de sensibilidade é a regressão\nquantílica, com restrições de não cruzamento e incerteza",
 "A rota de sensibilidade é a regressão\nquantílica~\\cite{KoenkerBassett1978}, com restrições de não\ncruzamento~\\cite{Chernozhukov2010} e incerteza"),
("um sinal de um\nmonitor sequencial sobre as inovações, não uma data no calendário",
 "um sinal de um\nmonitor sequencial~\\cite{Page1954,Lai1995} sobre as inovações, não uma data\nno calendário"),
("uma banda mais\nestreita em torno de um ponto marginalmente melhor é uma banda muito pior.",
 "uma banda mais\nestreita em torno de um ponto marginalmente melhor é uma banda muito pior:\na nitidez só vale sujeita à calibração~\\cite{Gneiting2007}."),
("ordem escolhida por critério de informação só no treino (entre um e sete\ndias)",
 "ordem escolhida pelo critério de informação bayesiano~\\cite{Schwarz1978} só\nno treino (entre um e sete dias)"),
("E a inovação de um filtro de nível assimila um desvio\nsustentado em poucos dias:",
 "E a inovação de um filtro de nível~\\cite{DurbinKoopman2012} assimila um\ndesvio sustentado em poucos dias:"),
("vinte e quatro meses, ou expansiva, dá uma leitura qualitativa",
 "vinte e quatro meses, ou expansiva~\\cite{PesaranTimmermann2007}, dá uma\nleitura qualitativa"),
("um acima do nominal pelo limite de\nWilson, compatível com o acaso)",
 "um acima do nominal pelo limite de\nWilson~\\cite{Wilson1927}, compatível com o acaso)"),
("(mínimos quadrados ou modelo aditivo) e monitor",
 "(mínimos quadrados ou modelo aditivo~\\cite{HastieTibshirani1986,Wood2017}) e\nmonitor"),
("a\ncorrelação de séries acumuladas é inteiramente fabricada pela acumulação,",
 "a\ncorrelação de séries acumuladas é inteiramente fabricada pela\nacumulação~\\cite{Yule1926,GrangerNewbold1974},"),
("remove\nexatamente a mudança de nível que se quer ver:",
 "remove\nexatamente a mudança de nível que se quer ver~\\cite{AlwanRoberts1988,Wardell1994}:"),
("``Não rejeitado'' nunca é\n``equivalente'': não há margens práticas elicitadas.",
 "``Não rejeitado'' nunca é\n``equivalente''~\\cite{Lakens2017}: não há margens práticas elicitadas."),
]
patch(f"{ROOT}/2-MainMatter/chapter-4-metodos.tex",C4)
patch(f"{ROOT}/2-MainMatter/chapter-7-discussao.tex",C7)
