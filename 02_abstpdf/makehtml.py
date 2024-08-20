import sys
import json
import os
from logging import getLogger, basicConfig, INFO, DEBUG

basicConfig(level=INFO)
logger = getLogger()

with open("template.html") as f:
    template = f.read()

id = sys.argv[1]
master_js = f"../../../master/{id}.js"
master_json = f"../master/{id}.json"
with open(master_json) as f:
    rec = json.load(f)

if "deleted" in rec:
    try:
        os.remove(sys.argv[2])
    except:
        logger.info(f"{sys.argv[2]} does not exist.")
else:
    r = template.replace("%%IDJS%%", master_js)
    r = r.replace("%%CSS%%", "preview.css")
    r = r.replace("%%JS%%", "preview.js")
    with open(sys.argv[2], "w") as f:
        print(r, file=f)
