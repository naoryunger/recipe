import hashlib
import requests


class RecipeAPIClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def test__create_user(self, name, surname, password):
        # Define the data for the POST request
        data = {
            "name": name,
            "surname": surname,
            "password": password,
        }

        # Send the POST request
        response = requests.post("http://{}:{}/users/".format(self.host, self.port), json=data)

        # Print the response
        print(response.status_code)
        print(response.json())

    def test__create_recipe(self, name, owner_id, recipe_content, recipe_category):
        # Define the data for the POST request
        data = {
            "name": name,
            "owner_id": owner_id,
            "recipe_content": recipe_content,
            "recipe_category": recipe_category
        }

        # Send the POST request
        response = requests.post("http://{}:{}/recipes/".format(self.host, self.port), json=data)

        # Print the response
        print(response.status_code)
        print(response.json())


if __name__ == '__main__':
    client = RecipeAPIClient("localhost", 8003)
    client.test__create_user("admin", "admin", hashlib.md5("Password1!".encode()).hexdigest())
    # client.test__create_recipe("carrot soup", 1, recipe_content=)
