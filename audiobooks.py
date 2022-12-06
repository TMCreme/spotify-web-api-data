import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


# Note: Audiobooks are only available for the
# US, UK, Ireland, New Zealand and Australia markets.
class AudioBooks:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_audiobooks(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/audiobooks/" + id,
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

    def get_several_audiobooks(self, ids: str, country_code="US"):
        response = requests.get(
            self.base_url + "/audiobooks",
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

    def get_audiobook_chapters(self, id: str, limit: int, country_code="US"):
        response = requests.get(
            self.base_url + "/audiobooks/" + id + "/chapters",
            headers=self.headers,
            params={
                "limit": limit,
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_user_saved_audiobooks(self, limit: int):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/audiobooks",
            headers=headers,
            params={
                "limit": limit,
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

    def check_user_saved_books(self, ids: str):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/audiobooks/contains",
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


# AudioBooks().get_audiobooks("2VQ0eAQdX9gN0rmF329p7r")
# AudioBooks().get_several_audiobooks("2VQ0eAQdX9gN0rmF329p7r")
# AudioBooks().get_audiobook_chapters("2VQ0eAQdX9gN0rmF329p7r")
AudioBooks().get_user_saved_audiobooks(4)
AudioBooks().check_user_saved_books("2VQ0eAQdX9gN0rmF329p7r,2VQ0eAQdX9gN0rmF329p7r")
