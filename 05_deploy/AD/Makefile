all: ads.js
ads.json: preparead.py
	-mkdir ../pdf
	-mkdir ../tn
	python preparead.py > $@

ads.js: ads.json
	echo -n "const ads = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@
