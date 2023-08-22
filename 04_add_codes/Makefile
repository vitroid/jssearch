# 個人情報などを、別の場所にまとめることにした。
PRIVATE=../private
SHELL=/bin/bash


# masterに講演番号を書きこみ、対応表をcodes.txtに残す。
# codes.txtは、受付システムに講演番号を反映させるのに利用する。
codes.txt: $(PRIVATE)/ID発表番号対応表.xlsx ../master/ pid.py
	# python pid.py $< '(参考)発表一覧' ../master > codes.txt # 2022
	python pid.py $< 'Poster' ../master > codes.txt
	python pid.py $< 'Oral' ../master >> codes.txt
