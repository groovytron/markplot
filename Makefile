.PHONY: dist, upload, clean

dist:
	python setup.py sdist
	python setup.py bdist_wheel

upload: dist
	twine upload dist/*

clean:
	rm -rf dist


