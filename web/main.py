from fastapi import FastAPI
import configparser

app = FastAPI()


# This is a simple Fast API app that receives the callback from Spotify
# After the user logs in from the browser, the code is sent to the callback
@app.get("/")
async def root(code: str):
    config = configparser.ConfigParser()
    config.add_section('authflow')

    config['authflow']['code'] = code

    with open('../base/secrets.ini', 'w') as configfile:
        config.write(configfile)
    print(code)
    return {"message": "Hello World: {}".format(code)}
