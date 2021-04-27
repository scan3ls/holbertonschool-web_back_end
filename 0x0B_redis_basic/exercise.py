#!/usr/bin/env python3
""" redis exercises """
import redis
from typing import Union, Callable


class Cache():
    """ caching class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis db """
        from uuid import uuid4

        key = str(uuid4())
        self._redis.append(key, data)
        self._redis.save()

        return key

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        """ return data in original form """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """ get w/ str function """
        try:
            return self.get(key, str)
        except ValueError as e:
            print(e)

    def get_int(self, key: str) -> int:
        """ get w/ int function """
        try:
            return self.get(key, int)
        except ValueError as e:
            print(e)
