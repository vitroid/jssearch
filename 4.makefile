# Step 2
# Render datasheet PDFs from sheet/*.html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

all:
	-mkdir sheetpdf
	-cd sheet; rm *.css *.js; ln -s ../4/* ../master ../img ../attach .
	ls sheet/*.html | sed -e 's/sheet/sheetpdf/g' -e 's/html/pdf/g' | xargs make -f 4.makefile -j 8
sheetpdf/%.pdf: sheet/%.html $(wildcard 4/*) master/%.js attach img
	$(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header

%.js: %.json
	echo -n "var data = " > $@
	cat $< >> $@
	echo ";" >> $@
