import requests 
import configparser
import os
import base64
import time


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


def auth_flow_for_token():
    # Read credentials from secrets
    client_id = read_config("CLIENT_CREDENTIALS", "CLIENT_ID")
    client_secret = read_config("CLIENT_CREDENTIALS", "CLIENT_SECRET")
    auth_url = read_config("CLIENT_CREDENTIALS", "AUTH_URL")
    # Composition of the Login URL to grant authorization to user
    login_url = "{0}response_type={1}&client_id={2}&scope={3}&redirect_uri={4}".format(
        read_config("AUTHCODE_FLOW", "BASE_URL"),
        read_config("AUTHCODE_FLOW", "RESPONSE_CODE"),
        client_id,
        read_config("AUTHCODE_FLOW", "SCOPE"),
        read_config("AUTHCODE_FLOW", "REDIRECT_URI")
    )
    # Checking if login from browser is complete before proceeding
    # Sleeping for 5 seconds before checking
    print("Copy and paste the URL below into the browser and login\n\n\n", login_url)
    while not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "secrets.ini")):
        print("Waiting for you to complete login and Agree...")
        time.sleep(5)
    config = configparser.ConfigParser()
    config.read(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "secrets.ini")
        )
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
    auth_token = requests.post(
        auth_url,
        data={
            "code": config["authflow"]["code"],
            "grant_type": "authorization_code",
            "redirect_uri": read_config("AUTHCODE_FLOW", "REDIRECT_URI")
            },
        headers=headers
    )
    # print(auth_token.json())
    return auth_token.json()
    # pass


# obtain_auth_token()
