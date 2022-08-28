#!/usr/bin/env python3
# coding: utf-8
import json
import sys
from logging import getLogger
from subprocess import STDOUT, TimeoutExpired, check_output

logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)

# records = json.load(sys.stdin)
records = dict()
for j in sys.argv[1:]:
    with open(j) as f:
        d = json.load(f)
        id = d["id"]
        records[id] = d

for id, rec in records.items():
    code = rec["code"]

    a = f"tn/{id}.jpg" # rec["tn"]
    b = f"tn/{code}.jpg" # rec["tn"]
    cmd = ["ln", a, b]
    try:
        check_output(cmd)
    except:
        pass


    a = f"pdf/{id}.pdf"
    b = f"pdf/{code}.pdf"
    cmd = ["ln", a, b]
    try:
        check_output(cmd)
    except:
        pass
