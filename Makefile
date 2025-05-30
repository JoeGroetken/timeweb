#!/bin/bash

setup:
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt && export FLASK_RUN_HOST=0.0.0.0 && export FLASK_RUN_PORT=853

clean:
	rm -r env
	rm -r __pycache__

test:
	. env/bin/activate && pytest

run:
	. env/bin/activate && export FLASK_RUN_HOST=0.0.0.0 && export FLASK_RUN_PORT=853 && flask run
