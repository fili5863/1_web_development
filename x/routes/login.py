from bottle import post, request, response
import x


##############################
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
        db = x.db()
        q = db.execute("SELECT * FROM users WHERE user_email = ? AND user_password= ?", (user_email, user_password))
        user = q.fetchone()
        if user: 
            print("........", user['user_name'])
        # TODO Connect to the db and check that the email and password are correct
        # db.execute(SELECT * FROM users WHERE user_email = ?  AND user_password = ?, (email, password));

            response.set_cookie("name", user['user_name'], secret="my_secret", httpOnly=True)
            return """
            <template mix-redirect="/admin">
            
            </template>
            """
        else: 
            return """
                <template mix-target="#error" mix-replace>
                    <div id="error">User doesn't exist</div>
                </template>
                """

    except Exception as ex:
        print(ex)
        print(ex.args[0])
        print(ex.args[1])
        print(type(ex))
        if "user_password" in ex.args[1]:
            return """
                <template mix-target="#error" mix-replace>
                    <div id="error">Invalid password</div>
                </template>
                """
        if "user_email" in ex.args[1]:
            return """
                <template mix-target="#error" mix-replace>
                    <div id="error">Invalid</div>
                </template>
                """
        
        return """
                <template mix-target="#error" mix-replace>
                    <div id="error">Under maintainance</div>
                </template>
                """
    finally:
        if "db" in locals(): db.close()