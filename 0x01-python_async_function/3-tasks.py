#!/usr/bin/env python3
"""creates a coroutine task"""
import asyncio
from typing import TypeVar


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates and returns a coroutine task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
