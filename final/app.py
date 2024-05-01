from flask import Flask, render_template, request

app = Flask(__name__)

#######################################################
@app.get('/')
def render_index():
    return render_template('index.html', name='Samuel', active_home='active-link')


#######################################################
@app.get('/login')
def render_login():
    return render_template('login.html', active_login='active-link')


#######################################################
@app.post('/items')
def create_item():
    return 'item created'


#######################################################
@app.put('/items')
def update_item():
    return 'item updated'


#######################################################
@app.delete('/items/<id>')
def delete_item(id):
    return f'item deleted with id {id}'
