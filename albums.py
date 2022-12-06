import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Albums:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_album(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/albums/" + id,
            headers=self.headers,
            params={
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json()["error"]["message"])
            return response.json()["error"]["message"]

    def get_several_albums(self, ids: str, country_code="US"):
        response = requests.get(
            self.base_url + "/albums",
            headers=self.headers,
            params={
                "market": country_code,
                "ids": ids
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json()["error"]["message"])
            return response.json()["error"]["message"]

    def get_album_tracks(self, id: str, limit: int, country_code="US"):
        response = requests.get(
            self.base_url + "/albums/" + id + "/tracks",
            headers=self.headers,
            params={
                "market": country_code,
                "limit": limit
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json()["error"]["message"])
            return response.json()["error"]["message"]

    # User data requires the Authorization flow for access token
    # To be implemented later
    def get_user_saved_albums(self, limit: int, country_code="US"):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/albums",
            headers=headers,
            params={
                "market": country_code,
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
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]

    # Also a user data that requires authorization flow
    def check_user_saved_albums(self, ids):
        auth_code_token = auth_flow_for_token("user-library-read")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/albums/contains",
            headers=headers,
            params={
                "ids": ids,
            }
        )
        try:
            os.remove("base/secrets.ini")
        except Exception as e:
            print(e)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print("There was an error, ", response.json())
            return response.json()["error"]["message"]

    def get_new_releases(self, limit: int, country_code="GH"):
        response = requests.get(
            self.base_url + "/browse/new-releases",
            headers=self.headers,
            params={
                "country": country_code,
                "limit": limit
            }
        )
        # print(self.headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        # elif response.status_code == 401:
        else:
            print(response.json())
            return response.json()["error"]["message"]


# Albums().get_album("3WCZbOcvzRlzyEnRVPtKQF", "GH")
# Albums().get_several_albums("3WCZbOcvzRlzyEnRVPtKQF,6LeAlLAh3zqe1PFaX0mqpF","GH")
# Albums().get_album_tracks("3WCZbOcvzRlzyEnRVPtKQF", 4)
# Albums().get_user_saved_albums(5)
Albums().check_user_saved_albums("3WCZbOcvzRlzyEnRVPtKQF,6LeAlLAh3zqe1PFaX0mqpF")
# Albums().get_new_releases(4)
