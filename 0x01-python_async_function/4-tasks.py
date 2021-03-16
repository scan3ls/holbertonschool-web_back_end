#!/usr/bin/env python3
""" More async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait random n times """
    mah_list = []
    mah_nums = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        mah_list.append(task)

    for task in asyncio.as_completed(mah_list):
        num = await task
        mah_nums.append(num)

    return mah_nums
