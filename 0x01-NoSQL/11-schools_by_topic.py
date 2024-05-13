#!/usr/bin/env python3
""" A python module that defines a function called school_by_topic"""

def schools_by_topic(mongo_collection, topic):
    """
    A function that returns the list of school having a specific topic
    """

    return mongo_collection.find({"topics": topic})
