import requests  # Import the requests library to send HTTP requests

def test_delete_request():  # Pytest will recognize this as a test function

    url = "https://jsonplaceholder.typicode.com/posts/1"  # Endpoint for deleting post with ID 1

    response = requests.delete(url)  # Send DELETE request to the specified URL
    
    assert response.status_code in (200, 204)
    print("Status Code:", response.status_code)  # Print HTTP status code returned by server