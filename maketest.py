#!/usr/bin/env python
from logging import getLogger
import sys
from replacer import line_replacer


d = {
    "%%URLBASE%%"   : "."
}

for line in sys.stdin:
    line = line_replacer(line, d)
    print(line, end="")
