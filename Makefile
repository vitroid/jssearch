all:

# revised PDFをunlabelled/に練りこむ。
prepare:
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


deploy: index.js tn parsed/content.html parsed/index.html .htpasswd .htaccess cjscc70.css
	-chmod -R +r tn index.js parsed/* .htpasswd .htaccess
	rsync -av tn index.js cjscc70.css chemist@www.chem.okayama-u.ac.jp:Sites/cjscc70/
	rsync -av parsed/ chemist@www.chem.okayama-u.ac.jp:Sites/cjscc70/
#push pdf to riis
	-chmod -R +r p
	rsync -av p riis-kanri@www.riis.okayama-u.ac.jp:/var/www/html/
# auth
	rsync -av .htaccess .htpasswd chemist@www.chem.okayama-u.ac.jp:Sites/cjscc70/

sync:
	rsync -av tn pdf unlabelled 2020.js index.html content.html ~/GoogleDrive/CJSCC70/
cnys:
	rsync -av ~/GoogleDrive/CJSCC70/ .

# rules
tn/%.jpg: pdf/%.pdf
	sips -s format jpeg "$<" -Z 200 --out "$@"

pdf/%.pdf: unlabelled/%.pdf
	python addlabel.py $< $* $@

parsed/%: %.in
	python3 maketest.py < $< > $@

.htpasswd: make_htpasswd.py 
	python3 make_htpasswd.py
