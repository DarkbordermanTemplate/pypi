.PHONY: clean init

init: clean
	pipenv --python 3.8
	pipenv install --dev

service_up:
	docker-compose up -d pypi

service_down:
	docker-compose down && docker volume rm pypi_data

ci-bundle: lint

lint: pylint flake8

flake8:
	pipenv run flake8 db_model --max-line-length=120

pylint:
	pipenv run pylint db_model/db_model

package:
	cd db_model/ && pipenv run python3 setup.py sdist bdist_wheel

upload:
	cd db_model/ && pipenv run python3 setup.py sdist bdist_wheel upload -r http://localhost:9999

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
