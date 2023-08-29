# Make search index for javascript and copy pdfs to ../unlabelled folder

# 個人情報などを、別の場所にまとめることにした。
PRIVATE=~/Unison/00Priority/2022錯討

award.json: ./award.xlsx award.py Aw*.pdf
	python award.py $< > $@
