import os
import json
import pytest
from app import app
from process_description import process_description
from handle_error import handle_error

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_handle_request(client):
    response = client.post('/visualize', json={"description": "healthy heart"})
    assert response.status_code == 200
    assert "visualization" in response.json

def test_process_description():
    organ_info = process_description("healthy heart")
    assert organ_info["name"] == "heart"
    assert organ_info["conditions"] == []
    assert organ_info["abnormalities"] == []

def test_handle_error():
    error_message = "Invalid request"
    response = handle_error(error_message)
    assert response.status_code == 400
    assert response.json["error"] == error_message
