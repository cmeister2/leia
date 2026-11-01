# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/cmeister2/leia/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

leia could always use more documentation, whether as part of the
official leia docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/cmeister2/leia/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `leia` for local development.

1. Fork the `leia` repo on GitHub.

2. Clone your fork locally:

    ```shell
    $ git clone git@github.com:your_name_here/leia.git
    ```

3. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync
   the development environment:

    ```shell
    $ cd leia/
    $ uv sync
    ```

   Python 3.11 or later is required. uv uses `.python-version` to select the
   development interpreter and creates `.venv` automatically. Dependencies are
   declared in `pyproject.toml` and resolved in `uv.lock`; commit changes to both
   files when updating dependencies.

4. Create a branch from `main` for local development:

    ```shell
    $ git switch main
    $ git switch -c name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. Run the tests, linter, and package build:

    ```shell
    $ uv run pytest
    $ uv run ruff check .
    $ uv build
    ```

   GitHub Actions runs the tests on the supported Python versions.

6. Commit your changes and push your branch to GitHub:

    ```shell
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, update its docstrings and usage
   documentation. Keep README.md focused on getting started.
3. The pull request should work on Python 3.11 or later. Check the
   [GitHub Actions runs](https://github.com/cmeister2/leia/actions/workflows/ci.yml)
   and make sure all checks pass.

## Tips

To run a subset of tests:

```shell
$ uv run pytest tests/test_leia.py
```

To collect coverage:

```shell
$ uv run coverage run --source=leia -m pytest
$ uv run coverage report -m
```

## Building documentation

The documentation uses Sphinx and MyST to include the Markdown guides. Generate
the API pages and build the HTML documentation with warnings treated as errors:

```shell
$ uv run --group docs sphinx-apidoc -o docs leia
$ uv run --group docs sphinx-build -W --keep-going -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to preview the result. `make docs` runs the
same build. The `docs` dependency group is installed by these uv commands.

## Releasing

Releases use the `release.yml` GitHub Actions workflow and
[PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).
The workflow exchanges its GitHub OIDC identity for a short-lived PyPI token.

### Publisher setup

Create a GitHub Actions environment named `pypi` in this repository. On the
`leia` project's PyPI **Publishing** page, add a GitHub publisher with:

| Field | Value |
| --- | --- |
| Owner | `cmeister2` |
| Repository | `leia` |
| Workflow filename | `release.yml` |
| Environment | `pypi` |

The filename refers to `.github/workflows/release.yml`. Configure the publisher
before pushing a release tag.

### Publishing a version

1. Update `__version__` in `leia/__init__.py` and add the release notes to
   `CHANGELOG.md`. Package metadata reads its version from `__version__`.
2. Run `uv lock`, the development checks above, and the documentation build.
3. Merge the version change into `main` through a pull request.
4. Tag that commit with `v` followed by the exact package version and push the
   tag. For example, for package version `0.1.1`:

    ```shell
    $ git tag v0.1.1
    $ git push origin v0.1.1
    ```

The workflow runs for tags matching `v*`, checks that the tag matches the package
version, builds the distributions, and publishes through the `pypi` environment.
Inspect the [release workflow](https://github.com/cmeister2/leia/actions/workflows/release.yml)
to confirm publication.
