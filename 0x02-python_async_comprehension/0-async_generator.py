#!/usr/bin/env python3
""" asaync generators """
from typing import Generator
import asyncio
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """generator function """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
