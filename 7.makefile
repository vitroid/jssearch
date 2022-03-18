all: index.js

index.json: 7/merge.py 6.json Sympo/sympo.json Award/award.json
	python 7/merge.py 6.json Sympo/sympo.json Award/award.json > $@

include 0.makefile
