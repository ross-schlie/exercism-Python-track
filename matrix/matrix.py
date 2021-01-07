'''
Introduction
Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:

9 8 7
5 3 2
6 6 7
representing this matrix:

    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
your code should be able to spit out:

A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.
The rows for our example matrix:

9, 8, 7
5, 3, 2
6, 6, 7
And its columns:

9, 5, 6
8, 3, 6
7, 2, 7
'''

class Matrix:

    # Build a 'map' a.k.a. matrix for the rows and columns (integers) 
    # based on the input matrix string
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.map = []
        for row in rows:
            cells = row.split()
            map_row = []
            for cell in cells:
                map_row.append(int(cell))

            self.map.append(map_row)

        # print(self.map)
        return

    # Since the matrix was built 'left-to-right while moving top-to-bottom' 
    # return the whole 'row' based on the index specified
    def row(self, index):
        return self.map[index - 1]

    # To get the 'column' we need to iterate over the rows 
    # and return the values at specified index
    # Convulted usage of zip vs simple list copy and iteration vs elegant usage of row
    def column(self, index):
        # iteration code:
        '''
        tmplist = []
        for row in self.map:
            tmplist.append(row[index])
        return tmplist
        '''
        # zip code
        '''
        a = zip(*self.map)
        b = list(a)[index - 1]
        return list(b)
        '''

        # smart solution as per other contributers
        return [row[index - 1] for row in self.map]
        

# Testing code.
# testdata = Matrix("1 2 3\n4 5 6\n7 8 9")
# print(testdata.row(1))
# print(testdata.row(2))
# print(testdata.column(1))
# print(testdata.column(3))