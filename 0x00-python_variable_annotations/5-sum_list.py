#!/usr/bin/env python3


"""Defines a type-annotated function sum_list that returns the sum
of values in a list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up elements in a list

    Args:
        input_list: A list of float values

    Returns:
        The sum of float values in input_list
    """
    res = 0

    for val in input_list:
        res += val

    return res
