.PHONY: clean clean-test clean-pyc clean-build docs help install lint test test-all coverage servedocs dist
.DEFAULT_GOAL := help

UV ?= uv
PYTHON_VERSIONS ?= 3.11 3.12 3.13 3.14 3.15

help: ## show available commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "%-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove build, test, and coverage artifacts

clean-build: ## remove build artifacts
	rm -rf build/ dist/ .eggs/ leia.egg-info/

clean-pyc: ## remove package and test bytecode
	find leia tests -name '*.py[co]' -delete
	find leia tests -type d -name '__pycache__' -exec rm -rf {} +

clean-test: ## remove test and coverage artifacts
	rm -rf .coverage htmlcov/ .pytest_cache/ .ruff_cache/

install: ## synchronize the uv development environment
	$(UV) sync --locked

lint: ## check style and docstrings with Ruff
	$(UV) run --locked ruff check .

test: ## run tests with the selected Python
	$(UV) run --locked pytest

test-all: ## run tests on all supported Python versions
	@set -e; for version in $(PYTHON_VERSIONS); do $(UV) run --locked --python $$version pytest; done

coverage: ## report test coverage and generate htmlcov/index.html
	$(UV) run --locked coverage run -m pytest
	$(UV) run --locked coverage report -m
	$(UV) run --locked coverage html

docs: ## generate and validate Sphinx HTML documentation
	$(UV) run --locked --group docs sphinx-apidoc -f -o docs/ leia
	$(UV) run --locked --group docs sphinx-build -W --keep-going -b html docs docs/_build/html

servedocs: docs ## rebuild documentation when its sources change
	$(UV) run --locked --group docs watchmedo shell-command -p '*.rst;*.md;*.py' -i '*/_build/*;*/leia.rst;*/modules.rst' -c '$(MAKE) docs' -R -D leia docs README.md CONTRIBUTING.md AUTHORS.md CHANGELOG.md

dist: ## build a source distribution and wheel
	$(UV) build --clear
