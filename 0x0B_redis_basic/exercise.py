#!/usr/bin/env python3
""" redis exercises """
import redis
from typing import Union, Callable, Any
from functool import wraps


def count_calls(method: Callable) -> Callable:
    """ store redis method calls in redis db """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key, amount=1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ caching class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis db """
        from uuid import uuid4

        key = str(uuid4())
        self._redis.append(key, data)
        self._redis.save()

        return key

    def get(self, key: str, fn: Callable) -> Any:
        """ return data in original form """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """ call get w/ fn=str """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ call get w/ fn=int """
        return self.get(key, int)
