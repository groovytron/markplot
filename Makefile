.PHONY: dist, upload

dist:
	python setup.py sdist
	python setup.py bdist_wheel

upload: dist
	twine upload dist/*



