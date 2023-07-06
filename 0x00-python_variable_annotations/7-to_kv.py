#!/usr/bin/env python3
"""Annotate a function that returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with an integer and a float | integer"""
    return (k, v * v)
