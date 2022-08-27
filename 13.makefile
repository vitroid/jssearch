# 13.makefile: for svelte

all: index.js
	cp index.js svelte-app/src
	rsync -av tn pdf --include="*/" --exclude="7[0-9][0-9][0-9][0-9].*" svelte-app/public/



prepare-chem:
# 認証ファイルの準備
	-mkdir build
	-mkdir build/chem
	-mkdir build/chem-access
	cp chem.htpasswd build/chem-access/jscc72.htpasswd
	cp chem.htaccess build/chem/.htaccess

deploy-chem: svelte-app/public/build/bundle.js
# prepare .htaccess and .htaccess
	rsync -av build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av svelte-app/public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc72


include 0.makefile
