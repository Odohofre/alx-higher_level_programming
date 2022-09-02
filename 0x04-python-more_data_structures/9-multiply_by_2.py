#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new_dictionary with all values multiplied by 2

    Args:
        a_dictionary (Any): original dictionary
    """
    new_dict = {k: v*2 for k, v in a_dictionary.items()}
    return (new_dict)
