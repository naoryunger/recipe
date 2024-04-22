import requests


def test__create_user__normal():
    # Define the data for the POST request
    data = {
        "name": "admin",
        "surname": "admin",
        "password": "0cef1fb10f60529028a71f58e54ed07b",
    }

    # Send the POST request
    response = requests.post("http://localhost:8001/users/", json=data)

    # Print the response
    print(response.status_code)
    print(response.json())


def test__create_recipe__normal():
    # Define the data for the POST request
    data = {
        "name": "New Recipe",
        "owner_id": 1,
        "recipe_content": "Recipe content goes here",
        "recipe_category": "Main Dish"
    }

    # Send the POST request
    response = requests.post("http://localhost:8001/recipes/", json=data)

    # Print the response
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    test__create_user__normal()
