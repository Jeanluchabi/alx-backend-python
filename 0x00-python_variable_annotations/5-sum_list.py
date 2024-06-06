#!/usr/bin/env python3
"""This is a module for defining a function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This Returns the sum of floats in the input list."""
    total_sum: float = sum(input_list)
    return total_sum
