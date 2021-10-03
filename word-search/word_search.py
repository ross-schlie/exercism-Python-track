"""exercism word search module."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        """
        Peform word search per row (left-to-right and right-to-left)

        :param word string - The word to search for.
        :return None or (Point(x, y), Point(x, y)) - None if not found,
            or a Set containing start and end Points
        """
        rowSearch = self.search_rows(word)
        if rowSearch is not None:
            return rowSearch

        colSearch = self.search_col(word)
        if colSearch is not None:
            return colSearch

        return None

    def search_rows(self, word):
        """
        Peform word search per row (left-to-right and right-to-left)

        :param word string - The word to search for.
        :return None or (Point(x, y), Point(x, y)) - None if not found,
            or a Set containing start and end Points
        """
        for row_index, row in enumerate(self.puzzle):
            #straight search
            index = row.find(word)
            if index >= 0:
                index_end = index + len(word) - 1
                return (Point(index, row_index), Point(index_end, row_index))

            #inverse search
            index = row[::-1].find(word)
            if index >= 0:
                index = len(row) - index - 1
                index_end = index - len(word) + 1
                return (Point(index, row_index), Point(index_end, row_index))

        return None

    def search_col(self, word):
        """
        Peform word search per column (up, down, diagonals)

        :param word string - The word to search for.
        :return None or (Point(x, y), Point(x, y)) - None if not found,
            or a Set containing start and end Points
        """
        word_length = len(word)
        puzzle_rows = len(self.puzzle)

        #check and see if the height (number of rows)
        # is greater than length of the word
        if puzzle_rows < word_length:
            return None

        # assumes each row has same length
        col_length = len(self.puzzle[0])
        for row_index, row in enumerate(self.puzzle):
            # if the word is too long to possibly start on the row
            rows_to_bottom = puzzle_rows - row_index
            rows_to_top = row_index + 1
            if (rows_to_bottom < word_length) and (rows_to_top < word_length):
                continue

            for col_index in range(0, col_length):
                # check for first letter in word
                search_result = self.search_word(word, row_index, col_index)
                if search_result is not None:
                    return search_result

        return None

    def search_word(self, word, row_index, col_index):
        """
        Peform word search per column (up, down, diagonals)

        :param word string - The word to search for.
        :param row_index int - The x or row in the puzzle to start searching in.
        :param col_index int - The y or col in the puzzle to start searching in.
        :return None or (Point(x, y), Point(x, y)) - None if not found,
            or a Set containing start and end Points
        """
        puzzle_rows = len(self.puzzle)
        word_length = len(word)
        rows_to_bottom = puzzle_rows - row_index
        rows_to_top = row_index + 1
        col_length = len(self.puzzle[0])
        cols_to_left = col_index + 1
        cols_to_right = col_length - col_index

        # check for first letter in word
        if word[0] == self.puzzle[row_index][col_index]:
            # search down (if it makes sense to)
            if rows_to_bottom >= word_length:
                coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'down')
                if coordinate_search is not None:
                    return coordinate_search

                # seach top-left to bottom-right (if it makes sense to)
                if cols_to_right >= word_length:
                    coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'top-left-bottom-right')
                    if coordinate_search is not None:
                        return coordinate_search

                # search top right to bottom-left (if it makes sense to)
                if cols_to_left >= word_length:
                    coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'top-right-bottom-left')
                    if coordinate_search is not None:
                        return coordinate_search

            # search up (if it makes sense to)
            if rows_to_top >= word_length:
                coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'up')
                if coordinate_search is not None:
                    return coordinate_search

                # seach bottom-left to top-right (if it makes sense to)
                if cols_to_right >= word_length:
                    coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'bottom-left-top-right')
                    if coordinate_search is not None:
                        return coordinate_search

                # search bottom-right to top-left (if it makes sense to)
                if cols_to_left >= word_length:
                    coordinate_search = self.search_word_coordinate(word, row_index, col_index, 'bottom-right-top-left')
                    if coordinate_search is not None:
                        return coordinate_search

        return None

    def search_word_coordinate(self, word, start_y, start_x, direction):
        """
        Peform word search starting at a given coordinate in a specific direction.

        :param word string - The word to search for.
        :param start_x int - The x or row in the puzzle to start searching in.
        :param start_y int - The y or col in the puzzle to start searching in.
        :param direction str - The direction to modify x, y for next letters in a word.
        :return None or (Point(x, y), Point(x, y)) - None if not found,
            or a Set containing start and end Points
        """
        word_found = True
        next_x = start_x
        next_y = start_y
        for char_index, char in enumerate(word):
            # @TODO Constants for directions
            if direction == 'down':
                next_y = start_y + char_index
            elif direction == 'up':
                next_y = start_y - char_index
            elif direction == 'top-left-bottom-right':
                next_y = start_y + char_index
                next_x = start_x + char_index
            elif direction == 'top-right-bottom-left':
                next_y = start_y + char_index
                next_x = start_x - char_index
            elif direction == 'bottom-left-top-right':
                next_y = start_y - char_index
                next_x = start_x + char_index
            elif direction == 'bottom-right-top-left':
                next_y = start_y - char_index
                next_x = start_x - char_index

            if char != self.puzzle[next_y][next_x]:
                word_found = False
                break

        if word_found:
            return (Point(start_x, start_y), Point(next_x, next_y))

        return None
