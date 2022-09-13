SHELL=/bin/bash

all: ads.js
ads.json: preparead.py
	-mkdir ../pdf
	-mkdir ../tn
	python preparead.py > $@

ads.js: ads.json
	echo -n "export const ads = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@
