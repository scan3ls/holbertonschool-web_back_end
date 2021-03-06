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

    def create_session(self, email: str) -> str:
        """ create a session id """
        session_id = _generate_uuid()

        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=session_id)
        except Exception:
            return None

        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """ get user from session_id """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """ destroy a user session """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            pass

        return None

    def get_reset_password_token(self, email: str) -> str:
        """ create and return passwd reset token """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            raise ValueError

        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """ update user password """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except Exception:
            raise ValueError

        hash_pass = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hash_pass,
            reset_token=None
        )
        return None
