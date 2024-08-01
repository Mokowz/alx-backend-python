#!/usr/bin/env python
"""safely_get_value function def"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """Return value of key in dictionary, otherwise default"""
    if key in dct:
        return dct[key]
    else:
        return default
