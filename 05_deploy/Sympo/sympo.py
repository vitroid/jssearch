# symposiumのデータをjs用に変換する。

import json
import shutil
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

with open(sys.argv[1]) as f:
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
    srcpdf = "Sympo/"+rec['lab']+".pdf"
    dstpdf = "pdf/"+rec['lab']+".pdf"
    shutil.copyfile("../"+srcpdf,"../"+dstpdf)

    rec["con"] = " ".join([rec[x] for x in ("tit", "spe", "loc")])

    # prepare thumbs
    cmd = ["sips",
            "-s", "format", "jpeg",
            "-z", "200", "200",
            f"../{rec['pdf']}",
            "--out", f"../{rec['pre']}"]
    print(cmd, file=sys.stderr)
    output = check_output(cmd)


print(json.dumps(js, indent=2, ensure_ascii=False))
