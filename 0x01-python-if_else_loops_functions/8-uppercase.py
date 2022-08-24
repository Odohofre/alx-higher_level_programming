#!/usr/bin/python3
def uppercase(str):
    str_list = list()

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str_list.append(chr(ord(i)-32))
        else:
            str_list.append(i)
    print("{}".format("".join(str_list)), end="")
    print()
