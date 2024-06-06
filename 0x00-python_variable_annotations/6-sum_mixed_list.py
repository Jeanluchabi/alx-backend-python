#!/usr/bin/env python3
"""This is a module defining a function to sum a list of integers or
floats and return the result as a float."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This will return the sum of integers and floats in the input list as a float."""
    total_sum: float = sum(mxd_lst)
    return total_sum
