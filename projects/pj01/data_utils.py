"""Utility Functitons."""

__author__ = "730319741"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read data file as CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of he CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Read that file

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(columns: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Make table with only a select number of rows of data for each column."""
    result = {}
    if rows > len(columns):
        for key in columns:
            values = []
            i: int = 0
            while i < rows: 
                values.append(columns[key][i])
                i += 1
            result[key] = values
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Make new column-based table with a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    # Loop through columns in second parameter
    for key in names:
        result[key] = column_table[key]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Make column-based table out of two combined column-based tables."""
    result: dict[str, list[str]] = {}
    # Loop through columns for table_1
    for key in table_1:
        # Assign list of values stored in first column to column key of result dictionary
        result[key] = table_1[key]
    # Loop through columns in table _2
    for key in table_2:
        # If key already in dictionary, add on listt of values stored in second parameter at same column
        if key in result:
            result[key] = table_1[key] + table_2[key]
        # Else: assign key list of values stored in second parameter
        else: 
            result[key] = table_2[key]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Create dictionary that counts the number of times they key is seen."""
    result: dict[str, int] = {}
    # Loop through items in values
    for key in values:
        # Check if item already a key in result
        if key in result:
            # If item in dict, increase value by 1
            result[key] += 1
        # If item not in dict, add to dict and assign value 1
        else: 
            result[key] = 1
    return result