from fastapi.testclient import TestClient
from app.main import app


def test_success_prediction():
    endpoint = '/v1/location/predict'
    body = {"data": [[0.2, 0.4],[0.65, 0.345],[0.134, 0.87]]}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        print(response_json)
        assert response.status_code == 200
        assert 'prediction' in response_json


def test_bad_request():
    endpoint = '/v1/location/predict'
    body = {"data": [[0.54, 0.65, 0.21], [0.2, 0.4]]}

    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        assert response.status_code == 422
