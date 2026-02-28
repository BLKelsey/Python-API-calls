import requests  # Import the requests library to send HTTP requests

def test_post_fail_request():  # Pytest will detect and run this function as a test

    url = "https://jsonplaceholder.typicode.com/postz"  # Intentionally incorrect endpoint (should return error)
    
    data = {                         # Payload dictionary (not used here since this is a GET request)
        "username": "Brian",
        "email": "name@example.com"
    }

    try:
        response = requests.post(url)                # Send POST request to invalid endpoint
        print("Status Code:", response.status_code)  # Print HTTP status code (visible with pytest -s)

        response.raise_for_status()  # Raise HTTPError automatically if status is 4xx or 5xx

    except requests.exceptions.HTTPError as error:  # Catch only HTTP status-related errors
        print("Caught HTTPError:", error)           # Print the exception message
        print("Status Code inside except:", response.status_code)  # Confirm expected 404 error code
        
         # If anything unexpected happens, explicitly fail the test        
        assert False, f"Unexpected error occurred: {error}"
