#!/usr/bin/python3
""" 5. LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        super().__init__()
        self.keys = []
        self.frequency = {}

    def put(self, key, item):
        """ Add item to cache using LFU Caching """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
                if len(self.keys) >= self.MAX_ITEMS:
                    least_frequency = min(self.frequency.values())
                    least_frequency_key = [
                        k for k, v in self.frequency.items()
                        if v == least_frequency]
                    if len(least_frequency_key) > 1:
                        discard = self.keys[self.keys.index(
                            min(least_frequency_key))]
                    else:
                        discard = least_frequency_key[0]
                    self.cache_data.pop(discard)
                    self.keys.remove(discard)
                    self.frequency.pop(discard)
                    print(f'DISCARD: {discard}')
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.keys.append(key)

    def get(self, key):
        """ Get item by key """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.frequency[key] += 1
            self.keys.append(key)
        return self.cache_data.get(key)
