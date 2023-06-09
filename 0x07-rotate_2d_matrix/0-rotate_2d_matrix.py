#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_
    """
    for i in range(len(matrix) // 2):
        for j in range(i, len(matrix) - i - 1):
            matrix[i][j], matrix[j][len(matrix) - i - 1], \
            matrix[len(matrix) - i - 1][len(matrix) - j - 1], \
            matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - j - 1][i], \
            matrix[i][j], matrix[j][len(matrix) - i - 1], \
            matrix[len(matrix) - i - 1][len(matrix) - j - 1]
