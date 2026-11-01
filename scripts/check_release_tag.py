"""Require the release tag to match the installed package version."""

import os
from importlib.metadata import version


def main():
    """Reject a release tag that differs from the package version."""
    expected = f"v{version('leia')}"
    actual = os.environ["RELEASE_TAG"]
    if actual != expected:
        raise SystemExit(f"Release tag {actual!r} must match {expected!r}")


if __name__ == "__main__":
    main()
