#!/usr/bin/python3
""" 0. Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end index for pagination.
    Args:
        - page (int): the current page number (1-indexed)
        - page_size (int): the number of item per page
    Return:
        - tuple: A tuple containing the start & end index for the page and size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
