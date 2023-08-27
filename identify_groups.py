def identify_columns(puzzle: list[list]) -> dict[list]:
    """
    Reads a given Sudoku puzzle and returns a dictionary with a list of values 
    from each column.
    """
    columns = {}
    for column_number in range(0, 9):
        column_values = []
        for row_number in range(0, 9):
            column_values.append(puzzle[row_number][column_number])
        columns[column_number] = column_values
    return columns


def identify_regions(puzzle: list[list]) -> dict[list]:
    """
    Reads a given Sudoku puzzle and returns a dictionary with a list of values 
    from each column.
    """
    regions = {}
    row_index = 0
    column_index = 0
    for region_number in range(0, 9):

        if region_number == 1:
            row_index = 0
            column_index = 3
        elif region_number == 2:
            row_index = 0
            column_index = 6
        elif region_number == 3:
            row_index = 3
            column_index = 0
        elif region_number == 4:
            row_index = 3
            column_index = 3
        elif region_number == 5:
            row_index = 3
            column_index = 6
        elif region_number == 6:
            row_index = 6
            column_index = 0
        elif region_number == 7:
            row_index = 6
            column_index = 3
        elif region_number == 8:
            row_index = 6
            column_index = 6

        region_values = []
        for row_number in range(row_index, (row_index + 3)):
            row_values = []
            for column_number in range(column_index, column_index + 3):
                row_values.append(puzzle[row_number][column_number])
            region_values.append(row_values[0])
            region_values.append(row_values[1])
            region_values.append(row_values[2])
        regions[region_number] = region_values

    return regions


def identify_rows(puzzle: list[list]) -> dict[list]:
    """
    Reads a given Sudoku puzzle and returns a dictionary with a list of values 
    from each column.
    """
    rows = {} 
    for row_number in range(0, 9):
        rows[row_number] = puzzle[row_number]
    return rows