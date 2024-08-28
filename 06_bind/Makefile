# 予稿を2ページごとに束ねる。
# masterを参照しよう。

all:
	make *.pdf

first:
	# 最後の行をコメントアウトしてから
	python3 bind.py

deploy:
	rsync -av *.pdf ~/'Dropbox/jscc74/abstract book/'

include makefile.*
