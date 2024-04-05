#!/usr/bin/env python3
"""Contains the definition of the class LFUCache"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements the LFU cache replacement technique"""

    def __init__(self):
        """The constructor method for an instance of the class LFUCache"""
        super().__init__()
        self.cache_history = {}

    def put(self, key, item):
        """Assigns a new item to the cache dictionary"""
        if key is not None and item is not None:
            mxItems = BaseCaching.MAX_ITEMS

            if len(self.cache_data) >= mxItems and key not in self.cache_data:
                lfu = sorted(self.cache_history.values())[0]

                for k, v in self.cache_history.items():
                    if v == lfu:
                        discard_key = k
                        break
                self.cache_data.pop(discard_key)
                self.cache_history.pop(discard_key)
                print("DISCARD: {}".format(discard_key))

            if key in self.cache_history.keys():
                self.cache_history[key] += 1
            else:
                self.cache_history.update({key: 0})

            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves the value in the cache dictionary linked to a key"""
        if key is not None and key in self.cache_data.keys():
            if key in self.cache_history.keys():
                self.cache_history[key] += 1
            else:
                self.cache_history.update({key: 0})

        return self.cache_data.get(key)
