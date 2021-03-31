""" Basic authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Basic authentication
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ get auth payload and check if valid format """

        if authorization_header is None:
            return None

        if isinstance(authorization_header, str) is False:
            return None

        try:
            start, end = authorization_header.split(' ')
            if start != 'Basic':
                return None
        except ValueError:
            return None

        return end

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decode valid auth payload """
        from base64 import b64decode

        if base64_authorization_header is None:
            return None

        if isinstance(base64_authorization_header, str) is False:
            return None

        value = self.extract_base64_authorization_header(
            f"Basic {base64_authorization_header}"
        )
        if value is None:
            return None

        return b64decode(value).decode('utf-8')

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """ extract user credentials from coded payload """

        if decoded_base64_authorization_header is None:
            return None, None

        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        start, end = decoded_base64_authorization_header.split(':')
        return start, end

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """ create user from extracted credentials """

        isString = isinstance(user_email, str)
        if user_email is None or isString is False:
            return None

        isString = isinstance(user_pwd, str)
        if user_pwd is None or isString is False:
            return None

        user = User(email=user_email, _password=user_pwd)

        result = user.search({"email": user_email})
        user = None if result == [] else result[0]

        if user is None:
            return None

        if user.is_valid_password(user_pwd):
            return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ send user to api; let them handle it """
        header = self.authorization_header(request)
        b64pwd = self.extract_base64_authorization_header(header)
        user_cred = self.decode_base64_authorization_header(b64pwd)
        email, pwd = self.extract_user_credentials(user_cred)
        user = self.user_object_from_credentials(email, pwd)
        return user
