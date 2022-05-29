from service.app import app

def test_app_status_code():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
