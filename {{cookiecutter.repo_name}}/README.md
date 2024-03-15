# {{cookiecutter.project_name}}

## Tools used in this project
* [Dynaconf](https://www.dynaconf.com): Manage configuration
* [MkDocs](https://www.mkdocs.org): Slick project documentation. With search functionality. Using a material theme. 
{% if cookiecutter.dependency_manager == "poetry" %}
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)
{% endif %}

## Project Structure

```bash
.
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   └── raw                         # raw data
├── docs                            # documentation for your project
├── models                          # store models
├── notebooks                       # store notebooks
├── references                      # Data dictionaries, manuals, and all other explanatory materials
├── reports                         # Generated analysis as HTML, PDF, LaTeX, etc.
├── {{ cookiecutter.package_name }}                # store source code
├── tests                           # store tests
├── Makefile                        # store useful commands to set up the environment
├── README.md                       # describe your project
{% if cookiecutter.use_sqlfluff == "yes" -%}
├── .sqlfluff                       # config file for SQL formatter SQLFluff
{%- endif %}
├── config.py                       # entry point for configs
{% if cookiecutter.dependency_manager == "pip" -%}
├── pyproject.toml                  # Configure black
{% elif cookiecutter.dependency_manager == "poetry" -%}
├── pyproject.toml                  # dependencies for poetry
{%- endif %}
└──  .gitignore                      # ignore files that cannot commit to Git
```

## Set up the environment

{% if cookiecutter.dependency_manager == "poetry" %}
## TL;DR
In the project root (make sure no virtual env is active)

```bash
make init  # init git and install all dependencies
make style  # check and format, using ruff
make tests  # check that all is working
make docs  # compile docs. To serve locally, run: make servedocs
make all  # this is a shortcut for (make) style, tests, docs
```

Or, follow this full description 
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Activate the virtual environment:
```bash
poetry shell
```
3. Install dependencies:
- To install all dependencies from pyproject.toml, run:
```bash
poetry install
```
- To install only production dependencies, run:
```bash
poetry install --only main
```
- To install a new package, run:
```bash
poetry add <package-name>
```
{% else %}
1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment:

- For Linux/MacOS:
```bash
source venv/bin/activate
```
- For Command Prompt:
```bash
.\venv\Scripts\activate
```
3. Install dependencies:
- To install all dependencies, run:
```bash
pip install -r requirements-dev.txt
```
- To install only production dependencies, run:
```bash
pip install -r requirements.txt
```
- To install a new package, run:
```bash
pip install <package-name>
```
{% endif %}


## Auto-generate API documentation

To auto-generate API document for your project and serve it locally, run:

```bash
make docs
```
