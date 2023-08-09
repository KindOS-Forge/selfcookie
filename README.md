<div align="center">
A simple Python Cookiecutter Generator.

[![PyPI](https://img.shields.io/pypi/v/selfcookie?logo=python&logoColor=%23cccccc)](https://pypi.org/project/selfcookie)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
</div>

## What is selfcookie?

selfcookie is a simple Python Cookiecutter generator. It is a tool that helps you create projects from templates. You can use it to quickly create a project skeleton without having to create all the boilerplate code yourself.

## Highlights of features

- Package management with [pdm](https://pdm.fming.dev)

- Code linting triggered on pre-commit:
    - [Codespell](https://github.com/codespell-project/codespell)
    - Code formatting with [black](https://github.com/psf/black)
    - [ruff](https://beta.ruff.rs/docs/)


## Installation

### Requirements
Python 3.11+

```bash
pip install selfcookie
```

## How to use

```sh
selfcookie package-name
```
