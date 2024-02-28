from bottle import get, template
import x


##############################
@get("/users/<id>")
def _(id):
    try:
        db = x.db()
        q = db.execute("SELECT * FROM users WHERE user_pk = ?", (id,))
        user = q.fetchone()
        title = "user" + id
        return template('user', id=id, user_name=user["user_name"], title=title)
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()


                    


