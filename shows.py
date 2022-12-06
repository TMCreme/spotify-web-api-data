import requests
import os
from base.main import (
    obtain_auth_token, read_config, auth_flow_for_token
)


class Shows:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_show(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/shows/" + id,
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

    def get_several_shows(self, id: str, country_code="US"):
        response = requests.get(
            self.base_url + "/shows",
            headers=self.headers,
            params={
                "ids": id,
                "market": country_code
            }
        )
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            return response.json()["error"]["message"]

    def get_show_episodes(self, id: str, limit: int, country_code="US"):
        response = requests.get(
            self.base_url + "/shows/" + id + "/episodes",
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

    # User data requires auth code
    def get_user_saved_shows(self, limit: int):
        auth_code_token = auth_flow_for_token("user-read-playback-position")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/shows",
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

    def check_user_saved_shows(self, ids: str):
        auth_code_token = auth_flow_for_token("user-read-playback-position")
        headers = {
            "Authorization": "Bearer " + auth_code_token["access_token"],
            "Content-Type": "application/json"
        }
        response = requests.get(
            self.base_url + "/me/shows/contains",
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


# Shows().get_show("53dHyhzazFrmPhwuambyuM")
# Shows().get_several_shows("53dHyhzazFrmPhwuambyuM,5exfRPDNCBHmntEkJrlLmX")
# Shows().get_show_episodes("53dHyhzazFrmPhwuambyuM", 4)
# Shows().get_user_saved_shows(5)
Shows().check_user_saved_shows("53dHyhzazFrmPhwuambyuM,5exfRPDNCBHmntEkJrlLmX")
