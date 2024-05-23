#!/usr/bin/env python3
""" LIFO caching """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key == None or item == None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.order.pop(-2)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
