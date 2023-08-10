# KindOS selfcookie

## What is selfcookie?
selfcookie is a tool that helps you create and maintain Python using templates.

## Which capabilities does it provide?

- Project management automation using [pdm](https://pdm.fming.dev/).
- Compreenshive [Linting](linting) and [testing](testing) support.

- Docs generation using [mkdocs](https://www.mkdocs.org/).

### Git Helpers
Some git helpers are also provided:
```bash
pdm push
pdm commit
pdm tag
pdm amend
pdm status
pdm version
```

### GitHub Actions
The following GitHub Actions are provided:

- workflow: Run testing and linting, on tag publish to GitHub and PyPI
- docs: Build and deploy docs to GitHub Pages
