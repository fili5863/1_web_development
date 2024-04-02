from bottle import delete, get, post, put, request, static_file, template, response
import x
from icecream import ic

##############################
@get("/favicon.ico")
def _():
    return static_file("favicon.ico", ".")

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")

##############################
@get("/")
def _():
    try:
        x.disable_cache()
        name = request.get_cookie("name", secret="my_secret")
        if name:
            users = x.db({"query":"FOR user IN users RETURN user"})
            return template("users", users=users["result"])
        else:
            return template("index")
    
    except Exception as ex:
        ic(ex)
        return "system under maintainance"         
    finally:
        pass
##############################
@get("/users")
def _():
    try:
        x.disable_cache()
        name = request.get_cookie("name", secret="my_secret")
        if name:
            users = x.db({"query":"FOR user IN users RETURN user"})
            return template("users", users=users["result"])
        else:
            response.status = 303
            response.set_header("Location", "/")
    except Exception as ex:
        ic(ex)
        return "system under maintainance"         
    finally:
        pass

##############################
@post("/users")
def _():
    try:
        valid_cookie = x.validate_cookie()
        if valid_cookie:
            user_name = x.validate_user_name()
            user_last_name = x.validate_user_last_name()
            user_username = x.validate_user_username()
            user_gender = x.validate_gender()

            ic(user_last_name)
            user = {"name":user_name, "last_name":user_last_name,   "username":user_username, "gender":user_gender}
            res = x.db({"query":"INSERT @doc IN users RETURN NEW",  "bindVars":{"doc":user}})
            html = template("_user.html", user=res["result"][0])
            form_create_user =  template("_form_create_user.html")
            return f"""
            <template mix-target="#users" mix-top>
                {html}
            </template>
            <template mix-target="#frm_user" mix-replace>
                {form_create_user}
            </template>
            """
    except Exception as ex:
        ic(ex)
        if "user_name" in str(ex):
            return f"""
            <template mix-target="#message">
                {ex.args[1]}
            </template>
            """            
    finally:
        pass

##############################
@delete("/users/<key>")
def _(key):
    try:
        valid_cookie = x.validate_cookie()
        if valid_cookie:
            valid_key = x.validate_key(key)
            ic(valid_key)
            ic(valid_cookie)

            res = x.db({"query":"""
                    FOR user IN users
                    FILTER user._key == @key
                    REMOVE user IN users RETURN OLD""", 
                    "bindVars":{"key":valid_key}})
            print(res)
            return f"""
            <template mix-target="[id='{valid_key}']" mix-replace>
            <div class="mix-fade-out user_deleted" mix-ttl="2000">User deleted</div>
            </template>
            """
    except Exception as ex:
        ic(ex)
    finally:
        pass

##############################
@put("/users/<key>")
def _(key):
    try:
        valid_cookie = x.validate_cookie()
        if valid_cookie:
            name = x.validate_user_name()
            last_name = x.validate_user_last_name()
            username = x.validate_user_username()
            res = x.db({"query":"""
                            UPDATE { _key: @key, name: @name,   last_name:@last_name, username: @username} 
                            IN users 
                            RETURN NEW""",
                        "bindVars":{
                            "key": f"{key}",
                            "name":f"{name}",
                            "last_name":f"{last_name}",
                            "username":f"{username}"
                        }})
            return f"""
            <template>            
            </template>
            """
    except Exception as ex:
        ic(ex)
        if "user_name" in str(ex):
            return f"""
            <template mix-target="#message">
                {ex.args[1]}
            </template>
            """            
    finally:
        pass

##############################
# @post ("/login")
# def _():
#     try:
#         # TODO: validate the email and password
#         # validate email
#         x.validate_user_email()
#         # validate password
#         x.validate_user_password()
#         user_email = request.forms.get("user_email")
#         user_password = request.forms.get("user_password")
#         db = x.rel_db()
#         q = db.execute("SELECT * FROM users WHERE user_email = ? AND user_password= ? AND user_role_fk= 1", (user_email, user_password))
#         user = q.fetchone()
#         if user: 
#             print("........", user['user_name'])
#         # TODO Connect to the db and check that the email and password are correct
#         # db.execute(SELECT * FROM users WHERE user_email = ?  AND user_password = ?, (email, password));

#             response.set_cookie("name", user['user_name'], secret="my_secret", httpOnly=True)
#             return """
#             <template mix-redirect="/users">
            
#             </template>
#             """
#         else: 
#             return """
#                 <template mix-target="#error" mix-replace>
#                     <div id="error">User doesn't exist</div>
#                 </template>
#                 """

#     except Exception as ex:
#         print(ex)
#         print(ex.args[0])
#         print(ex.args[1])
#         print(type(ex))
#         if "user_password" in ex.args[1]:
#             return """
#                 <template mix-target="#error" mix-replace>
#                     <div id="error">Invalid password</div>
#                 </template>
#                 """
#         if "user_email" in ex.args[1]:
#             return """
#                 <template mix-target="#error" mix-replace>
#                     <div id="error">Invalid</div>
#                 </template>
#                 """
        
#         return """
#                 <template mix-target="#error" mix-replace>
#                     <div id="error">Under maintainance</div>
#                 </template>
#                 """
#     finally:
#         if "db" in locals(): db.close()


@post ("/login")
def _():
    try:
        # TODO: validate the email and password
        # validate email
        x.validate_user_email()
        # validate password
        x.validate_user_password()
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")
        db = x.rel_db()
        q = db.execute("SELECT * FROM users WHERE user_email = ?", (user_email,))
        user = q.fetchone()
        if user:
            if user['user_password'] == user_password:
                print("........", user['user_name'])
                response.set_cookie("name", user['user_name'], secret="my_secret", httpOnly=True)
                return """
                <template mix-redirect="/users">
                
                </template>
                """
            else:
                return """
                    <template mix-target="#error" mix-replace>
                        <div id="error">Email/password is invalid</div>
                    </template>
                    """
    except Exception as ex:
        print(ex)
        print(ex.args[0])
        print(ex.args[1])
        print(type(ex))
        return """
                <template mix-target="#error" mix-replace>
                    <div id="error">Under maintainance</div>
                </template>
                """
    finally:
        if "db" in locals(): db.close()









