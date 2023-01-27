import click.testing
from hypermodern_python import console


def test_pytest_is_running():
    assert True


def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
