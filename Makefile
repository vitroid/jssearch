# revised PDFをunlabelled/に練りこむ。
thumbs:
	ls pdf/*.pdf | sed -e 's/\.pdf/.jpg/' -e 's/pdf/tn/' | xargs make -k

# CONTENT=index.js tn .htpasswd cjscc70.css
deploy: ~/work/papers
	rsync -av $^ riis-kanri@www.riis.okayama-u.ac.jp:/var/www/html/

# rules
tn/%.jpg: pdf/%.pdf
	sips -s format jpeg "$<" -Z 200 --out "$@"

prepare: index.html noimage-ls.png papers.css papers.js readme.txt
	-mkdir ~/work/papers
	-rm -rf ~/work/papers/pdf
	-rm -rf ~/work/papers/tn
	-mkdir ~/work/papers/pdf
	cp $^ ~/work/papers
	cp -RL pdf/ ~/work/papers/pdf
	chmod -R a+r ~/work/papers/pdf
	cp -RL tn/ ~/work/papers/tn

#.htpasswd: make_htpasswd.py
#	python3 make_htpasswd.py
papers.js: paperpile_csv2js.py papers.csv
	-rm -rf pdf tn
	mkdir pdf tn
	python paperpile_csv2js.py

all: papers.js thumbs prepare deploy
