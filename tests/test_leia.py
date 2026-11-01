"""Smoke tests for the installed leia package."""

from importlib.metadata import metadata, version

import leia
from leia import leia as module


def test_version():
    """Keep the installed distribution version consistent with the package."""
    assert version("leia") == leia.__version__


def test_module():
    """Include the existing leia.leia module in installed distributions."""
    assert module.__name__ == "leia.leia"


def test_metadata():
    """Preserve the package identity and declare the supported Python version."""
    package_metadata = metadata("leia")
    assert package_metadata["Name"] == "leia"
    assert package_metadata["Requires-Python"] == ">=3.11"
    assert package_metadata["License-Expression"] == "MIT"
