from flask import Flask, render_template, redirect, url_for, request, g, session
import flask
from flask_login import login_required, logout_user, login_user
from db import check_login, get_all_post_contents, get_first_admin, get_main_content
from jinja2 import Template
import hashlib
from datetime import datetime

#temp fix
logged_in = False

def md5(text):
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/', methods=['GET','POST'])
def main():
    if get_main_content() != False:
        content = get_main_content()
    name = get_first_admin()
    return render_template('index.html', name=name, content=content)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        hashed_password = md5(request.form['password'])
        if check_login(request.form['username']) == False:
            error = True
            return render_template('login.html', error=error)
        if check_login(request.form['username']) == hashed_password:
            logged_in = True
            return panel(logged_in)
    return render_template('login.html')

@app.route('/posts', methods=['GET','POST'])
def posts():
    posts = get_all_post_contents()
    return render_template('posts.html', posts=posts)

@app.route('/panel', methods=['GET','POST'])
def panel(logged_in):
    if logged_in == True:
        return render_template('panel.html')
    else:
        return login()

@app.route('/results', methods=['GET','POST'])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
