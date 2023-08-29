import json
import sys
from logging import INFO, basicConfig, getLogger, INFO
import re
import pandas as pd

basicConfig(level=INFO)
logger = getLogger()

book = sys.argv.pop(1)
sheet = sys.argv.pop(1)
master = sys.argv.pop(1)

program = pd.read_excel(book, sheet_name=sheet)

pids = dict()

# for id, pid in zip(program["id"], program["ポスター発表\n講演番号"]): 2022
for id, pid in zip(program["id"], program["delete"]):
    if str(id) != "nan":
        pids[f"{int(id)}"] = pid

# pids["72490"] = "2Ab-16"
# pids["72633"] = "???"

for id, code in pids.items():
    if str(code) == "nan":
        logger.warning(f"{code} {id}")
        continue
    print(code, int(id))
    m = re.search("^[0-9]+[A-Za-z]+-[0-9]+$", code)
    if m is None:
        logger.warning(f"{code} {id}")
    try:
        masterfile = f"{master}/{id}.json"
        with open(masterfile) as f:
            d = json.load(f)
            d["code"] = code
        with open(masterfile, "w") as f:
            json.dump(d, f, indent=4, ensure_ascii=False)
    except:
        logger.warning(f"Non-existent record {id}={code}")
