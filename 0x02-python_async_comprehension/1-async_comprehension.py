#!/usr/bin/env python3
"""An async generator"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generate numbers between 0 and 10"""
    result = [num async for num in async_generator()]
    return result
