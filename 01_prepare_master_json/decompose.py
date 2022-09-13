import json
import os
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

targetdir = sys.argv[2]

# remove " " and "#" from the title
for id, rec in data.items():
    if "deleted" not in rec:
        rec["titlee"] = rec["titlee"].lstrip(" #")
        targetfile = f"{targetdir}/{id}.json"
        if not os.path.exists(targetfile):
            with open(targetfile, "w") as f:
                json.dump(rec, f, indent=4, sort_keys=True, ensure_ascii=False)
