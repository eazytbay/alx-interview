#!/usr/bin/python3
'''N Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []  # coordinates format [row, column]
    stop = False
    x = 0
    y = 0

    # iterate thru rows
    while x < n:
        goback = False
        # iterate thru columns
        while y < n:
            # check is current column is safe
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if(col == y or col + (x-cord[0]) == y or
                        col - (x-cord[0]) == y):
                    safe = False
                    break

            if not safe:
                if y == n - 1:
                    goback = True
                    break
                y += 1
                continue

            # place queen
            cords = [x, y]
            placed_queens.append(cords)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if x == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        x = cord[0]
                        y = cord[1]
                for z in range(n - x):
                    placed_queens.pop()
                if x == n - 1 and y == n - 1:
                    placed_queens = []
                    stop = True
                x -= 1
                y += 1
            else:
                y = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            x -= 1
            while x >= 0:
                y = placed_queens[x][1] + 1
                del placed_queens[x]  # delete previous queen coordinates
                if y < n:
                    break
                x -= 1
            if x < 0:
                break
            continue
        x += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
