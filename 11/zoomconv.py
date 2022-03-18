

# awardのデータをjs用に変換する。

import json
import pandas as pd
from subprocess import STDOUT, check_output, TimeoutExpired
import sys
import shutil

df = pd.read_excel("Zoom URLs.xlsx")
df = df.rename(columns={"Pass code": "pw"})
df["room"] = df.index+1
# print(df)
#
# cond = df["講演番号"].str.contains("^Aw-") & df["講演番号"].notnull()
# df = df[cond]
# df["lab"] = df["講演番号"]
# df["ses"] = df["講演番号"].str.rstrip("0123456789").str.rstrip("-")
# df["loc"] = df["講演者所属"]
# df["spe"] = df["講演者"]
# df["pdf"] = "pdf/"+df['講演番号']+".pdf"
# df["tit"] = df["題名"]
# df["con"] = df["講演番号"] +" "+ df["題名"] +" "+ df["講演者"] +" "+ df["講演者所属"]
df = df.drop(columns=["Room"])
#
dic = df.to_dict('index')
js = {dic[rec]["room"]:dic[rec] for rec in sorted(dic, key=lambda x:dic[x]["room"])}
for id, rec in js.items():
    rec["pw"] = f"{rec['pw']:06d}"
    room = rec["room"]
    if room == 8:
        rec["room"] = "ZOOM1"
    else:
        rec["room"] = f"ZOOM{room}"
# for rec in js:
#     tit = rec["tit"].split("\n")
#     loc = rec["loc"].split("\n")
#     spe = rec["spe"].split("\n")
#     if len(tit) == 2:
#         rec["inf"] = [
#                       tit[1],
#                       f"({loc[1]}) {spe[1]}",
#                       tit[0],
#                       f"({loc[0]}) {spe[0]}",
#                                     ]
#     else:
#         rec["inf"] = [tit[0],
#                       f"({loc[0]}) {spe[0]}",
#                      ]
#     rec["sea"] = ""
#     rec["pre"] = f"tn/{rec['lab']}.jpg"
#     srcpdf = "Award/"+rec['lab']+".pdf"
#     dstpdf = "pdf/"+rec['lab']+".pdf"
#     shutil.copyfile("../"+srcpdf,"../"+dstpdf)
#     # prepare thumbs
#     cmd = ["sips",
#            "-s", "format", "jpeg",
#            "-z", "200", "200",
#            f"../{rec['pdf']}",
#            "--out", f"../{rec['pre']}"]
#     print(cmd, file=sys.stderr)
#     output = check_output(cmd)
#
#
#
print(json.dumps(js, indent=2, ensure_ascii=False))
