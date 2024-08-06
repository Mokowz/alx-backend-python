#!/usr/bin/env python3
"""Measure runtime for 4 parallel comprehensions"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime for 4 parallel comprehensions"""
    start = perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = perf_counter()
    return (end - start)
