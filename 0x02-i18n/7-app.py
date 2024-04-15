#!/usr/bin/env python3
""" 1. Basic Babel setup """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict
import pytz


class Config:
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
        function that returns a user dictionary or None
        if the ID cannot be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request() -> None:
    """
        should use get_user to find a user if any,
        and set it as a global on flask.g.user.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
        function with the babel.localeselector decorator.
        Use request.accept_languages to determine the best
        match with our supported languages.
    """
    locale = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user is not None and g.user['locale'] in app.config["LANGUAGES"]:
        user_locale = g.user.get('locale')
        return user_locale
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """doc doc doc"""
    try:
        if request.args.get("timezone"):
            return pytz.timezone(request.args.get("timezone")).zone
        if g.user and g.user.get("timezone"):
            return pytz.timezone(g.user["timezone"]).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


@app.route('/')
def index() -> str:
    """ render template """
    from datetime import datetime
    from flask_babel import format_datetime

    current_time = format_datetime(datetime.utcnow())
    return render_template('7-index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
