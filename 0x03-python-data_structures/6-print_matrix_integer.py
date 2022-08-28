#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col is not row[len(row) - 1]:
                print("{}".format(col), end=" ")
            else:
                print("{}".format(col), end="")
        print()
