

# awardのデータをjs用に変換する。

import json
import shutil
import sys
# import pandas as pd
from subprocess import STDOUT, TimeoutExpired, check_output

# df = pd.read_excel("Award修正.xlsx")


# cond = df["講演番号"].str.contains("^Aw-") & df["講演番号"].notnull()
# df = df[cond]
# df["lab"] = df["講演番号"]
# df["ses"] = df["講演番号"].str.rstrip("0123456789").str.rstrip("-")
# df["loc"] = df["講演者所属"]
# df["spe"] = df["講演者"]
# df["pdf"] = "pdf/"+df['講演番号']+".pdf"
# df["tit"] = df["題名"]
# df["con"] = df["講演番号"] +" "+ df["題名"] +" "+ df["講演者"] +" "+ df["講演者所属"]
# df = df.drop(columns=["講演番号", "講演者", "講演者所属", "題名", "PDFファイル名"])

# dic = df.to_dict('index')
# js = [dic[rec] for rec in sorted(dic, key=lambda x:dic[x]["lab"])]
with open("award72.json") as f:
    js = json.load(f)

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
        rec["inf"] = [tit[0],
            f"({loc[0]}) {spe[0]}",
        ]
    rec["sea"] = ""
    rec["pdf"] = f"pdf/{lab}.pdf"
    rec["pre"] = f"tn/{rec['lab']}.jpg"
    srcpdf = "Award/"+rec['lab']+".pdf"
    dstpdf = "pdf/"+rec['lab']+".pdf"
    shutil.copyfile("../"+srcpdf,"../"+dstpdf)

    rec["con"] = " ".join([rec[x] for x in ("awn", "tit", "spe", "loc")])

    # prepare thumbs
    cmd = ["sips",
           "-s", "format", "jpeg",
           "-z", "200", "200",
           f"../{rec['pdf']}",
           "--out", f"../{rec['pre']}"]
    print(cmd, file=sys.stderr)
    output = check_output(cmd)


print(json.dumps(js, indent=2, ensure_ascii=False))