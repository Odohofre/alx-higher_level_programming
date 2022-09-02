#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list (list, optional): list of tuples containing score and weight.\
        Defaults to [].

    Returns:
        average: weighted average
    """
    if len(my_list) == 0 or my_list is None:
        return (0)

    numerator = 0
    denominator = 0
    for i, j in my_list:
        numerator += i * j
        denominator += j

    average = numerator / denominator

    return (average)
