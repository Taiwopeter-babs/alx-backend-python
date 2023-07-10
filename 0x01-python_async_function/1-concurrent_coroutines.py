#!/usr/bin/env python3
"""Run coroutines concurrently"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a list of result of a coroutine run n times. The
    list is a list of tasks that were completed in a timely order
    """
    task_list: list = []
    done_tasks: list = []

    for _ in range(0, n):
        task_list.append(asyncio.create_task(wait_random(max_delay)))

    for res in asyncio.as_completed(task_list):
        earliest_res = await res
        done_tasks.append(earliest_res)
    return done_tasks
