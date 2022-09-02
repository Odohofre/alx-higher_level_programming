#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Returns the addition of all unique integers in a list\
        (only once for each integer).

    Args:
        my_list (list, optional): a list. Defaults to [].

    """
    new_set = {x for x in my_list}
    sum = 0
    for i in new_set:
        sum += i
    return (sum)
