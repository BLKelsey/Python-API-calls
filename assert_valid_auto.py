import requests
import json

url = "https://api.github.com/users/octocat"

response = requests.options(url)

print("Status Code:", response.status_code)

# Convert headers to regular dict for readable display
headers_dict = dict(response.headers)

print("\nFull Headers:")
print(json.dumps(headers_dict, indent=4))

# ---------------------------
# Extract values explicitly
# ---------------------------
allowed_methods = response.headers.get("access-control-allow-methods", "")
allowed_headers = response.headers.get("access-control-allow-headers", "")
allowed_origin = response.headers.get("Access-Control-Allow-Origin")

print("\nParsed Values:")
print("Allowed Methods:", allowed_methods)
print("Allowed Headers:", allowed_headers)
print("Allowed Origin:", allowed_origin)

# ---------------------------
# Assertions
# ---------------------------
assert response.status_code == 204, \
    f"Expected 204, got {response.status_code}"

methods_set = {m.strip() for m in allowed_methods.split(",")}
expected_methods = {"GET", "POST", "PATCH", "PUT", "DELETE"}
missing_methods = expected_methods - methods_set

assert not missing_methods, \
    f"Missing methods: {missing_methods}"

print("\nValidation passed.")
