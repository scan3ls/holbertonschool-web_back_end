#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request, redirect, url_for
from flask_cors import (CORS, cross_origin)
import os
from auth import Auth

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def basic() -> str:
    """ Basic home
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=["POST"], strict_slashes=False)
def users() -> str:
    """ register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ user login using
    """
    email = request.form.get('email')
    password = request.form.get('password')

    valid = AUTH.valid_login(email, password)

    if not valid:
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes)
def logout() -> str:
    """ user logout """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('basic'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
