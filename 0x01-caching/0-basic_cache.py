#!/usr/bin/env python3
""" BaseCaching module """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """A basic cache system"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key == None or item == None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key"""
        if key == None or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
