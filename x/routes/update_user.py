from bottle import put, request
import x

@put("/users/<id>")
def _(id):
    user_name = request.forms.get("update_user_name")
    try:
        db = x.db()
        q = db.execute("UPDATE users SET user_name = ? WHERE user_pk = ?", (user_name, id))
        db.commit()
        return f"""
        <template mix-target="#the_user_name" mix-replace>
      
           <h1>USER NAME: {user_name}</h1>
      
        </template>

                <template mix-target="#update_user_input" mix-replace>
      
             <input
            id="update_user_input"
            name="update_user_name"
            type="text"
            mix-check=".{2,20}"
            placeholder="{user_name}"
            />
      
        </template>
    """
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()