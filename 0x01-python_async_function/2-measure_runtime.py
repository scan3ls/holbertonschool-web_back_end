#!/usr/bin/env python3
""" More async """
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure average time of each wait_n """
    t1 = time()
    mah_nums = asyncio.run(wait_n(n, max_delay))
    t2 = time()
    return (t2 - t1) / n
