#!/usr/bin/env python3
""" redis exercises """
import redis
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ store redis method calls in redis db """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key, amount=1)
        # print(self._redis.get(key), key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ store history of inputs & outputs for a function """
    key = method.__qualname__
    input_key, output_key = f"{key}:inputs", f"{key}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> str:
    """ recall history of method calls zip """
    db = redis.Redis()
    key = method.__qualname__

    input_key, output_key = f"{key}:inputs", f"{key}:outputs"
    inputs = db.lrange(input_key, 0, -1)
    outputs = db.lrange(output_key, 0, -1)

    amount = int(db.get(key))
    print(f"{key} was called {amount} times:")
    for index, item in enumerate(inputs):
        s_input = inputs[index].decode('utf-8')
        s_output = outputs[index].decode('utf-8')
        s1 = f"{key}(*{s_input}) -> {s_output}"
        print(s1)


class Cache():
    """ caching class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis db """
        from uuid import uuid4

        key = str(uuid4())
        self._redis.append(key, data)
        self._redis.save()

        return key

    def get(self, key: str, fn: Callable = None) -> Any:
        """ return data in original form """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """ call get w/ fn=str """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ call get w/ fn=int """
        return self.get(key, int)
