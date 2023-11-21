#setup:
#	python3 -m venv ~/.multi-clouds
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib --cov=hello test_hello.py

lint:
	pylint --disable=R,C hello.py mylib/*.py
	

all: install lint test
	