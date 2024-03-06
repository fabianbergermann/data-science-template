.PHONY: tests docs init format lint

init:
	@echo "Initializing Git..."
	git init --initial-branch=main
	{% if cookiecutter.dependency_manager == "poetry" %}
	@echo "Installing dependencies..."
	poetry install --no-root
	poetry shell
	{% else %}
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	{% endif %}

tests:
	pytest

docs:
	mkdocs build
	mkdocs serve

format:
	ruff format

lint:
	ruff check