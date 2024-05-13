#!/usr/bin/env python3
""" A python module that defines a function called top_students"""

def top_students(mongo_collection):
    """
    A function that returns all students sorted by average score
    """

    data = mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
    return list(data)
