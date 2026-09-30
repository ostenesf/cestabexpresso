"""Monta a minuta .docx a partir de um texto marcado, com a formatação do MODELO UNIVERSAL.

Uso:
    python3 ferramentas/montar_minuta.py minuta.txt "MINUTA - SENTENCA - <número>.docx"

Marcação do arquivo de texto (uma linha = um parágrafo):
    # TEXTO     romano do relatório/fundamento/dispositivo (centralizado, negrito)
    ## Texto    título de seção (à esquerda, negrito)
    > Texto     citação (TNR 10, entrelinhas simples, recuo de 4 cm)
    = Texto     centralizado (local e data, cargo)
    =* Texto    centralizado em negrito (nome do juiz)
    (vazia)     parágrafo vazio
    Texto       corpo (TNR 12, justificado, 1,5, recuo de 1,25 cm)
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent
MODELO = RAIZ / "MODELO UNIVERSAL - PROTOTIPO GERAL.docx"

RPR = ('<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>{b}'
       '<w:color w:val="000000"/><w:sz w:val="{sz}"/></w:rPr>')
# margens da instrução do modelo: sup. 3, esq. 3, inf. 2,5, dir. 2,5 cm
PGMAR = ('<w:pgMar w:top="1701" w:right="1417" w:bottom="1417" w:left="1701" '
         'w:header="720" w:footer="720" w:gutter="0"/>')


def paragrafo(texto, *, line=360, first=709, left=0, jc="both", bold=False, sz=24):
    b = "<w:b/>" if bold else '<w:b w:val="0"/>'
    ppr = (f'<w:pPr><w:spacing w:before="0" w:after="0" w:line="{line}" w:lineRule="auto"/>'
           f'<w:ind w:firstLine="{first}" w:left="{left}"/><w:jc w:val="{jc}"/></w:pPr>')
    if not texto:
        return f"<w:p>{ppr}</w:p>"
    return (f'<w:p>{ppr}<w:r>{RPR.format(b=b, sz=sz)}'
            f'<w:t xml:space="preserve">{escape(texto)}</w:t></w:r></w:p>')


def converter(linha):
    linha = linha.rstrip("\n")
    if not linha.strip():
        return paragrafo("", first=0, jc="left")
    if linha.startswith("## "):
        return paragrafo(linha[3:], first=0, jc="left", bold=True)
    if linha.startswith("# "):
        return paragrafo(linha[2:], first=0, jc="center", bold=True)
    if linha.startswith("> "):
        return paragrafo(linha[2:], line=240, first=0, left=2268, sz=20)
    if linha.startswith("=* "):
        return paragrafo(linha[3:], first=0, jc="center", bold=True)
    if linha.startswith("= "):
        return paragrafo(linha[2:], first=0, jc="center")
    return paragrafo(linha)


def main(entrada, saida):
    corpo = "".join(converter(l) for l in Path(entrada).read_text(encoding="utf-8").splitlines())
    with zipfile.ZipFile(MODELO) as z:
        arquivos = {n: z.read(n) for n in z.namelist()}
    doc = arquivos["word/document.xml"].decode("utf-8")
    ini = doc.index("<w:body>") + len("<w:body>")
    sect = doc[doc.index("<w:sectPr"):doc.index("</w:body>")]
    sect = re.sub(r"<w:pgMar [^>]*/>", PGMAR, sect)
    arquivos["word/document.xml"] = (doc[:ini] + corpo + sect + "</w:body></w:document>").encode("utf-8")
    ordem = ["[Content_Types].xml"] + [n for n in arquivos if n != "[Content_Types].xml"]
    with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as z:
        for n in ordem:
            z.writestr(n, arquivos[n])
    print(f"ok: {saida}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
