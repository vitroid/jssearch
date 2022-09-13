# 日本語と英語の題名の交換。
# usage: python this.py 72120

import json
import sys

id = sys.argv[1]

with open(f"master/{id}.json") as f:
    data = json.load(f)

data["title"], data["titlee"] = data["titlee"], data["title"]
if "titlee.original" in data:
    del data["titlee.original"]

with open(f"master/{id}.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)

