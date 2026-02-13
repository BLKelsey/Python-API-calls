import requests  # Import the requests library to send HTTP requests

def test_put():  # Pytest will recognize this as a test function

    url = "https://jsonplaceholder.typicode.com/posts/1"  # Target endpoint for updating post with ID 1
  
     # JSON payload to send in the PUT request
    data = { 
        "username": "Brian",
        "email": "name@example.com",
        "address": "123 Main St",
        "id": "2"
    }

    try:
        response = requests.put(url, json=data)  # Send PUT request with JSON body
        print("Status Code:", response.status_code)  # Display HTTP status code returned by server
        print("Response Body:", response.json())  # Display JSON response returned from API

    except Exception as error:  # Catch any exception that occurs during request
        print("An error occurred during the PUT request.")  # Generic error message
        print()
        print("Caught Error:", error)  # Print the actual exception details
        print("Status Code inside except:", response.status_code if 'response' in locals() else "No response received")  
        # Print status code only if response exists (prevents crash if request failed before response was created)
