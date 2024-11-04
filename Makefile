.PHONY: install format test clean run build

install:
	uv pip install -e ".[dev]"

format:
	./scripts/format.sh

test:
	pytest

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	streamlit run src/app.py

build:
	uv run scripts/convert_to_html.py