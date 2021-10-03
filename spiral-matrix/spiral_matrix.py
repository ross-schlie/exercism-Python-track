"""exercism spiral matrix module."""


def spiral_matrix(size):
    matrix = []
    number = 0
    if size > 0:
        range_rows = range(0, size)
        range_cols = range(0, size)
        for row_index in range_rows:
            row = []
            for row_col in range_cols:
                row.append(0)

            matrix.append(row)

        number_range = range(1, size * size + 1)
        x = 0
        y = 0
        direction = 'left-to-right'
        rows = 1
        cols = 1
        for number in number_range:
            matrix[y][x] = number
            if direction == 'left-to-right' and x < size - rows:
                x += 1
            elif direction == 'left-to-right' and y < size - cols:
                y += 1
            elif direction == 'left-to-right' and x == size - rows and y == size - cols:
                # bottom right, so invert
                direction = 'right-to-left'
                cols += 1
                x -= 1
            elif direction == 'right-to-left' and x >= rows:
                x -= 1
            elif direction == 'right-to-left' and y >= cols:
                y -= 1
            else:
                direction = 'left-to-right'
                rows += 1
                x += 1

    return matrix
