#!/usr/bin/env python3
"""Define wait_n function."""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    tasks = []
    delays = []

    # run the coroutines concurrently
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    # get the return values in order of finishing
    for finished_task in asyncio.as_completed(tasks):
        delays.append(await finished_task)

    return delays
