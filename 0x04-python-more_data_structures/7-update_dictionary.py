#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary

    Args:
        a_dictionary: a dictionary
        key (string): dictonary keys
        value (Any): values

    Returns:
        updated dictionary
    """
    a_dictionary[key] = value
    return (a_dictionary)
