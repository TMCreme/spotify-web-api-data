from itertools import count
import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Player:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_player_state(self, country_code: str = "US"):
        auth_code_token = auth_flow_for_token("user-read-playback-state")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/player",
            headers=headers,
            params={
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
        elif response.status_code == 204:
            print("Playback not available or active")
        else:
            print(response.status_code)
            return response.json()["error"]["message"]

    def get_available_devices(self):
        auth_code_token = auth_flow_for_token("user-read-playback-state")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/player/devices",
            headers=headers
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        elif response.status_code == 204:
            print("Playback not available or active")
        else:
            print(response.status_code)
            return response.json()["error"]["message"]

    def get_currently_playing_track(self, country_code: str = "US"):
        auth_code_token = auth_flow_for_token("user-read-currently-playing")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/player/currently-playing",
            headers=headers,
            params={
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
        elif response.status_code == 204:
            print("Playback not available or active")
        else:
            print(response.status_code)
            return response.json()["error"]["message"]

    def get_recently_played_tracks(self):
        auth_code_token = auth_flow_for_token("user-read-recently-played")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/player/recently-played",
            headers=headers
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        elif response.status_code == 204:
            print("Playback not available or active")
        else:
            print(response.status_code)
            return response.json()["error"]["message"]

    def get_user_queue(self):
        auth_code_token = auth_flow_for_token("user-read-currently-playing")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/player/queue",
            headers=headers
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        elif response.status_code == 204:
            print("Playback not available or active")
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Player().get_player_state()
# Player().get_available_devices()
# Player().get_currently_playing_track()
# Player().get_recently_played_tracks()
Player().get_user_queue()
