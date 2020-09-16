#!/usr/bin/env python
from replacer import repl
import sys

d = {
    "%%PDFBASE%%"   : "http://www.riis.okayama-u.ac.jp/p/"
}

fin = sys.argv[1]
fout = sys.argv[2]
repl(d, fin, fout)
