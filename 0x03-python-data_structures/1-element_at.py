#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve an element from a list

    Args:
        my_list (int): list
        idx (int): index of element

    Returns:
        None: if less than 0 and out of range,
        The return value: retrieved element
    """
    if idx < 0:
        return "None"
    elif idx > len(my_list):
        return "None"
    else:
        return my_list[idx]
