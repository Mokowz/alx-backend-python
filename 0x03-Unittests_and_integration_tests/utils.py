#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)

# class Mat:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     @memoize
#     def add(self):
#         print("Addddd")
#         return self.a + self.b
# # print(access_nested_map({"a": {"b": 2}}, "a"))
# # print(access_nested_map({"a": {"b": {"c": 4}}}, ("a", "b", "c")))
# # print(access_nested_map({"a": {"b": {"c": 4}}}, ("a",)))
# # print(access_nested_map({"a": {"b": {"c": 4}}}, ("d",)))
# # print(get_json("https://docs.python.org/3/library/unittest.html"))
# matho = Mat(32, 8)
# # matho.add()
# print(matho.add, '\n')
# print(matho.add)