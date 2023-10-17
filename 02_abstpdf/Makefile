# Step 2
# Render PDFs from html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


all: $(patsubst %.json, %.js, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/index.html, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/figure.jpg, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/index.pdf, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, genpdf/%/tocg.jpg, $(wildcard ../master/*.json))
	echo Done.

genpdf/%/index.html: makehtml.py
	-mkdir genpdf/$*
	python3 makehtml.py $* > $@

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

# all:
# 	-mkdir pdf
# 	-cd html; rm *.css *.js; ln -s ../2/* ../img ../attach ../master .
# 	ls html/*.html | sed -e 's/html/pdf/g' | xargs make -k -j 8 -f 2.makefile

genpdf/%/index.pdf: genpdf/%/index.html ../master/%.js genpdf/%/preview.css genpdf/%/preview.js
	-mkdir genpdf/$*
	$(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header

# %.js: %.json
# 	echo -n "var data = " > $@
# 	cat $< >> $@
# 	echo ";" >> $@
