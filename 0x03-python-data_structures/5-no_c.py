#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a strings

    Args:
        my_string (Strings): String to be edited

    Returns:
        String: new string without characters c and C
    """
    my_list = [i for i in my_string]
    new_str = ""

    for i in my_list:
        if i == 'c' or i == 'C':
            my_list.remove(i)
    return (new_str.join(my_list))
