all:

sync:
	rsync -av --exclude='*.jpg' --exclude='*.png' --exclude='*.pdf' --exclude='Makefile' --exclude='*.tgz' --exclude='tn/' --exclude='tmp/' --exclude='*~' chemist@www.chem.okayama-u.ac.jp:Sites/search/ .
