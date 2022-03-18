#!/usr/bin/env python3
# coding: utf-8
from logging import getLogger
import sys
import json
from subprocess import STDOUT, check_output, TimeoutExpired


logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)

records = json.load(sys.stdin)

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
