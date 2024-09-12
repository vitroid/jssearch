# Step 2
# Render PDFs from html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


all: genpdf \
$(patsubst ../master/%.json, ../master/%.js, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/index.html, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/figure.jpg, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/tocg.jpg, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/index.pdf, $(wildcard ../master/*.json))
	echo Done.


genpdf:
	mkdir genpdf
genpdf/%/index.html: makehtml.py ../master/%.js ../master/%.json
	-mkdir genpdf/$*
	python3 makehtml.py $* $@

# % is subst by genpdf/7xxxx
%/preview.css: preview.css
	cd $*; ln -s ../../preview.css .
%/preview.js:
	cd $*; ln -s ../../preview.js .

genpdf/%/tocg.jpg: ../master/%.json maketocg.py genpdf/%/index.pdf
	-mkdir genpdf/$*
	python3 maketocg.py $<
genpdf/%/figure.jpg: ../master/%.json makefigure.py
	-mkdir genpdf/$*
	python3 makefigure.py $<

%.js: %.json
	echo -n "const data = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@

genpdf/%/index.pdf: genpdf/%/index.html ../master/%.js genpdf/%/preview.css genpdf/%/preview.js
	-mkdir genpdf/$*
	-[ -e $< ] && $(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header
	-[ -e $< ] && python3 single_page.py $@


sheet.pdf: $(wildcard ../03_sheetpdf/genpdf/*/index.pdf)
	python3 ./bind.py $^
