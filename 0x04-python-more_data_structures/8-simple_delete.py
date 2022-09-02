#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.

    Args:
        a_dictionary (Any): a dictionary
        key (str, optional): key to be deleted. Defaults to "".

    Returns:
        a new dictionary: if key exists
        original dictionary: if key does not dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
