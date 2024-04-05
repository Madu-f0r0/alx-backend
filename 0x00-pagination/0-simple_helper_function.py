#!/usr/bin/env python3
"""Contains the `index_range` function definition"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns the start and end index based on the page and size given"""
    return (((page_size * page) - page_size), page_size * page)
