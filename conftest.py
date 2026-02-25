import pytest
import requests

# ----------------------
# Restcountries Fixtures
# ----------------------

@pytest.fixture
def restcountries_base_url():
  return "https://restcountries.com/v3.1"

@pytest.fixture(params=["Turkey"])
def endpoint_url(request):
    return f"/name/{request.param}"
  
@pytest.fixture(params=["capital"] )
def capital(request):
    return f"?fields={request.param}"
  
@pytest.fixture(params=["population"])
def population(request):
    return f"?fields={request.param}"
  
@pytest.fixture(params=["currencies"])
def currency(request):
    return f"?fields={request.param}"
  
@pytest.fixture(params=["languages"])
def languages(request):
    return f"?fields={request.param}"
 
 #-----------------------
 # Exchangerate Fixtures
 #-----------------------
@pytest.fixture
def exchangerate_base_url():
  return "https://api.exchangerate-api.com/v4/"

@pytest.fixture(params=["latest/USD"])
def exchangerate_endpoint_url(request):
    return f"{request.param}"

#--------------------
# Weather Fixtures
#--------------------

@pytest.fixture
def test_weather_base_url():
    return "http://api.weatherbit.io/v2.0/current"

@pytest.fixture(params=["9981631dda5b49f2acb193ff8db04ebc"])
def test_key(request):
    return request.param

@pytest.fixture (params=["Istanbul"])
def city(request):
    return request.param

@pytest.fixture (params=['Turkey'])
def country(request):
    return request.param

@pytest.fixture(params=["I"])  # I = Fahrenheit
def units(request):
    return request.param











  