# Get Spotify Web API data using Python 

## introduction
This project contains multiple files, each representing a section in the Spotify Web API. The current functions have only GET APIs from the WEB APIs. The Spotify API has different forms of authentication/authorization. Specifically for User Data APIs, the Authorization Code Flow is used. It forces a user to login via a browser and approve/authorize the particular action on the user data before proceeding. 

## Description
This project contains multiple files, each representing a section in the Spotify Web API. The current functions have only GET APIs from the WEB APIs. The Spotify API has different forms of authentication/authorization. Specifically for User Data APIs, the Authorization Code Flow is used. It forces a user to login via a browser and approve/authorize the particular action on the user data before proceeding. Since these are purely APIs, I created a simple FastAPI app that acts as the callback endpoint to receive the authorization code to be used in such cases that require the Authorization Code Flow.


## Running the code 
* Clone the project into a local directory
* Change directory to the root of the project and install requirements with `pip install -r requirements.txt`
* Fill the required information in the `base/config.ini` file as specified below. It contains the credentials and sensitive data needed to run the code. (NB: The REDIRECT_URI needs to be the one that the Fast API is running on. Remember to set it in the APP settings on the Spotify Dashboard)
* For all User Data APIs, start the FastAPI server with the command `uvicorn main:app --reload`. Otherwise it can be ignored
* Run the particular module with `python {filename}`
* For User Data APIs, a link is printed to the terminal which should be copied and pasted in the browser for authenticating and authorizing such an action on the user data
* After successfully authenticating, the result should be printed to the terminal. 
* Otherwise, an error will be printed to the terminal. 


### Sample config.ini
```
[CLIENT_CREDENTIALS]
CLIENT_ID=
CLIENT_SECRET=
AUTH_URL=
BASE_URL=

[AUTHCODE_FLOW]
BASE_URL=https://accounts.spotify.com/authorize?
RESPONSE_TYPE=code
SCOPE=user-library-read
REDIRECT_URI=http://localhost:8000/
```
## Packages
* requests
* fastapi 
