#!/usr/bin/env python3
"""Run coroutines concurrently"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a list of result of a coroutine run n times. The
    list is a list of tasks that were completed in a timely order
    """
    task_list: List[asyncio.Task] = []
    done_tasks: list = []

    for _ in range(0, n):
        task_list.append(task_wait_random(max_delay))

    for res in asyncio.as_completed(task_list):
        earliest_res = await res
        done_tasks.append(earliest_res)
    return done_tasks
