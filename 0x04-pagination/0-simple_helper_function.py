#!/usr/bin/env python3
""" Pagination Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return tuple with the range of indecies """
    end = page * page_size
    start = end - page_size
    return (start, end)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
