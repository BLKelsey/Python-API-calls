import requests
import pytest


def test_get_request():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200