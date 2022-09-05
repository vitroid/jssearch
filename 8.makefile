# 2021 Step 8
#

SHELL=/bin/bash


all:
	echo nothing.

# re-make pdfs with label
html/%.html: master/%.json 8/preparehtml.py 1/template.html
	-mkdir sheet
	-mkdir html
	-mkdir img
	-mkdir tn
	python 8/preparehtml.py $<




include 0.makefile
