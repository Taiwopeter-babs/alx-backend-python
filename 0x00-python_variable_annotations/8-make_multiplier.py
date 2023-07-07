#!/usr/bin/env python3
"""Annotate a function that returns a callable function"""
from typing import Callable

# define a return function
return_func: Callable[[float], float]


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a callable function """
    def return_func(arg: float) -> float:
        """ returns the multiplication product """
        return arg * multiplier
    return return_func
