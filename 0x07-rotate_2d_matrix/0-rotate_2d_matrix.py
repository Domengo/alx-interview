#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in place.

    Args:
        matrix: The 2D matrix to rotate.

    Returns:
        None
    """
    # for i in range(len(matrix) // 2):
    #     for j in range(i, len(matrix) - i - 1):
    #         matrix[i][j], matrix[j][len(matrix) - i - 1], \
    #         matrix[len(matrix) - i - 1][len(matrix) - j - 1], \
    #         matrix[len(matrix) - j - 1][i] \
    #         = matrix[len(matrix) - j - 1][i], \
    #         matrix[i][j], matrix[j][len(matrix) - i - 1], \
    #         matrix[len(matrix) - i - 1][len(matrix) - j - 1]

    # for i in range(len(matrix) // 2):
    #     for j in range(i, len(matrix[0]) - i - 1):
    #         temp = matrix[i][j]
    #         matrix[i][j] = matrix[len(matrix) - 1 - j][i]
    #         matrix[len(matrix) - 1 - j][i] \
    #             = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
    #         matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] \
    #             = matrix[j][len(matrix) - 1 - i]
    #         matrix[j][len(matrix) - 1 - i] = temp
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
