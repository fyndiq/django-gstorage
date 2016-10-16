.PHONY: test release

test:
	py.test --traceconfig

release:
	python setup.py sdist bdist_wheel register upload -s


