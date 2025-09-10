"""
https://leetcode.com/problems/valid-sudoku/description/
"""

class Solution(object):
    def isValidSudoku(self, board):
        
        def if_rows_valid():
            for row in board:
                seen = set()
                for element in row:
                    if element != ".":
                        if element in seen:
                            return False
                        seen.add(element)
            return True

        def if_cols_valid():
            for col_id in range(9):
                column = [row[col_id] for row in board]
                seen = set()
                for element in column:
                    if element != ".":
                        if element in seen:
                            return False
                        seen.add(element)
            return True

        def if_cells_valid():
            for yc in range(3):
                for xc in range(3):
                    submatrix = [row[3 * xc : 3 * xc + 3] for row in board[3 * yc : 3 * yc+3]]
                    
                    seen = set()
                    for y in range(3):
                        for x in range(3):
                            element = submatrix[y][x]
                            if element != ".":
                                if element in seen:
                                    return False
                                seen.add(element)
            return True

        return if_cells_valid() & if_rows_valid() & if_cols_valid()