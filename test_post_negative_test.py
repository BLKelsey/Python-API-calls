import requests

def test_post_fail_request():

    url = "https://jsonplaceholder.typicode.com/postz"

    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)

        response.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print("Caught HTTPError:", error)
        print("Status Code inside except:", response.status_code)   # Expect error code 404

       
