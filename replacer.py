#!/usr/bin/env python
from logging import getLogger
import json
import shutil

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

    # make backups
    shutil.copyfile(fin, "history/"+fin+".{0}".format(build))
    with open(fin) as fh:
        with open(fout, "w") as fg:
            for line in fh:
                line = line_replacer(line, d)
                fg.write(line)
