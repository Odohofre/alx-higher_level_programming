#!/usr/bin/python3
def no_c(my_string):
    my_list = [i for i in my_string]
    new_str = ""

    for i in my_list:
        if (i in 'C' and i in 'c'):
            my_list.remove(i)
    return (new_str.join(my_list))
