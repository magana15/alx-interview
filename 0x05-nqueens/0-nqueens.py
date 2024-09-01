#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    """
    Check whether it's safe to place a queen at board[row][col].
    """
    # check column
    for i in range(row):
        if board[i] == col:
            return False

    # check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row):
    """
    Use backtracking to find all solutions to the N-Queens problem.
    """
    n = len(board)
    if row == n:
        # A valid solution is found, print it
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            # Backtrack: remove the queen and try the next column
            board[row] = -1

def print_solution(board):
    """
    Print the board configuration where the queens are placed.
    """
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)

def validate_and_parse_args():
    """
    Validate and parse the command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n

def main():
    """
    The main function of the program.
    It validates input, initializes the board, and calls the solver function.
    """
    n = validate_and_parse_args()
    board = [-1] * n
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()
