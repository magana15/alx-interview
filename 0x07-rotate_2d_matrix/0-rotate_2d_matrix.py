#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    # Step 1: Transpose the matrix
    n = len(matrix)  # Get the size of the matrix (n x n)

    for i in range(n):
        for j in range(i, n):  # we start from i to avoid swapping back
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reversing each row
    for i in range(n):
        matrix[i].reverse()
