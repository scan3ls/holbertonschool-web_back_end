#!/usr/bin/env python3
""" password encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ password encryption using bcrypt """
    return bcrypt.hashpw(
        bytes(password, 'utf-8'),
        bcrypt.gensalt()
    )


def is_valid(hashed_passwrod: bytes, password: str) -> bool:
    """ check hashed password """
    passwd = bytes(password, 'utf-8')
    match =  bcrypt.checkpw(passwd, hashed_passwrod)
    return True if match else False
