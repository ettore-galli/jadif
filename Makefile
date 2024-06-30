
lint:
	black jadif/ tests/
	ruff check jadif/ tests/
	mypy jadif/ tests/

test:
	pytest tests/

all: lint test
	