#!/usr/bin/env python3
"""Contains the definition of the class LRUCache"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements the LRU cache replacement technique"""

    def __init__(self):
        """The constructor method for an instance of the class LRUCache"""
        super().__init__()
        self.cache_history = []

    def put(self, key, item):
        """Assigns a new item to the cache dictionary"""
        if key is not None and item is not None:
            mxItems = BaseCaching.MAX_ITEMS

            if len(self.cache_data) >= mxItems and key not in self.cache_data:
                discard_key = self.cache_history[0]
                self.cache_data.pop(discard_key)
                self.cache_history.pop(0)
                print("DISCARD: {}".format(discard_key))

            if key in self.cache_history:
                self.cache_history.remove(key)

            self.cache_data.update({key: item})
            self.cache_history.append(key)

    def get(self, key):
        """Retrieves the value in the cache dictionary linked to a key"""
        if key is not None and key in self.cache_data.keys():
            self.cache_history.remove(key)
            self.cache_history.append(key)

        return self.cache_data.get(key)
