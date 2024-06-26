#!/usr/bin/env python3
""" 1. Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        function with the babel.localeselector decorator.
        Use request.accept_languages to determine the best
        match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ render template """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
