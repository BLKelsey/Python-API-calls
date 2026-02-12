import requests

def test_post_request():
  
    # Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # Payload for the POST request
    data = {
        "name": "Brian",
        "email": "name@gmail.com"
    }

    # Sending the POST request
    response = requests.post(url, json=data)
    
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Assertions (this is what makes it a test)
    assert response.status_code == 201

    response_data = response.json()
    assert response_data["name"] == "Brian"
    assert response_data["email"] == "name@gmail.com"
