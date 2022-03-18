all: ads.js
ads.json: 10/preparead.py
	python 10/preparead.py > $@

include 0.makefile
