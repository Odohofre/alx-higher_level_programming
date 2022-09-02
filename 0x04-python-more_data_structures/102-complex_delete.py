#!/usr/bin/python3
def complex_delete(my_dict, value):
    """Deletes keys with a specific value in a dictionary

    Args:
        my_dict (Any): dictionary containing key and values
        value (Any): value to be deleted

    Returns:
        my_dict: original dictionary if value does not exist\
            else returns updated dictionary
    """
    if value not in my_dict.values():
        return my_dict

    for k, v in list(my_dict.items()):
        if v == value:
            my_dict.pop(k)

    return my_dict
