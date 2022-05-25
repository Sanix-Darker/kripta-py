isort  = isort kripta_py tests
flake8 = flake8 kripta_py tests
mypy   = mypy kripta_py 

format:
	$(isort)
	$(black)

lint:
	$(flake8)
	$(isort)
	$(mypy)

test:
	poetry run pytest

build:
	poetry install
	poetry build

install:
	pip install -U pip poetry &&\
	poetry install
