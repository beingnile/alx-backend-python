#!/usr/bin/env python3


"""Defines a type-annotated function sum_mixed_list that returns the sum
of values in a list of mixed types
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sums up elements in a list

    Args:
        mxd_list: A list of float values

    Returns:
        The sum of float values in input_list
    """
    res = 0

    for val in mxd_list:
        res += val

    return(res)
