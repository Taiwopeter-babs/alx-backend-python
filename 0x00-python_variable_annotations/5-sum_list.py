#!/usr/bin/env python3
"""Annotate a function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of a list of floats"""
    intial: float = 0.0
    for num in input_list:
        intial += num
    return intial
