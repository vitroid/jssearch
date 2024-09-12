# import glob
# import re
import sys
from logging import INFO, basicConfig, getLogger

# import os
import pypdf

basicConfig(level=INFO)
logger = getLogger()

filename = sys.argv[1]

with open(filename, "rb") as f:
    reader = pypdf.PdfReader()
page = reader.pages[0]
writer = pypdf.PdfWriter()
writer.add_page(page)

with open(filename, "wb") as f:
    writer.write(f)
