#!/usr/bin/env python3


import sys
import shutil
import glob
import os
import json

db = {x["reg"]:x for x in json.load(open("2020.js"))}


for path in glob.glob(sys.argv[1]+"/*.pdf"):
    basename = os.path.basename(path)[:-4]
    code = db[basename]["lab"]
    shutil.copyfile(path, "unlabelled/"+code+".pdf")
