import json
import sys


with open(sys.argv[1]) as f:
    data = json.load(f)

for id in sorted(data, key=lambda x:data[x]["code"]):
    style = data[id]["style"]
    if style in "34":
        email = data[id]["email"]
        name = data[id]["applicant.name"]
        code = data[id]["code"]
        print(f"{code}\t{email}\t{name}\t{id}")
