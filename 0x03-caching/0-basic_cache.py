#!/usr/bin/env python3
""" Basic Dictionary  """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Caching system """
    def __init__(self):
        """
        --------------
        Description:
            Constructor
        --------------
        """
        BaseCaching.__init__(self)

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
            return

        self.cache_data[key] = item

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
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
