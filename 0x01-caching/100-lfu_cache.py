#!/usr/bin/env python3
""" LFU caching """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    An LFU caching system
    Least Frequency Used
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []
        self.frequency = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key == None or item == None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_item()
        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.order:
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key, None)

    def remove_item(self):
        """Remove the least frequently used item"""
        lfu_keys = [
            k
            for k, v in self.frequency.items()
            if v == min(self.frequency.values())
        ]
        if len(lfu_keys) == 1:
            key_to_evict = lfu_keys[0]
        else:
            lfu_usage_order = [
                key for key in self.order if key in lfu_keys
            ]
            key_to_evict = lfu_usage_order[0]

        del self.cache_data[key_to_evict]
        del self.frequency[key_to_evict]
        self.order.remove(key_to_evict)
        print(f"DISCARD: {key_to_evict}")
