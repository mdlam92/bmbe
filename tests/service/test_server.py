"""Test the server module."""
import pytest

from fastapi.testclient import TestClient


@pytest.mark.asyncio
def test_get_server_root(test_client: TestClient):
    """Test getting the server root."""
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() is True
