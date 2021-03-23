#!/usr/bin/env python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Last in First out Caching """

    def __init__(self):
        super().__init__()
        self.LIFOList = []

    def put(self, key, item):
        """
        --------------
        Description:
            Store Key/ Value pair in cache
        Args:
            Key: key of item to store
            item: Value of key to store
        --------------
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.LIFOList.remove(key)
            self.LIFOList.append(key)
            return

        if len(self.LIFOList) > self.MAX_ITEMS - 1:
            F_Key = self.LIFOList.pop()
            del self.cache_data[F_Key]
            print("DISCARD:", F_Key)

        self.cache_data[key] = item
        self.LIFOList.append(key)

    def get(self, key):
        """
        --------------
        Description:
            Retrieve value of key from cache
        Args:
            Key of value to get
        --------------
        """
        if key is None:
            return

        value = None
        if key in self.cache_data:
            value = self.cache_data[key]
        if value is not None:
            return value


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
