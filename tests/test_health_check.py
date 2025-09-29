from fastapi.testclient import TestClient


def test_health_check(api_client: TestClient):
    response = api_client.get('/healthz')
    assert response.status_code == 200
