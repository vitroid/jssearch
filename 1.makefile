# 2021 Step 1
#
# 管理画面から落としてきたjsonから、preview htmlとfigureとTOC thumbsを生成する。
# ファイルの名前は、全部登録番号におきかえる。

SHELL=/bin/bash


all: data.js


pre.json: 1627394850.json 1/preprocess.py
	python 1/preprocess.py $< > $@
# and hand-edit the pre.json to make the master.json

data.json: master.json 1/preparehtml.py 1/template.html
	-mkdir sheet
	-mkdir html
	-mkdir img
	-mkdir tn
	python 1/preparehtml.py $< > $@




include 0.makefile
