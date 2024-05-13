#!/usr/bin/env python3
""" A python module that defines a function called insert_school"""

def insert_school(mongo_collection, **kwargs):
    """
    A python function that inserts a new document in a collection
    Args:
        mongo_collection: a pymongo collection object
        **kwargs: the document to be inserted
    Returns:
        the new _id
    """

    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
