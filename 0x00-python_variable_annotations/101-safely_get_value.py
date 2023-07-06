#!/usr/bin/env python3
"""Annotate a function with correct types"""
from typing import Any, Mapping, Union, TypeVar

# declare a `Type Vaiable` T
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Get a safe Value"""
    if key in dct:
        return dct[key]
    else:
        return default
