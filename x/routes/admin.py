from bottle import get, request, template, response
import x



##############################
@get ("/admin")
def _():
    try:
        x.disable_cache() # browser do not remember this page < >
        name = request.get_cookie("name", secret="my_secret")
        if name:
            return template("admin", name=name)
        else:
            response.status = 303
            response.set_header("Location", "/login")
            # return template("login")
        
    except Exception as ex:
        print(ex)
    finally:
        pass