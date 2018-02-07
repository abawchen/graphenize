clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@rm -rf .cache 2> /dev/null
	@rm -rf .pytest_cache 2> /dev/null

test: clean
	pytest
