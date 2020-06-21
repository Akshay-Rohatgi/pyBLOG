from db import check_login, get_all_post_contents, get_first_admin, get_main_content, change_main_content, get_specific_post, create_new_post, delete_post, change_bio, change_city, change_country
from flask import Flask, render_template, redirect, url_for, request, g, session
from flask_login import LoginManager, login_required, logout_user, login_user
from datetime import datetime
from jinja2 import Template
import hashlib
import flask


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

    try:
        username = session['username']
    except:
        username = None

    if request.method == 'POST':
        search_term = request.form['search']
        if get_specific_post(search_term) == False or get_specific_post(search_term) == '[]':
            error = True
            return render_template('posts.html', error=error)
        else:
            posts = get_specific_post(search_term)
            return render_template('posts.html', posts=posts)

    return render_template('index.html', name=name, content=content, username=username)

@app.route('/login', methods=['GET','POST'])
def login():

    try:
        username = session['username']
    except:
        username = None

    if request.method == 'POST':
        hashed_password = md5(request.form['password'])
        if check_login(request.form['username']) == False:
            error = True
            return render_template('login.html', error=error)
        if check_login(request.form['username']) == hashed_password:
            session['username'] = request.form['username']
            return redirect(url_for('panel'))

    return render_template('login.html', username=username)

@app.route('/posts', methods=['GET','POST'])
def posts():
    try:
        username = session['username']
    except:
        username = None

    posts = get_all_post_contents()
    if request.method == 'POST':
        search_term = request.form['search']
        if get_specific_post(search_term) == False or get_specific_post(search_term) == '[]':
            error = True
            return render_template('posts.html', error=error, username=username)
        else:
            posts = get_specific_post(search_term)
            return render_template('posts.html', posts=posts, username=username)
    return render_template('posts.html', posts=posts, username=username)

@app.route('/panel', methods=['GET','POST'])
def panel():
    if request.method == 'POST':

        if request.form.get('main_content', None) != None:
            if change_main_content(request.form.get('main_content')) == False:
                error = True
            else:
                error = False
    
        print(request.form.get('bio', None))
        if request.form.get('bio', None) != None:
            if change_bio(request.form.get('bio')) == False:
                error = True
            else:
                error = False

        if request.form.get('city', None) != None:
            if change_city(request.form.get('city')) == False:
                error = True
            else:
                error = False

        if request.form.get('country', None) != None:
            if change_country(request.form.get('country')) == False:
                error = True
            else:
                error = False
        return render_template('panel.html', error=error)

    if 'username' in session:
        username = session['username']
        return render_template('panel.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route('/post_man', methods=['GET','POST'])
def post_man():

    if request.method == 'POST':

        if request.form.get('title', None) != None and request.form.get('content', None) != None:
            if create_new_post(request.form['title'], request.form['content']) == False:
                error = True
            else:
                error = False
                return render_template('post_man.html', error=error)

        if request.form.get('delete', None) != None:
            if delete_post(request.form['delete']) == False:
                error = True
            else:
                error = False
                return render_template('post_man.html', error=error)

    if 'username' in session:
        username = session['username']
        return render_template('post_man.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/account_man', methods=['GET','POST'])
def account_man():

    if request.method == 'POST':
        print('placeholder')

    if 'username' in session:
        username = session['username']
        name = get_first_admin()
        return render_template('account_man.html', username=username, name=name)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'ba9&plln2_1siq984509mjd8340jjhhhHUH@&#$tQu89327493e8923y1eh3e283uyyw8ueh1273eh23ouwijwey892uj1hjwjjwjjj893eeeBBUIwi2sdhnjw8hu2pja8usjW%!'
    app.run(host = '0.0.0.0', port = 5000, debug=True)
