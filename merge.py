

# symposiumのデータをjs用に変換する。

import shutil
import json
import sys
from hashlib import md5
import yaml
from logging import getLogger

logger = getLogger()
setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)
salt = setting["salt"]
logger.error(salt)

D = dict()
# 辞書に変換する。あとから読んだデータで上書きする。
for file in sys.argv[1:]:
    data = json.load(open(file))
    for rec in data:
        key = rec["lab"]
        salty = salt+key
        rec["md5"] = md5(salty.encode()).hexdigest()
        D[key] = rec

js = [D[key] for key in D]
for rec in js:
    shutil.copyfile("pdf/"+rec["pdf"], "p/"+rec["md5"]+".pdf")

print("var data="+json.dumps(js, indent=2, ensure_ascii=False)+";")
