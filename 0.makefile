# Step 0
# Sync attachments from reg server

SHELL=/bin/bash

sync:
	rsync -av reg@www.chem.okayama-u.ac.jp:reg2/var/projects/apply/attach .

%.js: %.json
	-if [ x"$*" = x"index" ]; then \
	    echo -n "export const data = " > $@ ; \
	else \
	    echo -n "export const $* = " > $@ ; \
	fi
	cat $< >> $@
	echo ";" >> $@

%: %.in replacer.py zoom.js remo.js
	python3 replacer.py < $< > $@

DROPBOX=/Users/matto/Dropbox/錯体化学会第71回討論会/検索
deploy-dropbox: remo.js zoom.js search.css search.js ads.js index.js jscc71.js index.html
	# -rm 3Aa-04.pdf
	# -mv pdf/3Aa-04.pdf .
	chmod +r pdf/*.pdf
	chmod +r tn/*.jpg
	cp -r $^ $(DROPBOX)
	-mkdir $(DROPBOX)/pdf
	-mkdir $(DROPBOX)/tn
	cp -r pdf/*[-_]*.pdf $(DROPBOX)/pdf
	cp -r tn/*[-_]*.jpg $(DROPBOX)/tn

prepare-chem: remo.js zoom.js search.css search.js ads.js index.js jscc71.js index.html
	# -rm 3Aa-04.pdf
	# -mv pdf/3Aa-04.pdf .
	chmod +r pdf/*.pdf
	chmod +r tn/*.jpg
	-mkdir chem
	cp -rf $^ chem
	-mkdir chem/pdf
	-mkdir chem/tn
	cp -a pdf/*[-_]*.pdf chem/pdf
	cp -a tn/*[-_]*.jpg chem/tn
	-mkdir chem-access
	cp chem.htpasswd chem-access/jscc71.htpasswd
	cp chem.htaccess chem/.htaccess

deploy-chem: #prepare-chem
# prepare .htaccess and .htaccess
	rsync -av chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av chem/ reg@www.chem.okayama-u.ac.jp:Sites/jscc71
