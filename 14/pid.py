import json
import sys

import pandas as pd

book = sys.argv.pop(1)
sheet = sys.argv.pop(1)

program = pd.read_excel(book, sheet_name=sheet)
# program = program.astype({'id': 'int32'})

for id, code in zip(program["id"], program["ポスター発表\n講演番号"]):
    if str(id) != "nan":
        print(code, int(id))
