#!/usr/bin/python3
'Implementing a Minimal application for Flask'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'
