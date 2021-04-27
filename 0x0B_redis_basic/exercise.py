#!/usr/bin/env python3
""" redis exercises """
from redis import Redis
from typing import Union, Callable


class Cache():
    """ caching class """

    def __init__(self):
        """ constructor """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis db """
        from uuid import uuid4

        key = str(uuid4())
        self._redis.append(key, data)
        self._redis.save()

        return key
