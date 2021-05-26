from fastapi.testclient import TestClient
from app import app
import pytest
from math import pi

client = TestClient(app)

AREA = {
    "radius": 1,
    "area": pi,
}
CIRCUMFERENCE = {
    "radius": 1,
    "circumference": 2 * pi,
}


def test_area_path():
    response = client.get("/area/1")
    assert response.status_code == 200
    assert response.json() == AREA


@pytest.mark.parametrize("params", [{"radius": 1}, {"diameter": 2}])
def test_area_query(params):
    response = client.get("/area/", params=params)
    assert response.status_code == 200
    assert response.json() == AREA


@pytest.mark.parametrize("data", [{"radius": 1}, {"diameter": 2}])
def test_area_post(data):
    response = client.post("/area/", json=data)
    assert response.status_code == 200
    assert response.json() == AREA


def test_circumference_path():
    response = client.get("/circumference/1")
    assert response.status_code == 200
    assert response.json() == CIRCUMFERENCE


@pytest.mark.parametrize("params", [{"radius": 1}, {"diameter": 2}])
def test_circumference_query(params):
    response = client.get("/circumference/", params=params)
    assert response.status_code == 200
    assert response.json() == CIRCUMFERENCE


@pytest.mark.parametrize("data", [{"radius": 1}, {"diameter": 2}])
def test_circumference_post(data):
    response = client.post("/circumference/", json=data)
    assert response.status_code == 200
    assert response.json() == CIRCUMFERENCE


@pytest.mark.parametrize(
    "params",
    [{"measurement": 1, "param": "radius"}, {"measurement": 2, "param": "diameter"}],
)
def test_index_page(params):
    response = client.get("/", params=params)
    assert response.status_code == 200
    for check in [
        "area of a circle",
        "3.14",
        "circumference of a circle",
        "6.28",
    ]:
        assert check in response.text
