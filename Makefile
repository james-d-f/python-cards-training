clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.*cache' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +

install:
	pipenv install
	pipenv install --dev

test: clean
	pipenv run python -m pytest
