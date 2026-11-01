"""Require successful results from every prerequisite CI job."""

import os


def main():
    """Fail when a required CI job did not complete successfully."""
    for job in ("tests", "checks"):
        result = os.environ.get(f"{job.upper()}_RESULT", "missing")
        if result != "success":
            raise SystemExit(f"Required CI job {job!r} did not succeed: {result}")


if __name__ == "__main__":
    main()
