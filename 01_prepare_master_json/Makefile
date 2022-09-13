SHELL=/bin/bash
MASTER=../master

# 個人情報などを、別の場所にまとめることにした。
PRIVATE=~/Unison/00Priority/2022錯討


sync:
	rsync -av reg@www.chem.okayama-u.ac.jp:reg2/var/projects/apply/attach ..


prepare_master: $(PRIVATE)/1662990268.json decompose.py
	-mkdir $(MASTER)
	python decompose.py $< $(MASTER)


# プログラム編集のために、装飾文字が使えるexcelを生成する。あまりやりたくはない。
# ディレクトリ構造を再編してから実行していないので、動く保証はない。(2022)
contents.xlsx: ../master/*.json master2excel.py /Users/matto/Downloads/1658208630.tab
	python3 master2excel.py
