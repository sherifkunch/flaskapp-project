#!/usr/bin/python

from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

env = os.getenv('ENV', 'Development')

@app.route("/hello")
def hello():
    return f"Hello, World! \n This is {env} environment!"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/picture")
def pic():
    return render_template('index2.html')


@app.route("/user/<username>")
def show_user_profile(username):
    return f"Hello, {username}!"


@app.route("/friends")
def salvador():
    return "Hello, my friends!"
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

