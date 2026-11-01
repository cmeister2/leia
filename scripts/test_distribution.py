"""Run package tests against an installed distribution outside the checkout."""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    """Install the selected distribution in isolation and run its smoke tests."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("wheel", "sdist"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    pattern = "*.whl" if args.kind == "wheel" else "*.tar.gz"
    distributions = sorted((root / "dist").glob(pattern))
    if len(distributions) != 1:
        parser.error(
            f"Expected one {args.kind} in {root / 'dist'}, found {len(distributions)}"
        )

    with tempfile.TemporaryDirectory(prefix="leia-distribution-") as directory:
        result = subprocess.run(
            [
                "uv",
                "run",
                "--isolated",
                "--no-project",
                "--python",
                sys.executable,
                "--with",
                str(distributions[0]),
                "--with",
                "pytest",
                "pytest",
                "--import-mode=importlib",
                str(root / "tests"),
            ],
            cwd=directory,
            check=False,
        )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
