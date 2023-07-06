#!/usr/bin/env python3
"""Annotate a function that returns a callable function"""
from typing import Callable

# define a return function
return_func: Callable[[float], float]


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def return_func(arg: float) -> float:
        return arg * multiplier
    return return_func
