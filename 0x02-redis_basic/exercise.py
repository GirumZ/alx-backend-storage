#!/usr/bin/env python3
""" A python module for class defination of Cache"""
import sys
import uuid
import redis
from typing import Union, Optional, Callable


class Cache:
    """ Definition for the Cache class"""

    def __init__(self):
        """ constructor method for the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
