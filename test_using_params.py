import requests   

# ------------------
# RestCountries API
# ------------------
def test_get_name_countries(restcountries_base_url, endpoint_url):
    # Combine base URL + path (e.g. https://restcountries.com/v3.1 + /name/turkey)
    url = f"{restcountries_base_url}{endpoint_url}"

    response = requests.get(url)
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
    
 #------------------
 # Exchangerate API
 #------------------    
def test_exchangerate(exchangerate_base_url, exchangerate_endpoint_url):
    
    url = f"{exchangerate_base_url}{exchangerate_endpoint_url}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    usd_to_try = data["rates"]["TRY"]
    print(f"USD → TRY rate: {usd_to_try}")
    
#-------------
# Weather API
# ------------      
def test_weather_base_url(test_weather_base_url):
    assert "weatherbit.io" in test_weather_base_url

def test_weather(test_weather_base_url, city, country, units, test_key):

    params = {
        "city": city,
        "country": country,
        "units": units,
        "key": test_key
    }

    response = requests.get(test_weather_base_url, params=params)
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"
        
    data = response.json()
    
    assert "data" in data, "Response missing 'data' field"
    assert isinstance(data["data"], list), "'data' should be a list"
    assert len(data["data"]) > 0, "'data' list is empty"

    # "data" is a list of weather results.
    # take the first result (index 0) and extract its "temp" value.
    temp = data["data"][0]["temp"]
    
    assert isinstance(temp, (int, float)), \
     f"Temperature should be numeric, got {type(temp)}"

    print(f"Temperature in {city}: {temp} F")

    
