#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = list(my_list)

    if idx < 0 and idx > len(my_list):
        return (my_list)
    else:
        my_list_copy[idx] = element
        return (my_list_copy)