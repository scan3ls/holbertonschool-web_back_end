#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Last in First out Caching """

    def __init__(self):
        super().__init__()
        self.LRUList = []

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
            self.LRUList.remove(key)
            self.LRUList.append(key)
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.LRUList.append(key)

        if len(self.LRUList) > self.MAX_ITEMS:
            F_Key = self.LRUList.pop(0)
            del self.cache_data[F_Key]
            print("DISCARD: ", F_Key)

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
            self.LRUList.remove(key)
            self.LRUList.append(key)
            return value


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
