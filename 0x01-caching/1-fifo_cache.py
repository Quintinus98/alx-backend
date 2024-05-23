#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key == None or item == None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.cache_data))
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """Get an item by key"""
        if key == None or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
