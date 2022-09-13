import json
import os
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

import yaml

with open(sys.argv[1]) as f:
    data = json.load(f)

id = data["id"]

figure = data["figure"]
src = f'../attach/{figure}.body'
if "tocg" in data:
    toc = data["tocg"]
    if toc:
        src = f'../attach/{toc}.body'
dst = f"{id}/tocg.jpg"
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
