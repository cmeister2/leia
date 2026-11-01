.. highlight:: shell

============
Installation
============


In another project
------------------

leia requires Python 3.11 or later. With `uv`_ installed, add leia to an existing
Python project:

.. code-block:: console

    $ uv add leia

You can also install leia into an existing environment with pip:

.. code-block:: console

    $ python -m pip install leia

.. _uv: https://docs.astral.sh/uv/getting-started/installation/


From sources
------------

The sources for leia can be downloaded from the `GitHub repository`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone https://github.com/cmeister2/leia.git
    $ cd leia
    $ git switch main
    $ uv sync

This creates ``.venv`` and installs leia in editable mode with its development
dependencies. Run the tests with:

.. code-block:: console

    $ uv run pytest

You can also download the ``main`` branch as a `tarball`_. Extract it, enter the
source directory, and run ``uv sync``.

To build a source distribution and wheel:

.. code-block:: console

    $ uv build

The distributions are written to ``dist/``.

.. _GitHub repository: https://github.com/cmeister2/leia
.. _tarball: https://github.com/cmeister2/leia/archive/refs/heads/main.tar.gz
