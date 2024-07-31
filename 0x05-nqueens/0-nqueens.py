#!/usr/bin/python3
"""The Backtracking algorithm solution for NQueens task"""

import sys


class Nqueens:
    """Definition of A class containing the solution to the Nqueen problem"""
    def SolveNqueens(self, n):
        """The solution method and all the core data and
        algorithms"""
        column = []
        positiveDiagonal = set()  # row + column is constant
        negativeDiagonal = set()  # row - column is constant
        row = []

        res = []

        def check_validation(x, y):
            """Checks if the current position is valid to place a queen"""
            return y not in column and (x + y) not in positiveDiagonal \
                and (x - y) not in negativeDiagonal

        def bktrack(x):
            """This is a backtracking algo that validates if
            the queen is already on that given row and
            positiveDiagonal or negativeDiagonal then
            discarding that position recursively"""
            if x == n:
                res.append([[row[x], column[x]] for x in range(n)])
                return

            for y in range(n):
                if check_validation(x, y):
                    column.append(y)
                    row.append(x)
                    positiveDiagonal.add(x + y)
                    negativeDiagonal.add(x - y)

                    bktrack(x + 1)

                    column.pop()
                    row.pop()
                    positiveDiagonal.remove(x + y)
                    negativeDiagonal.remove(x - y)

        bktrack(0)

        for solution in res:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solution = Nqueens()
    if not sys.argv[1].isnumeric():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    solution.SolveNqueens(int(sys.argv[1]))
