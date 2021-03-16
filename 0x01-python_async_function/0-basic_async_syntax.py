#!/usr/bin/env python3
""" asyncio module using random """
import asyncio
import random


async def wait_random(max_delay=10):
    """ async function to wait and return"""
    wait_time = random.uniform(0, max_delay+1)
    await asyncio.sleep(wait_time)
    return wait_time
