
import pytest

from solver import sudoku_solver
import puzzles

@pytest.mark.parametrize("puzzle, solution", [
    (puzzles.easy_puzzle, puzzles.easy_solution),
    (puzzles.medium_puzzle, puzzles.medium_solution),
    (puzzles.hard_puzzle, puzzles.hard_solution),
])
def test_sudoku_solver(puzzle, solution):
    assert sudoku_solver(puzzle) == solution