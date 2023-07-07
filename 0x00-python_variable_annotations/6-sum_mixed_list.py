#!/usr/bin/env python3
"""Annotate a function"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns the sum of a list with floats and integers"""
    intial: float = 0.0
    for num in mxd_list:
        intial += num
    return intial
