#!/usr/bin/env python3
""" Password Authentication """
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ return a hashed password """
    import bcrypt
    hash_pass = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hash_pass.decode()

def _generate_uuid() -> str:
    """ generate a uuid """
    from uuid import uuid4
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self,
                      email: str = None,
                      password: str = None) -> User:
        """ register a new user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound as e:
            user = None

        if user:
            raise ValueError(f"User {user.email} already exists")

        hashed_password = _hash_password(password)

        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ check credentails """
        import bcrypt

        try:
            user = self._db.find_user_by(email=email)
        except Exception as e:
            return False

        return bcrypt.checkpw(
            password.encode(),
            user.hashed_password.encode()
        )
