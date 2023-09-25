"""The CLI entry point for the service."""
import json
from pathlib import Path

import typer
import uvicorn

from .server import app as webserver_app

app = typer.Typer()


@app.command()
def run(host: str = "127.0.0.1", port: int = 9001) -> None:
    """Run the server."""
    uvicorn.run(webserver_app, host=host, port=port)


@app.command()
def docs(path: Path = "openapi.json") -> None:
    """This command will have the server write the OpenAPI schema to a file."""
    typer.echo(f"Writing OpenAPI schema to {path}")
    with open(path, "w") as f:
        f.write(json.dumps(webserver_app.openapi()))


def execute() -> None:
    """Run the CLI."""
    app()
