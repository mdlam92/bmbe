"""Unit tests for the CLI module."""
import mock
import pytest
from typer.testing import CliRunner

from bmbe.service.cli import app


@pytest.fixture()
def runner() -> CliRunner:
    """A Click Test Runner."""

    return CliRunner()


def test_cli(runner: CliRunner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_run(runner: CliRunner):
    with mock.patch(
        "bmbe.service.cli.uvicorn.run", return_value=None
    ) as mock_uvicorn_run:
        result = runner.invoke(app, ["run"])
        assert result.exit_code == 0
        mock_uvicorn_run.assert_called_once()


def test_docs(runner: CliRunner):
    with mock.patch(
        "bmbe.service.cli.open", mock.mock_open(), create=True
    ) as mock_open:
        result = runner.invoke(app, ["docs"])
        assert result.exit_code == 0
        mock_open.assert_called_once()
