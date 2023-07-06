#!/usr/bin/env python3
"""Annotate a function with correct types"""
from typing import Any,  Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a list or None"""
    if lst:
        return lst[0]
    else:
        return None
