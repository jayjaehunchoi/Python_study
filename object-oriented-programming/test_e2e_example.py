from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class LoginRequest(BaseModel):
    id: str
    password: str


def login(user_id, user_password):
    # login 과정 생략
    return "token"


@app.post("/login")
def login_endpoint(req: LoginRequest):
    token = login(req.id, req.password)
    return {
        "token": token
    }


@app.get("get")
def get_test():
    return {
        "status": "ok"
    }


def test_get():
    response = requests.get("http://localhost:8000/get")
    assert response.status_code == 200


def test_login_endpoint():
    api_host = "localhost:8000"
    payload = {
        "id": "wogns0108",
        "password": "12345"
    }

    res = requests.post(url=f"http://{api_host}/login", json=payload)

    assert res.data() == {
        "token": "token"
    }

