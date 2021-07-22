# Step 2
# Render PDFs from html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

all:
	-mkdir pdf
	-cd html; rm *.css *.js; ln -s ../2/* ../data.js ../img ../attach .
	ls html/*.html | sed -e 's/html/pdf/g' | xargs make -k -f 2.makefile
pdf/%.pdf: html/%.html $(wildcard 2/*) data.js attach img
	$(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header
# html/template.%:
# 	-cd html; ln -s ../2/template.$* .
# html/preview.%:
# 	-cd html; ln -s ../2/preview.$* .
# html/data.js:
# 	-cd html; ln -s ../data.js .
# html/attach:
# 	-cd html; ln -s ../attach .
# html/img:
# 	-cd html; ln -s ../img .
