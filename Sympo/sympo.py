# symposiumのデータをjs用に変換する。

import json
import pandas as pd
from subprocess import STDOUT, check_output, TimeoutExpired
import sys
import shutil

# pdfs = dict()
# for dir in glob.glob("S*"):
#     for pdf in glob.glob(dir+"/S*.pdf"):
#         basename = os.path.basename(pdf)
#         code = basename[:5]
#         pdfs[code] = basename
#         shutil.copyfile(pdf, "../unlabelled/"+basename)
#
df = pd.read_excel("Symposium修正.xlsx")


cond = df["講演番号"].str.contains("^S[1-4]") & df["講演番号"].notnull()
df = df[cond]
df["lab"] = df["講演番号"]
df["ses"] = df["講演番号"].str.rstrip("0123456789").str.rstrip("-")
df["loc"] = df["講演者所属"]
df["spe"] = df["講演者"]
df["tit"] = df["題名"]
df["con"] = df["講演番号"] +" "+ df["題名"] +" "+ df["講演者"] +" "+ df["講演者所属"]
df = df.drop(columns=["講演番号", "講演者", "講演者所属", "題名", "PDFファイル名"])

dic = df.to_dict('index')
js = [dic[rec] for rec in dic]
for rec in js:
    rec["inf"] = [rec["tit"], f"({rec['loc']}) {rec['spe']}"]
    rec["sea"] = ""
    rec["pre"] = f"tn/{rec['lab']}.jpg"
    rec["pdf"] = f"pdf/{rec['lab']}.pdf"
    srcpdf = "Sympo/"+rec['lab']+".pdf"
    dstpdf = "pdf/"+rec['lab']+".pdf"
    shutil.copyfile("../"+srcpdf,"../"+dstpdf)

    # prepare thumbs
    cmd = ["sips",
           "-s", "format", "jpeg",
           "-z", "200", "200",
           f"../{srcpdf}",
           "--out", f"../{rec['pre']}"]
    print(cmd, file=sys.stderr)
    output = check_output(cmd)



print(json.dumps(js, indent=2, ensure_ascii=False))
