import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
import yaml
import shutil

with open(sys.argv[1]) as f:
    data = json.load(f)

for id in data:
    figure = data[id]["figure"]
    code = data[id]["code"]
    src = f'attach/{figure}.body'
    try:
        os.mkdir(f"verify/{code}", 0o755)
    except:
        pass
    if figure:
        name = open(f'attach/{figure}.name').readline().strip()
        shutil.copyfile(f'attach/{figure}.body', f'verify/{code}/{name}')
    if "tocg" in data[id]:
        toc = data[id]["tocg"]
        if toc:
            name = open(f'attach/{toc}.name').readline().strip()
            shutil.copyfile(f'attach/{toc}.body', f'verify/{code}/{name}')
    if figure:
        src = f'attach/{figure}.body'
        dst = f"verify/{code}/figure.jpg"
        if os.path.exists(src):
            cmd = ["sips",
                   "-s", "format", "jpeg",
                   "-z", "750", "1500",
                   f"{src}",
                   "--out", f"{dst}"]
            output = check_output(cmd) # , stderr=STDOUT, timeout=3)
            data[id]["resized"] = dst
        else:
            print(f'missing {src}', file=sys.stderr)

    src = f'attach/{figure}.body'
    if "tocg" in data[id]:
        toc = data[id]["tocg"]
        if toc:
            src = f'attach/{toc}.body'
    dst = f"verify/{code}/tocg.jpg"
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
