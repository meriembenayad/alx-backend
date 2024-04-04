#!/usr/bin/python3
""" 2. LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add item to cache using LIFO """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discard = self.keys.pop()
                self.cache_data.pop(discard)
                print(f'DISCARD: {discard}')
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get item by key """
        return self.cache_data.get(key)
