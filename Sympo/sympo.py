

# symposiumのデータをjs用に変換する。

import glob
import os
import shutil
import json

pdfs = dict()
for dir in glob.glob("S*"):
    for pdf in glob.glob(dir+"/S*.pdf"):
        basename = os.path.basename(pdf)
        code = basename[:5]
        pdfs[code] = basename
        shutil.copyfile(pdf, "../unlabelled/"+basename)


js = []
with open("SympoDB.tsv") as f:
    for line in f:
        code, time, chair, title, speaker = line.strip().split('\t')
        if code != "":
            rec = dict()
            rec["lab"] = code
            rec["ses"] = code[:code.find('-')]
            rec["tim"] = time
            rec["loc"] = ""
            rec["spe"] = speaker
            rec["tit"] = title
            rec["pdf"] = pdfs[code]
            rec["pre"] = pdfs[code].replace(".pdf", ".jpg")
            rec["con"] = " ".join([code, title, speaker])
            js.append(rec)


print(json.dumps(js, indent=2, ensure_ascii=False))
