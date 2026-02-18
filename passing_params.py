import requests

url = "https://api.coingecko.com/api/v3"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
     "page": 1
 }

def test_get_coin_list():
  response = requests.get(url + "/coins/markets", params=params)
  
  assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"
        
  data = response.json()
  
  print(f" Number of crypto-coins on page 1: {len(data)}")