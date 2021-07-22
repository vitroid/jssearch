# Step 3
# Make index.for search

all: index.js

index.json: data.json 3/makeindex.py
	python 3/makeindex.py < $< > $@

include 0.makefile
