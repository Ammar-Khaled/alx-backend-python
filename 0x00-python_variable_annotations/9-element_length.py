#!/usr/bin/env python3
"""Define the type-annotated function 'element_length'."""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples from the input iterable."""
    return [(i, len(i)) for i in lst]
