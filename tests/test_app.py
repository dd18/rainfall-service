from service.app import app,read_config,check_rainfall

def test_app_status_code():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200

def test_load_config_file():
    url,loc=read_config('conf/config.yaml')
    assert url == 'https://api.data.gov.sg/v1/environment/rainfall'
    assert loc == 'Kent Ridge Road'

def test_check_rainfall():
    output=check_rainfall('https://api.data.gov.sg/v1/environment/rainfall','Kent Ridge Road')
    assert 'Kent Ridge Road' in output
