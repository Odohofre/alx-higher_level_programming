#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position\
        without modifying the original list

    Args:
        my_list (integers): original list
        idx (integers): index of element
        element (integers): new element

    Returns:
        my_list_copy: copy of list with replaced element
        my_list: if index is out of range or less than 0
    """
    my_list_copy = list(my_list)

    if idx < 0 and idx > len(my_list):
        return (my_list)
    else:
        my_list_copy[idx] = element
        return (my_list_copy)
