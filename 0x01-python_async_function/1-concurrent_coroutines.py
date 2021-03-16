#!/usr/bin/env python3
""" More async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait random n times """
    mah_list = []
    mah_nums = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        mah_list.append(task)

    for task in mah_list:
        num = await task
        done, pending = await asyncio.wait({task})

        mah_nums.append(num)

        if task in done:
            mah_nums.sort()

    return mah_nums
