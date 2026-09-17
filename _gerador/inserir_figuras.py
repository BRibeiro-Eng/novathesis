#!/usr/bin/env python3
"""Substitui as caixas [Fxx] das figuras pelo float correspondente (2026-09-17).

Cada entrada tem: ficheiro, id da caixa, texto de chamada (uma frase que
introduz a figura e garante a referencia cruzada) e o corpo do float.
Idempotente: se a caixa ja nao existir, avisa e nao faz nada.
"""
import os, re, sys
TESE = os.path.expanduser("~/Desktop/Tese/novathesis")
if not os.path.isdir(TESE):
    TESE = os.path.expanduser("~/mnt/novathesis")

def gerada(nome, curta, longa, rotulo, largura=r"\textwidth", pos="tbp"):
    return (f"\\begin{{figure}}[{pos}]\n  \\centering\n"
            f"  \\includegraphics[width={largura}]{{gerado/{nome}}}\n"
            f"  \\caption[{curta}]%\n  {{{longa}}}\n  \\label{{{rotulo}}}\n\\end{{figure}}")

def tikz(f):
    return "\\input{5-Figures/tikz/" + f + "}"

INS = []
def add(fich, cid, chamada, corpo):
    INS.append((fich, cid, chamada, corpo))

# ------------------------------------------------------------ Capitulo 1 --
add("2-MainMatter/chapter-1-introducao.tex", "F01",
 "A Figura~\\ref{fig:duas-camadas} resume as duas camadas e o lugar de cada "
 "capítulo nelas.",
 tikz("f01-duas-camadas"))

# ------------------------------------------------------------ Capitulo 2 --
add("2-MainMatter/chapter-2-enquadramento.tex", "F03",
 "A Figura~\\ref{fig:fronteira-cdu} fixa o vocabulário: onde passa a fronteira "
 "do indicador, por onde entra cada vetor energético e em que ponto se mede.",
 tikz("f03-cdu"))

# ------------------------------------------------------------ Capitulo 3 --
add("2-MainMatter/chapter-3-revisao.tex", "F04",
 "A Figura~\\ref{fig:prisma} apresenta o percurso completo, da identificação à "
 "inclusão.",
 tikz("f04-prisma"))

# ------------------------------------------------------------ Capitulo 4 --
add("2-MainMatter/chapter-4-metodos.tex", "F06",
 "A Figura~\\ref{fig:arquitetura-dados} mostra o percurso de um valor desde a "
 "origem até ao facto e o esquema em estrela que dele resulta.",
 tikz("f06-arquitetura-dados"))

add("2-MainMatter/chapter-4-metodos.tex", "F07",
 "A Figura~\\ref{fig:desenhos-avaliacao} alinha os três desenhos no mesmo eixo "
 "temporal e torna visível o que cada um pode e não pode demonstrar.",
 tikz("f07-linha-temporal"))

# ------------------------------------------------------------ Capitulo 5 --
add("2-MainMatter/chapter-5-plataforma.tex", "F08",
 "A Figura~\\ref{fig:validacao-mapeamento} acompanha essa progressão versão a "
 "versão.",
 gerada("cap5-validacao-progressao",
  "Progressão da validação do mapeamento",
  "Progressão da validação do mapeamento, versão a versão. Cada barra reparte "
  "as mesmas 400 células unidade--vetor--mês da amostra de validação em "
  "coincidentes, divergentes e sem consumo, para que os vazios não sejam lidos "
  "como sucessos. As quatro primeiras barras são estados verificados célula a "
  "célula; a barra da v15.1, tracejada, é o resultado \\emph{esperado} do fecho "
  "das últimas cinco divergências, não uma verificação observada. As causas de "
  "cada divergência e o número de casos que explicam estão descritas no "
  "texto que se segue.",
  "fig:validacao-mapeamento", largura="0.86\\textwidth"))

# ------------------------------------------------------------ Capitulo 6 --
add("2-MainMatter/chapter-6-diagnostico.tex", "F10",
 "A Figura~\\ref{fig:amostra-filtros} mostra a cascata de filtros, pela ordem "
 "em que é aplicada, e a disponibilidade mês a mês que dela resulta.",
 gerada("cap6-amostra-e-filtros",
  "Construção da amostra e disponibilidade por mês",
  "Construção da amostra de análise. À esquerda, a cascata de filtros pela "
  "ordem em que é aplicada: 2\\,403 dias candidatos entre 2020-01-01 e "
  "2026-07-30, a data de corte oficial dos dados de 2026; 11\\,955 observações "
  "série--dia para os cinco vetores diários, que são 60 menos do que o produto "
  "$2\\,403\\times5$ por falta de eletricidade em novembro de 2021 e em julho de "
  "2026; 11\\,467 com energia medida; e 10\\,723 depois do limiar de carga, que "
  "remove 744 observações concentradas em 251 dias, 10,4\\,\\% dos dias. Cada "
  "etapa conta observações série--dia, não dias: um dia excluído retira até "
  "cinco observações. À direita, a fração de dias retidos em cada mês e vetor, "
  "que localiza no calendário as paragens e as lacunas de medição.",
  "fig:amostra-filtros"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F11",
 "A Figura~\\ref{fig:dispersao-energia-carga} põe lado a lado a relação que "
 "cada vetor tem com a carga e a população de dias que o filtro deixa de fora.",
 gerada("cap6-dispersao-energia-carga",
  "Consumo e carga por vetor energético",
  "Consumo diário contra carga diária, por vetor, na unidade de destilação "
  "atmosférica, de 2020 a 2025. Os pontos a cinzento são os dias excluídos --- "
  "carga abaixo do limiar oficial de 18,6\\,kt/d ou consumo nulo --- e estão "
  "desenhados para que a população não coberta pela \\emph{baseline} fique "
  "visível. As retas são as regressões anuais oficiais, da mais clara (2020) à "
  "mais escura (2025). O painel da eletricidade não é uma dispersão: mostra a "
  "série no tempo, e os patamares mensais são o efeito da alocação, não "
  "variação de consumo; a quase anulação da alocação em 2021 e 2022, que não se "
  "observa em nenhuma outra unidade, está assinalada e discutida no texto. O "
  "último painel compara a distribuição da carga diária antes e depois do "
  "limiar.",
  "fig:dispersao-energia-carga", pos="p"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F12",
 "A Figura~\\ref{fig:ganho-preditivo} mostra o contraste por vetor e por "
 "transição, com a sensibilidade ao comprimento do bloco à vista.",
 gerada("cap6-ganho-preditivo",
  "Ganho preditivo face ao nulo trivial",
  "Diferença de erro absoluto médio entre a \\emph{baseline} e o nulo trivial "
  "--- a média do ano de treino --- em cada transição treino\\,$\\to$\\,teste. "
  "Valores à direita da linha zero significam que o modelo erra menos do que o "
  "nulo. O traço grosso é o intervalo de confiança a 95\\,\\% com o comprimento "
  "de bloco base; o traço fino, deslocado, é o mesmo intervalo com blocos de "
  "60 dias, e a distância entre os dois é a medida honesta da sensibilidade a "
  "essa escolha. O $n$ anotado é o número de dias avaliados, comum ao modelo e "
  "ao nulo. Só o fuel gás tem ganho que exclui o zero na maioria das "
  "transições; nos três vapores há transições em que o nulo é melhor.",
  "fig:ganho-preditivo"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F13",
 "A Figura~\\ref{fig:predicoes-carga-comum} compara as predições em cargas "
 "dentro do suporte comum, que é onde a comparação entre anos tem sentido.",
 gerada("cap6-predicoes-carga-comum",
  "Predições a carga comum, por ano de \\emph{baseline}",
  "Consumo previsto por cada \\emph{baseline} anual, avaliado em duas cargas "
  "fixas dentro do suporte comum a todos os anos --- os percentis 25 e 75 da "
  "carga observada --- com o intervalo de confiança a 95\\,\\% construído com "
  "erros-padrão robustos a heterocedasticidade e autocorrelação. A comparação "
  "faz-se aqui, e não no intercepto: o valor da reta em $Q=0$ está fora do "
  "domínio observado e não é um consumo base físico. A rejeição estatística da "
  "hipótese de coeficientes constantes ao longo dos anos é sensível ao "
  "tratamento da dependência temporal, como o Apêndice~\\ref{app:tabelas} "
  "documenta.",
  "fig:predicoes-carga-comum"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F14",
 "A Figura~\\ref{fig:cobertura-bandas} reúne a cobertura de todas as "
 "transições, com o nível nominal e a contagem de dias fora à vista.",
 gerada("cap6-cobertura-bandas",
  "Cobertura das bandas de alarme fora da amostra",
  "Fração de dias do ano de aplicação que caem dentro da banda de alarme "
  "construída no ano de treino, por vetor e por transição. A linha vertical é "
  "o nível nominal de 0,9545, o que a banda promete. O traço grosso é o "
  "intervalo obtido por reamostragem em blocos com o comprimento base; os "
  "traços finos, deslocados, repetem o exercício com blocos de 30 e de 60 dias. "
  "Um intervalo que inclui o valor nominal não certifica a banda: apenas diz "
  "que os dados disponíveis não a excluem. A contagem à direita dá os dias fora "
  "da banda sobre os dias avaliados.",
  "fig:cobertura-bandas", pos="p"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F15",
 "A Figura~\\ref{fig:acoplamento-vapores} mostra os dois vapores no mesmo "
 "calendário e a associação que deles resulta.",
 gerada("cap6-acoplamento-vapores",
  "Associação entre os resíduos dos vapores de 24 e de 10 bar",
  "Resíduos padronizados das \\emph{baselines} oficiais dos vapores de 24 e de "
  "10\\,bar. À esquerda, as duas séries no mesmo calendário de 2025; à direita, "
  "a dispersão de todos os anos, com cada ano numa tonalidade. A associação é "
  "forte e persistente, e é compatível com um circuito de vapor partilhado, com "
  "uma regra de alocação comum aos dois níveis ou com as duas coisas ao mesmo "
  "tempo: os dados não distinguem entre estas explicações e a figura não "
  "sustenta nenhuma seta causal. Os coeficientes anuais e agregados estão "
  "anotados no painel da direita.",
  "fig:acoplamento-vapores"))

add("2-MainMatter/chapter-6-diagnostico.tex", "F16",
 "A Figura~\\ref{fig:sensibilidade-convencoes} mede quanto das conclusões "
 "sobrevive a mudar essas convenções.",
 gerada("cap6-sensibilidade-convencoes",
  "Sensibilidade das conclusões às convenções de janela e de limiar",
  "Percentagem de conclusões que mudam de rótulo quando se altera a convenção "
  "de janela --- ano civil ou ano móvel de julho a junho --- e o limiar de "
  "carga, multiplicado por 0,8 e por 1,2. Cada célula dá a percentagem e, entre "
  "parênteses, o número de reavaliações em que assenta. A célula de referência "
  "é a de ano civil com o limiar oficial. A comparação entre as duas metades da "
  "figura confunde dois efeitos, mudança de partição e mudança de período "
  "coberto, e por isso não permite atribuir o resultado à âncora anual; nenhuma "
  "das janelas foi escolhida depois de ver qual favorecia a conclusão.",
  "fig:sensibilidade-convencoes"))

# ------------------------------------------------------------ Capitulo 7 --
add("2-MainMatter/chapter-7-discussao.tex", "F17",
 "A Figura~\\ref{fig:ref-estado-monitor} separa os três objetos e mostra onde "
 "cada um entra.",
 tikz("f17-referencia-estado-monitor"))

add("2-MainMatter/chapter-7-discussao.tex", "F18",
 "A Figura~\\ref{fig:matriz-decisao} mostra a matriz completa: cada candidato, "
 "cada par anual e o estado de cada um dos dois critérios.",
 gerada("cap7-matriz-decisao",
  "Matriz de decisão por candidato e por par anual",
  "Os trinta e dois candidatos efetivamente avaliados --- quatro vetores, três "
  "ajustes pontuais e as bandas construídas sobre cada um --- contra os cinco "
  "pares anuais. Cada célula tem duas metades: à esquerda o critério de ganho "
  "preditivo, que é uma propriedade do ajuste pontual e por isso se repete "
  "entre bandas do mesmo estimador; à direita o critério de suporte da banda. "
  "As contagens à direita são os pares em que cada critério é cumprido, e os "
  "dois quadrados marcam se atingem a regra declarada de quatro em cinco. "
  "Nenhum candidato a cumpre nos dois critérios, e a regra de sensibilidade de "
  "três em cinco não altera essa conclusão. O conjunto avaliado não é o "
  "fatorial de estimadores por bandas: as bandas robustas só existem para os "
  "estimadores robustos.",
  "fig:matriz-decisao", pos="p"))

add("2-MainMatter/chapter-7-discussao.tex", "F19",
 "A Figura~\\ref{fig:injeccao} mostra, dia a dia, quanto do desvio inserido "
 "cada componente ainda deixa ver.",
 gerada("cap7-injeccao-degrau",
  "Quanto sinal sobrevive a cada componente",
  "Experiência de injeção no fuel gás: um desvio conhecido é somado à série e "
  "segue-se o que resta dele em cada componente, nos primeiros 150 dias de "
  "aplicação, para um degrau e para uma rampa da mesma amplitude. Em cima, o "
  "desvio inserido. Ao meio, o desvio medido contra a referência congelada e a "
  "parte que o reajuste anual absorve. Em baixo, a inovação do filtro. A "
  "diferença entre os dois primeiros painéis é uma identidade algébrica, não "
  "uma medição; o terceiro painel é que mostra a atenuação efetiva. Os valores "
  "numéricos citados no texto vêm do lote validado, não desta ilustração.",
  "fig:injeccao"))

add("2-MainMatter/chapter-7-discussao.tex", "F20",
 "A Figura~\\ref{fig:deteccao} compara os três monitores sob o mesmo "
 "orçamento de falsos sinais.",
 gerada("cap7-deteccao-simulacao",
  "Deteção simulada, ao mesmo orçamento de falsos sinais",
  "Probabilidade de detetar um desvio nos primeiros 90 dias, por amplitude, "
  "para três monitores calibrados ao mesmo orçamento de falsos sinais. Os dois "
  "primeiros painéis separam degrau de rampa com dependência moderada "
  "($\\rho=0{,}6$); o terceiro fixa a amplitude num desvio-padrão e varia a "
  "dependência do gerador. A banda é o intervalo de Wilson sobre as réplicas. A "
  "linha a tracejado marca metade das deteções. Os valores descrevem o gerador "
  "simulado e as suas hipóteses, e não são uma previsão do que aconteceria na "
  "refinaria.",
  "fig:deteccao"))

add("2-MainMatter/chapter-7-discussao.tex", "F21",
 "A Figura~\\ref{fig:ficha-estados} concretiza os requisitos numa ficha e num "
 "ciclo de vida.",
 tikz("f21-ficha-estados"))

# ---------------------------------------------------------------- aplicar --
def main():
    por_ficheiro = {}
    for fich, cid, chamada, corpo in INS:
        por_ficheiro.setdefault(fich, []).append((cid, chamada, corpo))
    for fich, itens in por_ficheiro.items():
        p = os.path.join(TESE, fich)
        s = open(p, encoding="utf-8").read()
        for cid, chamada, corpo in itens:
            pat = re.compile(r"% \[REV-[0-9-]+\]\[" + cid + r"\]\[[^\]]*\]\[[^\]]*\]\n"
                             r".*?% \[/REV-[0-9-]+\]\n", re.S)
            m = pat.search(s)
            if not m:
                print(f"  ! {fich}: caixa {cid} não encontrada (já resolvida?)")
                continue
            s = s[:m.start()] + chamada + "\n\n" + corpo + "\n" + s[m.end():]
            print(f"  + {fich}: {cid}")
        open(p, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    main()
