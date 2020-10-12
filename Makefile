SHELL=/bin/bash

.PHONY: dist/url2markdown

dist/restic-qt: venv
	( \
	. venv/bin/activate; \
	pyinstaller -F url2markdown/url2markdown.py; \
	)

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip3 install wheel; pip3 install -Ur requirements.txt
	touch venv/bin/activate

init:
	rm -rf venv
	python3 -m venv venv
	. venv/bin/activate
	( \
	pip3 install -r requirements.txt; \
	pip3 install -e .; \
	)

test:
	@. venv/bin/activate
	@( \
	cd tests/; \
	pytest; \
	)

clean: distclean
	rm -rf build/
	rm -rf venv/
	find -iname "*.pyc" -delete

distclean:
	rm -rf dist/
