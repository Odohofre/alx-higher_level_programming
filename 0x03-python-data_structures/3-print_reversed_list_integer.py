#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints integers of a list in reversed order

    Args:
        my_list (list, optional): list. Defaults to [].
    Returns:
        list in reversed order
    """
    if my_list is None:
        return
    else:
        print(f"{my_list[::-1]}")
