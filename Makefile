SHELL=/bin/bash

.PHONY: dist/restic_qt

dist/restic-qt: venv
	( \
	. venv/bin/activate; \
	pyinstaller -F url2markdown; \
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
	TEST_REPO=/tmp/test-resticqt; \
	export RESTIC_REPOSITORY=$$TEST_REPO; \
	export RESTIC_PASSWORD='foo'; \
	rm -rf $$TEST_REPO; \
	mkdir $$TEST_REPO; \
	restic init; \
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
