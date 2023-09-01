# search用のデータ生成

# ad, award, sympoはそれぞれのディレクトリの中で作業し、pdfとtnを生成し、jsonを作る。
# 一般講演は、masterとpdfを束ねる。

# deploy用のワークディレクトリ
BUILD=~/Unison/github/search/build

# 検索システムの所在 2023もここでいい。
SVELTE=~/Unison/github/search/svelte-app
SHELL=/bin/bash

# prepare for local test site
all: index.js AD/ads.js
	cp index.js AD/ads.js $(SVELTE)/src

# pdfとサムネイルをこっちにひっぱってくる。
hardlinks:
	-mkdir pdf tn
	python makehlink.py ../master/*.json

# 個人情報などを、別の場所にまとめることにした。
# PRIVATE=~/Unison/00Priority/2022錯討
PRIVATE=../private

# combine master/ and make a single big file for searching
general.json: $(wildcard ../master/*.json)
	python makeindex.py $(PRIVATE)/settings/setting.json ../master/*.json > $@


index.json: merge.py general.json Sympo/sympo.json Award/award.json
	python merge.py general.json Sympo/sympo.json Award/award.json > $@




# こちらはsearchの動作確認後でいい。
deploy:
# 認証ファイルの準備
	-mkdir $(BUILD)
	-mkdir $(BUILD)/chem
	-mkdir $(BUILD)/chem-access
	cp $(PRIVATE)/auth/jscc73.htpasswd $(BUILD)/chem-access/jscc73.htpasswd
	cp chem.htaccess $(BUILD)/chem/.htaccess
	chmod +r tn/* pdf/*
	rsync -av tn pdf --include="*/" --exclude="7[0-9][0-9][0-9][0-9].*" $(SVELTE)/public/




#### RULES
%.js: %.json
	echo -n "export const data = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@
