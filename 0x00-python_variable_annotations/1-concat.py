#!usr/bin/env python3


"""Defines a type-annotated function concat
"""


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings passed as arguments

    Args:
        str1: First string
        str2: Second string

    Returns:
        A concatenated string from the passed arguments
    """
    return(str1 + str2)
