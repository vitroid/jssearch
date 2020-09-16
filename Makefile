all:

# revised PDFをunlabelled/に練りこむ。
prepare0:
	python3 prep_pdf.py Revised_pdf_Oral
	python3 prep_pdf.py Revised_pdf_Poster

pdfs:
	ls unlabelled/*.pdf | sed -e s/unlabelled/pdf/ | xargs make -k

thumbs:
	ls pdf/*.pdf | sed -e 's/\.pdf/.jpg/' -e 's/pdf/tn/' | xargs make -k

2020.js:
	rsync -av reg@www.chem.okayama-u.ac.jp:github/reg2-projects/apply2/2020.js .

index.js: merge.py 2020.js Sympo/sympo.js Award/award.js
	python merge.py 2020.js Sympo/sympo.js Award/award.js > $@

CONTENT=index.js tn .htpasswd cjscc70.css

prepare: riis/index.html riis/.htaccess chem/index.html chem/.htaccess $(CONTENT)

deploy: deploy-riis deploy-chem

deploy-riis: riis/index.html riis/.htaccess $(CONTENT)
	chmod -R +r $^
	rsync -av $^ riis-kanri@www.riis.okayama-u.ac.jp:/var/www/html/cjscc70
	chmod -R +r p
	rsync -av p/ riis-kanri@www.riis.okayama-u.ac.jp:/var/www/html/p/

deploy-chem: chem/index.html chem/.htaccess $(CONTENT)
	chmod -R +r $^
	rsync -av $^ reg@www.chem.okayama-u.ac.jp:Sites/cjscc70/
	chmod -R +r p
	rsync -av p/ reg@www.chem.okayama-u.ac.jp:Sites/cjscc70/p/

sync:
	rsync -av tn pdf unlabelled 2020.js index.html content.html ~/GoogleDrive/CJSCC70/
cnys:
	rsync -av ~/GoogleDrive/CJSCC70/ .

# rules
tn/%.jpg: pdf/%.pdf
	sips -s format jpeg "$<" -Z 200 --out "$@"

pdf/%.pdf: unlabelled/%.pdf
	python addlabel.py $< $* $@

p/AD%.pdf: pdf/AD%.pdf
	cp $< $@

riis/%: %.in makeriis.py
	python3 makeriis.py $< $@
chem/%: %.in makechem.py
	python3 makechem.py $< $@

.htpasswd: make_htpasswd.py
	python3 make_htpasswd.py
