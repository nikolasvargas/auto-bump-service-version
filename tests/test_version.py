from setuptools.config import read_configuration

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Beep": "boop"}

def test_get_version():
    response = client.get("/version")
    config = read_configuration('setup.cfg')
    assert response.status_code == 200
    assert response.json() == {"version": config['metadata']['version']}

