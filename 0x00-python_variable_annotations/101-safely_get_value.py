#!/usr/bin/env python3


"""Safely get values from a dictionary
"""


from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'), None]
                     ) -> Union[Any, TypeVar('T')]:
    """Safely get values from a dictionary

    Args:
        dct: Mapping
        key: Any
        default: Union
    Returns:
        default
    """

    if key in dct:
        return dct[key]
    else:
        return default
