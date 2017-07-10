#!/usr/bin/env bash
pep8 . && python3 -m unittest discover -v ./tests/
rc=$?
if [[ "$rc" != 0 ]]; then
	exit "$rc";
fi
> ./dev/file.json
rm -rf ./__pycache__
