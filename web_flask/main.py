#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask , render_template
marketmate = Flask(__name__)


@marketmate.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    """ Main Function """
    marketmate.run(debug=True, port=5001)