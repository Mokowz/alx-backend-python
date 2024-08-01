#!/usr/bin/env python3
"""element_length function def"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length function"""
    return [(i, len(i)) for i in lst]
