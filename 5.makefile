# add presentation ID to master/*.json
all: master/ 5/pid.py
	python 5/pid.py master/*.json
