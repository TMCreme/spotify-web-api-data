import requests
import os
from base.main import (
    obtain_auth_token, read_config
)


# Note: Chapter are only available for the
# US, UK, Ireland, New Zealand and Australia markets.
class Chapters:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_chapter(self, id: str, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/chapters/" + id,
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

    def get_several_chapters(self, ids: str, country_code="US"):
        response = requests.get(
            self.base_url + "/chapters",
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


# Chapters().get_chapter("")
# Chapters().get_several_chapters("")
