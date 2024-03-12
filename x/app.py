from bottle import default_app, error, get, redirect, static_file, template, response 
import sqlite3
import x



##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")
##############################
@get("/favicon.ico")
def _():
    return static_file("favicon.ico", ".")
##############################
@get("/art.billyraycyrus.gi.jpeg")
def _():
    return static_file("art.billyraycyrus.gi.jpeg", ".")

##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")


############################## USERS
import routes.get_users
import routes.get_user
import routes.create_user
import routes.delete_user
import routes.update_user
############################## ITEMS
import routes.get_items
import routes.get_item
import routes.create_item
import routes.delete_item
import routes.update_item

############################## API
import api_html.signup



############################## LOGIN
import routes.login
import routes.admin

############################## LOGOUT
@get("/logout")
def _():
  response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
  response.add_header("Pragma", "no-cache")
  response.add_header("Expires", 0)    
  response.delete_cookie("name")
  response.status = 303
  response.set_header("Location", "/login")
  return

##############################
@get("/")
def _():
    return template("index.html")
##############################

@error(404)
def _(error):
    return "page not found :(("

##############################

@get("/signup")
def _():
    return template("signup.html")

##############################
@get("/login")
def _():
    return template("login.html")


##############################

app = default_app()

