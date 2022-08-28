# Step 3
# Make index.for search

all: 6.json

6.json: master 6/makeindex.py 6/makehlink.py
	python 6/makeindex.py master/*.json > $@
	# make hard links of pdf
	python 6/makehlink.py master/*.json

include 0.makefile
