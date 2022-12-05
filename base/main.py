import requests 
import configparser
import os
import base64


def obtain_auth_token():
    # Read credentials from secrets
    client_id = read_config("CLIENT_CREDENTIALS", "CLIENT_ID")
    client_secret = read_config("CLIENT_CREDENTIALS", "CLIENT_SECRET")
    auth_url = read_config("CLIENT_CREDENTIALS", "AUTH_URL")

    # Encode the secrets as a base64 byte
    # Encode the string with ascii before encoding to base64
    encoded_creds = base64.b64encode(
            (client_id + ":" + client_secret).encode("ascii")
    )
    # Decode to produce a base64 encoded string
    encoded_str = encoded_creds.decode("ascii")

    # print(client_id)
    # print(str(encoded_str))
    # Set the headers for the request
    headers = {
        "Authorization": "Basic " + encoded_str,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # Make the auth request
    auth_token = requests.post(
        auth_url, headers=headers,
        data={"grant_type": "client_credentials"}
    )
    # Return the auth token result to use for other requests
    # print(auth_token.json())
    return auth_token.json()


def read_config(section, item):
    # Initialize configparser and local file
    config = configparser.ConfigParser()
    config.read(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "config.ini")
        )
    return config[section][item]


# obtain_auth_token()
