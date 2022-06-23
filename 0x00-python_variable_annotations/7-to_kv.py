#!/usr/bin/env python3


"""Defines a type-annotated function to_kv and returns a tuple of the values
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR float v
    as arguments and returns a tuple

    Args:
        k: A string
        v: Either an int or tuple

    Returns:
        A tuple containing a string and a square of v
    """

    return (k, float(v) ** 2)
