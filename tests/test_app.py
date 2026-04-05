from app import app

def test_app_exists():
    assert app is not None

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"

def test_api():
    client = app.test_client()
    res = client.get("/api")
    assert res.status_code == 200
    assert "message" in res.json

def test_fail():
    client = app.test_client()
    res = client.get("/fail")
    assert res.status_code == 500
