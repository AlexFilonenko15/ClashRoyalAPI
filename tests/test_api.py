import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)

def test_get_cards():
    response = client.get(f'/clashroyal/cards', headers={"Secret-Key": os.getenv('SECRET_KEY')})
    data = response.json()
    assert len(data) == 121