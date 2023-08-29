"""
reg2のDBからとってきた内容とこちらのmasterの内容の差を調べる。

差分を反映させるために、diffを生成したいが、うまくいかないかも。
"""

import json
import sys
import glob
from logging import getLogger, basicConfig, INFO, DEBUG
import re


basicConfig(level=INFO)
logger = getLogger()

with open(sys.argv[1]) as f:
    original = json.load(f)

ids = set()
for fname in glob.glob(f"{sys.argv[2]}/*.json"):
    with open(fname) as f:
        modified = json.load(f)
        id = modified["id"]

        ids.add(id)

        msg = ""
        # 講演番号が変なやつを弾く
        m = re.search(r"^[0-9]+[A-Za-z]+-[0-9]+$", modified["code"])
        if m is None:
            msg += f"  Unassigned for presentation: {modified['code']}\n"
        
        else:
            # keys only in original
            keys = set(original[id]) - set(modified)
            for key in keys:
                msg += f"  Deleted: {key} = {original[key]}\n"

            # keys only in modified
            keys = set(modified) - set(original[id])
            for key in keys:
                if key != "code":
                    msg += f"  Added: {key} = {modified[key]}\n"

            # 共通のkeyで、値が違うものを表示する。
            for key in sorted(list(set(modified) & set(original[id]))):
                if original[id][key] != modified[key]:
                     msg += f"  Modified: {key}\n"
                     msg += f"  {key}={original[id][key]}\n"
                     msg += f"  {key}={modified[key]}\n"

        if msg != "":
            logger.info(f"{id}##############################\n"+msg)




# originalにしかないrecord
diff = set(original) - ids
logger.info(f"消されたレコード: {diff}")

# あとから追加されたrecord
diff = ids - set(original)
logger.info(f"追加されたレコード: {diff}")