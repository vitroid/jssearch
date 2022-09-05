# Step 2
# Render PDFs from html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

all:
	-mkdir pdf
	-cd html; rm *.css *.js; ln -s ../2/* ../img ../attach ../master .
	ls html/*.html | sed -e 's/html/pdf/g' | xargs make -k -j 8 -f 2.makefile
pdf/%.pdf: html/%.html $(wildcard 2/*) master/%.js # attach img
	$(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header

%.js: %.json
	echo -n "var data = " > $@
	cat $< >> $@
	echo ";" >> $@
