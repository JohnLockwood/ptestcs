init:
	pip install pipenv --upgrade
	pipenv install --dev

publish:
	python setup.py sdist bdist
	rm -fr dist .egg *.egg-info
	
test:
	pipenv run python3 tests/demo_test.py
