# 2021 Step 8
#

SHELL=/bin/bash


all: data.js


# re-make pdfs with label
data.json: master+pid.json 1/preparehtml.py 1/template.html
	-mkdir sheet
	-mkdir html
	-mkdir img
	-mkdir tn
	python 1/preparehtml.py $< > $@




include 0.makefile
