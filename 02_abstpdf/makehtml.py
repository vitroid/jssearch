import sys

with open("template.html") as f:
    template = f.read()

id = sys.argv[1]
r = template.replace("%%IDJS%%", f"../../../master/{id}.js")
r = r.replace("%%CSS%%", "preview.css")
r = r.replace("%%JS%%", "preview.js")
print(r)
