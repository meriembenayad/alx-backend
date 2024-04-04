#!/usr/bin/python3
""" 3. LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add item in cache using LRU caching """
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
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
