import json
# import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
# import yaml

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


with open(sys.argv[1]) as f:
    data = json.load(f)



drop = set()
for id in data:
    if data[id]["email"] in ("vitroid@gmail.com", "matsu-m3@okayama-u.ac.jp"):
        drop.add(id)
    elif "deleted" in data[id]:
        drop.add(id)
    elif "titlee" not in data[id]:
        data[id]["titlee"] = ""

for id in drop:
    del data[id]


# find the identical postings.
distinct = dict()
for id1 in sorted(data, reverse=True):
    found = False
    for id2 in distinct:
        sim = similar(data[id1]["titlee"], data[id2]["titlee"])
        #if 0.7 < sim < 1.0:
        #    print(sim)
        #    print(data[id1]["titlee"])
        #    print(data[id2]["titlee"])
        if sim  > 0.9:
            if data[id1]["email"] !=  data[id2]["email"]:
                print(f'Similar content:\n{id1} {data[id1]["email"]}\n{id2} {data[id2]["email"]}',file=sys.stderr)
            found = True
            break
    if found:
        distinct[id2].append(id1)
    else:
        distinct[id1] = [id1]


nodup = dict()
for id in distinct:
    print(id, distinct[id], file=sys.stderr)
    nodup[id] = data[id]

# remove " " and "#" from the title
for id in nodup:
    nodup[id]["titlee"] = nodup[id]["titlee"].lstrip(" #")


# other automatic processes specific to JSCC71@2021
# for nid in (71082, 71067, 71337, 71586, 71019, 71719, 71055, 71061, 71522, 71605, 71016):
#     id = f"{nid}"
#     nodup[id]["title"], nodup[id]["titlee"] = nodup[id]["titlee"], nodup[id]["title"]


    
    
print(json.dumps(nodup, indent=4, sort_keys=True, ensure_ascii=False))
