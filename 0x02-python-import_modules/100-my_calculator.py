#!/usr/bin/python3
from email.policy import default
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, a + b))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, a - b))
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, a * b))
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, *, /")
            exit(1)
