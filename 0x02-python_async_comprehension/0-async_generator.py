#!/usr/bin/env python3

"""Defines a coroutine async_generator
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, each time asynchronously waiting 1 second
    Then yeilds a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
