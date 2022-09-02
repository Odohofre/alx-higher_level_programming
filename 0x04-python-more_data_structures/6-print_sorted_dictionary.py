#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary ordered by keys.

    Args:
        a_dictionary (Any): a dictionary
    """
    for k, v in sorted(a_dictionary.items()):
        print("{:s}: {}".format(k, v))
