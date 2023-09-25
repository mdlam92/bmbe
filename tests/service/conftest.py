"""Unit tests configuration."""
from pytest import fixture

from fastapi.testclient import TestClient

from bmbe.service.server import app


@fixture()
def test_client() -> TestClient:
    """A FastAPI Test Client."""
    return TestClient(app)
