import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, TimeoutExpired, check_output

import yaml

prepositions = """
aboard
about
above
across
after
against
along
amid
among
anti
around
as
at
before
behind
below
beneath
beside
besides
between
beyond
but
by
concerning
considering
despite
down
during
except
excepting
excluding
following
for
from
in
inside
into
like
minus
near
of
off
on
onto
opposite
outside
over
past
per
plus
regarding
round
save
since
than
through
to
toward
towards
under
underneath
unlike
until
up
upon
versus
via
with
within
without

having
using
""".split()


conjunctions = """
and
but
for
nor
or
so
yet
""".split()

articles = """
a
an
the
""".split()

terms = """
ph
"""


def titlecase_word(w):
    if w.lower() in prepositions:
        return w
    if w.lower() in conjunctions:
        return w
    if w.lower() in articles:
        return w
    if w.lower() in terms:
        return w
    if w[0] in "abcdefghijklmnopqrstuvwxyz":
        return w[0].upper() + w[1:]
    return w


def titlecase(s):
    words = s.split()
    print(words, file=sys.stderr)
    t = []
    for w in words:
        t.append(titlecase_word(w))
    print(t, file=sys.stderr)
    return " ".join(t)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


with open(sys.argv[1]) as f:
    record = json.load(f)


with open("1/template.html") as f:
    template = f.read()



mt = {}

id = record["id"]
print(id, file=sys.stderr)
r = template.replace("%%ID%%", id)
r = r.replace("%%CSS%%", "preview.css")
r = r.replace("%%JS%%", "preview.js")
with open(f"html/{id}.html", "w") as f:
    f.write(r)
r = template.replace("%%ID%%", id)
r = r.replace("%%CSS%%", "recordssheet.css")
r = r.replace("%%JS%%", "recordssheet.js")
with open(f"sheet/{id}.html", "w") as f:
    f.write(r)

figure = record["figure"]
# print(record["title"])
record["resized"] = ""
# make titlecased title
s = titlecase(record["titlee"])
record["mtitlee"] = s
if record["mtitlee"] != record["titlee"]:
    mt[id] = { "old": record["titlee"],
                "new": record["mtitlee"]
                }

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
        record["resized"] = dst
        # try:
        #     im = Image.open(f'attach/{figure}.body')
        #     print(im.format, im.size, im.mode, file=sys.stderr)
        #     resized = im.resize((1500, 750))
        #     if im.mode == "CMYK":
        #         filename = f"img/{id}.jpg"
        #     else:
        #         filename = f"img/{id}.png"
        #     resized.save(filename)
        #     record["resized"] = filename
    else:
        print(f'missing {src}', file=sys.stderr)

src = f'attach/{figure}.body'
if "tocg" in record:
    toc = record["tocg"]
    if toc:
        src = f'attach/{toc}.body'
dst = f"tn/{id}.jpg"
if "code" in record:
    code = record["code"]
    dst = f"tn/{code}.jpg"
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
    record["tn"] = dst
    


# print(json.dumps(records, indent=4, sort_keys=True))
# with open("mtitles.json", "w") as mtf:
#     json.dump(mt, mtf, indent=4, sort_keys=True, ensure_ascii=False)
