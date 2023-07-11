#!/usr/bin/env python3
"""Measure total runtime of tasks"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of four tasks that run parallel
    to each other and return the total runtime, which is the
    maximum runtime of the tasks gathered and scheduled
    """
    coro_tasks = [async_comprehension() for _ in range(0, 4)]

    start_time = time.perf_counter()
    await asyncio.gather(*coro_tasks)
    finish_time = time.perf_counter() - start_time
    return finish_time
