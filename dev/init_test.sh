#!/usr/bin/env bash
# This initializes testing suite.
# Checks pep8 style of all python files
# also runs all unittests
ret_val=0
pep8 .
ret_val+=$?

python3 -m unittest discover -v ./tests/
ret_val+=$?

./dev/w3c_validator.py \
    `find ./web_static -maxdepth 1 -name "*.html" -type f ! -name "4*"`
ret_val+=$?

./dev/w3c_validator.py \
    `find ./web_static/styles -maxdepth 1 -name "*.css" -type f`
ret_val+=$?

# Stores the return status code
rc=$?

# clears file.json
> ./dev/file.json

# removes __pycache__ folder
py3clean .

# exits with status from tests
exit "$rc"
