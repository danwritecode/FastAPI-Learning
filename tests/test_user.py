from tests.conftest import test_app
import main

def test_settings(test_app):
    response = test_app.get("/settings")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}

def test_hello_world(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_user(test_app):
    response = test_app.get("/user/34532356")
    assert response.status_code == 200
    assert "User_Id" in response.json()
    assert "Email" in response.json()
    assert "Name" in response.json()

