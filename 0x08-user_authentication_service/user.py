#!/usr/bin/env python3
""" User module using sqlAlchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()

class User(Base):
    """ User object
    """

    __tablename__ = 'users'

    id = Column(Integer, Sequence('id'), primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args, **kwargs):
        """ constructor """
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        """ string representation """
        user_id = getattr(self, 'id')
        user_email = getattr(self, 'email')

        return f"<User {user_id} {user_email}>"
