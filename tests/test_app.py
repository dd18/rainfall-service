import pytest
import requests
from service.app import app,read_config,check_rainfall,LocationException

@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_load_config_file():
    url,loc=read_config('conf/config.yaml')
    assert url == 'https://api.data.gov.sg/v1/environment/rainfall'
    assert loc == 'Kent Ridge Road'

def test_check_rainfall():
    output=check_rainfall('https://api.data.gov.sg/v1/environment/rainfall','Kent Ridge Road')
    assert 'Kent Ridge Road' in output
    assert 'Raining' or 'Not Raining' in output
    assert '0mm' or '.' in output

def test_app_status(client):
    response = client.get("/")
    assert response.status_code == 200
    assert 'Kent Ridge Road' in response.get_data(as_text=True)

@pytest.mark.exceptions
def test_exceptions():
    with pytest.raises((FileNotFoundError,requests.exceptions.ConnectionError,LocationException)):
        url,loc=read_config('conf/config1.yaml')
