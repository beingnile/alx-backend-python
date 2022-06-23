#!/usr/bin/env python3


"""Defines a function that returns a list of element lengths
"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Gets element lists

    Args:
        lst: A duck type iterable

    Returns:
        A tuple of element and element lengths
    """

    return [(i, len(i)) for i in lst]
