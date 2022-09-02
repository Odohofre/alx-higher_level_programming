#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): initial list
        search (int): the element to replace in the list
        replace (int): new element
    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return (new_list)
