#!/usr/bin/env python3
""" A python function that lists all documents in a collection"""

def list_all(mongo_collection):
    """
    A python function that lists all documents in a collection
    Args:
        mango_collection: a pymongo collection object
    Returns:
        all the documents in the collection
    """

    documents = mongo_collection.find()
    return documents
