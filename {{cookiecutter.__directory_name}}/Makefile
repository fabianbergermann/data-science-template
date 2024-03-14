.PHONY: tests docs init format lint style fullcheck

init:
	@echo "Initializing Git..."
	git init --initial-branch=main
	@echo "Installing dependencies..."
	{% if cookiecutter.dependency_manager == "poetry" %}
	poetry config --local virtualenvs.in-project true
	poetry install
	poetry shell
	{% else %}
	pip install -r requirements.txt
	{% endif %}

tests:
	pytest

docs:
	cd docs && mkdocs build
	cd docs && mkdocs serve

format:
	ruff format

lint:
	ruff check

style: format
	ruff check --fix

fullcheck: style tests docs
