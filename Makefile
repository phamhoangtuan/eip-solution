##@ Install

setup:
	@echo "Installing..."
	@pyenv install 3.10 -s
	@pyenv local 3.10
	@pdm install

##@ Formatters

format-blue:
	@pdm run blue .

format-ruff:
	@pdm run ruff check --fix .

format: format-blue format-ruff

##@ Linters

lint-blue:
	@pdm run blue --check .

lint-ruff:
	@pdm run ruff check .

lint-mypy:
	@pdm run mypy .

lint: lint-blue lint-ruff lint-mypy

##@ Tests

test:
	@pdm run pytest

all: format lint test
