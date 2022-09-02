#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary

    Args:
        a_dictionary (Any): dictionary
    """
    count = 0
    for key in a_dictionary:
        count += 1
    return (count)
