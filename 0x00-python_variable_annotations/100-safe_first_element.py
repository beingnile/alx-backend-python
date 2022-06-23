#!/usr/bin/env python3


"""Augmented Code with correct duck-typed annotations
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of an iterable

    Args:
        lst: A sequence
    Returns:
        The first element of the sequence
    """

    if lst:
        return lst[0]
    else:
        return None
