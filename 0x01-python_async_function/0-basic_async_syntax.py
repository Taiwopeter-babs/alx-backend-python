#!/usr/bin/env python3
""" Write a simple coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a random delay time"""
    return_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(return_time)
    return return_time
