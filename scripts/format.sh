#!/bin/bash
set -e

echo "Running black..."
black .

echo "Running isort..."
isort .

echo "Running mypy..."
mypy src/

echo "Running pytest..."
pytest
