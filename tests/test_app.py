from service.app import app,read_config

def test_app_status_code():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200

def test_load_config_file():
    url,loc=read_config('conf/config.yaml')
    assert url == 'https://api.data.gov.sg/v1/environment/rainfall'
    assert loc == 'Kent Ridge Road'
