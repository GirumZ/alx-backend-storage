#!/usr/bin/env python3
""" A python module for class defination of Cache"""

from functools import wraps
import uuid
import redis
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """ A method to wrap the counter function"""

    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """ A method counter function"""

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter


def call_history(method: Callable) -> callable:
    """ wrapper function to the history method"""

    key = method.__qualname__

    @wraps(method)
    def history(self, *args, **kwargs):
        """ A method to save the input and outputs of a function"""

        inp = str(args)
        self._redis.rpush(key + ":inputs", inp)
        outp = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", outp)
        return outp

    return history


class Cache:
    """ Definition for the Cache class"""

    def __init__(self):
        """ constructor method for the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A method to generate a key and store data with the key"""

        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """ A method to convert the data back to desired format """

        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """ A method to change bytes to int"""
        return int(self)

    def get_str(self: bytes) -> str:
        """ A method to change bytes to str"""

        return self.decode("utf-8")
