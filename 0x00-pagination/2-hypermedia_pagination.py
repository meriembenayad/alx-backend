#!/usr/bin/env python3
""" 2. Hypermedia pagination """
import csv
import math
from typing import List, Tuple


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
        return dataset[start_index: end_index]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end index for pagination.
        Args:
            - page (int): the current page number (1-indexed)
            - page_size (int): the number of item per page
        Return:
            - tuple: A tuple contains the start & end idx for the page and size
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of dataset
        Args:
            - page (int): current page index 1
            - page_size (int): number of items per page
        Return:
            - List[List]: A list lists representing the rows of the dataset
            for the specific page
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset = self.dataset()
        if page_size == 0:
            return []

        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index, end_index = self.index_range(page, page_size)
        return dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve a specific page of dataset with hypermedia
        Args:
            - page (int): current page index 1
            - page_size (int): number of items per page
        Return:
            - A dictionary the following key-value pairs:
            {
                'page_size': 'page_size',
                'page': 'current_page',
                'data': 'hypermedia_info',
                'next_page': 'next_page',
                'prev_page': 'prev_page',
                'total_page': 'total_page'
            }
        """
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page < 1 else None,
            "total_page": total_pages
        }
