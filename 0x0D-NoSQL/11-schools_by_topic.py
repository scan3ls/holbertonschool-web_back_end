#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic):
    """
    ===========================================
    returns the list of schools having a specific topic
    ===========================================
    Args:
        mongo_collection - pymongo collection object
        topic - (string) will be topic searched
    ===========================================
    """
    return mongo_collection.find( {"topics": {"$in": [topic]}} )
