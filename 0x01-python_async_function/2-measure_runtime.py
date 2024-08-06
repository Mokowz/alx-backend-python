#!/usr/bin/env python3
"""MEasure execution time"""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n"""
    total_time = time.time(wait_n(n, max_delay))
    return total_time / n
