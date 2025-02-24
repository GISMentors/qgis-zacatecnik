SHELL := /bin/bash

build:
	source ./venv/bin/activate; \
	python3 -m mkdocs build

install:
	python3 -m venv ./venv; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt
