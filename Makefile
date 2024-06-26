install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

prepare: 
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

