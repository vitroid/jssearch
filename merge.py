

# symposiumのデータをjs用に変換する。

import shutil
import json
import sys
from hashlib import md5
from logging import getLogger
import glob

def session(ses):
    if ses[0] in "123":
        return int(ses[0]), ses[1:]
    return 0, ses


logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)
setting = json.load(open("setting.json"))
salt = setting["salt"]
logger.error(salt)

rooms = {"A":1,"B":2,"C":3,"D":4,"E":3,
        "Fa":5,"Fb":2,"Aw":5,
        "S1":1,"S2":2,"S3":3,"S4":4,"S5":5}
halls = {"PA":1, "PB":1, "PC":2, "PD":2, "PE":2, "PF":2,}

D = dict()
# 辞書に変換する。あとから読んだデータで上書きする。
# さらに、会場に関する情報(URL)を追加する。
for file in sys.argv[1:]:
    data = json.load(open(file))
    for rec in data:
        key = rec["lab"]
        salty = salt+key
        rec["md5"] = md5(salty.encode()).hexdigest()
        # session name
        day, ses = session(rec["ses"])
        if ses[0] == "P":
            # poster sessions on Remo
            rec["typ"] = "remo"
            rec["roo"] = day*10+halls[ses]
        else:
            # oral sessions on Zoom
            rec["typ"] = "zoom"
            rec["roo"] = rooms[ses]
        D[key] = rec

js = sorted([D[key] for key in D], key=lambda x:x["lab"])
for rec in js:
    shutil.copyfile("pdf/"+rec["pdf"], "p/"+rec["md5"]+".pdf")

print("var data="+json.dumps(js, indent=2, ensure_ascii=False)+";")
