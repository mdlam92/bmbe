"""sytemctl service module."""
from fastapi import APIRouter, HTTPException

from .execution import run_command


router = APIRouter(
    prefix="/systemctl",
    tags=["systemctl"],
)


systemd_services = [
    "transmission.service",
    "surfshark.service",
]


@router.get("/services")
async def get_services() -> list[str]:
    """Return the list of services."""
    return systemd_services


@router.get("/{service}/status")
async def get_service_status(service: str) -> str:
    """Return the current status for the given service."""
    if service not in systemd_services:
        raise HTTPException(status_code=404, detail="Service not found")
    else:
        (stdout, stderr) = await run_command(f"systemctl status {service} --no-pager")
        return stdout
