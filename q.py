#!/usr/bin/env python
# 引数で指定された何かの情報を表示する便利ツール

import glob
import json
import re
import sys
import subprocess

query = sys.argv[1]

m = re.search("^[0-9]+[A-Za-z]+-[0-9][0-9]$", query)
if m is not None:
    # Lecture order
    for filename in glob.glob("master/*.json"):
        with open(filename) as f:
            data = json.load(f)
            if data["code"] == m.group(0):
                id = data["id"]
                print(id)
                subprocess.run(["code", f"master/{id}.json"])
    sys.exit(0)

m = re.search(r"^[0-9]+\.[0-9]+$", query)
if m is not None:
    # attachments
    id = m.group(0)
    print(f"attach/{id}.type")
    for filename in glob.glob(f"attach/{id}.type"):
        with open(filename) as f:
            print(f"[{f.read()}]")
    sys.exit(0)

m = re.search("^[0-9]+$", query)
if m is not None:
    # registration ID
    id = m.group(0)
    subprocess.run(["code", f"master/{id}.json"])
    sys.exit(0)

