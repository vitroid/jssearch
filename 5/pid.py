import json
import sys

import pandas as pd

program = pd.read_excel("プログラム編成用_72_7f_松本先生送付用.xlsx", sheet_name="(参考)発表一覧")


pids = dict()

for id, pid in zip(program["id"], program["ポスター発表\n講演番号"]):
    if str(id) != "nan":
        pids[f"{int(id)}"] = pid


pids["72490"] = "2Ab-16"
pids["72633"] = "???"

for j in sys.argv[1:]:
    with open(j) as f:
        d = json.load(f)
        id = d["id"]
        d["code"] = pids[id]
    with open(j, "w") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)
