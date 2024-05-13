#!/usr/bin/env python3
""" A python module that defines a function called update_topics"""

def update_topics(mongo_collection, name, topics):
    """ A function that updates the topics
    Args:
        mongo_collection: a pymoongo collection
        name: the school name to update
        topic: the topic
    """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
