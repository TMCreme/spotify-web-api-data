import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Episodes:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_episodes(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/episodes/" + id,
            headers=self.headers,
            params={
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_several_episodes(self, ids: str, country_code="US"):
        response = requests.get(
            self.base_url + "/episodes",
            headers=self.headers,
            params={
                "ids": ids,
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    # User data requires the authorization flow
    def get_user_saved_episodes(self, limit: int, country_code="US"):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/episodes",
            headers=headers,
            params={
                "limit": limit,
                "market": country_code
            }
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    # User data requires the authorization flow
    def check_user_saved_episodes(self, ids: str):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/episodes/contains",
            headers=headers,
            params={
                "ids": ids
            }
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Episodes().get_episodes("6RIiUh2nVvaVtamIvtlIiq")
# Episodes().get_several_episodes("6RIiUh2nVvaVtamIvtlIiq,5qAY9Jh3qw6cpkUulQ18h1")
# Episodes().get_user_saved_episodes(4)
Episodes().check_user_saved_episodes("6RIiUh2nVvaVtamIvtlIiq,5qAY9Jh3qw6cpkUulQ18h1")
