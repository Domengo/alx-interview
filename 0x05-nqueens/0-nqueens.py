#!/usr/bin/python3
"""N Queens problem"""
from sys import argv


def solve_n_queens(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    def is_valid(board, row, col):
        """Check row and column"""
        for i in range(n):
            if board[row][i] == 1 or board[i][col] == 1:
                return False
        # Check diagonals
        for i in range(n):
            for j in range(n):
                if (i + j == row + col) or (i - j == row - col):
                    if board[i][j] == 1:
                        return False
        return True

    def backtrack(board, col):
        """_summary_

        Args:
            board (_type_): _description_
            col (_type_): _description_
        """
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return
        for row in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1)
                board[row][col] = 0

    solutions = []
    empty_board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(empty_board, 0)
    return solutions


# Example usage
n = argv[1]
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)
