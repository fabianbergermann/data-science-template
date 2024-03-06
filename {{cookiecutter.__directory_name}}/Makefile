.PHONY: tests docs

deps: 
	@echo "Initializing Git..."
	git init
	{% if cookiecutter.dependency_manager == "poetry" %}
	@echo "Installing dependencies..."
	poetry install --no-root
	{% else %}
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	{% endif %}
tests:
	pytest

docs:
    mkdocs build
    mkdocs serve
