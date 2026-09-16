# Revisão de estilo e progressão do capítulo 3

> Atualização: as cinco propostas foram aplicadas ao ficheiro principal `2-MainMatter/chapter-3-revisao.tex`, a pedido do autor. A versão anterior está guardada em `antes-de-aplicar.tex`; o diagnóstico abaixo documenta a revisão que levou a essa aplicação.

**Recomendação:** cinco alterações localizadas. A organização geral funciona; o problema principal é a repetição de ressalvas depois de contagens que já foram apresentadas como provisórias.

Aplicadas as skills humanizer e narrativa, em modo de revisão de não-ficção. Registo: académico, português europeu. Perspetiva: as perguntas da revisão e o alcance dos dados disponíveis. A concretização faz-se pelas contagens do corpus, sem inventar exemplos industriais. O original está preservado; a proposta encontra-se em `2-MainMatter/chapter-3-revisao-proposta-estilo.tex`.

## Diagnóstico por prioridade

1. **Inferência sobre as fontes, linhas 409–418.** “Esta dispersão por fontes justifica articular literatura de gestão de energia, engenharia e métodos de medição.” A contagem das fontes não demonstra essa composição temática. A proposta conserva as contagens e a limitação da normalização. É uma correção de substância, antes de estilo.
2. **Repetição de ressalvas, sobretudo linhas 577–585 e 646–665.** As fórmulas “não demonstra”, “não permite” e “não estabelece” são muitas vezes necessárias, mas a repetição sem informação nova afasta a atenção dos resultados. Na proposta, a secção temática explica o trabalho de interpretação que a rede exige; o fecho liga as famílias mais frequentes às variáveis, ao ajuste e à validação a recuperar em B.
3. **Tautologia, linhas 184–191.** “A concordância entre modelos é apenas um sinal de concordância entre pré-extrações” não explica o limite dessa concordância. A reescrita identifica o problema: ambos os modelos podem produzir o mesmo erro, pelo que a comparação humana também deve abranger acordos.
4. **Abertura centrada na exposição, linhas 12–29.** “Importa agora conhecer” e a enumeração do que o capítulo fará atrasam a finalidade da revisão. A proposta começa pelos modelos e contextos de aplicação e explicita o que será necessário para discutir a transferência para a refinação.

## Sequência de leitura

Mantém-se protocolo → seleção e composição → métodos bibliométricos → cobertura → resultados → ligação a B. A inconsistência 331/42/333 surge antes dos resultados e a cobertura de 162 classificações antes das frequências dos modelos. Essa ordem evita surpresas metodológicas. No fecho proposto, as famílias mais frequentes voltam como ponto de partida para a leitura das condições de aplicação.

## Humanizer: o que foi alterado e o que ficou

- **Tier A, camada 3 do modo pt-PT:** interpretação genérica sobre as fontes (A3), anúncio de trabalho na abertura (A24) e ressalvas repetidas próximas de paralelismos negativos (A12). Estes rótulos são uma aplicação semântica ao português, não uma prova sobre a autoria.
- **Camadas 1 e 2:** não identifiquei deriva relevante para pt-BR. Os termos técnicos em inglês não foram tratados como erros por si só.
- **Tiers B/C:** não motivaram alterações autónomas. A revisão do ritmo foi localizada, sem impor frases curtas a toda a prosa.
- **Tier D conservado:** registo académico, voz passiva adequada, qualificadores de incerteza e títulos coordenados que realmente abrangem os dois assuntos. Mantiveram-se as distinções entre publicação/estudo, ausência/falta de dados, pertença a B/A e frequência/adequação.

## Segunda passagem

O rascunho ainda tinha “Esta combinação permite articular…” e “deve ser interpretada com cuidado”: substituí essas formulações por relações específicas e pela consulta dos procedimentos no texto integral. Persistem enumerações técnicas, necessárias para identificar categorias. As caixas editoriais continuam visíveis por pedido do autor; não são restos de instruções esquecidos.

## Verificações factuais pendentes

A autoria completa e a cronologia do depósito OSF continuam por confirmar publicamente, conforme a caixa C3-01 e a nota bibliográfica existentes. A composição dos corpora e a adjudicação dos campos também permanecem pendentes. Esta revisão não voltou a validar os dados nem resolveu essas questões; preserva os valores e as citações da versão anterior.

## Ficheiros

- `rascunho-reescritas.md`: primeira passagem.
- `comparacao.md`: antes/depois das cinco passagens.
- `alteracoes.diff`: diferenças exatas.
- `capitulo-3-proposta-estilo.pdf`: versão proposta compilada.
- `verificacao.json`: resultado das verificações de compilação e preservação.

Compilação verificada: `latexmk` terminou com código 0; sem referências indefinidas nem caixas horizontais em excesso no capítulo. As 11 sugestões de figuras continuam visíveis. Inspecionadas as páginas 1, 8 e 12 do excerto.
