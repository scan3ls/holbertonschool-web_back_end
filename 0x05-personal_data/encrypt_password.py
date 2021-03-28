#!/usr/bin/env python3
""" password encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ password encryption using bcrypt """
    return bcrypt.hashpw(
        bytes(password, 'utf-8'),
        bcrypt.gensalt()
    )
