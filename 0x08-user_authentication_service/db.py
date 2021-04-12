#!/usr/bin/env python3
""" sqlAlchemy DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User
from typing import TypeVar


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

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """ add user to db """
        new_user = User(email=email, hashed_password=hashed_password)

        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs: dict) -> TypeVar('User'):
        """ search for user given key word """

        session = self._session
        query = session.query(User).filter_by(**kwargs)

        return query.one()

    def update_user(self, user_id: int, **kwargs: dict):
        """ update kwargs of user """
        user = self.find_user_by(id=user_id)

        for key in kwargs:
            setattr(user, key, kwargs[key])

        self._session.commit()
