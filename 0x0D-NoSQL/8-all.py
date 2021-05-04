#!/usr/bin/env python3
""" 8-all docstring """


def list_all(mongo_collection):
    """ list all collections in mongodb """
    return [item for item in mongo_collection.find()]
