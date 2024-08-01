#!/usr/bin/env python3
"""safe_first_element function def"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of list if exists, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
