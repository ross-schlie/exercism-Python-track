"""exercism minesweeper module."""


def annotate(minefield):
    """
    Add the mine counts to a completed Minesweeper board.
    """

    max_y = len(minefield) - 1
    if max_y < 0:
        return minefield

    max_x = len(minefield[0]) - 1
    for row_index, row in enumerate(minefield):
        if len(row) -1 != max_x:
            raise ValueError(f"In row {row_index}, column width {len(row)} is different from first row's column width {max_x + 1}.")

        row = list(row)
        for col_index, char in enumerate(row):
            if char == "*":
                continue
            elif char == " ":
                row[col_index] = count_adjecent_mine(minefield, col_index, row_index, max_x, max_y)
            else:
                raise ValueError(f"In row {row_index}, column {col_index}, invalid value: {char} was found")

        minefield[row_index] = "".join(row)

    return minefield

def count_adjecent_mine(minefield, x, y, max_x, max_y):
    value = " "
    count = 0

    # progression:
    # (x - 1, y - 1)
    # (x - 1, y)
    # (x - 1, y + 1)
    # (x, y - 1)
    # (x, y - 1)
    # (x + 1, y - 1)
    # (x + 1, y)
    # (x + 1, y  1)


    # left-top
    if x > 0 and y > 0 and minefield[y - 1][x - 1] == "*":
        count += 1

    # left
    if x > 0 and minefield[y][x - 1] == "*":
        count += 1

    # left-bottom
    if x > 0 and y < max_y and minefield[y + 1][x - 1] == "*":
        count += 1

    # top
    if y > 0 and minefield[y - 1][x] == "*":
        count += 1

    #bottom
    if y < max_y and minefield[y + 1][x] == "*":
        count += 1

    # right-top
    if x < max_x and y > 0 and minefield[y - 1][x + 1] == "*":
        count += 1

    # right
    if x < max_x and minefield[y][x + 1] == "*":
        count += 1

    # right-bottom
    if x < max_x and y < max_y and minefield[y + 1][x + 1] == "*":
        count += 1

    if count > 0:
        value = str(count)

    return value
