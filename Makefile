.PHONY: lint format typecheck test check

lint:
	uv run ruff check src/

format:
	uv run ruff format src/

typecheck:
	uv run pyright src/

test:
	uv run pytest

check: lint typecheck
