.PHONY: tests docs servedocs init format lint all install {% if cookiecutter.use_sqlfluff == "yes" %} format-sql {% endif %}


init: git-init install

git-init:
	@echo "Initializing Git..."
	git init --initial-branch=main
	git add .
	git commit -m "Initial commit, using the Cookiecutter Data Science template"

install:
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

servedocs:
	cd docs && mkdocs serve

lint:
	ruff check

format:
	ruff check --fix
	ruff format

{% if cookiecutter.use_sqlfluff == "yes" %}
format-sql:
	sqlfluff fix .

{% endif %}
.DEFAULT_GOAL := all

all: format tests docs