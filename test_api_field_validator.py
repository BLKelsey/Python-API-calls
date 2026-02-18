import requests

def test_agify_response_structure():

    # -------------------------------
    # Step 1: Make API call
    # -------------------------------
    url = "https://api.agify.io/?name=brian"
    response = requests.get(url)

    # -------------------------------
    # Step 2: Validate status code
    # -------------------------------
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"
    print("Status Code:", response.status_code)

    # -------------------------------
    # Step 3: Convert to JSON
    # -------------------------------
    data = response.json()

    # -------------------------------
    # Step 4: Validate required fields exist
    # -------------------------------
    expected_fields = ["name", "age", "count"]

    for field in expected_fields:
        assert field in data, \
            f"Missing field: {field}"
    print(f"Data: {data}")

    # ----------------------------------------------
    # Step 5: Validate data types - schema validation
    # ---------------------------------------------
    assert isinstance(data["age"], int), \
        f"age is not integer. {type(data['age'])}"

    assert isinstance(data["count"], int), \
        f"count is not integer. {type(data['count'])}"


