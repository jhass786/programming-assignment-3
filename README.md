# Sudoku via SAT — PA3
## Overview
A command-line Sudoku solver built in Python.  
Encodes a 9×9 Sudoku puzzle as a **conjunctive normal form (CNF)** boolean formula, then solves it using the **DPLL-based SAT solver from PA2**.
## Features
- Encodes a full 9×9 Sudoku puzzle as a CNF boolean formula
- Supports empty cells (`0`) and pre-filled given digits (`1–9`)
- Uses `varnum(row, col, digit) = 100 * row + 10 * col + digit` to map cell-digit triples to SAT variables
- Accepts the puzzle grid directly as a command-line argument
- Returns a solved 9×9 grid when satisfiable, or `None` when unsolvable
## CNF Constraints
- Every cell contains at least one digit
- Every cell contains at most one digit
- Every digit appears at least once in each row
- Every digit appears at least once in each column
- Every digit appears at least once in each 3×3 box
- Pre-filled digits from the input grid are forced true
## Core Components
- `varnum()` — maps a (row, col, digit) triple to a unique positive SAT variable
- `sudoku_encode()` — builds the full CNF formula enforcing all six Sudoku constraints
- `solve()` — encodes the puzzle, calls the PA2 SAT solver, and decodes the assignment back into a 9×9 grid
## Group Members
- Jibran Hassankhil
- Andrew Bahsoun
- Sami Hammoud
