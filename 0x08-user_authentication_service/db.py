#!/usr/bin/env python3
""" sqlAlchemy DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """ sqlAlchemy DB
    """
    def __init__(self):
        """ db constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ create a sqlAlchemy session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add user to db """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ search for user given key word """

        session = self._session
        query = session.query(User).filter_by(**kwargs)

        return query.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update kwargs of user """
        user = self.find_user_by(id=user_id)

        for key in kwargs:
            if key not in user.__dir__():
                raise ValueError
            setattr(user, key, kwargs[key])

        self._session.commit()
        return None
