#!/usr/bin/env python3

"""Defines an asynchronous coroutine wait_n
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """Creates a task

    Args:
        max_delay: Maximum delay value
    Returns:
        Asyncio.Task object
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
