#!/usr/bin/env python3
"""Define wait_random function."""


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay up to max_delay seconds then returns it."""
    import random
    import asyncio
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
