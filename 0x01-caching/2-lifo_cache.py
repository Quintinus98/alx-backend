#!/usr/bin/env python3
""" LIFO caching """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key == None or item == None:
            return
        if self.cache_data.get(key):
            del self.cache_data[key]
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = next(reversed(self.cache_data.keys()))
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key == None or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
