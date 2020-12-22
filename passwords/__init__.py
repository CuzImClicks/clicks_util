from hashlib import sha512
import json
from getpass import getpass

def read():
    with open("passwords.json", "w+") as f:

        return json.load(f)

def check(username, password):
    if read()[username["password"]] == password:
        return True

    else:
        return False

def pwd_in():
    username = input("Username >>> ")
    password = getpass("Password >>> ")
    check(username, password)

pwd_in()