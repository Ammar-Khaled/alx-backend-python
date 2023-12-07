#!/usr/bin/env python3
"""Define the type-annotated function 'make_multiplier'."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by `multiplier`."""
    def fun(n):
        return n * multiplier
    return fun
