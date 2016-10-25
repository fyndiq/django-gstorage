.PHONY: clean release test

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete

test:
	py.test

release:
	python setup.py sdist bdist_wheel register upload -s
