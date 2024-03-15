from click.testing import CliRunner

from {{ cookiecutter.package_name }}.data.make_dataset import main, main_cli


def test_main_cli():
    runner = CliRunner()
    result = runner.invoke(main_cli, ["--environment", "production"])
    assert result.exit_code == 0


def test_main():
    assert main(environment="production") is None
