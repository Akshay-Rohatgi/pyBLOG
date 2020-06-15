from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')