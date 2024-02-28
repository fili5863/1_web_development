from bottle import post, request
import x
import uuid
##############################
@post("/users")
def _():
    try:
        # Validation 
        x.validate_user_name()
        x.validate_user_last_name()
        user_name = request.forms.get("user_name")
        user_last_name = request.forms.get("user_last_name")
        return f"Hi {user_name}s {user_last_name}"
    except Exception as ex:
        print(ex)
        return f"{ex}"
    finally:   
        pass