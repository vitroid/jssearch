



all:
	ls pdf/7????.pdf | sed -e 's/pdf/tn/' -e 's/pdf/jpg/' | xargs make -f 12.makefile


# 7xxxx.jpg
tn/%.jpg:
	python 12/tn.py master+pid.json $*
