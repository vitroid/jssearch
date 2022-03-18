import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
import yaml


with open(sys.argv[1]) as f:
    data = json.load(f)


if len(sys.argv) > 2:
    dataset = sys.argv[2:]
else:
    dataset = sorted(data) # , key=lambda x:data[x]["titlee"])


for id in dataset:

    figure = data[id]["figure"]
    # print(data[id]["title"])

    src = f'attach/{figure}.body'
    if "tocg" in data[id]:
        toc = data[id]["tocg"]
        if toc:
            src = f'attach/{toc}.body'
    dst = f"tn/{id}.jpg"
    tmp = f"/tmp/{id}.jpg"
    # print(src, file=sys.stderr)
    if os.path.exists(src):
        # print("TOC", file=sys.stderr)
        cmd = ["sips",
               "--getProperty", "pixelWidth",
               "--getProperty", "pixelHeight",
               f"{src}"]
        lines = "\n".join(check_output(cmd).decode("utf-8").splitlines()[1:])
        output = yaml.safe_load(lines)

        # assert False, output
        w = output["pixelWidth"]
        h = output["pixelHeight"]
        if w > h:
            wh = h
        else:
            wh = w
        cmd = ["sips",
               "-s", "format", "jpeg",
               "--cropToHeightWidth", f"{wh}", f"{wh}",
               # "-z", "200", "200",
               f"{src}",
               "--out", f"{tmp}"]
        output = check_output(cmd)
        cmd = ["sips",
               #"-s", "format", "jpeg",
               #"--cropToHeightWidth", f"{wh}", f"{wh}",
               "-z", "200", "200",
               f"{tmp}",
               "--out", f"{dst}"]
        output = check_output(cmd)
        data[id]["tn"] = dst

# print(json.dumps(data, indent=4, sort_keys=True))
