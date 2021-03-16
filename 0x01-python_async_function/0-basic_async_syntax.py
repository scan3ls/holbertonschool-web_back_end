#!/usr/bin/env python3
""" asyncio module using random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async function to wait and return"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
