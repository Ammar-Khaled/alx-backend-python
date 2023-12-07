#!/usr/bin/env python3
"""Define the type-annotated function 'sum_mixed_list'."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a key-value pair as a tuple."""
    return (k, v ** 2)
