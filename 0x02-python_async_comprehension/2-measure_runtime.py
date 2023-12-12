#!/usr/bin/env python3
"""Define measure_runtime coroutine."""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel."""
    import asyncio
    import time
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
