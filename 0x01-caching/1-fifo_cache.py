#!/usr/bin/python3
""" 1. FIFO caching """
import base_caching


class FIFOCache(base_caching.BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item to cache using FIFO """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discard = self.keys.pop(0)
                self.cache_data.pop(discard)
                print(f'DISCARD: {discard}')
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get item by key """
        return self.cache_data.get(key, None)
