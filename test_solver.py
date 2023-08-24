
import pytest

from solver import sudoku_solver
import puzzles


easy_cells = []
medium_cells = []
hard_cells = []

for row in range(0, 9):
    for column in range(0, 9):
        easy_cells.append((puzzles.easy_puzzle[row][column], puzzles.easy_solution[row][column]))
        medium_cells.append((puzzles.medium_puzzle[row][column], puzzles.medium_solution[row][column]))
        hard_cells.append((puzzles.hard_puzzle[row][column], puzzles.hard_solution[row][column]))

@pytest.mark.parametrize("puzzle_cell, solution_cell", easy_cells)
def test_easy_puzzle(puzzle_cell, solution_cell):
    assert puzzle_cell, solution_cell

@pytest.mark.parametrize("puzzle_cell, solution_cell", medium_cells)
def test_medium_puzzle(puzzle_cell, solution_cell):
    assert puzzle_cell, solution_cell

@pytest.mark.parametrize("puzzle_cell, solution_cell", hard_cells)
def test_hard_puzzle(puzzle_cell, solution_cell):
    assert puzzle_cell, solution_cell


@pytest.mark.parametrize("puzzle, solution", [
    (puzzles.easy_puzzle, puzzles.easy_solution),
    (puzzles.medium_puzzle, puzzles.medium_solution),
    (puzzles.hard_puzzle, puzzles.hard_solution),
])
def test_sudoku_solver(puzzle, solution):
    assert sudoku_solver(puzzle) == solution