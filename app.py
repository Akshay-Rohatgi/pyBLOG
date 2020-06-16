from flask import Flask, render_template, redirect, url_for, request, g
from db import check_login, get_all_post_contents
from jinja2 import Template
import hashlib

def md5(text):
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        hashed_password = md5(request.form['password'])
        if check_login(request.form['username']) == False:
            return render_template('login.html')
        if check_login(request.form['username']) == hashed_password:
            return render_template('panel.html')
    return render_template('login.html')

@app.route('/posts')
def posts():
    posts = get_all_post_contents()
    return render_template('posts.html', posts=posts)

@app.route('/panel')
def panel():
    return render_template('panel.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
