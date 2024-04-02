from bottle import get, template, run, post, request, static_file

import uuid
import x

######################################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")

######################################
@get('/')
def _():
    return template('index', name='Samuel')

######################################
@post("/users")
def _():
    try:
        user_pk = uuid.uuid4().hex
        user_name = request.forms.get('user_name')
        user_email = request.forms.get('user_email')
        user_password = request.forms.get('user_password')
        user_verification_key = uuid.uuid4().hex
        print(f"""Din mor blows \n {user_name} \n {user_email} \n {user_password} \n {user_verification_key}""")
        db = x.db()
        db.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", (user_pk, user_name, user_email, user_password, 0, user_verification_key))
        db.commit()
        x.send_mail(user_email, user_email, "Verify your account", template("email_verification", key=user_verification_key))
        return f"""
        <template>
        <p>Thank you for signing up {user_name}!</p>
        <p>We have sent you an email to verify your account</p>
        </template>
"""
    except Exception as ex:
        return ex
    finally:
        if "db" in locals(): db.close()
######################################
@get("/verify/<key>")
def _(key):
    db = x.db()
    db.execute("UPDATE users SET user_verified = 1 WHERE user_verification_key = ?", (key,))
    user_name = db.execute("SELECT user_name FROM users WHERE user_verification_key = ?", (key,)).fetchone()["user_name"]
    db.commit()
    return template("email_welcome", user_name=user_name)

######################################
run(host='127.0.0.1', port=8080, debug=True, reloader=True, interval=0)