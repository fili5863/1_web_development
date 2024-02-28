from bottle import get, template 
import x


##############################
@get("/users")
def _():
    try:
        db = x.db()
        q = db.execute("SELECT * FROM users") # Runs the command in the db
        users = q.fetchall() # Parses data from db to python
        return template("users", users=users) # Returns the users to the template
    except Exception as ex:
        return f"Error {ex}" 
    finally:
       if db is not None: 
            db.close()
        
