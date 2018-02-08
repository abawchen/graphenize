clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@rm -f .coverage 2> /dev/null
	@rm -f graphenize/tests/build/* 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@rm -rf .eggs 2> /dev/null
	@rm -rf .pytest_cache 2> /dev/null
	@rm -rf dist 2> /dev/null
	@rm -rf graphenize.egg-info 2> /dev/null

lint:
	@flake8 graphenize

test: clean lint
	py.test --cov=graphenize

deploy: clean
	python setup.py sdist upload -r pypi

