#!/usr/bin/python3
"""Script starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Route definition"""
    app.url_map.strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """Displays HBNB"""
    app.url_map.strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def replace_var(text):
    """Replaces an input variable"""
    new_text = text.replace('_', ' ')
    app.url_map.strict_slashes = False
    return ('C %s' % new_text)


@app.route('/c/<text>')
def replace_var_default(text='is cool'):
    """Replaces an input variable"""
    new_text = text.replace('_', ' ')
    app.url_map.strict_slashes = False
    return ('C %s' % new_text)


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
