from setuptools.config import read_configuration

from fastapi.testclient import TestClient

from autobump import API_VERSION
from autobump.main import app


client = TestClient(app)


def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Beep": "boop"}


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()['ok']


def test_get_version():
    response = client.get("/versions")
    config = read_configuration('setup.cfg')
    expected = {
        "api_version": API_VERSION,
        "package_name": config['metadata']['name'],
        "package_version": config['metadata']['version']
    }
    assert response.status_code == 200
    assert response.json() == expected

