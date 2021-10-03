"""exercism saddle points module."""


def saddle_points(matrix):
    """
    Find saddle points in a matrix

    :param matrix list - A list of rows containing values.
    :return list - A list containing dictionary(ies) indicating
        where the saddle point(s) in the matrix are.

    It's called a "saddle point" because it is greater than or
        equal to every element in its row and less than or equal
        to every element in its column.

    A matrix may have zero or more saddle points.
    The matrix can have a different number of rows and columns (Non square).
    """

    points = []
    rows_num = len(matrix)
    if rows_num > 0:
        colums_num = len(matrix[0])
        # travese the row, and find highest value
        for current_row_index, row in enumerate(matrix):
            if len(row) != colums_num:
                raise ValueError(f"Irregular matrix, row {current_row_index + 1} "
                    f"has {len(row)} columns instead of expected {colums_num}.")

            max_value = max(row)
            # for cases where the highest value occurs in multiple colums, iterate
            max_value_count = row.count(max_value)
            next_index = 0
            while max_value_count > 0:
                # Given the column index for candidate (highest value in row)
                # Find out if it's the lowest in the column
                col_index = row.index(max_value, next_index)
                next_index = col_index + 1
                max_value_count -= 1
                is_lowest_in_col = True
                for row_index in range(0, rows_num):
                    # skip 'current' row
                    if row_index == current_row_index:
                        continue

                    # check to make sure col exists in row
                    if len(matrix[row_index]) - 1 < col_index:
                        raise ValueError(f"Irregular matrix, row {row_index} is missing column {col_index}")
                        #continue

                    value = matrix[row_index][col_index]
                    if value < max_value:
                        # we found a value in the col that's less than the candidate
                        # so it's not a saddle in this column
                        is_lowest_in_col = False
                        break

                if is_lowest_in_col:
                    # current_row_index and col_index start at 0, so up 1
                    points.append({"row": current_row_index + 1, "column": col_index + 1})

    return points
