import requests  # Import the requests library to send HTTP requests

def test_patch_request():  # Pytest recognizes this as a test function

    url = "https://jsonplaceholder.typicode.com/posts/1"  # Endpoint for updating post with ID 1
  
    data = {  # Partial update payload for the PATCH request
        "username": "Chris",
        "email": "chris@example.com"
    }

    try:
        response = requests.patch(url, json=data)  # Send PATCH request with JSON body
        print("Status Code:", response.status_code)  # Print HTTP status code returned by server
        print("Response Body:", response.json())  # Print JSON response returned from API
        
    except Exception as error:             # Catch any exception that occurs during request
        print("An error occurred during the PATCH request.")  # Generic error message
       
        # If anything unexpected happens, explicitly fail the test        
        assert False, f"Unexpected error occurred: {error}"
