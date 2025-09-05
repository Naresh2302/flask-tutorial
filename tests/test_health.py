def test_health_ok(client):
    rv = client.get("/health/")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["status"] == "ok"
    assert data["app"] == "flask-tutorial"
