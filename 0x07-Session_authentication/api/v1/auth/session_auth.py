#!/usr/bin/env python3
""" Session authentication """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session authentication """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session for a user """
        if user_id is None:
            return None
        if isinstance(user_id, str) is False:
            return None

        sessionID = str(uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return user_id based on session_id """
        if session_id is None:
            return None
        if isinstance(session_id, str) is False:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        return self.user_id_by_session_id[session_id]

    def current_user(self, request=None) -> str:
        """ Returns a user based on a cookie """
        from models.user import User

        if request is None:
            return None

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """ delets the user session / logout """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
