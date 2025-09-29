import pytest
from fastapi.testclient import TestClient
from app.api import create_app


@pytest.fixture
def api_client() -> TestClient:
    app = create_app()
    return TestClient(
        app=app,
    )
