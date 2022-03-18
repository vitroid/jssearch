# add presentation ID to master.json
master+pid.json: master.json 5/pid.py
	python 5/pid.py < $< > $@
