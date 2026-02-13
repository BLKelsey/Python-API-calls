import requests  # Import the requests library to send HTTP requests

def test_get_headers():  # Pytest recognizes this function as a test

    url = "https://jsonplaceholder.typicode.com/posts"  # Endpoint to retrieve all posts

    headers = {                                           # Custom request headers sent to the server
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",  # Identifies the client making the request
        "Accept": "application/json"                      # Tells the server we expect JSON in the response
    }

    response = requests.get(url, headers=headers)  # Send GET request with custom headers

    print("Status Code:", response.status_code)   # Display HTTP status code returned by server
    print("Response Headers:", response.headers)  # Display headers returned by the server
    print()  
    print("Response Body:", response.json())       # Display JSON body of the response

    assert response.status_code == 200  # Verify request succeeded 
