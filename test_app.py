import pytest

from app import app
from app import formatDate



@pytest.fixture
def client():
    with app.test_client() as app_client:
        yield app_client

testData = formatDate()
def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == bytes(testData, encoding="utf-8")
