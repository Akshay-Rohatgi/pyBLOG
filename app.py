from flask import Flask, render_template, redirect, url_for, request, g, session
import flask
from flask_login import LoginManager, login_required, logout_user, login_user
from db import check_login, get_all_post_contents, get_first_admin, get_main_content, get_specific_post
from jinja2 import Template
import hashlib
from datetime import datetime



def md5(text):
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

app = Flask(__name__, static_folder='static', static_url_path='')
login_manager = LoginManager()

@app.route('/', methods=['GET','POST'])
def main():
    if get_main_content() != False:
        content = get_main_content()
    name = get_first_admin()

    if request.method == 'POST':
        search_term = request.form['search']
        if get_specific_post(search_term) == False or get_specific_post(search_term) == '[]':
            error = True
            return render_template('posts.html', error=error)
        else:
            posts = get_specific_post(search_term)
            return render_template('posts.html', posts=posts)

    return render_template('index.html', name=name, content=content)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        hashed_password = md5(request.form['password'])
        if check_login(request.form['username']) == False:
            error = True
            return render_template('login.html', error=error)
        if check_login(request.form['username']) == hashed_password:
            session['username'] = request.form['username']
            return redirect(url_for('panel'))
        
        if len(request.form['search']) > 0:
            search_term = request.form['search']
        
        if get_specific_post(search_term) == False or get_specific_post(search_term) == '[]':
            error = True
            return render_template('posts.html', error=error)
        else:
            posts = get_specific_post(search_term)
            return render_template('posts.html', posts=posts)

    return render_template('login.html')

@app.route('/posts', methods=['GET','POST'])
def posts():
    posts = get_all_post_contents()
    if request.method == 'POST':
        search_term = request.form['search']
        if get_specific_post(search_term) == False or get_specific_post(search_term) == '[]':
            error = True
            return render_template('posts.html', error=error)
        else:
            posts = get_specific_post(search_term)
            return render_template('posts.html', posts=posts)
    return render_template('posts.html', posts=posts)

@app.route('/panel', methods=['GET','POST'])
def panel():
    if 'username' in session:
        return render_template('panel.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route('/results', methods=['GET','POST'])
def results():
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.secret_key = 'ba9&plln2_1siq984509mjd8340jjhhhHUH@&#$tQW%!'
    app.run(host = '0.0.0.0', port = 5000, debug=True)
