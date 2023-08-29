# Step 2
# Render PDFs from html
# (And add presentation labels if possible)

SHELL=/bin/bash
RENDERER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


all: $(patsubst %.json, %.js, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, %/index.html, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, %/figure.jpg, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, %/index.pdf, $(wildcard ../master/*.json)) \
$(patsubst ../master/%.json, %/tocg.jpg, $(wildcard ../master/*.json))
	echo Done.

%/index.html: makehtml.py
	-mkdir $*
	python3 makehtml.py $* > $@

%/preview.css: preview.css
	cd $*; ln -s ../preview.css .
%/preview.js:
	cd $*; ln -s ../preview.js .

%/tocg.jpg: ../master/%.json maketocg.py %/index.pdf
	-mkdir $*
	python3 maketocg.py $<
%/figure.jpg: ../master/%.json makefigure.py
	-mkdir $*
	python3 makefigure.py $<

%.js: %.json
	echo -n "const data = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@

# all:
# 	-mkdir pdf
# 	-cd html; rm *.css *.js; ln -s ../2/* ../img ../attach ../master .
# 	ls html/*.html | sed -e 's/html/pdf/g' | xargs make -k -j 8 -f 2.makefile

%/index.pdf: %/index.html ../master/%.js %/preview.css %/preview.js
	-mkdir $*
	$(RENDERER) --headless $< --print-to-pdf=$@ --print-to-pdf-no-header

# %.js: %.json
# 	echo -n "var data = " > $@
# 	cat $< >> $@
# 	echo ";" >> $@
