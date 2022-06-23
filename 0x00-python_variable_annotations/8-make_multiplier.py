#!/usr/bin/env python3


"""Defines a function make_multiplier that returns
a function that multiplies a float by a multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by a multiplier

    Args:
        multiplier: A float by which the Callable argument is multiplied to

    Return:
        A callable function that multiplies a float by the multiplier
    """
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
