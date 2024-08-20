import json
import os
import sys
from datetime import datetime
from logging import getLogger, basicConfig, INFO, DEBUG

# masterには削除されたレコードも含む。

basicConfig(level=INFO)
logger = getLogger()

with open(sys.argv[1]) as f:
    data = json.load(f)

targetdir = sys.argv[2]

# remove " " and "#" from the title
for id, rec in data.items():
    targetfile = f"{targetdir}/{id}.json"
    rec["titlee"] = rec["titlee"].lstrip(" #")

    if os.path.exists(targetfile):
        with open(targetfile) as f:
            original = json.load(f)
        o_modtime = datetime.strptime(original["modtime"], "%Y/%m/%d %H:%M").timestamp()

        # "2024/06/10 12:56",
        modtime = datetime.strptime(rec["modtime"], "%Y/%m/%d %H:%M").timestamp()

        if modtime <= o_modtime:
            continue

    logger.info(f"Update {id}")
    with open(targetfile, "w") as f:
        json.dump(rec, f, indent=4, sort_keys=True, ensure_ascii=False)
