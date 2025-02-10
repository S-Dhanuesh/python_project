def test_list_teachers(client):
    headers = {"X-Principal": '{"user_id":5, "principal_id":1}'}
    response = client.get("/principal/teachers", headers=headers)
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0