# Setting up a project

## Initial Setup:

- Create `src`, `tests`, and `.venv` directories.
- Declare python version (with `pyenv` or other tool)
    - `pyenv local 3.11`
- Create new virtual environment with pipenv or similar
    - [pipenv](https://pipenv.pypa.io/en/latest/install/) `pipenv install`
    - [poetry](https://python-poetry.org/) `poetry init`
    - Python: `python -m venv .venv --prompt {pjct_name} --upgrade-deps`

### Custom command-line script options

- Python: using `pyproject.toml`

- [Typer](https://typer.tiangolo.com/)

- [Click](https://click.palletsprojects.com/en/8.1.x/)

---

- `poetry install click`
- Create `src/hypermodern_python/console.py`
- add script definition to the `pyproject.toml` file
```toml
[tool.poetry.scripts]
hmp = "hypermodern_python.console:main"
```

## Testing

- Install [`pytest`](https://docs.pytest.org/): `poetry add --group dev pytest`

- Create a blank file called `__init__.py` in the `tests/` folder

- Create a new python file in `tests/` that starts with "test_", like `test_console.py`

- Add a function in `test_console.py` like this:

    ```python
    def test_setup_correctly():
        assert False
    ```

- Run your tests by running `poetry run pytest` (or `pytest tests/` in an activated virtual environment). ("tests" is the folder your tests are in. Pytest will look throughout that folder for tests to run.)

- Add `coverage`

    - `poetry add --group dev coverage[toml] pytest-cov`

- Add coverage configuration to the `pyproject.toml` file:

```toml
# pyproject.toml
[tool.coverage.paths]
source = ["src", "*/site-packages"][tool.coverage.run]
branch = true
source = ["hypermodern_python"][tool.coverage.report]
show_missing = true
```

- Run tests with coverage information `poetry run pytest --cov`

- You can configure coverage to fail if it falls below a certian percentage by adding this to `pyproject.toml`:

```toml
# pyproject.toml
[tool.coverage.report]
fail_under = 100
```

## Add support for multiple Python version

- Install `nox` and follow the [article's instructions](https://cjolowicz.github.io/posts/hypermodern-python-02-testing/#test-automation-with-nox).


## Linting

Linting is a way to is the process of running a program that will analyse code for potential errors, bugs, stylistic issues, and other things.

- Install ruff: `poetry add --group dev ruff`
- Install black: `poetry add --group dev black` (Black will automatically format your code)


## Vulnerability checking
You can install a project to check for vulnerabilityies.
More in [the article](https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#finding-security-vulnerabilities-in-dependencies-with-safety).


## Add the ability to automatically check these tools before you commit code

- Install pre-commit `poetry add --group dev pre-commit`

- Create a `.pre-commit-config.yaml` file. We reccomend grabbing the one from [`pre-commit`'s website](https://pre-commit.com/#2-add-a-pre-commit-configuration).

- Look for plugins for tools you use: https://pre-commit.com/#plugins

- Install the latest version of each hook via `poetry run pre-commit autoupdate`

- Install the hooks: `poetry run pre-commit install`

- Pre-commit will automagically run your configured tools whenever you attempt to commit anything.

## Ensure your type hints are correct

- Install `mypy`: `poetry add --group dev mypy`

More detail in [the article](https://cjolowicz.github.io/posts/hypermodern-python-04-typing).

Add it to pre-commit
```yaml
# in .pre-commit-config.yaml
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: mypy
```

## Documentation

[The article](https://cjolowicz.github.io/posts/hypermodern-python-05-documentation/) recommends sphinx. Brian prefers [mkdocs](https://www.mkdocs.org/).
