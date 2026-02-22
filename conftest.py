import pytest
import requests

# ----Restcountries Fixtures----
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
 
 #-----Exchangerate Fixtures----
@pytest.fixture
def exchangerate_base_url():
  return "https://api.exchangerate-api.com/v4/"

@pytest.fixture(params=["latest/USD"])
def exchangerate_endpoint_url(request):
    return f"{request.param}"


    





  