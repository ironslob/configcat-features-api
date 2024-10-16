import configcatclient
import os
import json

from fastapi import FastAPI, Depends, HTTPException
from configcatclient.user import User

# TODO HTTP auth

configcat_sdk_key = os.environ["CONFIGCAT_SDK_KEY"]

app = FastAPI()


@app.get("/")
def get_feature_flag(
    feature_flag: str,
    default: str,
    user_identifier: str | None = None,
    user_email: str | None = None,
    user_country: str | None = None,
):

    configcat_client = configcatclient.get(configcat_sdk_key)
    user = None

    if user_identifier:
        user = User(user_identifier, user_email, user_country)

    if default:
        try:
            default = json.loads(default)

        except:
            pass

    value = configcat_client.get_value(feature_flag, default, user)

    return {feature_flag: value}
