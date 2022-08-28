# 2021 Step 1
#
# 管理画面から落としてきたjsonから、preview htmlとfigureとTOC thumbsを生成する。
# ファイルの名前は、全部登録番号におきかえる。

SHELL=/bin/bash


all: master


pre.json: 1661415966.json 1/preprocess.py
	python 1/preprocess.py $< > $@
# and hand-edit the pre.json to make the master.json

master: pre.json 1/preparemaster.py 1/template.html
	-mkdir sheet
	-mkdir html
	-mkdir img
	-mkdir tn
	-mkdir master
	python 1/preparemaster.py $<

# プログラム編成委員会の結果との突き合わせと修正はverify2022.ipynbで行った。
# 修正はmaster/の個別jsonに加える。
