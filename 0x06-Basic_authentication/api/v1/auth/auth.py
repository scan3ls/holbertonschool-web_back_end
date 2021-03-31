#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication aclass
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Define which routes don't need authentications
        """

        if path is None or excluded_paths is None:
            return True

        s1 = [char for char in path]
        if s1[-1] != '/':
            s1.append('/')
            path = "".join(s1)

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Checks for an Auth payload
        """
        if request is None:
            return None

        for header in request.headers:
            key, value = header
            if key == 'Authorization':
                return value

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Default to overload in child classes """
        return None
