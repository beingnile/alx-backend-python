#!/usr/bin/env python3

"""Measures the total runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times
    in parallel using asyncio.gather and measures the total runtime

    Returns:
        The total runtime
    """
    tasks = [async_comprehension() for i in range(4)]
    start = time.time()
    await asyncio.gather(*tasks)
    stop = time.time()
    total_runtime = stop - start

    return total_runtime
