

# symposiumのデータをjs用に変換する。

import glob
import os
import shutil
import json

pdfs={'Fasan': 'Fasan_Awarding_lecture.pdf',
'Okuda': 'Jun_Okuda_sakuto_temp_Eng_for_Awarding_lecture.pdf',
'Iwasaki': 'iwasaki_UT_sakuto_temp_jp_for_Awarding_lecture.pdf',
'Kato': 'sakuto_mkato_jp_for_Awarding_lecture.pdf',
'Sakata': 'Abstract_YokoSakata_final.pdf',
'Chen': 'Chen_XM_Abstract_for_Awarding_lecture.pdf',
}

js = []
with open("AwardDB.tsv") as f:
    for line in f:
        code, pdf, time, title, speaker = line.strip().split('\t')
        if code != "":
            rec = dict()
            rec["lab"] = code
            rec["ses"] = code[:code.find('-')]
            rec["tim"] = time
            rec["loc"] = ""
            rec["spe"] = speaker
            rec["tit"] = title
            rec["pdf"] = pdfs[pdf]
            rec["pre"] = pdfs[pdf].replace(".pdf", ".jpg")
            rec["con"] = " ".join([code, title, speaker])
            js.append(rec)

print(json.dumps(js, indent=2, ensure_ascii=False))
