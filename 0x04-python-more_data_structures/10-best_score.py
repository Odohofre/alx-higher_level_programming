#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value

    Args:
        a_dictionary (Any): a dictionary

    Returns:
        None: if no score is found
    """
    if a_dictionary is None or a_dictionary == {}:
        return "None"

    biggest = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v is biggest:
            return (k)
