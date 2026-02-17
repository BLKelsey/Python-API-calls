import requests
import pytest


def test_get_request():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    
    print("   Status Code:", response.status_code)
    print("Response Body:", response.json())
    assert response.status_code == 200
    
   