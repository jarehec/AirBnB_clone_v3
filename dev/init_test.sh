#!/bin/bash
pep8 . && python3 -m unittest discover -v ./tests/
> ./dev/file.json
rm -rf ./__pycache__
