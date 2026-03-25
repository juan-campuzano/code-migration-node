import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Python App with Outdated Dependencies'
    assert 'uuid' in data


def test_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    data = response.get_json()
    assert data['unique_values'] == [1, 2, 3, 4]
    assert 'summary' in data


def test_config(client):
    response = client.get('/config')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app']['name'] == 'python-app'
    assert data['app']['version'] == '1.0.0'


def test_db(client):
    response = client.get('/db')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['items']) == 3
    assert data['items'][0]['name'] == 'alpha'


def test_image(client):
    response = client.get('/image')
    assert response.status_code == 200
    data = response.get_json()
    assert data['format'] == 'PNG'
    assert data['size'] == '64x64'
    assert 'data' in data


def test_encrypt(client):
    response = client.get('/encrypt')
    assert response.status_code == 200
    data = response.get_json()
    assert data['original'] == 'Hello, Migration Tooling!'
    assert data['decrypted'] == 'Hello, Migration Tooling!'
    assert data['match'] is True
