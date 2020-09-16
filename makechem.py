#!/usr/bin/env python
from replacer import repl
import sys

d = {
    "%%PDFBASE%%"   : "http://www.chem.okayama-u.ac.jp/~reg/cjscc70/p/",
    }

fin = sys.argv[1]
fout = sys.argv[2]
repl(d, fin, fout)
