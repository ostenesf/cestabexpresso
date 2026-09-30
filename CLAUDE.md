# Minutas de sentença — Vara Única da Comarca de Itaueira

Este repositório guarda o `MODELO UNIVERSAL - PROTOTIPO GERAL.docx` e os autos (PDF do PJe) de processos
bancários. A tarefa típica é: **"Crie uma minuta de sentença para o processo X baseando-se no modelo universal."**
As regras abaixo valem para toda minuta.

## 0. Modelo matriz

O modelo matriz é o `MODELO UNIVERSAL - PROTOTIPO GERAL.docx` da raiz deste repositório, no branch `main`. Se o
usuário indicar outra cópia (Drive, anexo), compare-a parágrafo a parágrafo com a do repositório; havendo diferença,
pergunte qual prevalece antes de usar e, confirmada a nova, atualize o repositório com ela.

## 1. Regra de ouro: fidelidade absoluta ao modelo

1. Leia o modelo inteiro antes de começar, inclusive as instruções `###`, as ROTAS 1 a 7 e os blocos D1 a D6.
2. Use **somente os blocos indicados pela rota aplicável**, na ordem em que aparecem no modelo.
3. **Não crie** seções, parágrafos, títulos, teses, fundamentos ou citações que não estejam no modelo — nem
   para enfrentar preliminares ou teses da contestação que o modelo não cobre (ver item 4, c).
4. **Não altere o texto fixo** do modelo — nem para corrigir erro de digitação. Suspeita de erro vai para o chat.
5. Preencha **apenas** os campos `[[[ ]]]` e decida os blocos `{{{ }}}` (entram inteiros ou saem inteiros),
   seguindo as instruções `###`. As instruções `###` nunca entram na minuta.
6. Ao apagar um trecho de campo, ajuste só vírgula e conectivo.
7. Nunca deduza nem estime valor, data, taxa, prazo ou número. Sem o dado nos autos, escreva
   `[[[CONFERIR NOS AUTOS]]]` — inclusive na data do fecho. Nenhum outro marcador pode sobrar.
8. Todo documento mencionado leva o **Id do PJe**.
9. O relatório tem **no máximo meia página** (cerca de 16 linhas na formatação da minuta).

## 2. Leitura dos autos

- O PDF do PJe vem em **ordem cronológica inversa** (documentos mais recentes primeiro); o índice de Ids está
  nas primeiras páginas.
- Extração de texto: `pip install pypdfium2 python-docx` e use `pypdfium2` (o `pypdf` falha neste ambiente).
- Documentos pessoais, procurações e contratos costumam ser imagem: renderize as páginas
  (`pdf[i].render(scale=1.4).to_pil()`) e leia a imagem. Verifique no RG a data de nascimento (pessoa idosa)
  e eventual anotação "Não Alfabetizado".
- Confira nos despachos se o réu foi intimado a juntar o contrato e o que respondeu.
- Some os descontos comprovados (extratos do autor e do réu) e o eventual crédito a compensar, para a conta
  da ROTA 7.

## 3. Geração do arquivo

1. Escreva o conteúdo em um texto marcado (no scratchpad) e monte o .docx com:
   `python3 ferramentas/montar_minuta.py minuta.txt "MINUTA - SENTENCA - <número do processo>.docx"`
   (a marcação está no cabeçalho do script; ele usa o pacote e a formatação do modelo).
2. Salve a minuta na raiz do repositório com esse nome.
3. Verifique com `python-docx`: nenhum `###`, `{{{` ou `[[[` sobrando (salvo `[[[CONFERIR NOS AUTOS]]]`), e
   compare cada parágrafo com o modelo — só podem diferir os parágrafos com campos preenchidos.
4. O LibreOffice deste ambiente não abre arquivos; não gaste tempo tentando gerar PDF.
5. Faça commit e push no branch designado da sessão e envie o .docx ao usuário.

## 4. Relatório no chat (fora da minuta)

Ao entregar, informe, em tópicos:

a) **Rota escolhida e por quê**: C1 (prova da contratação, com Id), C2 (prova do repasse ou "não exigível"),
   ROTA 6 (se aplicável) e gatilhos da ROTA 7 com a conta
   `total descontado − crédito compensável = prejuízo efetivo (% do total)`.
b) **Escolhas feitas nos campos** de opção (ex.: juros desde o evento danoso ou a citação; custas).
c) **Teses da contestação que o modelo não enfrenta** (ex.: segredo de justiça, interesse de agir, pedido
   contraposto, litigância de má-fé, modulação do EAREsp 676.608), para decisão do Juiz — sem inseri-las na minuta.
d) **Pontos de atenção** (ex.: pedido declaratório ausente na inicial, campos `[[[CONFERIR NOS AUTOS]]]`,
   suspeitas de erro de digitação no modelo).

Seja objetivo; o usuário é assessor de um Juiz legalista e aprecia explicações organizadas em subdivisões.
