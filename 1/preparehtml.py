import json
from PIL import Image, ImageFilter
import os
import sys


with open(sys.argv[1]) as f:
    data = json.load(f)


with open("1/template.html") as f:
    s = f.read()


drop = set()
for id in data:
    if data[id]["email"] in ("vitroid@gmail.com", "matsu-m3@okayama-u.ac.jp"):
        drop.add(id)
    elif "deleted" in data[id]:
        drop.add(id)
    elif "titlee" not in data[id]:
        print("no titlee", id)
        data[id]["titlee"] = ""

for id in drop:
    del data[id]

for id in sorted(data, key=lambda x:data[x]["titlee"]):
    r = s.replace("%%ID%%", id)
    print(id, data[id]["titlee"])
    with open(f"html/{id}.html", "w") as f:
        f.write(r)

    figure = data[id]["figure"]
    # print(data[id]["title"])
    data[id]["resized"] = ""
    if figure:
        if os.path.exists(f'attach/{figure}.body'):
            im = Image.open(f'attach/{figure}.body')
            # print(im.format, im.size, im.mode)
            resized = im.resize((1500, 750))
            if im.mode == "CMYK":
                filename = f"img/{id}.jpg"
            else:
                filename = f"img/{id}.png"
            resized.save(filename)
            data[id]["resized"] = filename
        else:
            print(f'missing attach/{figure}.body')

    if "tocg" in data[id]:
        toc = data[id]["tocg"]
        if os.path.exists(f'attach/{toc}.body'):
            im = Image.open(f'attach/{toc}.body')
        elif os.path.exists(f'attach/{figure}.body'):
            im = Image.open(f'attach/{figure}.body')
        # tn is a 200x200 image
        # it is cropped if not a square.
        w, h = im.size
        if w > h:
            cropped = im.crop(((w-h)//2,0,(w-h)//2+h, h))
        else:
            cropped = im.crop((0,(h-w)//2,w,(h-w)//2+w))
        resized = cropped.resize((200,200))
        if im.mode == "CMYK":
            filename = f"tn/{id}.jpg"
        else:
            filename = f"tn/{id}.png"
        resized.save(filename)
        data[id]["tn"] = filename



json.dumps(data, f, indent=4, sort_keys=True)
