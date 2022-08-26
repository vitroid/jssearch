import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
import yaml



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


with open(sys.argv[1]) as f:
    data = json.load(f)


with open("1/template.html") as f:
    template = f.read()


if len(sys.argv) > 2:
    dataset = sys.argv[2:]
else:
    dataset = sorted(data) # , key=lambda x:data[x]["titlee"])


for id in dataset:
# for id in ("71191",):
    print(id, file=sys.stderr)
    r = template.replace("%%ID%%", id)
    r = r.replace("%%CSS%%", "preview.css")
    r = r.replace("%%JS%%", "preview.js")
    with open(f"html/{id}.html", "w") as f:
        f.write(r)
    r = template.replace("%%ID%%", id)
    r = r.replace("%%CSS%%", "datasheet.css")
    r = r.replace("%%JS%%", "datasheet.js")
    with open(f"sheet/{id}.html", "w") as f:
        f.write(r)

    figure = data[id]["figure"]
    # print(data[id]["title"])
    data[id]["resized"] = ""

    if figure:
        # print("Figure", file=sys.stderr)
        src = f'attach/{figure}.body'
        dst = f"img/{id}.jpg"
        if os.path.exists(src):
            cmd = ["sips",
                   "-s", "format", "jpeg",
                   "-z", "750", "1500",
                   f"{src}",
                   "--out", f"{dst}"]
            output = check_output(cmd) # , stderr=STDOUT, timeout=3)
            data[id]["resized"] = dst
            # try:
            #     im = Image.open(f'attach/{figure}.body')
            #     print(im.format, im.size, im.mode, file=sys.stderr)
            #     resized = im.resize((1500, 750))
            #     if im.mode == "CMYK":
            #         filename = f"img/{id}.jpg"
            #     else:
            #         filename = f"img/{id}.png"
            #     resized.save(filename)
            #     data[id]["resized"] = filename
        else:
            print(f'missing {src}', file=sys.stderr)

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
        # output = check_output(cmd) # , stderr=STDOUT, timeout=3)
        # data[id]["tn"] = dst

        # dst = f"img/{id}.jpg"
        # if os.path.exists(f'attach/{toc}.body'):
        #     im = Image.open(f'attach/{toc}.body')
        # elif os.path.exists(f'attach/{figure}.body'):
        #     im = Image.open(f'attach/{figure}.body')
        # # tn is a 200x200 image
        # # it is cropped if not a square.
        # w, h = im.size
        # if w > h:
        #     cropped = im.crop(((w-h)//2,0,(w-h)//2+h, h))
        # else:
        #     cropped = im.crop((0,(h-w)//2,w,(h-w)//2+w))
        # resized = cropped.resize((200,200))
        # if im.mode == "CMYK":
        #     filename = f"tn/{id}.jpg"
        # else:
        #     filename = f"tn/{id}.png"
        # resized.save(filename)
        # data[id]["tn"] = filename


for key, value in data.items():
    with open(f"master/{key}.json", "w") as f:
        json.dump(value, f, indent=4, sort_keys=True, ensure_ascii=False)
