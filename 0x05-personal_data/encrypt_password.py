#!/usr/bin/env python3
""" password encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ password encryption using bcrypt """
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check hashed password """
    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )
