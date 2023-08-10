# Linting

To run the lint validation, type:

```bash
pdm test
```

In order to prevent from quality issues in the code we use the following tools:

| Tool | Purpose |
| --- | --- |
| [codespell] | Spell checking |
| [pre-commit] | Force lint to before any commit |
| [isort] | Import sorting |
| [Black] | Code formatting |
| [Ruff] | Linting |
| [mypy] | Type checking |


[codespell]: https://github.com/codespell-project/codespell
[pre-commit]: https://pre-commit.com/
[isort]: https://pycqa.github.io/isort/
[Black]: https://black.readthedocs.io/en/stable/
[Ruff]: https://beta.ruff.rs/docs/

[mypy]: https://mypy.readthedocs.io/en/stable/


The following checks are also performed:
| ID                            | Description                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------|
| check-added-large-files        | Checks for large added files in a repository.                                                  |
| check-ast                      | Analyzes code's Abstract Syntax Tree (AST) for issues.                                         |
| check-case-conflict            | Identifies case conflicts in file or directory names.                                          |
| check-docstring-first          | Enforces docstrings at the beginning of functions, classes, or modules.                        |
| check-executables-have-shebangs| Ensures executable scripts have shebang lines for interpreters.                                |
| check-json                     | Validates JSON files for syntax and structure.                                                 |
| check-merge-conflict           | Identifies files with unresolved merge conflicts.                                              |
| check-symlinks                 | Checks for symbolic links to manage dependencies.                                              |
| check-toml                     | Validates TOML files for correct syntax and structure.                                         |
| check-xml                      | Validates XML files for well-formedness and adherence to standards.                            |
| check-yaml                     | Validates YAML files for correct syntax and structure.                                         |
| trailing-whitespace            | Detects and flags trailing whitespace at line ends.                                            |



