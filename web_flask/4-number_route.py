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


@app.route('/python/')
@app.route('/python/<text>')
def replace_var_default(text="is cool"):
    """Replaces an input variable"""
    new_text = text.replace('_', ' ')
    app.url_map.strict_slashes = False
    return ('Python {}'.format(new_text))


@app.route('/number/<int:n>')
def replace_var_int(n):
    """Replaces an input variable"""
    app.url_map.strict_slashes = False
    return ('{} is a number'.format(n))


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
