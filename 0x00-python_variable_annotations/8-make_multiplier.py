#!/usr/bin/env python3
"""make_multiplier function def"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier function"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
