import requests
from base.main import (
    obtain_auth_token, read_config
)


class Genres:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_available_genre_seeds(self):
        response = requests.get(
            self.base_url + "/recommendations/available-genre-seeds",
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


Genres().get_available_genre_seeds()
