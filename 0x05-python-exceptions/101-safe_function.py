#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (TypeError, ZeroDivisionError, ValueError, IndexError) as e:
        stderr.write("Exception: {}\n".format(e))
        return None
