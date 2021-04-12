#!/usr/bin/env python3
""" Password Authentication """
from typing import TypeVar
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ return a hashed password """
    import bcrypt
    hash_pass = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hash_pass.decode()


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self,
                      email: str = None,
                      password: str = None) -> TypeVar('User'):
        """ register a new user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound as e:
            user = None

        if user:
            raise ValueError(f"User {user.email} already exists")

        hashed_password = _hash_password(password)

        return self._db.add_user(email, hashed_password)
