#!/usr/bin/env python3
"""Contains the definition of the class MRUCache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements the MRU cache replacement technique"""

    def __init__(self):
        """The constructor method for an instance of the class MRUCache"""
        super().__init__()
        self.mru = ""

    def put(self, key, item):
        """Assigns a new item to the cache dictionary"""
        if key is not None and item is not None:
            mxItems = BaseCaching.MAX_ITEMS

            if len(self.cache_data) >= mxItems and key not in self.cache_data:
                self.cache_data.pop(self.mru)
                print("DISCARD: {}".format(self.mru))

            self.mru = key
            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves the value in the cache dictionary linked to a key"""
        if key is not None and key in self.cache_data.keys():
            self.mru = key

        return self.cache_data.get(key)
