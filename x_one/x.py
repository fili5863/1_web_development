from bottle import request, response
from icecream import ic
import re
import requests
import random
import sqlite3
import pathlib

##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)   


##############################

def db(query):
    try:
        url = "http://arangodb:8529/_api/cursor"
        res = requests.post( url, json = query )
        ic(res)
        ic(res.text)
        return res.json()
    except Exception as ex:
        print("#"*50)
        print(ex)
    finally:
        pass


##############################
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

##############################
    
def rel_db():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/database/company.db")
        db.execute("PRAGMA foreign_keys = ON")
        db.row_factory = dict_factory # JSON objects
        return db
    except Exception as ex:
        print("db function has an errror")
        print(ex)
    finally:
        pass


##############################   
USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = "^.{2,20}$"

def validate_user_name():
    error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} characters"
    user_name = request.forms.get("user_name", "")
    user_name = user_name.strip()
    if not re.match(USER_NAME_REGEX, user_name): raise Exception(400, error)
    return user_name


##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
USER_LAST_NAME_REGEX = "^.{2,20}$"

def validate_user_last_name():
    error = f"user_last_name {USER_LAST_NAME_MIN} to {USER_LAST_NAME_MAX} characters"
    user_last_name = request.forms.get("user_last_name", "")
    user_last_name = user_last_name.strip()
    if not re.match(USER_LAST_NAME_REGEX, user_last_name): raise Exception(400, error)
    return user_last_name


##############################
USER_USERNAME_MIN = 2
USER_USERNAME_MAX = 20
USER_USERNAME_REGEX = "^.{2,20}$"

def validate_user_username():
    error = f"user_username {USER_USERNAME_MIN} to {USER_USERNAME_MAX} characters"
    user_username = request.forms.get("user_username", "")
    user_username = user_username.strip()
    if not re.match(USER_USERNAME_REGEX, user_username): raise Exception(400, error)
    return user_username


##############################

KEY_REGEX = "^[1-9][0-9]*$"

def validate_key(key):
    if not re.match(KEY_REGEX, key): raise Exception(400, "invalid key")
    return key

##############################

GENDER_REGEX = "^[0-1]$"

def validate_gender():
    gender = request.forms.get("user_gender", "")
    print("-------------------------", gender)
    if not re.match(GENDER_REGEX, gender): raise Exception(400, 'Invalid Gender')
    return gender

##############################

def generate_random_color():
    r = random.randint(0, 170)
    g = random.randint(0, 170)
    b = random.randint(0, 170)
    return '#%02x%02x%02x' % (r, g, b)


##############################
USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50
USER_PASSWORD_REGEX = "^.{6,50}$"

def validate_user_password():
        error = f"user_password {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
        user_password = request.forms.get("user_password", "")
        user_password = user_password.strip()
        if not re.match(USER_PASSWORD_REGEX, user_password): raise Exception(400, error)
        return user_password

##############################

USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_user_email():
	error = f"user_email invalid"
	user_email = request.forms.get("user_email", "")
	user_email = user_email.strip()
	if len(user_email) < USER_EMAIL_MIN : raise Exception(400, error)
	if len(user_email) > USER_EMAIL_MAX : raise Exception(400, error)  
	if not re.match(USER_EMAIL_REGEX, user_email): raise Exception(400, error)
	return user_email


##############################
def validate_cookie():
    try:
        name = request.get_cookie("name", secret="my_secret")
        if name: 
            return name
    except Exception as ex:
        print(ex)
    finally:
        pass