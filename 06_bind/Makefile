# 予稿を2ページごとに束ねる。
# masterを参照しよう。

all:
	make *.pdf

first:
	python3 bind.py

deploy:
	rsync -av *.pdf ~/'Dropbox/jscc73/abstract book/'

include makefile.*
