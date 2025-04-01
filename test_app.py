import pytest
import subprocess
from app import app
from app import formatDate



@pytest.fixture
def client():
    with app.test_client() as app_client:
        yield app_client

rawDate = subprocess.run(['date', "+%b %d, %Y, %H:%M"], stdout=subprocess.PIPE, universal_newlines=True)
date = rawDate.stdout

testData = formatDate(date)
def test_today(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == bytes(testData, encoding="utf-8")


