#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all values multiplied by a number

    Args:
        my_list (list, optional): list. Defaults to [].
        number (int, optional): number. Defaults to 0.
    """
    new_list = list(map(lambda x: x * number, my_list))
    return (new_list)
