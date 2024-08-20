# import glob
# import re
import sys
from logging import INFO, basicConfig, getLogger

# import os
import pypdf

basicConfig(level=INFO)
logger = getLogger()

files = sorted(sys.argv[1:])

writer = pypdf.PdfWriter()
for filename in files:
    reader = pypdf.PdfReader(open(filename, "rb"))
    page = reader.pages[0]
    writer.add_page(page)

with open(f"sheet.pdf", "wb") as f:
    writer.write(f)
