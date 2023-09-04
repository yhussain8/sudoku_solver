import pandas as pd

from puzzles import easy_puzzle, medium_puzzle, hard_puzzle


def initialize_cell_index():
    cell_index = []
    for row_id in range(0, 9):
        for column_id in range(0, 9):
            cell_index.append(f'{row_id}_{column_id}')
    return cell_index


def initialize_grid_possible_values(cell_index):
    grid_possible_values = {}
    for cell_id in cell_index:
        grid_possible_values[cell_id] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return grid_possible_values


def identify_column_cells(row_id, column_id):
    column_cells = []
    for row_id_new in range(0, 9):
        if row_id_new == row_id:
            continue
        else:
            column_cells.append(f'{row_id_new}_{column_id}')
    return column_cells


def identify_row_cells(row_id, column_id):
    row_cells = []
    for column_id_new in range(0, 9):
        if column_id_new == column_id:
            continue
        else:
            row_cells.append(f'{row_id}_{column_id_new}')
    return row_cells


def identify_region_cells(cell_id):
    region_0 = [
        '0_0', '0_1', '0_2', 
        '1_0', '1_1', '1_2', 
        '2_0', '2_1', '2_2'
    ]
    region_1 = [
        '0_3', '0_4', '0_5', 
        '1_3', '1_4', '1_5', 
        '2_3', '2_4', '2_5'
    ]
    region_2 = [
        '0_6', '0_7', '0_8', 
        '1_6', '1_7', '1_8', 
        '2_6', '2_7', '2_8'
    ]
    region_3 = [
        '3_0', '3_1', '3_2', 
        '4_0', '4_1', '4_2', 
        '5_0', '5_1', '5_2'
    ]
    region_4 = [
        '3_3', '3_4', '3_5', 
        '4_3', '4_4', '4_5', 
        '5_3', '5_4', '5_5'
    ]
    region_5 = [
        '3_6', '3_7', '3_8', 
        '4_6', '4_7', '4_8', 
        '5_6', '5_7', '5_8'
    ]
    region_6 = [
        '6_0', '6_1', '6_2', 
        '7_0', '7_1', '7_2', 
        '8_0', '8_1', '8_2'
    ]
    region_7 = [
        '6_3', '6_4', '6_5', 
        '7_3', '7_4', '7_5', 
        '8_3', '8_4', '8_5'
    ]
    region_8 = [
        '6_6', '6_7', '6_8', 
        '7_6', '7_7', '7_8', 
        '8_6', '8_7', '8_8'
    ]
    regions = [
        region_0,
        region_1,
        region_2,
        region_3,
        region_4,
        region_5,
        region_6,
        region_7,
        region_8
    ]
    for region in regions:
        if cell_id in region:
            region.remove(cell_id)
            return region


def consolidate_neighbours(cell_id, column_cells, row_cells, region_cells):
    neighbours = set(column_cells + row_cells + region_cells)
    neighbours = list(neighbours)
    neighbours.sort()
    neighbours.remove(cell_id)
    return neighbours


def initialize_grid_groupings(cell_index):
    grid_groupings = {}
    for cell_id in cell_index:
        row_id, column_id = cell_id.split("_")
        column_cells = identify_column_cells(row_id, column_id)
        row_cells = identify_row_cells(row_id, column_id)
        region_cells = identify_region_cells(cell_id)
        neighbour_cells = consolidate_neighbours(cell_id, column_cells, row_cells, region_cells)
        grid_groupings[cell_id] = neighbour_cells
    return grid_groupings


def initialize_grid(cell_index, puzzle):
    grid = {}
    for cell_id in cell_index:
        row_id, column_id = cell_id.split("_")
        grid[cell_id] = puzzle[int(row_id)][int(column_id)]
    return grid


def reduce_possible_values(grid, grid_groupings, grid_possible_values):
    # print(type(grid))
    for cell_id, cell_value in grid.items():
        if cell_value is not None:
            # grid_groupings.pop(cell_id)
            grid_possible_values.pop(cell_id)
    # print('grid')
    # print(grid)
    # print('grid_groupings')
    # print(grid_groupings)
    # print('grid_possible_values')
    # print(grid_possible_values)
    return grid_groupings, grid_possible_values


def eliminate_possible_values(grid, grid_groupings, grid_possible_values):
    # print(grid_possible_values)
    # print('\n')
    for grid_cell_id, grid_cell_value in grid.items():
        if grid_cell_value is not None:
            # consolidate into function
            cell_neighbours = grid_groupings.get(grid_cell_id)
            for cell_neighbour_id in cell_neighbours:
                cell_neighbour_possible_values = grid_possible_values.get(cell_neighbour_id)
                if cell_neighbour_possible_values:
                    if grid_cell_value in cell_neighbour_possible_values:
                        grid_possible_values[cell_neighbour_id].remove(grid_cell_value)
    # print(grid_groupings)
    return grid_possible_values


def simple_elimination_loop(grid, grid_groupings, grid_possible_values):
    # print(grid_possible_values)
    grid_updated = True
    while grid_updated:
        grid_updated = False
        for cell_id, cell_possible_values in grid_possible_values.items():
            if len(cell_possible_values) == 1:
                known_value = cell_possible_values[0]
                grid[cell_id] = known_value
                grid_updated = True
                grid_possible_values.pop(cell_id)
                # consolidate into function
                cell_neighbours = grid_groupings.get(cell_id)
                for cell_neighbour_id in cell_neighbours:
                    cell_neighbour_possible_values = grid_possible_values.get(cell_neighbour_id)
                    if cell_neighbour_possible_values:
                        if known_value in cell_neighbour_possible_values:
                            grid_possible_values[cell_neighbour_id].remove(known_value)
                break
        # loop through possible values
        # if possible values == 1 then update grid with remaining value as a known value
        # mark grid_updated = True
        # remove the cell_id from possible values dictionary
        # eliminate value from list of possible values for each cell neighbour
        # identify list of cell neighbours for cell being updated with known value
        # for each cell neighbours list remove the known value
    # print(grid_possible_values)
    # print(grid)
    return grid, grid_possible_values


def generate_solution(grid):
    solution = []
    for row_id in range(0, 9):
        row = []
        for column_id in range(0, 9):
            cell_id = f'{row_id}_{column_id}'
            row.append(grid[cell_id])
        solution.append(row)
    return solution


def print_puzzle(solution):
    df = pd.DataFrame(solution)
    df = df.fillna(0)
    df = df.astype(int)
    df = df.replace(0, "_")
    print(df)
    # for row in solution:
    #     print(row)


def sudoku_solver(puzzle: list[list[int]]) -> list[list[int]]:
    print('Unsolved:\n')
    print_puzzle(puzzle)
    cell_index = initialize_cell_index()
    grid_possible_values = initialize_grid_possible_values(cell_index)
    grid_groupings = initialize_grid_groupings(cell_index)
    grid = initialize_grid(cell_index, puzzle)
    # print(grid)
    grid_groupings, grid_possible_values = reduce_possible_values(grid, grid_groupings, grid_possible_values)
    grid_possible_values = eliminate_possible_values(grid, grid_groupings, grid_possible_values)
    grid, grid_possible_values = simple_elimination_loop(grid, grid_groupings, grid_possible_values)
    solution = generate_solution(grid)
    # solution = puzzle
    print("\nSolved:\n")
    print_puzzle(solution)
    return solution

print('\nEasy Puzzle\n')
sudoku_solver(easy_puzzle)
print('\nMedium Puzzle\n')
sudoku_solver(medium_puzzle)
print('\nHard Puzzle\n')
sudoku_solver(hard_puzzle)



# test_cell_id = "7_5"
# row_id, column_id = test_cell_id.split("_")
# print(row_id, column_id)


# Output for test from initialize_cell_index()
# ['0_0', '0_1', '0_2', '0_3', '0_4', '0_5', '0_6', '0_7', '0_8', '1_0', '1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8', '2_0', '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8', '3_0', '3_1', '3_2', '3_3', '3_4', '3_5', '3_6', '3_7', '3_8', '4_0', '4_1', '4_2', '4_3', '4_4', '4_5', '4_6', '4_7', '4_8', '5_0', '5_1', '5_2', '5_3', '5_4', '5_5', '5_6', '5_7', '5_8', '6_0', '6_1', '6_2', '6_3', '6_4', '6_5', '6_6', '6_7', '6_8', '7_0', '7_1', '7_2', '7_3', '7_4', '7_5', '7_6', '7_7', '7_8', '8_0', '8_1', '8_2', '8_3', '8_4', '8_5', '8_6', '8_7', '8_8']

# cell_0_0 = "0-0"
# cell_0_0_possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cell_0_0_neighbours = ["0_1", "0_2", "...", "8-7", "8-8"]

# grid_possible_values = {
#     cell_0_0: cell_0_0_possible_values
# }

# grid_groupings = {
#     cell_0_0: cell_0_0_neighbours
# }

# grid = {
#     "grid_possible_values": grid_possible_values,
#     "grid_groupings": grid_groupings
# }