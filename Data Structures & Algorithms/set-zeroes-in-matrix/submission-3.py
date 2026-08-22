class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        left_col, top_row = False, False
        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    # if it's row zero, then top_row = True
                    if i == 0: 
                        top_row = True
                    if j == 0:
                        left_col = True
                    if i != 0 and j != 0:
                        # set the row to zero
                        matrix[i][0] = 0
                        # set the column to zero
                        matrix[0][j] = 0
        
        for r in range(1, ROWS):
            # if left column is zero, set the whole row to zero
            if matrix[r][0] == 0:
                for c in range(COLS):
                    matrix[r][c] = 0

        for c in range(1, COLS):
            # if top row is zero, set the whole column to zero
            if matrix[0][c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0
        # print(left_col, top_row)
        if left_col: 
            # set everything in in the left col to zero
            for r in range(ROWS):
                matrix[r][0] = 0
        if top_row: 
            for c in range(COLS):
                matrix[0][c] = 0

        
        