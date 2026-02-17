
import requests


def test_options_request():
  url = "https://api.github.com/users/octocat"
  
  response = requests.options(url)

  print("Status Code:", response.status_code)

  assert response.status_code == 204, \
    f"Expected 204, got {response.status_code}"

  allowed_methods = response.headers.get("access-control-allow-methods", "")
  allowed_headers = response.headers.get("access-control-allow-headers", "")
  allowed_origin = response.headers.get("Access-Control-Allow-Origin")

  print("Allowed Methods List:", allowed_methods)
  print("Allowed Headers List:", allowed_headers)
  print("Allowed Origin:", allowed_origin)

  assert allowed_origin == "*"