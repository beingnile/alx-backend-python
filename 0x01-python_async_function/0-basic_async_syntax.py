#!/usr/bin/env python3

"""Defines an asynchronous coroutine wait_random
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
    seconds

    Args:
        max_delay: Maximum delay value
    Returns:
        A random delay between 0 and max_delay(included)
    """
    ret = random.uniform(0, float(max_delay))
    await asyncio.sleep(ret)
    return ret
