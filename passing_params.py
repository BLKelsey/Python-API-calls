import requests   # Import the requests library so we can make HTTP calls

# Base URL for the CoinGecko API (version 3)
url = "https://api.coingecko.com/api/v3"

# Query parameters we are sending to the API
# These will be added to the URL like:
# ?vs_currency=usd&order=market_cap_desc&page=1
params = {
    "vs_currency": "usd",          # REQUIRED → tells API to return prices in USD
    "order": "market_cap_desc",    # Sort results by highest market cap first
    "page": 1                      # Return the first page of results
}

def test_get_coin_list():
  
    # Send a GET request to the /coins/markets endpoint
    # params=params automatically attaches query parameters to the URL
    response = requests.get(url + "/coins/markets", params=params)

    # Verify the request was successful (HTTP 200 = OK)
    # If not, show the actual status code for debugging
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"

    # Convert the response body (JSON) into Python data  
    data = response.json()

    # Print how many coins were returned on page 1
    print(f"Number of crypto-coins on page 1: {len(data)}")
