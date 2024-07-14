
install:
	pip install .
	pip install ."[format]"
	pip install ."[lint]"
	pip install ."[test]"
	pip install ."[build]"

lint:
	black jadif/ tests/ demo/
	ruff check jadif/ tests/ demo/
	mypy jadif/ tests/ demo/

test:
	pytest tests/ demo/

all: lint test

build-project:
	ci/build-project
	