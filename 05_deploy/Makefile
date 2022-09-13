# search用のデータ生成

# ad, award, sympoはそれぞれのディレクトリの中で作業し、pdfとtnを生成し、jsonを作る。
# 一般講演は、masterとpdfを束ねる。


all: index.js

# pdfとサムネイルをこっちにひっぱってくる。
hardlinks:
	python makehlink.py ../master/*.json

# 個人情報などを、別の場所にまとめることにした。
PRIVATE=~/Unison/00Priority/2022錯討
SHELL=/bin/bash

# combine master/ and make a single big file for searching
general.json:
	python makeindex.py $(PRIVATE)/settings/setting.json ../master/*.json > $@


index.json: merge.py general.json Sympo/sympo.json Award/award.json
	python merge.py general.json Sympo/sympo.json Award/award.json > $@

%.js: %.json
	echo -n "const data = " > $@ ; \
	cat $< >> $@
	echo ";" >> $@
