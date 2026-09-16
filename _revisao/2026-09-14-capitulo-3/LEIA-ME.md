# Capítulo 3 — redação de 14 de setembro de 2026

Redigidos a introdução e os conteúdos gerais e bibliométricos das secções 3.1–3.3. Síntese narrativa de B e gap preservados.

## Proveniência dos resultados

Base: `/Users/bernardoribeiro/LocalResearch/Screening/level3_extraction/`.

- Protocolo e critérios: `PROTOCOL.md` e `VALIDATION_PROTOCOL_C.md`.
- Seleção e recuperação: `MISSINGNESS.md` e export de triagem.
- Contagens bibliométricas: `bibliometrics/results/union_inclusiva/tables/`, em particular `annual.csv`, `document_type.csv`, `source.csv`, `concentration_summary.csv`, `field_status.csv`, `paper_type.csv`, `type_of_organisation.csv`, `enpi_enb_model_types.csv`, `ems_standard.csv`, `mv_protocol.csv`, `metadata_enrichment_coverage.csv` e `citation_summary.csv`.
- Lista registada de A: 331; B: 42; interseção: 40; união inclusiva exploratória: 333. As decisões de elegibilidade não foram alteradas.
- Fontes metodológicas: sete novas entradas na bibliografia; metadados de quatro artigos arquivados em `referencias_crossref.json`. DOI/autoria completa/cronologia do protocolo público carecem da confirmação indicada em caixa.

## Sugestões de figuras

| Caixa | Página no PDF completo | Página impressa |
|---|---:|---:|
| C3-V01 | 36 | 24 |
| F04 | 38 | 26 |
| C3-V02 | 40 | 28 |
| C3-V03 | 41 | 29 |
| C3-V04 | 41 | 29 |
| C3-V05 | 42 | 30 |
| C3-V06 | 43 | 31 |
| C3-V07 | 43 | 31 |
| C3-V08 | 43 | 31 |
| C3-V09 | 44 | 32 |
| C3-V10 | 45 | 33 |

As caixas identificam a finalidade, posição e ficheiros existentes. O esquema conceptual C3-V01 ainda requer desenho. As figuras não foram incorporadas como resultados finais.

## Verificação

Compilação nativa `latexmk` concluída com código 0. Sem referências indefinidas nem caixas horizontais em excesso no capítulo 3. As 11 sugestões foram encontradas no texto do PDF. Confirmadas as 22 referências a ficheiros existentes nas sugestões. Inspeção visual das páginas 34, 38, 40, 43 e 45 do PDF completo. As quebras de caixas são permitidas pelo mecanismo de revisão já existente.

PDF completo atualizado em `template.pdf`; excerto de 13 páginas em `capitulo-3.pdf`. Evidência automática em `verificacao.json`. Cópias anteriores de LaTeX e bibliografia na pasta `antes/`.

O wrapper do plugin teve um erro de descodificação de caracteres na saída, após executar o compilador; a verificação nativa subsequente confirmou a compilação. Os avisos preexistentes do template e das entradas de divulgação de IA não foram tratados nesta alteração.
