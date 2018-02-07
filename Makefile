clean:
	rm -rf .eggs build cryptoportfolio.egg-info dist .mypy_cache

test:
	flake8 .
	mypy --ignore-missing-imports .
	python3 setup.py test

install: test
	python3 setup.py install