all:

push:
	rsync -av tn pdf 2020.js index.html chemist@www.chem.okayama-u.ac.jp:Sites/search2020/

thumbs:
	ls pdf/*.pdf | sed -e 's/\.pdf/.jpg/' -e 's/pdf/tn/' | xargs make

tn/%.jpg: pdf/%.pdf
	sips -s format jpeg $< -Z 200 --out $@
