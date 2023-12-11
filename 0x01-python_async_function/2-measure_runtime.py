#!/usr/bin/env python3
"""Define measure_time function."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)."""
    before = time.time()
    asyncio.run(wait_n(n, max_delay))
    after = time.time()
    return (after - before) / n
