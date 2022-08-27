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

# moved to 13.makefile
# prepare-chem:
# # リンクファイルの準備 (/chem)
# 	chmod +r pdf/*.pdf
# 	chmod +r tn/*.jpg
# 	-mkdir chem
# 	-mkdir chem/pdf
# 	-mkdir chem/tn
# 	cp -a pdf/*[-_]*.pdf chem/pdf
# 	cp -a tn/*[-_]*.jpg chem/tn
# # 認証ファイルの準備
# 	-mkdir chem-access
# 	cp chem.htpasswd chem-access/jscc72.htpasswd
# 	cp chem.htaccess chem/.htaccess

# deploy-chem: svelte-app/public/build/bundle.js
# # prepare .htaccess and .htaccess
# 	rsync -av chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
# 	rsync -av chem/ reg@www.chem.okayama-u.ac.jp:Sites/jscc72
# 	rsync -av svelte-app/public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc72
