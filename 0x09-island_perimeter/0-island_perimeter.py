#!/usr/bin/python3

"""Solution to the Island perimeter"""


def island_perimeter(grid):
    """function definition of the island perimeter"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                perimeter += 4

                if x > 0 and grid[x - 1][y] == 1:
                    perimeter -= 2
                if y > 0 and grid[x][y - 1] == 1:
                    perimeter -= 2

    return perimeter
