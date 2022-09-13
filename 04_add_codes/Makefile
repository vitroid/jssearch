# 個人情報などを、別の場所にまとめることにした。
PRIVATE=~/Unison/00Priority/2022錯討
SHELL=/bin/bash


# masterに講演番号を書きこみ、対応表をcodes.txtに残す。
# codes.txtは、受付システムに講演番号を反映させるのに利用する。
codes.txt: $(PRIVATE)/プログラム編成用_72_7f_松本先生送付用.xlsx ../master/ pid.py
	python pid.py $< '(参考)発表一覧' ../master > codes.txt
