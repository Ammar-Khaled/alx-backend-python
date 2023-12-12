#!/usr/bin/env python3
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Execute async_comprehension four times in parallel using asyncio.gather()."""
    import asyncio
    import time
    before = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - before
