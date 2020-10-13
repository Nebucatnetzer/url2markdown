SHELL=/bin/bash

.PHONY: dist/url2markdown

dist/url2markdown: venv
	( \
	. venv/bin/activate; \
	pyinstaller -F url2markdown/__main__.py -n url2markdown; \
	)

venv: venv/bin/activate

venv/bin/activate: requirements/base.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip3 install wheel; pip3 install -Ur requirements/base.txt
	touch venv/bin/activate

init:
	rm -rf venv
	python3 -m venv venv
	. venv/bin/activate
	( \
	pip3 install -r requirements/development.txt; \
	pip3 install -e .; \
	)

test:
	@. venv/bin/activate
	@( \
	pytest --cov=. --cov-report=html; \
	)

clean: distclean
	rm -rf build/
	rm -rf venv/
	find -iname "*.pyc" -delete

distclean:
	rm -rf dist/
