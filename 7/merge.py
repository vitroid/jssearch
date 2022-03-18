

# symposiumのデータをjs用に変換する。

import shutil
import json
import sys
from logging import getLogger
import glob

def session(ses):
    if ses[0] in "1234":
        return int(ses[0]), ses[1:]
    # posters are on the first day
    return 1, ses[:-1]


logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)
# setting = json.load(open("setting.json"))
# salt = setting["salt"]
# logger.error(salt)

rooms = {"2Aa":1,"2Ab":2,"2B":3,"2C":4,"2D":5,"2Fa":6,"2Fb":7,
         "3Aa":1,"3Ab":2,"3B":3,"3C":4,"3D":5,"3E":3,"3Fa":6,"3Fb":7,
         "4Aa":1,"4Ab":2,"4E":3,"4C":4,"4Fa":5,"4Fb":6,
         "Aw-01":1,
         "Aw-02":1,
         "Aw-03":1,
         "Aw-04":2,
         "Aw-05":1,
         "Aw-06":2,
         "Aw-07":1,
         "Aw-08":2,
         "Aw-09":1,
         "Aw-10":1,
         "S1":8,
         "S2":2,
         "S3":3,
         "S4":4}
halls = {"PA1":1, "PB1":1, "PC1":2, "PD1":2, "PE1":2, "PF1":2,
         "PA2":3, "PB2":3, "PC2":4, "PD2":4, "PE2":4, "PF2":4}



D = []
# 辞書に変換する。あとから読んだデータで上書きする。
# さらに、会場に関する情報(URL)を追加する。
for file in sys.argv[1:]:
    data = json.load(open(file))
    for rec in data:
        # session name
        day, ses = session(rec["ses"])
        if ses[0] == "P":
            # poster sessions on Remo
            rec["typ"] = "remo"
            rec["roo"] = halls[rec["ses"]]
            # print(f"{day}.{ses}.{parity}.{group}", file=sys.stderr)
        else:
            # oral sessions on Zoom
            rec["typ"] = "zoom"
            if rec["ses"] in rooms:
                rec["roo"] = rooms[rec["ses"]]
            elif rec["lab"] in rooms:
                rec["roo"] = rooms[rec["lab"]]
            else:
                print(f"Unassigned oral session {day}{ses}", file=sys.stderr)

        # 検索用文字列
        s = " ".join([rec["lab"],] + rec["inf"] + [rec["sea"],])
        rec["con"] = s

        D.append(rec)

print(json.dumps(D, indent=2, ensure_ascii=False))
