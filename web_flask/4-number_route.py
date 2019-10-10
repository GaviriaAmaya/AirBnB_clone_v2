#!/usr/bin/python3
'Implementing a Minimal application for Flask'
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C ' + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is_cool'):
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if (n.isdigit() is True):
        return n + " is a number"
    else:
        n = 404
        return n

if __name__ == '__main__':
    app.run(host='0.0.0.0')
