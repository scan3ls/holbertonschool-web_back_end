#!/usr/bin/env python3
""" module docstring super """
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Asynchronous comprehension """
    return [i async for i in async_generator()]
