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


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
