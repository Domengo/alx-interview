#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""
import sys


def solve_n_queens(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    def is_valid(board, row, col):
        '''Check row and column'''
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check upper diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # Check lower diagonal
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def backtrack(board, col):
        """_summary_

        Args:
            board (_type_): _description_
            col (_type_): _description_
        """
        if col == n:
            solution = []
            for i in range(n):
                queen_pos = board[i].index(1)
                solution.append([i, queen_pos])
            solutions.append(solution)
            return
        for row in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1)
                board[row][col] = 0

    solutions = []
    empty_board = [[0] * n for _ in range(n)]
    backtrack(empty_board, 0)
    return solutions


if __name__ == "__main__":
    """_summary_
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)

    for solution in solutions:
        print(solution)
