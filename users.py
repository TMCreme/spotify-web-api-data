import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Users:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_current_user_profile(self):
        auth_code_token = auth_flow_for_token("user-read-private")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me",
            headers=headers
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

    def get_user_top_items(self, type: str = "artists", limit: int = 20):
        auth_code_token = auth_flow_for_token("user-top-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/top/" + type,
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

    def get_user_profile(self, user_id: str):
        response = requests.get(
            self.base_url + "/users/" + user_id,
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_followed_artists(self, type: str = "artist"):
        auth_code_token = auth_flow_for_token("user-follow-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/following",
            headers=headers,
            params={
                "type": type
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

    def check_if_user_follows_artist_or_user(self, ids: str, type: str = "artist"):
        auth_code_token = auth_flow_for_token("user-follow-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/following/contains",
            headers=headers,
            params={
                "ids": ids,
                "type": type
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

    def check_if_user_follows_playlist(self, playlist_id: str, ids: str):
        response = requests.get(
            self.base_url + "/playlists/" + playlist_id + "/followers/contains",
            headers=self.headers,
            params={
                "ids":ids
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Users().get_current_user_profile()
# Users().get_user_top_items()
# Users().get_user_profile("31loxat22ivp4gseo2e633hl3xoq")
# Users().get_followed_artists()
# Users().check_if_user_follows_artist_or_user("1ukmGETCwXTbgrTrkRDnmn")
Users().check_if_user_follows_playlist("3cEYpjA9oz9GiPac4AsH4n", "31loxat22ivp4gseo2e633hl3xoq")
