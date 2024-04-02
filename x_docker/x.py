from bottle import request
import re


USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = "^.{2,20}$"

def validate_user_name():
    error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} characters"
    user_name = request.forms.get("user_name", "")
    user_last_name = request.forms.get("user_last_name", "")



    user_name = user_name.strip()
    user_last_name = user_last_name.strip()
    if not re.match(USER_NAME_REGEX, user_name): 
        raise Exception(400, f"user_name {error}")
    if not re.match(USER_NAME_REGEX, user_last_name): 
        raise Exception(400, f"user_last_name {error}")

    return user_name, user_last_name