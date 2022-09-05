# add presentation ID to master/*.json
all: プログラム編成用_72_7f_松本先生送付用.xlsx master/ 5/pid.py
	python 5/pid.py $< (参考)発表一覧 master/*.json
