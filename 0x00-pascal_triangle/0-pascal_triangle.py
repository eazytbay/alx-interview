#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """list of lists of numbers
    representing the pascal triangle is returned"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for x in range(n):
        # define a row and fill first and last idx with 1
        custom_row = [0] * (x+1)
        custom_row[0] = 1
        custom_row[len(custom_row) - 1] = 1

        for y in range(1, x):
            if y > 0 and y < len(custom_row):
                i = pascal_triangle[x - 1][y]
                j = pascal_triangle[x - 1][y - 1]
                custom_row[y] = i + j

        pascal_triangle[x] = custom_row

    return pascal_triangle
