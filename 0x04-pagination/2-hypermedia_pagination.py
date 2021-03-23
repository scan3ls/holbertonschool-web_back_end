#!/usr/bin/env python3
""" Pagination Simple helper function """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return tuple with the range of indecies """
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get results of query """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        query = index_range(page, page_size)
        start, end = query[0], query[1]

        data = self.dataset()

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get results of query as dict """
        pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": pages
        }


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
