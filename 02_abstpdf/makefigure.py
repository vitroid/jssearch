import json
import os
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

with open(sys.argv[1]) as f:
    data = json.load(f)

id = data["id"]

figure = data["figure"]
# print(data["title"])
data["resized"] = ""

if figure:
    # print("Figure", file=sys.stderr)
    src = f"../attach/{figure}.body"
    dst = f"genpdf/{id}/figure.jpg"
    if os.path.exists(src):
        cmd = [
            "sips",
            "-s",
            "format",
            "jpeg",
            "-z",
            "750",
            "1500",
            f"{src}",
            "--out",
            f"{dst}",
        ]
        output = check_output(cmd)  # , stderr=STDOUT, timeout=3)
        data["resized"] = dst
        # try:
        #     im = Image.open(f'attach/{figure}.body')
        #     print(im.format, im.size, im.mode, file=sys.stderr)
        #     resized = im.resize((1500, 750))
        #     if im.mode == "CMYK":
        #         filename = f"img/{id}.jpg"
        #     else:
        #         filename = f"img/{id}.png"
        #     resized.save(filename)
        #     data["resized"] = filename
    else:
        print(f"missing {src}", file=sys.stderr)
