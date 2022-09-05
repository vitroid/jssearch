# make the code list for reg2.system
codes.txt: プログラム編成用_72_7f_松本先生送付用.xlsx 14/pid.py
	python 14/pid.py $< '(参考)発表一覧' > $@
