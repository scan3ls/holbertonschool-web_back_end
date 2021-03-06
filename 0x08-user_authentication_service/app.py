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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ user logout """
    session_id = request.cookies.get('session_id')
    if session_id is None:
        return abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('basic'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ get user profile route """
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ get reset passwd token """
    email = request.form.get('email')

    session = AUTH.create_session(email)
    if session is None:
        abort(403)

    token = AUTH.get_reset_password_token(email)
    return jsonify({"email": email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ update user password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_pass = request.form.get('new_password')

    try:
        session = AUTH.create_session(email)
        user = AUTH.get_user_from_session_id(session)
        AUTH.update_password(reset_token, new_pass)
    except Exception:
        abort(403)

    return jsonify({"email": user.email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
