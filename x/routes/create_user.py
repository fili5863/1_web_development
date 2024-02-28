from bottle import post, request
import x
import uuid
##############################
@post("/users")
def _():
    try:
        # Validation 
        

        user_name = request.forms.get("user_name")
        user_pk = uuid.uuid4().hex
        db = x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?, ?)" , (user_pk, user_name, "0", "0"))
        db.commit()
        return f"""
        <template mix-target="#users" mix-top>
            <div>
            {user_name}
            </div>
        </template>
    """
     
    except Exception as ex:
        print(ex)
        return f"{ex}"
    finally:   
        if "db" in locals(): db.close()