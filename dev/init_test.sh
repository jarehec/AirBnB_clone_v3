#!/usr/bin/env bash
# This initializes testing suite.
# Checks pep8 style of all python files
# also runs all unittests
pep8 . && python3 -m unittest discover -v ./tests/

# Stores the return status code
rc=$?

# clears file.json
> ./dev/file.json

# removes __pycache__ folder
py3clean .

# exits with status from tests
exit "$rc"
