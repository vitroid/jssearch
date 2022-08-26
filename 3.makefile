# 2022 新設
# master/のレコードから、書式ありexcel表を作る。
# masterに修正を加えたら、すぐに作りなおせるように。
# master/を本当のmaster databaseとする。

contents.xlsx: master/* 3/master2excel.py
	python3 3/master2excel.py

