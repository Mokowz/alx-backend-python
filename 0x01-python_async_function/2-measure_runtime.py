#!/usr/bin/env python3
"""MEasure execution time"""
from time import perf_counter
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    ttime = perf_counter() - start
    return ttime / n
