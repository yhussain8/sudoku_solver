"""
Source: New York Times Sudoku as on August 24, 2023
https://www.nytimes.com/puzzles/sudoku

Puzzles are organized as a list of a list so that each cell can be referenced
by its row and column number.
"""

easy_puzzle = [
    [None, 9, None, None, 5, 3, 7, None, 6],
    [6, 7, None, 1, 9, None, None, 5, None],
    [5, None, 4, None, None, 2, None, None, 1],
    [4, None, None, 6, None, None, 2, 3, None],
    [3, 1, None, None, None, 9, None, 6, 5],
    [None, None, None, 5, 3, None, None, 8, 7],
    [None, None, None, None, 2, 5, 9, None, None],
    [None, None, 1, 9, None, None, 5, None, 3],
    [None, 5, 3, 8, None, None, None, 7, None]
]

easy_solution = [
    [1, 9, 8, 4, 5, 3, 7, 2, 6],
    [6, 7, 2, 1, 9, 8, 3, 5, 4],
    [5, 3, 4, 7, 6, 2, 8, 9, 1],
    [4, 8, 5, 6, 1, 7, 2, 3, 9],
    [3, 1, 7, 2, 8, 9, 4, 6, 5],
    [2, 6, 9, 5, 3, 4, 1, 8, 7],
    [7, 4, 6, 3, 2, 5, 9, 1, 8],
    [8, 2, 1, 9, 7, 6, 5, 4, 3],
    [9, 5, 3, 8, 4, 1, 6, 7, 2]
]

medium_puzzle = [
    [None, None, None, None, None, None, 6, None, None],
    [None, 2, None, 5, None, None, 7, None, None], 
    [1, 7, None, None, None, 9, None, None, None],
    [None, None, 5, None, 3, None, None, None, 8],
    [None, None, None, None, 5, None, None, 6, None],
    [None, None, None, None, 2, None, 4, 1, None],
    [None, None, 4, None, 9, 8, None, 3, None],
    [None, 9, 8, None, None, None, 2, None, 6],
    [None, None, None, 4, None, None, None, None, None]
]

medium_solution = [
    [5, 4, 9, 3, 7, 2, 6, 8, 1],
    [8, 2, 6, 5, 4, 1, 7, 9, 3], 
    [1, 7, 3, 6, 8, 9, 5, 2, 4],
    [2, 6, 5, 1, 3, 4, 9, 7, 8],
    [4, 8, 1, 9, 5, 7, 3, 6, 2],
    [9, 3, 7, 8, 2, 6, 4, 1, 5],
    [6, 5, 4, 2, 9, 8, 1, 3, 7],
    [3, 9, 8, 7, 1, 5, 2, 4, 6],
    [7, 1, 2, 4, 6, 3, 8, 5, 9]
]

hard_puzzle = [
    [None, None, None, None, None, None, 1, None, None],
    [None, None, 1, None, 4, 7, 6, None, None],
    [None, 6, None, None, None, None, None, 5, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, 3, None, 5, 7, None, 8],
    [4, None, None, 2, 9, None, None, None, None],
    [7, None, 3, 1, None, None, None, None, 6],
    [None, None, 8, None, 6, None, 4, None, 1],
    [None, None, None, None, 2, None, None, None, 9]
]
    
hard_solution = [
    [3, 7, 9, 6, 5, 2, 1, 8, 4],
    [2, 5, 1, 8, 4, 7, 6, 9, 3],
    [8, 6, 4, 9, 3, 1, 2, 5, 7],
    [1, 3, 5, 4, 7, 8, 9, 6, 2],
    [6, 9, 2, 3, 1, 5, 7, 4, 8],
    [4, 8, 7, 2, 9, 6, 3, 1, 5],
    [7, 4, 3, 1, 8, 9, 5, 2, 6],
    [9, 2, 8, 5, 6, 3, 4, 7, 1],
    [5, 1, 6, 7, 2, 4, 8, 3, 9]
]