#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int):
    """Return tuple"""
    total_page_size = page_size * page
    return (total_page_size - page_size, total_page_size)
