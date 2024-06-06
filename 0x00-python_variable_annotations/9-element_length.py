#!/usr/bin/env python3
from typing import List, Tuple
"""This is a module annotated appropriately"""


def element_length(lst: List[List]) -> Tuple[List]:
    return [(i, len(i)) for i in lst]
