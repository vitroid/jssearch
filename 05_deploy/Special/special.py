# specialのxlsxデータをjs用に変換する。

import json

# import shutil
import sys
import pandas as pd
from subprocess import STDOUT, TimeoutExpired, check_output
import pypdf

# import PIL
from reportlab.pdfgen import canvas

js = pd.read_excel(sys.argv[1]).to_dict(orient="records")

for rec in js:
    lab = rec["lab"]  # label
    tit = rec["tit"]  # title
    rec["inf"] = [
        tit,
    ]
    rec["pdf"] = f"pdf/{lab}.pdf"
    rec["pre"] = f"tn/{rec['lab']}.jpg"
    srcpdf = "../Special/" + rec["lab"] + ".pdf"
    dstpdf = "../pdf/" + rec["lab"] + ".pdf"
    rec["sea"] = ""
    rec["spe"] = ""  # speakers
    rec["loc"] = ""  # location of research

    # # ラベルをつける場合
    # can = canvas.Canvas(dstpdf)
    # can.setFillColorRGB(0.5, 0.5, 0.5)
    # can.setFont("Helvetica", 36)
    # can.drawString(50, 750, lab)
    # can.save()
    # reader = pypdf.PdfReader(srcpdf)
    # overlay = pypdf.PdfReader(dstpdf)
    # writer = pypdf.PdfWriter()
    # # reader = pypdf.PdfReader(open(f"../{srcpdf}", "rb"))
    # page = reader.pages[0]
    # page.merge_page(overlay.pages[0])
    # writer.add_page(page)
    # with open(dstpdf, "wb") as f:
    #     writer.write(f)

    # ラベルをつけない場合
    reader = pypdf.PdfReader(srcpdf)
    writer = pypdf.PdfWriter()
    page = reader.pages[0]
    writer.add_page(page)
    with open(dstpdf, "wb") as f:
        writer.write(f)

    rec["con"] = " ".join([rec[x] for x in ("tit", "spe", "loc")])

    # prepare thumbs
    cmd = [
        "sips",
        "-s",
        "format",
        "jpeg",
        "-z",
        "200",
        "200",
        f"../{rec['pdf']}",
        "--out",
        f"../{rec['pre']}",
    ]
    print(cmd, file=sys.stderr)
    output = check_output(cmd)


print(json.dumps(js, indent=2, ensure_ascii=False))
