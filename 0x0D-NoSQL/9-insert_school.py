#!/usr/bin/env python3

def insert_school(mongo_collection, **kwargs):
    """ Inerts new document in collections """
    mongo_collection.insert_one(kwargs)
    new_document = mongo_collection.find(kwargs)
    return new_document[0]['_id']
