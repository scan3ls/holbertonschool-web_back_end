#!/usr/bin/env python3
""" basic flask app """
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import Dict

# ===============================
# Imported mock user data

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# ===============================

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ language config for babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get best language """
    locale = request.args.get('locale')
    if locale is not None:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ simple route to index.html """
    try:
        user = g.user
        name = user['name']
    except Exception:
        user, name = None, None
    return render_template('5-index.html', user=user, username=name)


def get_user() -> Dict:
    """ return user from mock users data """
    user_id = request.args.get('login_as')
    user_id = int(user_id) if user_id is not None else None
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """ before request runtime """
    user = get_user()
    if user:
        g.user = user
