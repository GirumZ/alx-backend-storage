#!/usr/bin/env python3
""" A python module for class defination of Cache"""
import uuid
import redis
from typing import Union


class Cache:
    """ Definition for the Cache class"""

    def __init__(self):
        """ constructor method for the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A method to generate a key and store data with the key"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    main()
