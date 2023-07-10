#!/usr/bin/env python3
"""Measure an approximate runtime for asynchronous tasks (coroutines)"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ 
    returns an approximate value of the runtime of
    coroutine tasks
    """
    start_time = time.perf_counter()
    asyncio.get_event_loop().run_until_complete(wait_n(n, max_delay))
    finish_time = time.perf_counter() - start_time

    # return average time for one task
    return finish_time / n
