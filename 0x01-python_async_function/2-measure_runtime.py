#!/usr/bin/env python3

"""Defines a function measure_time
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the execution time of wait_n

    Args:
        n: Number of times to spawn wait_random in wait_n
        max_delay: Maximum delay value
    Returns:
        total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total_time = stop - start

    return (total_time / n)
