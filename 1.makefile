# 2021 Step 1
#
# 管理画面から落としてきたjsonから、preview htmlとfigureとTOC thumbsを生成する。
# ファイルの名前は、全部登録番号におきかえる。

SHELL=/bin/bash


all: data.js

data.json: 1626878951.json 1/preparehtml.py
	-mkdir html
	-mkdir img
	-mkdir tn
	python 1/preparehtml.py 1626878951.json > data.json

include 0.makefile
