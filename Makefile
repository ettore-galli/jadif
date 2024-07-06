
install:
	pip install .
	pip install ."[format]"
	pip install ."[lint]"
	pip install ."[test]"
	pip install ."[build]"

lint:
	black jadif/ tests/
	ruff check jadif/ tests/
	mypy jadif/ tests/

test:
	pytest tests/

all: lint test

build-project:
	ci/build-project
	