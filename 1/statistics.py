import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
import yaml
import numpy as np

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


with open(sys.argv[1]) as f:
    data = json.load(f)


accum = np.zeros([6,4])
for id in data:
    print(id)
    subject = int(data[id]["subject"]) - 1
    style = int(data[id]["style"])
    award = data[id]["award.apply"] != ""
    award2 = data[id]["award2.apply"] != ""
    if style in (1,2):
        accum[subject][0] += 1
        if award2:
            accum[subject][1] += 1
    else:
        accum[subject][2] += 1
        if award:
            accum[subject][3] += 1
print(accum)

print(np.sum(accum, axis=0))
print(np.sum(accum[:,[0,2]], axis=1))


    #print(json.dumps(nodup, indent=4, sort_keys=True, ensure_ascii=False))
