class Matrix:

    def __init__(self, matrix_string):
        """Build a 'map' a.k.a. matrix for the rows and columns (integers).
        
        Based on the input matrix string
        """
        rows = matrix_string.split('\n')
        self._map = []
        for row in rows:
            cells = row.split()
            map_row = []
            for cell in cells:
                map_row.append(int(cell))

            self._map.append(map_row)

    def row(self, index):
        """Get a given row from the matrix.
        
        Since the matrix was built 'left-to-right while moving top-to-bottom'
        return the whole 'row' based on the index specified

        Parameters
        ----------
        arg1 : int
            Index of which row to retrieve
    
        Returns
        ------ 
        list
            Matrix row
        """
        return self._map[index - 1]

    def column(self, index):
        """Get a given column from the matrix.
        
        To get the 'column' we need to iterate over the rows 
        and return the values at specified index

        Parameters
        ----------
        arg1 : int
            Index of which row to retrieve
    
        Returns
        ------ 
        list
            Matrix column

        Convulted usage of zip vs simple list copy 
        and iteration vs elegant usage of row
        """
        # iteration code:
        # tmplist = []
        # for row in self.map:
        #     tmplist.append(row[index])
        # return tmplist
  
        # zip code
        # a = zip(*self.map)
        # b = list(a)[index - 1]
        # return list(b)

        # smart solution as per other contributers
        return [row[index - 1] for row in self._map]
        