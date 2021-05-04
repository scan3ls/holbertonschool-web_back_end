#!/usr/bin/env python3

def update_topics(mongo_collection, name, topics):
    """ 
    ===========================================
        changes all topics of a school document
    ===========================================
    Args:
        mongo_collection - pymongo collection object
        name - (string) school name to update
        topics - (list of strings) list of topics approached in the school
    ===========================================
    """
    query = {"name": name}
    update_values = {"$set": {"topics": str(topics)}}
    mongo_collection.update_many(query, update_values)
