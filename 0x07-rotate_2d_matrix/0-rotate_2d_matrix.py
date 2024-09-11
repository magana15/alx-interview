#!/usr/bin/python3
"""Matrix rotation module"""


def rotate_2d_matrix(matrix):
    """
    The function `rotate_2d_matrix` rotates a given 2D
    matrix by 90 degrees clockwise.

    :param matrix: The `rotate_2d_matrix` function you provided
    takes a 2D matrix as input and rotates
    it 90 degrees clockwise in place
    """
    # Step 1: Transpose the matrix
    n = len(matrix)  # Get the size of the matrix (n x n)

    for i in range(n):
        for j in range(i, n):  # we start from i to avoid swapping back
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reversing each row
    for i in range(n):
        matrix[i].reverse()
