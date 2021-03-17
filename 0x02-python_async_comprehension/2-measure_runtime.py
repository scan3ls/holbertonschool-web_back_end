#!/usr/bin/env python3
""" module docstring super """
from time import time
import asyncio
foo = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure delta t """
    t1 = time()
    await asyncio.gather(foo(), foo(), foo(), foo())
    t2 = time()
    return t2 - t1
