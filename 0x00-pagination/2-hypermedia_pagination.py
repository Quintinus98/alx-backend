#!/usr/bin/env python3
"""
Simple helper function
"""

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int):
    """Return tuple"""
    total_page_size = page_size * page
    return (total_page_size - page_size, total_page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page"""
        assert (
            isinstance(page, int) and page > 0
        ), "Page must be a postive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page_size must be a postive integer"
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Returns a dictionary containing key-value pairs"""
        data = self.get_page(page, page_size)
        total_pages = len(self.__dataset) // page_size
        next_page = prev_page = None
        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
