# Step 3
# Make index.for search

all: 6.json

6.json: master+pid.json 6/makeindex.py 6/makehlink.py
	python 6/makeindex.py < $< > $@
	# make hard links of pdf
	python 6/makehlink.py < $<

include 0.makefile
