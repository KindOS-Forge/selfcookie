<div align="center">
A simple Python Cookiecutter Generator.

![License: MIT](https://img.shields.io/github/license/KindOS-Forge/selfcookie?style=for-the-badge&color=%23007ec6)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet?style=for-the-badge)](https://pdm.fming.dev)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/ambv/black)


![example workflow](https://github.com/KindOS-Forge/selfcookie/actions/workflows/workflow.yaml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/selfcookie?logo=python&logoColor=%23cccccc)](https://pypi.org/project/selfcookie)

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
