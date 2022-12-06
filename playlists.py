import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Playlists:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_playlist(self, playlist_id: str, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/playlists/" + playlist_id,
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

    def get_playlist_items(self, playlist_id: str, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/playlists/" + playlist_id + "/tracks",
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

    def get_current_user_playlist(self, limit: int = 20):
        auth_code_token = auth_flow_for_token("playlist-read-private")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/playlists",
            headers=headers,
            params={
                "limit": limit
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

    def get_user_playlists(self, user_id: str):
        response = requests.get(
            self.base_url + "/users/" + user_id + "/playlists",
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_featured_playlist(self, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/browse/featured-playlists",
            headers=self.headers,
            params={
                "country": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def category_playlists(self, category_id: str = "dinner", country_code: str = "US"):
        response = requests.get(
            self.base_url + "/browse/categories/" + category_id + "/playlists",
            headers=self.headers,
            params={
                "country": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_playlist_cover_image(self, playlist_id: str):
        response = requests.get(
            self.base_url + "/playlists/" + playlist_id + "/images",
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Playlists().get_playlist("3cEYpjA9oz9GiPac4AsH4n")
# Playlists().get_playlist_items("3cEYpjA9oz9GiPac4AsH4n")
# Playlists().get_current_user_playlist()
# Playlists().get_user_playlists("31loxat22ivp4gseo2e633hl3xoq")
# Playlists().get_featured_playlist()
# Playlists().category_playlists()
Playlists().get_playlist_cover_image("3cEYpjA9oz9GiPac4AsH4n")
