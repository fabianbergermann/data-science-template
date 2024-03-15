# Cookiecutter Data Science

_A logical, reasonably standardized but flexible project structure for doing and sharing data science work._

> **Important Note**
> 
>This template is an opinionated blend of two established Data Science Cookiecutter templates, who have done an amazing work:
> - **Cookiecutter Data Science (CCDS), v2 [Link](https://github.com/drivendata/cookiecutter-data-science/tree/v2)**
> - **Data Science Template** [Link](https://github.com/khuyentran1401/data-science-template)
> 
> It is highly recommended to read through the documentation of these two projects

## Tools used in this project
* [Dynaconf](https://www.dynaconf.com/): Manage configuration files 
* [MkDocs](https://www.mkdocs.org): Create documentation for your project
* [Poetry](https://python-poetry.org/): Dependency management - [setup guide](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f), [comparison with pip and conda](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)

## Installation
Since this is a cross-project utility application, we recommend installing it with [pipx](https://pypa.github.io/pipx/). 
Installation command options (further installation options in the [cookiecutter docs](https://cookiecutter.readthedocs.io/en/stable/installation.html) ):

### With pipx from PyPI (recommended)
```bash
pipx install cookiecutter
```

## Starting a new project
Create a project based on the template:
```bash
cookiecutter https://github.com/fabianbergermann/data-science-template
```