# awardのデータをjs用に変換する。

import json

# import shutil
import sys
import pandas as pd
from subprocess import STDOUT, TimeoutExpired, check_output
from reportlab.pdfgen import canvas
import pypdf

js = pd.read_excel(sys.argv[1]).to_dict(orient="records")

for rec in js:
    tit = rec["tit"].split("\n")
    loc = rec["loc"].split("\n")
    spe = rec["spe"].split("\n")
    lab = rec["lab"]
    if len(tit) == 2:
        rec["inf"] = [
            tit[1],
            f"({loc[1]}) {spe[1]}",
            tit[0],
            f"({loc[0]}) {spe[0]}",
        ]
    else:
        rec["inf"] = [
            tit[0],
            f"({loc[0]}) {spe[0]}",
        ]
    rec["sea"] = ""
    rec["pdf"] = f"pdf/{lab}.pdf"
    rec["pre"] = f"tn/{rec['lab']}.jpg"
    srcpdf = "../Award/" + rec["lab"] + ".pdf"
    dstpdf = "../pdf/" + rec["lab"] + ".pdf"

    # ラベルを付ける。
    can = canvas.Canvas(dstpdf)
    can.setFillColorRGB(0.5, 0.5, 0.5)
    can.setFont("Helvetica", 36)
    can.drawString(50, 750, lab)
    can.save()
    reader = pypdf.PdfReader(srcpdf)
    overlay = pypdf.PdfReader(dstpdf)
    writer = pypdf.PdfWriter()
    # reader = pypdf.PdfReader(open(f"../{srcpdf}", "rb"))
    page = reader.pages[0]
    page.merge_page(overlay.pages[0])
    writer.add_page(page)
    with open(dstpdf, "wb") as f:
        writer.write(f)

    rec["con"] = " ".join([rec[x] for x in ("awn", "tit", "spe", "loc")])

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
