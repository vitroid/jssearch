all: index.js
	cp index.js svelte-app/src
	rsync -av tn pdf svelte-app/public/

include 0.makefile
