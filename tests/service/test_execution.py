"""Unit tests for the execution module."""
import mock
import pytest

from fastapi import HTTPException

from bmbe.service.execution import run_command


@pytest.mark.asyncio
async def test_run_command_success():
    """Test running a command."""
    with mock.patch(
        "asyncio.create_subprocess_exec",
        return_value=mock.AsyncMock(
            communicate=mock.AsyncMock(
                return_value=(b"stdout", b"stderr"),
            ),
            returncode=0,
        ),
    ):
        output = await run_command("echo hello")
        assert output == "stdout"


@pytest.mark.asyncio
async def test_run_command_failure():
    """Test running a command."""
    with mock.patch(
        "asyncio.create_subprocess_exec",
        return_value=mock.AsyncMock(
            communicate=mock.AsyncMock(
                return_value=(b"stdout", b"stderr"),
            ),
            returncode=1,
        ),
    ):
        with pytest.raises(HTTPException):
            await run_command("echo hello")


@pytest.mark.asyncio
async def test_run_command_exception():
    """Test running a command."""
    with mock.patch(
        "asyncio.create_subprocess_exec",
        side_effect=Exception("error"),
    ):
        with pytest.raises(HTTPException):
            await run_command("echo hello")
