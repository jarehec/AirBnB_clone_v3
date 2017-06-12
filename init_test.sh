#!/bin/bash
pep8 . && python3 -m unittest discover -v ./tests/ && > file.json
