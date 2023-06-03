install:
	pip install -r requirements.txt

lint:
	pylint hello.py

test:
	python -m pytest -vv

run:
	python -m uvicorn app:app
