# 2021 Step 1
#
# 管理画面から落としてきたjsonから、preview htmlとfigureとTOC thumbsを生成する。
# ファイルの名前は、全部登録番号におきかえる。

SHELL=/bin/bash


all: master


pre.json: 1661415966.json 1/preprocess.py
	python 1/preprocess.py $< > $@
# and hand-edit the pre.json to make the master.json

master: master.json 1/preparemaster.py 1/template.html
	-mkdir sheet
	-mkdir html
	-mkdir img
	-mkdir tn
	-mkdir master
	python 1/preparemaster.py $<

# master/を生成したあとの、手作業の自動化。

# 1. 和英題名の入れ替え 2022
ejtitle:
	for n in 72131 72166 72412 72594 72320 72622 72321 72028 72027 72211 72559 72220 72431 72572 72088 72315 72600 72207; do python3 1/exchange_ej_titles.py $$n; done

# 2. 英文題名のtitlecase化
titlecase:
	for n in `(cd master; ls *.json) | sed -e s/.json// `; do python3 1/add_titlecase.py $$n; done
