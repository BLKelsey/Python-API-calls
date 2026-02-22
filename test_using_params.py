import requests   
import pytest     # Import pytest (not strictly needed here unless using markers such as @pytest.mark.smoke, skip, etc.)


def test_get_name_countries(restcountries_base_url, endpoint_url):
    # Combine base URL + path (e.g. https://restcountries.com/v3.1 + /name/turkey)
    url = f"{restcountries_base_url}{endpoint_url}"

    response = requests.get(url)

    # Verify HTTP response is OK
    assert response.status_code == 200

    # Convert JSON response to Python object
    data = response.json()

    # Print country name from response
    # data is a list → first element → name → common: (*common - everyday name of the country)
    print(f"Country name: {data[0]['name']['common']}")
  
def test_get_capital_countries(restcountries_base_url, endpoint_url, capital):
    
    url = f"{restcountries_base_url}{endpoint_url}{capital}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(f"Capital: {data[0]['capital'][0]}")
    
def test_population(restcountries_base_url, endpoint_url, population):
    
    url = f"{restcountries_base_url}{endpoint_url}{population}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(f"Population: {data[0]['population']}") 
    
def test_currency(restcountries_base_url, endpoint_url, currency):
    
    url = f"{restcountries_base_url}{endpoint_url}{currency}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(f"Currency: {data[0]['currencies']}")
    
def test_languages(restcountries_base_url, endpoint_url, languages):
    
    url = f"{restcountries_base_url}{endpoint_url}{languages}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(f"Languages: {data[0]['languages']}")
    
def test_exchangerate(exchangerate_base_url, exchangerate_endpoint_url):
    
    url = f"{exchangerate_base_url}{exchangerate_endpoint_url}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    usd_to_try = data["rates"]["TRY"]
    print(f"USD → TRY rate: {usd_to_try}")

    

    
