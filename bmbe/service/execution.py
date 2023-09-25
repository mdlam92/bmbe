"""The command execution module."""
import asyncio
import shlex

from fastapi import HTTPException


async def run_command(command: str) -> str:
    """Runs the given command and returns the output.

    Args:
        command (str): The command to run.

    Returns:
        str: The output of the command.

    Raises:
        HTTPException: 400 If the command fails. 500 If the command cannot be run.

    """
    try:
        sanitized_command = shlex.split(command)

        process = await asyncio.create_subprocess_exec(
            *sanitized_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise HTTPException(
                status_code=400,
                detail=f"Command failed with error: {stderr.decode().strip()}",
            )

        return stdout.decode().strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
