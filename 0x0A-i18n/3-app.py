#!/usr/bin/env python3
""" basic flask app """
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config[LANGUAGES])


@app.route('/')
def index():
    """ simple route to index.html """
    return render_template('2-index.html')
