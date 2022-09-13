#!/usr/bin/env python3
# coding: utf-8
import json
import sys
from logging import getLogger
from subprocess import STDOUT, TimeoutExpired, check_output

logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)


srcpath="../02_abstpdf"

# records = json.load(sys.stdin)
records = dict()
for j in sys.argv[1:]:
    with open(j) as f:
        d = json.load(f)
        id = d["id"]
        records[id] = d

for id, rec in records.items():
    code = rec["code"]

    a = f"{srcpath}/{id}/tocg.jpg" # rec["tn"]
    b = f"tn/{code}.jpg" # rec["tn"]
    cmd = ["ln", a, b]
    try:
        check_output(cmd)
    except:
        pass


    a = f"{srcpath}/{id}/index.pdf"
    b = f"pdf/{code}.pdf"
    cmd = ["ln", a, b]
    try:
        check_output(cmd)
    except:
        pass
