
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-test:
	pip install -r requirements-test.txt

lint-force:
	isort .
	black .
	flake8 . --ignore=E501
	pylint --disable=R,C,pointless-string-statement ./*.py

lint-check:
	isort . --check-only
	black --check .
	flake8 . --ignore=E501
	#pylint --disable=R,C,pointless-string-statement ./*.py

test:
	python -m pytest test_lambda_function.py
