#!/usr/bin/python3
""" n x n 2D matrix, rotate it 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """An inplace 90 deg rotation of an N X N matrix"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
