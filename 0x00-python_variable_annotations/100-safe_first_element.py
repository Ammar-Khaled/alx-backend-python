#!/usr/bin/env python3
"""Define the type-annotated function 'safe_first_element'."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the input iterable safely."""
    if lst:
        return lst[0]
    else:
        return None
