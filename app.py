from fastapi import FastAPI
from routes.product import product
from routes.user import user
from scrapp.scrapper import scrapp
from fastapi.testclient import TestClient

app = FastAPI()
scrapp()

app.include_router(product)
app.include_router(user)

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"msg": "Not authenticated"}