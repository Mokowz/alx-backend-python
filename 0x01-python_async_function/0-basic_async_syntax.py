#!/usr/bin/env python3
"""Basic Async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
