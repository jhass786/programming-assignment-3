"""
sudoku_solver.py - Sudoku Solver via SAT (PA3)
Authors: Jibran, Andrew Bahsoun, Sami Hammoud

Encodes a 9x9 Sudoku puzzle as a CNF boolean formula, then solves it
using the DPLL-based SAT solver from PA2.

Variable encoding:
    varnum(row, col, digit) = 100 * row + 10 * col + digit
    where row, col, digit are all in {1, ..., 9}
"""

import sys
import ast
from sat_solver import sat_solve


# each (row, col, digit) combo needs its own unique variable number
def varnum(row, col, digit):
    return 100 * row + 10 * col + digit


def sudoku_encode(grid):
    clauses = []
    digits = range(1, 10)
    cells  = range(1, 10)

    # every cell has to have at least one digit
    for row in cells:
        for col in cells:
            clauses.append([varnum(row, col, d) for d in digits])

    # but no cell can have two digits at once
    for row in cells:
        for col in cells:
            for d1 in digits:
                for d2 in digits:
                    if d1 < d2:
                        clauses.append([-varnum(row, col, d1),
                                        -varnum(row, col, d2)])

    # each digit has to show up somewhere in every row
    for row in cells:
        for d in digits:
            clauses.append([varnum(row, col, d) for col in cells])

    # same deal for columns
    for col in cells:
        for d in digits:
            clauses.append([varnum(row, col, d) for row in cells])

    # and every digit has to appear in each 3x3 box
    box_starts = [1, 4, 7]
    for box_row_start in box_starts:
        for box_col_start in box_starts:
            for d in digits:
                box_cells = [
                    varnum(box_row_start + dr, box_col_start + dc, d)
                    for dr in range(3)
                    for dc in range(3)
                ]
                clauses.append(box_cells)

    # lock in the digits that are already given in the puzzle
    for row in cells:
        for col in cells:
            given = grid[row - 1][col - 1]
            if given != 0:
                clauses.append([varnum(row, col, given)])

    return clauses


def solve(grid):
    clauses    = sudoku_encode(grid)
    assignment = sat_solve(clauses, {})

    # no assignment means the puzzle has no solution
    if assignment is None:
        return None

    # translate the SAT variable assignments back into a readable 9x9 grid
    solved = [[0] * 9 for _ in range(9)]

    for row in range(1, 10):
        for col in range(1, 10):
            for d in range(1, 10):
                var = varnum(row, col, d)
                if assignment.get(var, False):
                    solved[row - 1][col - 1] = d
                    break

    return solved


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 sudoku_solver.py \"<grid>\"")
        print("Example: python3 sudoku_solver.py \"[[5,3,0,...],[...],...]\"")
        sys.exit(1)

    input_grid = ast.literal_eval(sys.argv[1])
    result = solve(input_grid)

    if result is None:
        print(None)
    else:
        for row in result:
            print(row)
