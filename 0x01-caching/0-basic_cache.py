#!/usr/bin/python3
""" 0. Basic dictionary """
import base_caching


class BasicCache(base_caching.BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        """ Add an item in cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key """
        return self.cache_data.get(key, None)
