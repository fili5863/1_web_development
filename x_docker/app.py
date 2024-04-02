from bottle import get, post, put, static_file, template, request, response, delete
import requests
import x

url = "http://arangodb:8529/_api/cursor"


##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

##########################################

@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")

##########################################

@get("/")
def _():
    try:
        user_query = {"query": "FOR user IN users SORT user._key DESC RETURN user"}
        r = requests.post(url, json=user_query)
        if r.status_code == 201:
            data = r.json()
            return template("index.html", users=data["result"])
    except Exception as ex:
        print(ex)
        return "Error"

##########################################

@post ("/users")
def _():
    try:
    # Get the values from the form
        user_name, user_last_name = x.validate_user_name()

    # Insert the user into the database
        user_query = {"query": f"INSERT {{'version': 1, 'user_name': '{user_name}', 'user_last_name': '{user_last_name}'}} INTO users RETURN NEW"}
        r = requests.post(url, json = user_query)

        if r.status_code == 201:
            data = r.json()
            result = data.get("result", [])
            user = result[0]



            return f"""
            
            <template mix-target="#userSection" mix-top>
            <div class='flex p-3 justify-between align-middle bg-gray-200' id='user_{{user['_key']}}'
            class="relative flex gap-3 items-center justify-center border rounded-md
            bg-white border-gray-200 p-2">
                <p class='text-blue-500 text-center'>{user["_key"]}</p>
                    <form id='editFrm' class='flex gap-3'>
                        <input 
                        class='text-black p-1 rounded-md' 
                        type="text" mix-put='/user/{{user['_key']}}' 
                        mix-blur 
                        mix-data='#editFrm' 
                        name="user_name_change" 
                        value='{user['user_name']}'/>
                        <input 
                        class='text-black p-1 rounded-md' 
                        type="text" 
                        mix-put='/user/{{user['_key']}}' 
                        mix-blur mix-data='#editFrm' 
                        name="user_last_name_change" 
                        value='{user["user_last_name"]}'/>
                    </form>
                    <button mix-delete='/user/{{user['_key']}}'>
                        🗑️
                    </button>
                    </div>
                    </template>
                """
        else:
            raise Exception("Error")
        
        print (result[0]['first_name']) 


        
    except Exception as ex:
        print(ex)
        return "Error"
    finally:
        pass

##########################################

@put ("/user/<id>")
def _(id):
    try:
    # Get the user data from the id
        user_query_get = {"query": f"FOR user IN users FILTER user._key == '{id}' RETURN user"}
        user_response = requests.post(url, json=user_query_get)
        user_data = user_response.json()["result"][0]

    # Update the user version, so it changes for every time the user is updated
        new_version = int(user_data["version"]) + 1
    # Get the values from the form
        first_name = request.forms.get("user_name_change")
        last_name = request.forms.get("user_last_name_change")
        user_query = {"query": f"UPDATE '{id}' WITH {{'version': {new_version}, 'user_name': '{first_name}', 'user_last_name': '{last_name}'}} IN users"}
        print("THIS HERE IS THE KEY OF THE USER", user_query)

        user_response_post = requests.post(url, json = user_query)


        if user_response_post.status_code == 201:
            data = user_response_post.json()
            result = data.get("result", [])
            user = result[0]

            return f"""
            <template mix-target="#user_{{user['_key']}}" mix-replace>
                <div class='flex p-3 justify-between align-middle bg-gray-200' id='user_{{user['_key']}}'
                class="relative flex gap-3 items-center justify-center border rounded-md
                bg-white border-gray-200 p-2">
                <p class='text-blue-500 text-center'>{{user["_key"]}}</p>
                    <form id='editFrm_{{user["_key"]}}' class='flex gap-3'>
                        <input 
                        class='text-black p-1 rounded-md' 
                        type="text" mix-put='/user/{{user['_key']}}' 
                        mix-blur 
                        mix-data='#editFrm_{{user["_key"]}}'
                        name="user_name_change" 
                        value='{user['user_name']}'/>
                        <input 
                        class='text-black p-1 rounded-md' 
                        type="text" 
                        mix-put='/user/{{user['_key']}}' 
                        mix-blur 
                        mix-data='#editFrm_{{user["_key"]}}' 
                        name="user_last_name_change" 
                        value='{{user["user_last_name"]}}'/>
                    </form>
                    <button mix-delete='/user/{{user['_key']}}'>
                        🗑️
                    </button>
                </div>
                </template>
                """
        
    except Exception as ex:
        print(ex)
    finally: 
        pass
   

##########################################
    

    
@delete ("/user/<id>")
def _(id):
    try: 
    # Delete the user from the database
        user_query = {"query": f"FOR user IN users FILTER user._key == '{id}' REMOVE user in users"}
        user_response = requests.post(url, json=user_query)
        if (user_response.status_code == 201):
        
            return f"""
            <template mix-target="#user_{id}" mix-replace >
                <div class='flex p-3 justify-between align-middle bg-gray-200' id='user_{{user['_key']}}'
                class="relative flex gap-3 items-center justify-center border rounded-md
                bg-white border-gray-200 p-2" mix-ttl=1500>
                User has been deleted
                </div>
                </template>
                """
    except Exception as ex:
        print(ex)
    finally:
        pass