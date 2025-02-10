def test_grade_assignment(client):
    headers = {"X-Principal": '{"user_id":3, "teacher_id":1}'}
    payload = {"id": 1, "grade": "A"}
    response = client.post("/teacher/assignments/grade", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["grade"] == "A"
    assert response.json()["data"]["state"] == "GRADED"