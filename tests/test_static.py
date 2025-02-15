import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_static_css(client):
    response = client.get('/static/style.css')
    assert response.status_code == 200
