#!/usr/bin/env python3
"""Define the type-annotated function 'safely_get_value'."""
from typing import Any, Union, TypeVar, Mapping
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of a specific key safely."""
    if key in dct:
        return dct[key]
    else:
        return default
