#!/usr/bin/env python3
"""Loop 10 times as an async comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """"Loop 10 times and append to a list"""
    return [i async for i in async_generator()]
