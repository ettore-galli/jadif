
lint:
	black src/ tests/
	ruff check src/ tests/
	mypy src/ tests/

test:
	pytest tests/

all: lint test
	