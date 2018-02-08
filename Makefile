clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@rm -f graphene_from_json/tests/build/* 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@rm -rf .pytest_cache 2> /dev/null

test: clean
	pytest
