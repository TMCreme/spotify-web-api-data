import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Tracks:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_track(self, id: str, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/tracks/" + id,
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

    def get_several_tracks(self, ids: str, country_code="US"):
        response = requests.get(
            self.base_url + "/tracks",
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

    def get_user_saved_tracks(self, limit: int, country_code="US"):
        auth_code_token = auth_flow_for_token()
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/tracks",
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

    def check_user_saved_tracks(self, ids: str):
        auth_code_token = auth_flow_for_token()
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/tracks/contains",
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

    # Multiple tracks' audio features
    def get_tracks_audio_features(self, ids: str):
        response = requests.get(
            self.base_url + "/audio-features",
            headers=self.headers,
            params={
                "ids": ids
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    # Single track's audion features
    def get_track_audio_features(self, id: str):
        response = requests.get(
            self.base_url + "/audio-features/" + id,
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_track_audio_analysis(self, id: str):
        response = requests.get(
            self.base_url + "/audio-analysis/" + id,
            headers=self.headers
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_recommendations(self, seed_artists: str, seed_genres: str, seed_tracks: str, limit: int=None, country_code="US", max_acousticness=range(0, 1)):
        response = requests.get(
            self.base_url + "/recommendations",
            headers=self.headers,
            params={
                "seed_artists": seed_artists,
                "seed_genres": seed_genres,
                "sedd_tracks": seed_tracks,
                "limit": limit,
                "market": country_code,
                "max_acousticness": max_acousticness
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Tracks().get_track("4iV5W9uYEdYUVa79Axb7Rh")
# Tracks().get_several_tracks("4iV5W9uYEdYUVa79Axb7Rh,1301WleyT98MSxVHPZCA6M")
# Tracks().get_user_saved_tracks(4)
# Tracks().check_user_saved_tracks("4iV5W9uYEdYUVa79Axb7Rh,1301WleyT98MSxVHPZCA6M")
# Tracks().get_tracks_audio_features("4iV5W9uYEdYUVa79Axb7Rh,1301WleyT98MSxVHPZCA6M")
# Tracks().get_track_audio_features("4iV5W9uYEdYUVa79Axb7Rh")
# Tracks().get_track_audio_analysis("4iV5W9uYEdYUVa79Axb7Rh")
Tracks().get_recommendations("1ukmGETCwXTbgrTrkRDnmn","gospel","4iV5W9uYEdYUVa79Axb7Rh",limit=4, max_acousticness=1)
