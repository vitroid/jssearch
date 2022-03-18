#!/usr/bin/env python
from logging import getLogger
import json
import shutil
# from airium import Airium
#
#
# def oral_table(zoom, attr):
#     a = Airium()
#
#     with a.table(klass="c"):
#         with a.tbody():
#             with a.tr():
#                 with a.th(colspan="3"):
#                     a("Oral presentations / 口頭発表")
#             for ch in zoom:
#                 url, id, pw = zoom[ch]
#                 with a.tr(klass="r"):
#                     with a.td(klass="c"):
#                         with a.a(klass="zm", href=zoom[ch][0]):
#                             a(f"ZOOM{ch}")
#                     with a.td(klass="c"):
#                         a("<br />".join([date + " " + "".join([i for i in attr[ch][date]]) for date in sorted(attr[ch])]))
#                     with a.td(klass="c"):
#                         a(f"ZoomミーティングID: {id}<br />パスコード: {pw}")
#     return str(a)


def line_replacer(line, d):
    logger = getLogger()
    s = ""
    for tag in d:
        loc = line.find(tag)
        if loc >= 0:
            logger.debug("From {0} by {1}.".format(tag, d[tag]))
            replacement = d[tag].splitlines()
            if len(replacement) == 1:
                s = line.replace(tag, replacement[0])
            else:
                indent = line[:loc]
                for newline in replacement:
                    s += indent + newline + "\n"
            return s
    return line


def build_number():
    settingfile = "setting.json"
    settings = json.load(open(settingfile))
    settings["build"] += 1
    with open(settingfile, "w") as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
    return settings["build"]


def repl(d, fin, fout):
    build = build_number()
    d["%%CREDIT%%"] = "jssearch build {0} Copyright (c) 2020 by Masakazu Matsumoto".format(build)
    # zoom = json.load(open("zoom.json"))
    # oral = json.load(open("oral.json"))
    # zoom_attr = dict()
    # for session in oral:
    #     ch = oral[session]["zoom"]
    #     if name in oral[session]:
    #         name = oral[session]["name"]
    #     else:
    #         name = session
    #     date = oral[session]["date"]
    #     query = oral[session]["query"]
    #     if ch not in zoom_attr:
    #         zoom_attr[ch] = dict()
    #     if date not in zoom_attr[ch]:
    #         zoom_attr[ch][date] = []
    #     zoom_attr[ch][date].append(f"<span class='lk' onclick='query(\"{query}\")'>{name}</span>")
    # d["%%ORAL%%"] = oral_table(zoom, zoom_attr)
    # make backups
    # shutil.copyfile(fin, "history/"+fin+".{0}".format(build))
    for line in fin:
        line = line_replacer(line, d)
        fout.write(line)

if __name__ == "__main__":
    import sys
    import json

    fin = sys.stdin
    fout = sys.stdout
    d = dict() #json.load(open(sys.argv[3]))
    repl(d, fin, fout)
