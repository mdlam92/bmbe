"""Server top level module."""
from fastapi import FastAPI

from .systemctl import router as systemctl_router

app = FastAPI()

app.include_router(systemctl_router)


@app.get("/")
async def root() -> bool:
    """Return the root of the server."""
    return True
