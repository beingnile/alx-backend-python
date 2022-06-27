#!/usr/bin/env python3

"""Defines an asynchronous coroutine wait_n
"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay value
    Returns:
        Sorted list of all delays
    """
    ret = []
    for i in range(n):
        task = task_wait_random(max_delay)
        value = await task
        ret.append(value)

    return sorted(ret)
