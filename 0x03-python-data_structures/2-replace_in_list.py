#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific location

    Args:
        my_list (int): list
        idx (int): index of element to be replaced
        element (int): new element

    Returns:
        NONE: if idx is less than zero or out of range
        The return value: new list with new element
    """
    if idx <= 0 or idx >= len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
