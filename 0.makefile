# Step 0
# Sync attachments from reg server

SHELL=/bin/bash

sync:
	rsync -av reg@www.chem.okayama-u.ac.jp:reg2/var/projects/apply2/attach .

%.js: %.json
	echo -n "data = " > $@
	cat $< >> $@
	echo ";" >> $@
