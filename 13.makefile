# 13.makefile: for svelte


# prepare for local test site
all: index.js AD/ads.js
	cp index.js AD/ads.js svelte-app/src



prepare-chem:
# 認証ファイルの準備
	-mkdir build
	-mkdir build/chem
	-mkdir build/chem-access
	cp jscc72.htpasswd build/chem-access/jscc72.htpasswd
	cp chem.htaccess build/chem/.htaccess
	chmod +r tn/* pdf/*
	rsync -av tn pdf --include="*/" --exclude="7[0-9][0-9][0-9][0-9].*" svelte-app/public/

test-deploy-chem: svelte-app/public/build/bundle.js
	rsync -av build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/test72
	rsync -av svelte-app/public/ reg@www.chem.okayama-u.ac.jp:Sites/test72

deploy-chem: svelte-app/public/build/bundle.js
	# WARNING THIS OVERWRITES THE PASSWORD FILE
	rsync -av build/chem-access/ reg@www.chem.okayama-u.ac.jp:.reg/
	rsync -av build/chem/.htaccess reg@www.chem.okayama-u.ac.jp:Sites/jscc72
	rsync -av svelte-app/public/ reg@www.chem.okayama-u.ac.jp:Sites/jscc72




include 0.makefile
