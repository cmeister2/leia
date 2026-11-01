# leia

[![pypi version](https://img.shields.io/pypi/v/leia.svg)](https://pypi.org/project/leia/)
[![CI](https://github.com/cmeister2/leia/actions/workflows/ci.yml/badge.svg)](https://github.com/cmeister2/leia/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/leia/badge/?version=latest)](https://leia.readthedocs.io/en/latest/?badge=latest)

leia is a layering and compositing library for Python and PIL images.
The project is pre-alpha and requires Python 3.11 or later.

- Free software: MIT license
- Documentation: https://leia.readthedocs.io.

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then clone
the repository and create the development environment:

```shell
git clone https://github.com/cmeister2/leia.git
cd leia
uv sync
uv run pytest
uv run ruff check .
```

uv uses the development Python version in `.python-version` and installs the
project into `.venv`. See the [contributor guide](https://github.com/cmeister2/leia/blob/main/CONTRIBUTING.md)
for documentation builds and releases.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cmeister2/cookiecutter-pypackage](https://github.com/cmeister2/cookiecutter-pypackage) project template.
