from os import environ


class Setting():
    SECRET_KEY = environ.get("SECRET_KEY", default="development")
