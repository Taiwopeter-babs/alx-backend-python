#!/usr/bin/env python3
"""An async generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate numbers between 0 and 10"""

    for _ in range(0, 10):
        random_num: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_num
