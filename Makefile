clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@rm -f graphenize/tests/build/* 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@rm -rf .pytest_cache 2> /dev/null

lint:
	@flake8 graphenize

test: clean lint
	py.test --cov=graphenize
