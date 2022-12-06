import requests
from base.main import (
    obtain_auth_token, read_config
)


class Categories:
    def __init__(self):
        self.base_url = read_config("CLIENT_CREDENTIALS", "BASE_URL")
        self.auth_token = obtain_auth_token()
        self.headers = {
            "Authorization": self.auth_token[
                "token_type"
                ] + " " + self.auth_token["access_token"],
            "Content-Type": "application/json"
        }

    def get_several_browse_categories(self, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/browse/categories",
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

    def get_single_browse_category(self, category_id: str, country_code: str = "US"):
        response = requests.get(
            self.base_url + "/browse/categories/" + category_id,
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


# Categories().get_several_browse_categories()
Categories().get_single_browse_category("0JQ5DAqbMKFQ00XGBls6ym")
