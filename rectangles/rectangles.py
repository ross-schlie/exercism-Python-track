"""exercism rectangles module."""

def rectangles(strings):
    """
    Find rectangles in text.

    :param strings string - Text that may contain rectangles.
    :return int - Number of valid rectangles found.
    """
    if len(strings) == 0:
        return 0

    corner_count = 0
    corners = []
    for y, line in enumerate(strings):
        corners_in_line = line.count("+")
        if corners_in_line > 0:
            corner_count += corners_in_line
            for x, value in enumerate(line):
                if value == "+":
                    corners.append((y, x))

    if len(corners) < 4:
        return 0

    valid_rectangles = 0
    max_y = len(strings) - 1
    max_x = len(strings[0]) - 1
    for coords in corners:
        possible_bottom_left_corners = []
        # check if we can go right
        possible_right_corners = walk_line(strings, max_x, max_y, [coords], "+", "-")
        if len(possible_right_corners) == 0:
            continue

        # check if we can go down
        possible_bottom_right_corners = walk_line(strings, max_x, max_y, possible_right_corners, "+", "|")
        if len(possible_bottom_right_corners) == 0:
            continue

        # check if we can go left
        possible_bottom_left_corners = walk_line(strings, max_x, max_y, possible_bottom_right_corners, "-", "-")
        if len(possible_bottom_left_corners) == 0:
            continue

        # check if we can go back up to the origin
        ending_coords = walk_line(strings, max_x, max_y, possible_bottom_left_corners, "-", "|")
        if len(ending_coords) == 0:
            continue

        # count success returns to origin
        for corner_coords in ending_coords:
            if corner_coords[0] == coords[0] and corner_coords[1] == coords[1]:
                valid_rectangles += 1

    return valid_rectangles

def walk_line(strings, max_x, max_y, coordinates, direction, path_char):
    """
    Given some starting points and a direction, find any connected corners in said direction.

    :param strings string - the text that may contain rectangles.
    :param max_x int - the boundary/width of the text.
    :param max_y int - the boundary/height of the text.
    :param coordinates list[(tuple),...] - List containing starting locations (y, x).
    :param direction string - "+" or "-" for incrementing/decrmenting x or y depending on path_char.
    :param path_char string - "|" or "-" the connecting char to look for.
    :return list[(tuple),...] - List containing any valid corners in the direction specified.
    """
    corner_coords = []
    for coords in coordinates:
        y = coords[0]
        x = coords[1]

        in_bounds = True
        while (in_bounds):
            # move 'forward'
            if path_char == "-" and direction == "+":
                x += 1
            elif path_char == "-" and direction == "-":
                x -= 1
            elif path_char == "|" and direction == "+":
                y += 1
            elif path_char == "|" and direction == "-":
                y -= 1

            if x < 0 or x > max_x or y < 0 or y > max_y:
                in_bounds = False
                break

            if strings[y][x] == path_char:
                continue
            elif strings[y][x] == "+":
                corner_coords.append((y, x))
            else:
                break

    return corner_coords