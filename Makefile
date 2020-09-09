all:

test-deploy: index.js tn index.html content.html
	-chmod -R +r tn index.js index.html content.html
	rsync -av tn index.js index.html content.html chemist@www.chem.okayama-u.ac.jp:Sites/search2020/

deploy: #push to riis
	-chmod -R +r p
	rsync -av p riis-kanri@www.riis.okayama-u.ac.jp:/var/www/html/

sync:
	rsync -av tn pdf unlabelled 2020.js index.html content.html ~/GoogleDrive/CJSCC70/
cnys:
	rsync -av ~/GoogleDrive/CJSCC70/ .

thumbs:
	ls pdf/*.pdf | sed -e 's/\.pdf/.jpg/' -e 's/pdf/tn/' | xargs make -k

tn/%.jpg: pdf/%.pdf
	sips -s format jpeg "$<" -Z 200 --out "$@"

pdf/%.pdf: unlabelled/%.pdf
	python addlabel.py $< $* $@

pdfs:
	ls unlabelled/*.pdf | sed -e s/unlabelled/pdf/ | xargs make -k

index.js: merge.py 2020.js Sympo/sympo.js Award/award.js
	python merge.py 2020.js Sympo/sympo.js Award/award.js > $@
