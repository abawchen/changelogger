clean:
	@rm -f .coverage 2> /dev/null
	@rm -rf .eggs 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@rm -rf ./changelogger/.cache 2> /dev/null
	@rm -rf build 2> /dev/null
	@rm -rf dist 2> /dev/null
	@rm -rf graphene_mongo.egg-info 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

lint:
	@flake8 changelogger

test: clean lint
	py.test --cov=changelogger

