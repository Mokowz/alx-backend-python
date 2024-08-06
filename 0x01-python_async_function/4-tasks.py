#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay n times"""
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
