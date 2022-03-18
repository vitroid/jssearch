all: zoom.js

zoom.json: Zoom\ URLs.xlsx 11/zoomconv.py
	python 11/zoomconv.py > $@

include 0.makefile
