#!/usr/bin/env python3


def _hash_password(password: str) -> str:
    """ return a hashed password """
    import bcrypt
    hash_pass = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hash_pass.decode()
