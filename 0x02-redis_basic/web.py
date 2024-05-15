#!/usr/bin/env/ python3
""" A python module for the get_page function"""

from functools import wraps
import requests
import redis


r = redis.Redis()


def url_access_count(method):
    """ A wrapper function for the counter function"""

    @wraps(method)
    def counter(url):
        """ A counter function"""

        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        key_count = "count:" + url
        html_content = method(url)

        r.incr(key_count)
        r.set(key, html_content, ex=10)
        r.expire(key, 10)
        return html_content
    return counter


@url_access_count
def get_page(url: str) -> str:
    """ requests a url"""

    data = requests.get(url)
    return data.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
