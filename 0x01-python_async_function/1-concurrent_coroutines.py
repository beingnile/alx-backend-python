#!/usr/bin/env python3

"""Defines an asynchronous coroutine wait_n
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawns wait_random n times

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay value
    Returns:
        Sorted list of all delays
    """
    ret = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        value = await task
        ret.append(value)

    return sorted(ret)
