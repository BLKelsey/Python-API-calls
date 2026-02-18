import requests

def test_options_request():
    # ------------------------------------------------
    # Base API URL (CoinGecko public API)
    # ------------------------------------------------
    base_url = "https://api.coingecko.com/api/v3"

    # ------------------------------------------------
    # Simulate a browser CORS preflight request
    #
    # Origin:
    #   The domain making the request (what a browser would send)
    #
    # Access-Control-Request-Method:
    #   The HTTP method the browser intends to use
    #
    # Access-Control-Request-Headers:
    #   Headers the browser plans to send
    # ------------------------------------------------
    headers = {
        "Origin": "https://myserver.com",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "Content-Type"
    }

    # ------------------------------------------------
    # Send OPTIONS request to simulate CORS preflight
    # ------------------------------------------------
    response = requests.options(
        base_url + "/coins/markets",
        headers=headers
    )

    # ------------------------------------------------
    # Print status code for debugging visibility
    # ------------------------------------------------
    print(f"OPTIONS request status code: {response.status_code}")

    # ------------------------------------------------
    # Validate successful preflight response
    #
    # Some servers return 200
    # Some return 204
    # Both are valid success responses
    # ------------------------------------------------
    assert response.status_code in [200, 204], \
        f"Unexpected status code: {response.status_code}"

    # ------------------------------------------------
    # Validate CORS headers (if present)
    # ------------------------------------------------
    allowed_methods = response.headers.get("access-control-allow-methods")
    allowed_origin = response.headers.get("access-control-allow-origin")

    print("Allowed Methods:", allowed_methods)
    print("Allowed Origin:", allowed_origin)

    # Optional: Validate that GET is allowed
    if allowed_methods:
        assert "GET" in allowed_methods
