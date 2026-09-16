# Manual de Utilização — NOVAthesis no VS Code

> Template: NOVAthesis v7.10.3 · MSc Engenharia Química e Biológica · NOVA FCT
> Ambiente: VS Code + LaTeX Workshop (já configurado e operacional)

---

## Parte 1 — Configuração Inicial

Esta parte faz-se uma vez. Se já a fizeste, passa à Parte 2.

### 1.1 Título da tese — `0-Config/3_cover.tex`

Abre o ficheiro e preenche as duas linhas do título:

```latex
\nttitle(main,en){O teu título em inglês}
\nttitle(main,pt){O teu título em português}
```

Se não tiveres subtítulo (caso mais comum), deixa as linhas `sub` vazias como estão:

```latex
\nttitle(sub,en){}
\nttitle(sub,pt){}
```

### 1.2 Orientador — `0-Config/3_cover.tex`

Substitui o placeholder pelo nome real:

```latex
\ntaddperson{adviser}(a,m){Nome do Orientador, Professor Auxiliar, NOVA FCT}
```

O segundo argumento `(a,m)` significa: papel `a` = adviser, género `m` = masculino. Se for feminino, usa `f`. Se houver co-orientador, descomenta e preenche a linha seguinte:

```latex
\ntaddperson{adviser}(c,f){Nome da Co-orientadora, Investigadora, NOVA FCT}
```

### 1.3 Estado do documento — `0-Config/1_novathesis.tex`

O `docstatus` controla o que é impresso. Há três fases:

| Valor | Quando usar | O que muda |
|---|---|---|
| `working` | Durante a escrita (default) | Sem dedicatória, sem agradecimentos, sem júri — compila mais rápido |
| `provisional` | Antes da entrega | Tudo impresso, sem júri |
| `final` | Após aprovação e marcação de defesa | Com júri, sem timestamp |

Enquanto escreves, mantém `working`. A linha já está activa:

```latex
% \ntsetup{docstatus=final}   ← está comentada
```

Não precisas de alterar nada por agora.

### 1.4 Limpar pacotes de demo — `0-Config/5_packages.tex`

O template inclui pacotes que só existem para os exemplos do documento demo. Remove estas linhas:

```latex
\usepackage{float}        % FOR DEMO PURPOSES ONLY --- PLEASE REMOVE
\usepackage{wrapfig}      % FOR DEMO PURPOSES ONLY --- PLEASE REMOVE
\restylefloat{figure}     % FOR DEMO PURPOSES ONLY --- PLEASE REMOVE
\usepackage{metalogo}     % FOR DEMO PURPOSES ONLY --- PLEASE REMOVE
\usepackage{lipsum}       % FOR DEMO PURPOSES ONLY --- PLEASE REMOVE
```

E o bloco de emojis logo a seguir (que também é demo):

```latex
\IfFileExists{byo-twemojiss.sty}{
  ...
}{
  ...
}
```

---

## Parte 2 — Workflow Diário no VS Code

### 2.1 Compilar

No VS Code, tens três formas de compilar:

**Opção A — Atalho de teclado (mais rápido):**
`Cmd+Alt+B` (macOS) ou `Ctrl+Alt+B` (Windows/Linux)

**Opção B — Botão verde de play:**
No canto superior direito do editor, quando tens o `template.tex` aberto.

**Opção C — Painel LaTeX Workshop:**
Clica no ícone `TeX` na barra lateral esquerda → `Build LaTeX project`.

> **Importante:** Compila sempre com `template.tex` activo no editor, não com um ficheiro de capítulo. O LaTeX Workshop detecta o root automaticamente pela linha `%!TEX root = ../template.tex` que existe em cada ficheiro, mas é mais seguro garantir que o root está aberto.

A primeira compilação demora mais (instala dependências via biber). As seguintes são mais rápidas.

### 2.2 Ver o PDF

O preview abre automaticamente à direita. Se não estiver visível:
`Cmd+Alt+V` (macOS) / `Ctrl+Alt+V` (Windows) — abre o PDF preview dividido.

**SyncTeX — navegar entre código e PDF:**

- **Código → PDF:** Clica numa linha de código e prime `Cmd+Alt+J` (macOS) / `Ctrl+Alt+J` (Windows). O PDF salta para o ponto correspondente.
- **PDF → Código:** `Cmd+Click` (macOS) / `Ctrl+Click` (Windows) em qualquer ponto do PDF. O editor abre o ficheiro `.tex` e posiciona o cursor na linha certa.

### 2.3 Ler erros e avisos

Após compilar, os erros aparecem no painel `Problems` (em baixo no VS Code). Também podes ver o log completo em LaTeX Workshop → `View Log Messages`.

**O que é erro vs aviso:**

- **Erros (vermelho):** Param a compilação. Normalmente são syntax errors, comandos mal escritos, ou ficheiros em falta. Têm de ser corrigidos.
- **Avisos (amarelo):** A compilação termina mas há algo suspeito — referências indefinidas, overfull hboxes, etc. Podes ignorar durante a escrita mas convém limpar antes de submeter.

**Avisos que podes ignorar com segurança:**
- `Overfull \hbox` — linha ligeiramente demasiado larga. Resolve-se no final.
- `Citation 'X' on page Y undefined` — a referência está no `.bib` mas o biber ainda não correu. Compila duas vezes seguidas.
- Avisos do tipo `Token not allowed in a PDF string` — vêm do hyperref e são inofensivos.

**Aviso que não podes ignorar:**
- `Reference 'X' on page Y undefined` — tens um `\label` que não existe. Verifica o nome da label.

### 2.4 Onde está o PDF final

O PDF gerado chama-se `template.pdf` e fica na raiz da pasta do projecto (`novathesis/`). É esse o ficheiro que entregas. Não precisas de exportar nem converter nada — está directamente no teu computador.

---

## Parte 3 — Adicionar Conteúdo

### 3.1 Criar um novo capítulo

**Passo 1:** Cria o ficheiro `.tex` na pasta `2-MainMatter/`. Usa o padrão de nomes existente:

```
2-MainMatter/chapter-nomedocapitulo.tex
```

**Passo 2:** O conteúdo mínimo do ficheiro é:

```latex
%!TEX root = ../template.tex

\chapter{Título do Capítulo}
\label{cha:nomedocapitulo}

% conteúdo aqui
```

**Passo 3:** Regista o capítulo em `0-Config/4_files.tex`, na secção de capítulos, pela ordem em que deve aparecer:

```latex
\ntaddfile{chapter}{chapter-introduction}
\ntaddfile{chapter}{chapter-background}
\ntaddfile{chapter}{chapter-nomedocapitulo}   ← adiciona aqui
\ntaddfile{chapter}{chapter-conclusions}
```

Não precisas de colocar a extensão `.tex` — o template trata disso.

### 3.2 Adicionar figuras

**Passo 1:** Coloca os ficheiros de imagem na pasta `5-Figures/`. Formatos recomendados: `.pdf` para vectoriais, `.png` ou `.jpg` para raster.

**Passo 2:** No texto do capítulo:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{nome-da-figura}
  \caption{Legenda da figura.}
  \label{fig:nome-da-figura}
\end{figure}
```

Não precisas de escrever o caminho completo nem a extensão — o template já configura o LaTeX para procurar em `5-Figures/`.

**Para referenciar a figura no texto:**

```latex
Como se pode observar na Figura~\ref{fig:nome-da-figura}, ...
```

O `~` evita que o número da figura fique numa linha separada da palavra "Figura".

### 3.3 Citar referências

**Passo 1:** Adiciona a entrada ao ficheiro `4-Bibliography/bibliography.bib`. Exemplo de artigo:

```bibtex
@article{autor2023titulo,
  author  = {Apelido, Nome and Outro, Autor},
  title   = {Título do artigo},
  journal = {Nome da revista},
  year    = {2023},
  volume  = {10},
  pages   = {100--110},
  doi     = {10.xxxx/xxxxx}
}
```

A chave `autor2023titulo` é o identificador que usas no texto.

**Passo 2:** No texto, há três formas de citar:

| Comando | Resultado | Quando usar |
|---|---|---|
| `\cite{chave}` | `[1]` | Citação numérica simples |
| `\parencite{chave}` | `(Autor, 2023)` | Citação entre parênteses (author-year) |
| `\textcite{chave}` | `Autor (2023)` | Quando o nome do autor faz parte da frase |

> O estilo activo no teu template é numérico (`numeric-comp`). Portanto `\cite{}` é o que usas na grande maioria dos casos. Se mudares para author-year no futuro (em `2_biblatex.tex`), passa a usar `\parencite{}` e `\textcite{}`.

**Depois de adicionar novas referências**, compila duas vezes para o biber processar o `.bib` e as citações aparecerem correctamente.

### 3.4 Acrónimos

Os acrónimos são definidos em `1-FrontMatter/acronyms.tex`. Para adicionar um:

```latex
\newacronym{msc}{MSc}{Master of Science}
\newacronym{hplc}{HPLC}{High-Performance Liquid Chromatography}
```

No texto, usa:

| Comando | Resultado na primeira ocorrência | Ocorrências seguintes |
|---|---|---|
| `\ac{hplc}` | High-Performance Liquid Chromatography (HPLC) | HPLC |
| `\acp{hplc}` | forma plural | plural |
| `\Ac{hplc}` | Maiúscula no início | HPLC |

O template gera a lista de acrónimos automaticamente no frontmatter.

### 3.5 Símbolos e Glossário

Se não precisares de lista de símbolos ou glossário, comenta as linhas correspondentes em `0-Config/4_files.tex`:

```latex
% \ntaddfile{glossaries}[glossary]{glossary}
% \ntaddfile{glossaries}[symbols]{symbols}
```

Se precisares, os ficheiros são `1-FrontMatter/symbols.tex` e `1-FrontMatter/glossary.tex`, com sintaxe semelhante aos acrónimos.

### 3.6 Apêndices e Anexos

**Apêndice** = material teu (demonstrações, tabelas extensas, código). Fica em `3-BackMatter/appendix1.tex`.

**Anexo** = material externo que juntas ao documento. Fica em `3-BackMatter/annex1.tex`.

Se não tiveres anexos, comenta a linha em `4_files.tex`:

```latex
% \ntaddfile{annex}{annex1}
```

Para criar apêndices adicionais, cria `appendix2.tex` em `3-BackMatter/` e regista em `4_files.tex`:

```latex
\ntaddfile{appendix}{appendix1}
\ntaddfile{appendix}{appendix2}
```

---

## Parte 4 — Referência Rápida de Opções

Todas as opções abaixo são configuradas em `0-Config/1_novathesis.tex` com o comando `\ntsetup{opção=valor}`.

### Opções principais

| Opção | Valores | Default | Descrição |
|---|---|---|---|
| `doctype` | `msc`, `phd`, `bsc`, `plain`, ... | `phd` | Tipo de documento |
| `docstatus` | `working`, `provisional`, `final` | `working` | Fase do documento |
| `lang` | `en`, `pt`, `de`, `fr`, ... | `en` | Língua principal |
| `media` | `screen`, `paper` | `screen` | Screen = margens iguais + links coloridos; Paper = margens assimétricas + links pretos |

### Opções de impressão

| Opção | Valores | Default | Descrição |
|---|---|---|---|
| `print/aidisclosure` | `false`, `aidisclose`, `filename.tex` | `aidisclose` | Declaração de uso de IA |
| `print/committee` | `true`, `false` | Auto por docstatus | Imprimir júri |
| `print/statement` | `true`, `false` | `false` | Declaração de integridade |
| `print/spine` | `true`, `false` | Auto por docstatus | Lombada do livro |
| `print/copyright` | `true`, `false` | `true` | Mensagem de copyright |
| `print/index` | `true`, `false` | `false` | Índice remissivo |
| `print/timestamp` | `true`, `false` | Auto por docstatus | Timestamp "Draft: data" na capa |
| `print/frontpage` | `true`, `false` | `false` | Forçar segunda página de rosto |

### Estilos

| Opção | Valores | Default | Descrição |
|---|---|---|---|
| `style/font` | `newpx`, `libertine`, `palatino`, `arial`*, ... | `newpx` | Fonte do documento (`*` requer XeLaTeX/LuaLaTeX) |
| `style/chapter` | `bar`, `bar-compact`, `elegant`, `bluebox`, ... | `bar` | Estilo do cabeçalho de capítulo |

### SDGs (opcional)

Se a tua tese se enquadra nos Objetivos de Desenvolvimento Sustentável da ONU:

```latex
\ntsetup{print/sdgs/list={3,9,13}}
```

Os ícones aparecem na capa. A lista completa de números (1–17) está comentada no ficheiro `1_novathesis.tex`.

### Estilos de bibliografia — `0-Config/2_biblatex.tex`

| Estilo | Aspecto | Quando usar |
|---|---|---|
| `numeric-comp, sorting=nyt` | `[1]` ordenado por autor | Default — referências ordenadas alfabeticamente |
| `numeric-comp, sorting=none` | `[1]` ordenado por citação | Referências ordenadas pela ordem em que aparecem no texto |
| `authoryear-comp` | `(Autor, 2023)` | Ciências sociais / áreas onde se prefere author-year |
| `alphabetic` | `[Aut23]` | Menos comum em engenharia |

---

## Parte 5 — Preparação para Submissão

### 5.1 Sequência de transições de docstatus

```
working  →  provisional  →  final
```

**Para `provisional`** (versão a entregar para avaliação — sem júri definido):

Em `0-Config/1_novathesis.tex`:
```latex
\ntsetup{docstatus=provisional}
```

Nesta fase são impressos: capa, dedicatória, agradecimentos, citação, abstracts, índices.
O timestamp "Draft" desaparece.

**Para `final`** (após marcação da data de defesa — com júri):

```latex
\ntsetup{docstatus=final}
```

### 5.2 Preencher datas — `0-Config/3_cover.tex`

```latex
\ntdate(submission){2026-06-30}   % data de entrega
\ntdate(exam){2026-09-15}         % data da defesa (preenche quando estiver marcada)
```

### 5.3 Definir o júri — `0-Config/3_cover.tex`

Só é usado quando `docstatus=final`. Descomenta e preenche:

```latex
\ntaddperson{committee}(c,m){Nome do Presidente, Professor Catedrático, NOVA FCT}
\ntaddperson{committee}(r,f){Nome da Arguente, Professora Associada, Outra Universidade}
\ntaddperson{committee}(a,m){Nome do Orientador, Professor Auxiliar, NOVA FCT}
```

Papéis disponíveis: `c` (presidente), `r` (arguente), `a` (orientador), `co` (co-orientador), `m` (membro), `g` (convidado).

### 5.4 Declaração de uso de IA — `0-Config/7-aidisclose.tex`

Antes de submeter, activa os itens que correspondem ao teu uso real de IA. Cada `\AIDactivate{}` corresponde a uma categoria de uso. Exemplos:

```latex
\AIDactivate{w:poly}    % polishing e edição de texto
\AIDactivate{s:gen}     % geração de código
\AIDactivate{d:viz}     % criação de gráficos
```

No final, declara as ferramentas usadas:

```latex
\AIDtoolsUsed{ChatGPT, Claude, GitHub Copilot}
```

Se não usaste IA, desactiva completamente a secção em `1_novathesis.tex`:

```latex
\ntsetup{print/aidisclosure=false}
```

### 5.5 Checklist final antes de entregar

- [ ] `docstatus=provisional` activo
- [ ] Título em PT e EN preenchidos (sem "TODO")
- [ ] Nome do orientador correcto
- [ ] Data de submissão preenchida (`\ntdate(submission){...}`)
- [ ] Abstracts escritos em PT e EN (`1-FrontMatter/abstract-pt.tex` e `abstract-en.tex`)
- [ ] Dedicatória e agradecimentos escritos (`dedication.tex`, `acknowledgements.tex`)
- [ ] AI disclosure preenchida
- [ ] Compila sem erros
- [ ] Referências todas resolvidas (sem "?" no PDF)
- [ ] `template.pdf` gerado e verificado

---

## Apêndice — Problemas Comuns

**"Referências aparecem como [?] no PDF"**
Compila duas vezes. Na primeira o biber processa o `.bib`; na segunda o LaTeX resolve as citações.

**"O capítulo que criei não aparece no documento"**
Verifica se adicionaste `\ntaddfile{chapter}{nome-do-ficheiro}` em `0-Config/4_files.tex`.

**"A figura não é encontrada"**
Confirma que o ficheiro está em `5-Figures/` e que o nome no `\includegraphics{}` corresponde exactamente (incluindo capitalização).

**"Compila mas o PDF não actualiza no preview"**
Clica no ícone de refresh no preview, ou fecha e reabre com `Cmd+Alt+V`.

**"Erro: cannot find file 'biber'"**
O biber não está instalado ou não está no PATH. No VS Code, vai a Settings → LaTeX Workshop → `latex.tools` e verifica se o biber está configurado. Em alternativa, muda para `bibtex` em `0-Config/2_biblatex.tex`:
```latex
\ntbibsetup{backend=bibtex}
```
