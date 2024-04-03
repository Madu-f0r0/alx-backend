#!/usr/bin/env python3
"""BasicCache class is implemented here"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The basic implementation of the caching system"""

    def put(self, key, item):
        """Assigns a new item to the cache dictionary"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves the value in the cache dictionary linked to a key"""
        return self.cache_data.get(key)
